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

async def search_asktable_data(datasource_id:str, question:str)->str:
    client = Asktable(api_key=api_key)

    bot = client.bots.create(
        datasource_ids=[datasource_id],
        name="example_bot"
    )
    chat = client.chats.create(
        bot_id=bot.id
    )
    message = client.chats.messages.create(
        chat_id=chat.id,
        question=question
    )

    return message.content.text