import asyncio
import sqlite3
import telebot



from aiogram import Router, Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from selenium import webdriver
from lxml import html # импорт библиотеки HTML парсера
from webbrowser import *
from jinja2 import Template

router = Router()
bot = telebot.TeleBot("7535373221:AAHcgr-bHLbZVpmrLUV_L6mKnb6DadqJGqw")

conn = sqlite3.connect('c:/Users/eruha/Documents/FOr_University/HSE-Coin/BASED/BD1', check_same_thread=False)
cursor = conn.cursor()

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == '/start':
        us_id = message.from_user.id
        info = cursor.execute('SELECT * FROM test WHERE user_id=?', (us_id, ))
        if info.fetchone() is None:
            db_table_val(user_id=us_id)

bot.polling(none_stop=True)
@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.reply(
        "Click! Click! Click!",
        reply_markup=webapp_builder()
    )

async def main() -> None:
    bot = Bot("7535373221:AAHcgr-bHLbZVpmrLUV_L6mKnb6DadqJGqw", default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(True)
    await dp.start_polling(bot)


if name == "main":
    asyncio.run(main())