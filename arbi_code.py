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
'''ВАНЯ В СТРОЧКУ СНИЗУ ВСТАТЬ ПРАВИЛЬНЫЙ ТОКЕН, ЕСЛИ Я НЕ ТО ВСТАВИЛ'''
bot = telebot.TeleBot("7535373221:AAHcgr-bHLbZVpmrLUV_L6mKnb6DadqJGqw")

conn = sqlite3.connect('c:/Users/eruha/Documents/FOr_University/HSE-Coin/BASED/BD1', check_same_thread=False)
cursor = conn.cursor()