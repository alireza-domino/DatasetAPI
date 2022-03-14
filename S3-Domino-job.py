from domino import data_sources
import os
import shutil



myClient = data_sources.DataSourceClient()
myClient


DATA_SOURCE_NAME = "ali-test-2-S3"
data_source_obj = myClient.get_datasource(DATA_SOURCE_NAME)


print(data_source_obj)


# Key object
file_name = "iris.csv"

my_key = data_source_obj.Object(file_name)
print(my_key)

# GEt content as binary
content = my_key.get()
print("content binary")
print(content)

# Downlaoding 
data_source_obj.Object(file_name).download_file("/mnt/artifacts/" + file_name)



