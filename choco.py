import os
from datetime import datetime, timedelta
import random
from ydb import Driver, TableDescription, PrimitiveType, SerializableReadWrite, credentials_from_env_variables, load_ydb_root_certificate

def initialize_connection(endpoint, database):
    driver_config = {
        "endpoint": endpoint,
        "database": database,
        "credentials": credentials_from_env_variables(),
        "root_certificates": load_ydb_root_certificate()
    }

    with Driver(driver_config) as driver:
        try:
            driver.wait(timeout=5)
        except TimeoutError:
            print("Connection to YDB failed")
            exit(1)

        return driver

def create_calls_table(driver, table_path):
    table_description = TableDescription()
    table_description \
        .with_column("call_id", PrimitiveType.Uint64) \
        .with_column("caller_number", PrimitiveType.Utf8) \
        .with_column("callee_number", PrimitiveType.Utf8) \
        .with_column("start_time", PrimitiveType.Timestamp) \
        .with_column("end_time", PrimitiveType.Timestamp) \
        .with_column("duration_seconds", PrimitiveType.Uint64) \
        .with_primary_key("call_id")

    with driver.table_client.session().create() as session:
        session.create_table(table_path, table_description)

        print("Table 'calls' created successfully.")

def fill_calls_table(driver, table_path):
    with driver.table_client.session().create() as session:
        tx = session.transaction(SerializableReadWrite()).begin()

        for _ in range(1000):
            start_time = datetime.now() - timedelta(days=random.randint(1, 7))
            end_time = start_time + timedelta(seconds=random.randint(1, 3600))
            duration_seconds = int((end_time - start_time).total_seconds())
            caller_number = "1234567890"  # Пример номера звонящего
            callee_number = "9876543210"  # Пример номера вызываемого

            query = f"""
                UPSERT INTO {table_path} (caller_number, callee_number, start_time, end_time, duration_seconds)
                VALUES ('{caller_number}', '{callee_number}', '{start_time.isoformat()}', '{end_time.isoformat()}', {duration_seconds})
            """
            tx.execute(query)

        tx.commit()

        print("Data inserted successfully.")

if __name__ == "__main__":
    endpoint = "ru-central1-1.ydb.yandex.net:2135"
    database = "your_database"
    table_path = "/calls"

    driver = initialize_connection(endpoint, database)
    create_calls_table(driver, table_path)
    fill_calls_table(driver, table_path)
