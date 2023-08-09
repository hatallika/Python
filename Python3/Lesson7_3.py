# Продолжение темы Создаем меню для телеграм бота
import os
from dotenv import load_dotenv
import logging
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()

TOKEN = os.getenv('TOKEN')
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# @dp.message_handler(content_types=types.ContentType.VIDEO)
# @dp.message_handler(content_types=types.ContentTypes.VIDEO | types.ContentTypes.AUDIO)
@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def catch_document(message: types.Message):
    await message.document.download()
    await message.reply('Документ скачан\n'
                        f'{message.document.file_id}')


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def catch_video(message: types.Message):
    await message.video.download()
    await message.reply('Видео было загружено')


@dp.message_handler(content_types=types.ContentType.AUDIO)
async def catch_audio(message: types.Message):
    await message.audio.download()
    await message.reply('Аудио скачано\n'
                        f'{message.audio.file_id}')


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def catch_photo(message: types.Message):
    await message.photo[-1].download()
    await message.reply('Фото было загружено')


@dp.message_handler(content_types=types.ContentType.ANY)
async def catch_content(message: types.Message):
    await message.reply(f'Вы прислали {message.content_type}')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
