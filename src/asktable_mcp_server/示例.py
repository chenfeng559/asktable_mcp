# -*- coding: utf-8 -*-
from fastmcp import FastMCP

from asktable import Asktable

api_key = 'ADMIN_54RVZUHXDTONK3Z8GU35'
datasource_id = "ds_6iewvP4cpSyhO76P2Tv8MW"


client = Asktable(api_key=api_key)

# meta = client.datasources.meta.create(
#     datasource_id=datasource_id,
#     name="example_excel"
# )

bot = client.bots.create(
    datasource_ids=[datasource_id],
    name="example_bot"
)
chat = client.chats.create(
    bot_id=bot.id
)
message = client.chats.messages.create(
    chat_id=chat.id,
    question="有多少部门？"
)

print(message.content.text)