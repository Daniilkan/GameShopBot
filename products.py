from aiogram import Bot, Dispatcher, types, filters, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from pyqiwip2p import QiwiP2P
import config
import sqlite3
import logging
import asyncio

import main

pay_photo = 'template.jpg'
#p2p = QiwiP2P(auth_key="GH7879hhgiTTFYN6826")
global prodName

def billmake(price: int, name: str):
    pass

def billcheck(bill):
    pass

class Product():
    def __init__(self, name, price):
        self.prName = name
        self.prPrice = price
        main.prName = name
        global prodName
        prodName = name
    async def billprint(self, callback: types.CallbackQuery):
        bill = billmake(self.prName, self.prPrice)
        billlink_b = InlineKeyboardButton(text="Ссылка на оплату💳", url="youtube.com")
        billcheck_b = InlineKeyboardButton(text="Проверить оплату🔍", callback_data="checking")
        billreject_b = InlineKeyboardButton(text="Отменить оплату❌", callback_data="reject")
        bill_list = InlineKeyboardMarkup(inline_keyboard=[[billlink_b], [billcheck_b], [billreject_b]])
        await callback.message.delete()
        await callback.message.answer_photo(photo=types.FSInputFile(path=pay_photo), caption=f"Оплата {self.prName} - {self.prPrice}P", reply_markup=bill_list)