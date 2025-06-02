# -*- coding: utf-8 -*-

from asktable import Asktable

api_key = 'ADMIN_54RVZUHXDTONK3Z8GU35'
datasource_id = "ds_5cyDhikeSfJVXk55lWE4ts"

import asyncio

async def asktable_query(datasource_id, question)->str:
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

# 示例调用
if __name__ == "__main__":
    result = asyncio.run(asktable_query(datasource_id, "有多少用户？"))
    print(result)
