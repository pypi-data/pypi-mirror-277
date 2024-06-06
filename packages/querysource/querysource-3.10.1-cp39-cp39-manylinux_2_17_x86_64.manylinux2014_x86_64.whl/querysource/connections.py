"""Connections.

Manage Database connections and supporting datasources.
"""
import asyncio
from collections.abc import Callable
from datetime import datetime
from importlib import import_module
from typing import Any, Union

from aiohttp import web
from datamodel import BaseModel
from datamodel.exceptions import ValidationError
from asyncdb import AsyncDB, AsyncPool
from asyncdb.exceptions import (
    NoDataFound,
    ProviderError,
    DriverError
)
from asyncdb.utils import cPrint
from navconfig.logging import logging
from navigator.applications.base import BaseApplication
from navigator.types import WebApp

from .conf import (
    POSTGRES_MAX_CONNECTIONS,
    POSTGRES_MIN_CONNECTIONS,
    POSTGRES_SSL,
    POSTGRES_SSL_CA,
    POSTGRES_SSL_CERT,
    POSTGRES_SSL_KEY,
    POSTGRES_TIMEOUT,
    DB_SESSION_TIMEOUT,
    DB_IDLE_IN_TRANSACTION_TIMEOUT,
    DB_KEEPALIVE_IDLE,
    DB_MAX_WORKERS,
    QUERYSET_REDIS,
    asyncpg_url,
    default_dsn,
)
from .datasources.drivers import SUPPORTED, DataDriver
from .models import QueryModel
from .providers import BaseProvider
from .types import Singleton
from .exceptions import (
    ConfigError,
    QueryError,
    QueryException,
    SlugNotFound
)

DATASOURCES: dict = {}
PROVIDERS: dict = {}

EXTERNAL_PROVIDERS = ('http', 'rest', )


class QueryConnection(metaclass=Singleton):
    """QueryConnection.

    TODO: QueryConnection will be affected by environment
    (get connection params from enviroment)
    """
    pgargs: dict = {
        "min_size": 2,
        "server_settings": {
            "application_name": "QS.Master",
            "client_min_messages": "notice",
            "max_parallel_workers": f"{DB_MAX_WORKERS}",
            "jit": "on",
            "effective_cache_size": "2147483647",
            "tcp_keepalives_idle": f"{DB_KEEPALIVE_IDLE}",
            "idle_in_transaction_session_timeout": f"{DB_IDLE_IN_TRANSACTION_TIMEOUT}",
            "idle_session_timeout": f"{DB_SESSION_TIMEOUT}"
        }
    }

    def __init__(self, **kwargs):
        if hasattr(self, '__initialized__'):
            if self.__initialized__ is True:
                return  # already configured.
        self._postgres = None
        self._connection = None
        self._connected: bool = False
        self._dsmodule = None
        self._loop: asyncio.AbstractEventLoop = None
        if 'lazy' in kwargs:
            self.lazy = kwargs['lazy']
        else:
            self.lazy: bool = False
        if 'loop' in kwargs:
            self._loop = kwargs['loop']
        self.start_cache(QUERYSET_REDIS)
        self.logger = logging.getLogger(name='QS.Connection')

    def start_cache(self, dsn):
        ### redis connection:
        self._redis = AsyncDB(
            'redis',
            dsn=dsn,
            loop=self._loop
        )

    def pool(self):
        return self._postgres

    def is_connected(self):
        return bool(self._connected)

    @property
    def connected(self):
        return bool(self._connected)

    async def in_cache(self, key: str) -> Any:
        try:
            async with await self._redis.connection() as conn:
                return await conn.exists(key)
        except (ProviderError, DriverError):
            return False

    async def get_from_cache(self, key: str) -> Any:
        try:
            async with await self._redis.connection() as conn:
                return await conn.get(key)
        except asyncio.TimeoutError:
            # trying to reconect:
            try:
                self.start_cache(QUERYSET_REDIS)
                async with await self._redis.connection() as conn:
                    return await conn.get(key)
            except Exception as exc:
                self.logger.exception(
                    f"Failure on REDIS Cache: {exc}"
                )
                return False
        except (ProviderError, DriverError):
            return False

    async def acquire(self):
        """acquire.

        Getting a connection from Pool.
        """
        return await self._postgres.acquire()

    async def get_connection(self, provider: str = 'pg'):
        """Useful for internal connections of QS.
        """
        if POSTGRES_SSL is True:
            self.pgargs['ssl'] = {
                "check_hostname": True,
                "cafile": POSTGRES_SSL_CA,
                "certfile": POSTGRES_SSL_CERT,
                "keyfile": POSTGRES_SSL_KEY,
            }
        if self.lazy is True:
            self.pgargs['server_settings']['application_name'] = 'QS.Lazy'
            try:
                loop = asyncio.get_event_loop()
            except RuntimeError:
                loop = asyncio.get_running_loop()
            return AsyncDB(
                provider,
                dsn=asyncpg_url,
                loop=loop,
                timeout=int(POSTGRES_TIMEOUT),
                **self.pgargs
            )
        else:
            ### using current Pool
            return None

    def set_connection(self, conn):
        self._connection = conn

    def setup(self, app: web.Application) -> web.Application:
        if isinstance(app, BaseApplication):  # migrate to BaseApplication (on types)
            self.app = app.get_app()
        elif isinstance(app, WebApp):
            self.app = app  # register the app into the Extension
        else:
            raise TypeError(
                f"Invalid type for Application Setup: {app}:{type(app)}"
            )
        ### startup and shutdown:
        self.app.on_startup.append(
            self.start
        )
        self.app.on_shutdown.append(
            self.stop
        )
        return self.app

    async def start(self, app: Union[web.Application, None] = None):
        """
         Create the default connection for Postgres.
         Create the connection to the database cache (redis).
         Also, reading the existing datasources in a list.
        """
        if not self._loop:
            self._loop = asyncio.get_event_loop()
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = self._loop
        if self.lazy is True:
            self.logger.debug(':: Starting QuerySource in Lazy Mode ::')
            cPrint(':: Starting QuerySource in Lazy Mode ::', level='DEBUG')
            # # lazy mode: create a simple database connector
            try:
                self.pgargs['server_settings']['application_name'] = 'QS.Lazy'
                self._connection = AsyncDB(
                    'pg',
                    dsn=asyncpg_url,
                    loop=loop,
                    timeout=int(POSTGRES_TIMEOUT),
                    **self.pgargs
                )
                await self._connection.connection()
            except Exception as err:
                self.logger.exception(err)
                raise ConfigError(
                    f"Unable to Connect to Database. {err}"
                ) from err
        else:
            cPrint(':: Starting QuerySource in Master Mode ::', level='DEBUG')
            self.logger.debug(':: Starting QuerySource in Master Mode ::')
            # pgpool (postgres)
            self.pgargs['min_size'] = POSTGRES_MIN_CONNECTIONS
            self.pgargs['max_clients'] = POSTGRES_MAX_CONNECTIONS
            self.logger.debug(' :: Starting PostgreSQL with parameters ::')
            self.logger.debug(f"{self.pgargs!r}")
            try:
                self._postgres = AsyncPool(
                    'pg',
                    dsn=default_dsn,
                    loop=loop,
                    timeout=int(POSTGRES_TIMEOUT),
                    **self.pgargs
                )
                await self._postgres.connect()
            except Exception as err:
                self.logger.exception(err)
                raise
            ## getting all datasources (saved into variable)
            sql = "SELECT * FROM public.datasources;"
            async with await self._postgres.acquire() as conn:
                result, error = await conn.query(sql)
                if error:
                    raise ConfigError(
                        f'Error on Starting QuerySource: {error!s}'
                    )
                for row in result:
                    if row['params'] is None or row['credentials'] is None:
                        self.logger.warning(
                            f"Error in DataSource {row['name']}: Missing Params or Credentials."
                        )
                        continue
                    # building a datasource based on driver:
                    name = row['name']
                    try:
                        driver = self.get_driver(row['driver'])
                    except Exception as ex:  # pylint: disable=W0703
                        self.logger.exception(ex, stack_info=True)
                        continue
                    try:
                        # TODO: encrypting credentials in database:
                        if row['dsn']:
                            data = {
                                "dsn": row['dsn']
                            }
                        else:
                            try:
                                data = {**dict(row['params']), **dict(row['credentials'])}
                            except TypeError:
                                data = dict(row['params'])
                        DATASOURCES[name] = driver(**data)
                    except (ValueError, ValidationError) as ex:
                        self.logger.exception(ex, stack_info=False)
            # TODO: SAVING DATASOURCES IN MEMORY (memcached)
        app['qs_connection'] = self
        self._connected = True

    def supported_drivers(self, driver):  # pylint: disable=W0613
        try:
            return SUPPORTED[driver]
        except KeyError:
            return False

    def get_driver(self, driver) -> DataDriver:
        """Getting a Database Driver from Datasource Drivers.
        """
        if not (drv := self.supported_drivers(driver)):
            raise ConfigError(
                f"QS: Error unsupported Driver: {driver}"
            )
        else:
            if 'driver' in drv:
                return drv['driver']
            else:
                # load dynamically
                clspath = f'querysource.datasources.drivers.{driver}'
                clsname = f'{driver}Driver'
                try:
                    self._dsmodule = import_module(clspath)
                    return getattr(self._dsmodule, clsname)
                except (AttributeError, ImportError) as ex:
                    raise RuntimeError(
                        f"QS: There is no Driver {driver}: {ex}"
                    ) from ex

    async def default_driver(self, driver: str) -> Any:
        """Get a default driver connection.
        """
        if not (self.supported_drivers(driver)):
            raise ConfigError(
                f"QS: Error unsupported Driver: {driver}"
            )
        else:
            self.logger.notice(
                f"Getting Default Connection for Driver {driver}"
            )
            default = None
            try:
                if not self._dsmodule:
                    # load dynamically
                    clspath = f'querysource.datasources.drivers.{driver}'
                    self.logger.notice(
                        f"Loading Driver {driver} Module: {clspath}"
                    )
                    try:
                        self._dsmodule = import_module(clspath)
                    except (AttributeError, ImportError) as ex:
                        raise RuntimeError(
                            f"QS: There is no DataSource called {driver}: {ex}"
                        ) from ex
                clsname = f'{driver}_default'
                default = getattr(self._dsmodule, clsname)
            except (AttributeError, ImportError) as ex:
                # No module for driver exists.
                raise RuntimeError(
                    f"QS: There is no default connection for Driver {driver}: {ex}"
                ) from ex
        ### creating a connector for this driver:
        if default.driver_type == 'asyncdb':
            try:
                return AsyncDB(driver, dsn=default.dsn, params=default.params())
            except (DriverError, ProviderError) as ex:
                raise QueryException(
                    f"Error creating AsyncDB instance: {ex}"
                ) from ex
        elif default.driver_type == 'external':
            ## returning -as-is- for use internal by provider
            return default
        else:
            ## Other Components.
            return None

    async def query_table_exists(self, connection: Callable, program: str) -> bool:
        sql = f"SELECT EXISTS ( \
                       SELECT FROM pg_catalog.pg_class c \
                       JOIN   pg_catalog.pg_namespace n ON n.oid = c.relnamespace \
                       WHERE  n.nspname = '{program}' \
                       AND    c.relname = 'tasks' \
                       AND    c.relkind = 'r');"
        row = await connection.fetchval(sql, column='exists')
        if row:
            return True
        else:
            return False

    async def get_query_slug(self, slug: str, conn: Any) -> BaseModel:
        try:
            QueryModel.Meta.connection = conn
            self.logger.debug(
                f'::: Getting Slug {slug} from {QueryModel.Meta.schema}.{QueryModel.Meta.name}'
            )
            return await QueryModel.get(query_slug=slug)
        except ValidationError as ex:
            raise SlugNotFound(
                f'Invalid Slug Data {slug!s}: {ex}'
            ) from ex
        except NoDataFound as ex:
            raise SlugNotFound(
                f'Slug not Found {slug!s}'
            ) from ex
        except (ProviderError, DriverError) as ex:
            raise SlugNotFound(
                f"Error getting Slug: {ex}"
            ) from ex

    async def get_slug(self, slug: str, program: str = None):
        start = datetime.now()
        if self.lazy is True:
            try:
                connection = await self.get_connection('pg')
                async with connection as conn:
                    obj = await self.get_query_slug(slug, conn)
            except Exception:  # pylint: disable=W0706
                raise
            finally:
                await connection.close()
                QueryModel.Meta.connection = None
        else:
            try:
                async with await self._postgres.acquire() as conn:
                    obj = await self.get_query_slug(slug, conn)
            except Exception:  # pylint: disable=W0706
                raise
            finally:
                QueryModel.Meta.connection = None
        exec_time = (datetime.now() - start).total_seconds()
        self.logger.debug(
            f"Getting Slug, Execution Time: {exec_time:.3f}ms\n"
        )
        if obj is None:
            raise SlugNotFound(
                f'Slug \'{slug}\' not found'
            )
        else:
            return obj

    def default_connection(self, driver: str = 'pg', dsn: str = None, params: dict = None):
        """Useful for internal connections of QS.
        """
        if not params:
            params = {}
        args = {}
        if driver == 'pg':
            args = {
                "timeout": int(POSTGRES_TIMEOUT),
                **self.pgargs
            }
            args['server_settings']['application_name'] = 'QS.Read'
        self.logger.debug(
            f"Connection Arguments: {args!s}"
        )
        connection = AsyncDB(
            driver,
            dsn=dsn,
            loop=self._loop,
            params=params,
            **args
        )
        self.logger.debug(
            f'DSN {driver} > {dsn}'
        )
        return connection

    async def from_provider(self, entry: dict):
        """
        Getting a connection from Table Provider.
        """
        try:
            provider = entry.provider
        except (TypeError, KeyError):
            provider = 'db'
        if provider == 'db':  # default DB connection for Postgres
            _provider = self.load_provider('db')
            conn = self.default_connection(
                driver='pg', dsn=asyncpg_url
            )
            # conn = await self._postgres.acquire()
            return [conn, _provider]
        elif provider in EXTERNAL_PROVIDERS:
            _provider = self.load_provider(provider)
            ## TODO: return a QS Provider for REST/External operations
            return [None, _provider]
        if provider in DATASOURCES:
            source, conn = await self.datasource(provider)
            ### get provider from datasource type:
            if source.driver == 'pg':
                provider = 'db'
            else:
                provider = source.driver
            _provider = self.load_provider(provider)
            ## getting the provider of datasource:
            return [conn, _provider]
        else:
            _provider = self.load_provider(provider)
            # can we use a default driver?
            try:
                conn = await self.default_driver(provider)
            except (AttributeError, TypeError, ValueError) as ex:
                print(ex)
                conn = None
            return [conn, _provider]  # can be a dummy provider.

    def load_provider(self, provider: str) -> BaseProvider:
        """
        Dynamically load a defined Provider.
        """
        if provider in PROVIDERS:
            return PROVIDERS[provider]
        else:
            srcname = f'{provider!s}Provider'
            classpath = f'querysource.providers.{provider}'
            try:
                cls = import_module(classpath, package=srcname)
                obj = getattr(cls, srcname)
                PROVIDERS[provider] = obj
                return obj
            except ImportError as ex:
                raise QueryException(
                    f"Error: No QuerySource Provider {provider} was found: {ex}"
                ) from ex

    async def datasource(self, name: str = 'default'):
        try:
            source = DATASOURCES[name]
        except KeyError:
            return None
        if source.driver_type == 'asyncdb':
            ### making an AsyncDB connection:
            driver = source.driver
            try:
                return source, AsyncDB(
                    driver,
                    dsn=source.dsn,
                    params=source.params()
                )
            except (DriverError, ProviderError) as ex:
                raise QueryException(
                    f"Error creating AsyncDB instance: {ex}"
                ) from ex
        else:
            raise QueryError(
                f'Invalid Datasource type {source.driver_type} for {name}'
            )

    async def dispose(self, conn: Callable = None):
        """
        dispose a connection from the pg pool.
        """
        # self.logger.debug('Disposing a Query Connection')
        if conn:
            # TODO: check if connection is from instance pg
            try:
                await self._postgres.release(conn)
            except Exception:  # pylint: disable=W0703
                await conn.close()

    async def stop(self, app: web.Application = None):
        """
        stop.
           Close and dispose all connections
        """
        self.logger.debug(':: Closing all Querysource connections ::')
        try:
            if self.lazy is True:
                await self._connection.close()
            else:
                await self._postgres.wait_close(gracefully=True, timeout=10)
                # await self._postgres.close(timeout=10)
        except RuntimeError as err:
            self.logger.exception(err)
        except Exception as err:
            self.logger.exception(err)
            raise
        self.logger.debug('Exiting ...')
        self._connected = False
