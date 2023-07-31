import snowflake.connector
import time
from datetime import datetime
import os

conn_attempts = 0;

while True:
    conn_attempts += 1;
    time_string = datetime.now().strftime("%H:%M:%S.%f")
    print("{time}: starting to connect..... [Attempt {no_attempts}]".format(time=time_string, no_attempts=conn_attempts))
    with snowflake.connector.connect(
            account=os.environ['SNOWFLAKE_ACCOUNT'],
            database=os.environ['SNOWFLAKE_SANDBOX_DATABASE'],
            schema=os.environ['SNOWFLAKE_SANDBOX_SCHEMA'],
            warehouse=os.environ['SNOWFLAKE_WAREHOUSE'],
            user=os.environ['SNOWFLAKE_USER'],
            role=os.environ['SNOWFLAKE_ROLE'],
            authenticator='externalbrowser',
            ) as conn:
        result = conn.cursor().execute("select 42;").fetchall()[0][0]
        time_string = datetime.now().strftime("%H:%M:%S.%f")
        print("{time}: SQL Result={result} [{no_attempts} Connection Attempts]".format(time=time_string, result=result, no_attempts=conn_attempts))
        print("sleeping .......")
        time.sleep(1)
