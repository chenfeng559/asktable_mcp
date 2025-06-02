from fastmcp import FastMCP, Image
import io
from asktable import Asktable
from tools import search_asktable_data
import yaml
import asyncio


with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

api_key = config['api_key']
datasource_id = config['datasource_id']

mcp = FastMCP(name="Asktable server")



@mcp.tool()
def get_sql(query:str,datasource_id:str)-> str:
    """"
    输入用户的查询
    :param 
        query: 用户的查询
        datasource_id: 数据源的id
    :return: 返回查询所用的sql
    """
    message = asyncio.run(search_asktable_data(datasource_id,query))
    return message

@mcp.tool()
def get_table_data(query:str,datasouce_id:str)-> str:
    """"
    输入用户的查询
    :param query: 用户的查询
    :return: 返回查询的信息
    """
    message = asyncio.run(search_asktable_data(datasource_id,query))
    return message


if __name__ == "__main__":
    mcp.run()
