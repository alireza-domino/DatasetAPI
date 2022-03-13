# DatasetAPI

```
ObjectStoreDatasource(
                client= DataSourceClient(),
                config={
                        'type': 'DataSourceS3Config', 
                        'dataSourceType': 'S3Config', 
                        'bucket': 's3regression', 
                        'region': 'us-west-2'},
                credential_type='Individual', 
                datasource_type='S3Config', 
                identifier='622becfc4b34ac67107429bd', 
                name='S3Config', 
                owner='ddl-alireza')
```
```
QueryDatasource(
                config={
                        'type': 'DataSourceSnowflakeConfig', 
                        'database': 'AD_DEMO', 
                        'role': '', 
                        'accountName': 'kma55258', 
                        'dataSourceType': 'SnowflakeConfig', 
                        'schema': 'public', 
                        'warehouse': 'DOMINODATALAB'}, 
                credential_type='Individual', 
                datasource_type='SnowflakeConfig', 
                identifier='622bec914b34ac67107429bb', 
                name='SnowflakeConfig', 
                owner='ddl-alireza')
```                

@attr.s(auto_attribs=True)
class SnowflakeConfig(Config):
    """Snowflake datasource configuration."""

configs:
```
    database: Optional[str] = _config(elem=ConfigElem.DATABASE)
    schema: Optional[str] = _config(elem=ConfigElem.SCHEMA)
    warehouse: Optional[str] = _config(elem=ConfigElem.WAREHOUSE)
    role: Optional[str] = _config(elem=ConfigElem.ROLE)

    password: Optional[str] = _cred(elem=CredElem.PASSWORD)
    username: Optional[str] = _cred(elem=CredElem.USERNAME)
```



```
[docs]
@attr.s(auto_attribs=True)
class S3Config(Config):
    """S3 datasource configuration."""

    bucket: Optional[str] = _config(elem=ConfigElem.BUCKET)
    region: Optional[str] = _config(elem=ConfigElem.REGION)

    aws_access_key_id: Optional[str] = _cred(elem=CredElem.USERNAME)
    aws_secret_access_key: Optional[str] = _cred(elem=CredElem.PASSWORD)
```


```
@attr.s(auto_attribs=True)
class RedshiftConfig(Config):
    """Redshift datasource configuration."""

    database: Optional[str] = _config(elem=ConfigElem.DATABASE)

    password: Optional[str] = _cred(elem=CredElem.PASSWORD)
    username: Optional[str] = _cred(elem=CredElem.USERNAME)
```