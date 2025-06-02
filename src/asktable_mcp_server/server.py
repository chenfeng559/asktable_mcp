from fastmcp import FastMCP, Image
import io
from asktable import Asktable

api_key = 'ADMIN_54RVZUHXDTONK3Z8GU35'
datasource_id = "ds_5cyDhikeSfJVXk55lWE4ts"

mcp = FastMCP(name="Asktable server")



@mcp.tool()
def get_sql(query:str)-> str:
    """"
    输入用户的查询
    :param query: 用户的查询
    :return: 返回查询的sql
    """
    return "None"


