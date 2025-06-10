from asktable import Asktable

import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

api_key = config['api_key']
datasource_id = config['datasource_id']

from asktable import Asktable

api_key = 'ADMIN_54RVZUHXDTONK3Z8GU35'
datasource_id = "ds_5cyDhikeSfJVXk55lWE4ts"

import asyncio

async def get_asktable_data(datasource_id, question):
    base_url = "https://api.asktable.com"
    asktable_client = Asktable(base_url= base_url,api_key=api_key)
    answer_response = asktable_client.answers.create(datasource_id=datasource_id, question=question)
    if answer_response.answer is None:
        raise ValueError("No answer returned for your query.")
    return answer_response.answer.text

async def get_asktable_sql(datasource_id, question):
    base_url = "https://api.asktable.com"
    asktable_client = Asktable(base_url= base_url,api_key=api_key)
    query_response = asktable_client.sqls.create(datasource_id=datasource_id, question=question)
    if query_response.query.sql is None: 
        raise ValueError("No answer returned for your query.")
    return query_response.query.sql
