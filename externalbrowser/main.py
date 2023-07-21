import snowflake.connector
import time
import os

select = "SELECT 42;"

while True:
    with snowflake.connector.connect(
            account=os.environ['SNOWFLAKE_ACCOUNT'],
            database=os.environ['SNOWFLAKE_SANDBOX_DATABASE'],
            schema=os.environ['SNOWFLAKE_SANDBOX_SCHEMA'],
            warehouse=os.environ['SNOWFLAKE_WAREHOUSE'],
            user=os.environ['SNOWFLAKE_USER'],
            role=os.environ['SNOWFLAKE_ROLE'],
            authenticator='externalbrowser',
            ) as conn:
        result = conn.cursor().execute("select 42;").fetchall()[0]
        print(result)
        time.sleep(5)
