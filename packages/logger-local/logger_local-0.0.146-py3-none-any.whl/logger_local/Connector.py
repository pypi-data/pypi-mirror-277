import mysql.connector
from python_sdk_remote.utilities import get_sql_hostname, get_sql_username, get_sql_password, our_get_env
from functools import lru_cache

# We are using the database directly to avoid cyclic dependency
@lru_cache
def get_connection(schema_name: str, is_treading: bool = False) -> mysql.connector:
    # is_treading is used to get a dedicated connection from cache.
    connection = mysql.connector.connect(
        host=our_get_env(key="LOGGER_MYSQL_HOST", default=get_sql_hostname()),
        user=our_get_env(key="LOGGER_MYSQL_USER", default=get_sql_username()),
        password=our_get_env(key="LOGGER_MYSQL_PASSWORD", default=get_sql_password()),
        database=schema_name
    )
    return connection
