import os
from urllib.request import urlopen
import json
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
print(TOKEN)

# Запрос
response = urlopen(f'https://api.telegram.org/bot{TOKEN}/getMe').read()

# print(type(response))
# # <class 'bytes'>
# print(response)
# # b'{"ok":true,"result":{"id":6011593536,"is_bot":true,"first_name":"HatallikaBot","username":"HatallikaBot"
# ,"can_join_groups":true,"can_read_all_group_messages":false,"supports_inline_queries":false}}'
# # print(type(response))

# Преобразовали байтовую строку в словарь
response = json.loads(response)
# print(type(response)) # <class 'dict'>
print(response['result']['id'])
print(response['result']['first_name'])

response = urlopen('https://api.telegram.org/bot6011593536:AAHdQS0aHOZ7y2yKXC09ORdSvzIx3hwP4RQ/getUpdates').read()
response = json.loads(response)
print(response)
b'{"ok":true,"result":[]}'
