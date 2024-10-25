# СЕРВЕР РАБОТАЕТ НА ЛОКАЛЬНОМ КОМПЬЮТЕРЕ!!! ЭТОТ КОД НЕАКТУАЛЬНЫЙ

import asyncio
import sqlite3
import telebot

from aiogram import Router, Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder


def db_table_val(user_id: int):
    cursor.execute('INSERT INTO test1 (user_id) VALUES (?)',
                   (user_id))
    conn.commit()


def webapp_builder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Let's Click!", web_app=WebAppInfo(
            url="https://hse-coin.netlify.app/"
        )
    )

    return builder.as_markup()


router = Router()
'''ВАНЯ В СТРОЧКУ СНИЗУ ВСТАТЬ ПРАВИЛЬНЫЙ ТОКЕН, ЕСЛИ Я НЕ ТО ВСТАВИЛ'''
bot = telebot.TeleBot("7535373221:AAHcgr-bHLbZVpmrLUV_L6mKnb6DadqJGqw")

conn = sqlite3.connect('C:/Users/eruha/Documents/FOr_University/Base_of_HSE/HSE.db', check_same_thread=False)
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