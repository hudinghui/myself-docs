from pymilvus import MilvusClient, DataType

client = MilvusClient("./milvus_demo.db")

# client = MilvusClient(
#     uri='http://localhost:19530', # replace with your own Milvus server address
#     token="root:Milvus"
# ) 

schema = MilvusClient.create_schema(
    auto_id=False,
    enable_dynamic_field=True,
)
# 3.2. Add fields to schema
schema.add_field(field_name="my_id", datatype=DataType.INT64, is_primary=True)
schema.add_field(field_name="my_vector", datatype=DataType.FLOAT_VECTOR, dim=5)
schema.add_field(field_name="my_varchar", datatype=DataType.VARCHAR, max_length=512)

# index_params = client.prepare_index_params()
# # 3.4. Add indexes
# index_params.add_index(
#     field_name="my_id",
#     index_type="AUTOINDEX"
# )
# index_params.add_index(
#     field_name="my_vector", 
#     index_type="AUTOINDEX",
#     metric_type="COSINE"
# )

client.create_collection(
    collection_name="customized_setup_1",
    schema=schema
)

res = client.list_collections()

print(res)