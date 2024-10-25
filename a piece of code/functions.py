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

score = 0

with open('index.html') as file:
    template = Template(file.read())

rendered_template = template.render(score = score)

# with open('index.html', 'w', encoding='utf-8') as html_file:
#     html_file.read()


# tree = html.fromstring('index.html')  # сохранение HTML кода страницы в переменную
# print(tree)
# one = tree.xpath('/ins/text()')

# driver = webdriver.Edge()
# driver.get("https://translated.turbopages.org/proxy_u/en-ru.ru.a10e9b55-671a61ab-f170b68d-74722d776562/https/www.geeksforgeeks.org/selenium-webdriver-tutorial/")
# first_form_input = driver.find_element_by_class_name("widget-area")
# print(first_form_input)

# user1 = 23455678


def db_table_val(user_id: int):
    cursor.execute('INSERT INTO test (user_id) VALUES (?)',
                   (user_id, ))
    conn.commit()


def webapp_builder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Let's Click!", web_app=WebAppInfo(
            url="https://hse-coin.netlify.app/"
        )
    )

    return builder.as_markup()
