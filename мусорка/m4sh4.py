import ydb

driver_config = ydb.DriverConfig(
    'grpcs://ydb.serverless.yandexcloud.net:2135', '/ru-central1/b1gqtnssdjmo31p257d9/etnv5hrf8quojf14b0q3',
    credentials=ydb.credentials_from_env_variables(),
    root_certificates=ydb.load_ydb_root_certificate(),
)
print(driver_config)
with ydb.Driver(driver_config) as driver:
    try:
        driver.wait(timeout=15)
    except TimeoutError:
        print("Connect failed to YDB")
        print("Last reported errors by discovery:")
        print(driver.discovery_debug_details())

