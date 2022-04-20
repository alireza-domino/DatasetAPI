from domino.data_sources import DataSourceClient

# instantiate a client and fetch the datasource instance
s3_dev = DataSourceClient().get_datasource("Amazon-S3-bucket-regression")

# list objects available in the datasource
objects = s3_dev.list_objects()

## get content as binary
# content = s3_dev.get("key")

## download content to file
# s3_dev.download_file("key", "./path/to/local/file")

## Download content to file object
# f = io.BytesIO()
# s3_dev.download_fileobj("key", f)