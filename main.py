from aiogram import Bot, Dispatcher, types, filters, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

import bot
import products
from products import *
from interface import *
import config
import sqlite3
import logging
import asyncio


botik = Bot(token=config.TOKEN_TG)
dp = Dispatcher()
db = sqlite3.connect('orders.db')
c = db.cursor()
user_id = 0

bill = None

minecraft_b = InlineKeyboardButton(text="Minecraft", callback_data="minecraft")
groups_list = [["Steam", "steam"], ["Brawl Stars", "bs"], ["RockStar Launcher", "rcl"]]
catalog_list = InlineKeyboardMarkup(inline_keyboard=[[minecraft_b]])
global catalog_ready
catalog_ready = False
alltime_replym = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Каталог🛒")], [KeyboardButton(text="Поддержка🎙")], [KeyboardButton(text="Кошелек💵")]], resize_keyboard=True)
catalog_photo = 'template-2.jpg'

@dp.message(filters.CommandStart())
async def Greeting(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}", reply_markup=alltime_replym)
    #c.execute("CREATE TABLE orders(id integer, prName text, chatID text)")
@dp.message(filters.Command('help', 'about'))
async def About(message: types.Message):
    await message.answer('Этот бот продает игры и донат. Ознакомиться с ассортиментом /catalog либо внизу выбрать "Каталог"')
@dp.message()
async def Catalog_show(message: types.Message):
    if message.text == 'Каталог🛒' or message.text == '/catalog':
        global catalog_ready
        if catalog_ready == False:
            for i in range(len(groups_list)):
                catalog_list.inline_keyboard.append([
                    InlineKeyboardButton(text=str(groups_list[i][0]), callback_data=groups_list[i][1])])
                catalog_ready = True
        await message.answer_photo(photo=types.FSInputFile(path=catalog_photo), caption="Вот наш каталог", reply_markup=catalog_list)
    elif message.text == 'Поддержка🎙':
        await message.answer("Вот контакт для поддержки: @Nurik_agusayang")
@dp.callback_query(F.data == "catalog")
async def Catalog_call(callback: types.CallbackQuery):
    await callback.message.edit_caption("Вот наш каталог", reply_markup=catalog_list)
@dp.callback_query(F.data == "minecraft")
async def Minecraft_cat(callback: types.CallbackQuery):
    await callback.message.edit_caption("Каталог товаров по Майнкрафту", reply_markup=prod_catalog("minecraft"))
@dp.callback_query(F.data == "rcl")
async def Minecraft_cat(callback: types.CallbackQuery):
    await callback.message.edit_caption("Каталог товаров для RockStar Launcher", reply_markup=prod_catalog("rcl"))
@dp.callback_query(F.data == "o_mine_std")
async def oplata(callback: types.CallbackQuery):
    product = Product("Minecraft Standart Edition", 1550)
    await product.billprint(callback)
@dp.callback_query(F.data == "o_mine_del")
async def oplata(callback: types.CallbackQuery):
    product = Product("Minecraft Deluxe Edition", 2000)
    await product.billprint(callback)
@dp.callback_query(F.data == "o_dun_std")
async def oplata(callback: types.CallbackQuery):
    product = Product("Minecraft Dungeons Standart Edition", 750)
    await product.billprint(callback)
@dp.callback_query(F.data == "o_dun_dlc")
async def oplata(callback: types.CallbackQuery):
    product = Product("Minecraft Dungeons + DLC", 1950)
    await product.billprint(callback)
@dp.callback_query(F.data == "o_rdr2")
async def oplata(callback: types.CallbackQuery):
    product = Product("Red Dead Redemption 2", 3150)
    await product.billprint(callback)
@dp.callback_query(F.data == "o_gta5_ws")
async def oplata(callback: types.CallbackQuery):
    product = Product("Grand Theft Auto 5 + WhiteShark Bundle", 2650)
    await product.billprint(callback)
@dp.callback_query(F.data == 'checking')
async def Bill_check(callback: types.callback_query):
    chat_id = callback.message.chat.id
    ids = c.execute("SELECT id FROM orders")
    latest = 0
    for i in ids:
        latest += 1
    c.execute('INSERT INTO orders (id, prName, chatID) VALUES(?,?,?)', (int(latest), str(products.prodName), str(chat_id)))
    db.commit()
    await callback.message.edit_caption(caption="Оплачено! \nОжидайте, мы вышлем вам ключ в этот чат, а пока почитайте инструкцию активации!")
    await bot.sending_key()
@dp.callback_query(F.data == 'reject')
async def Bill_reject(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(photo=types.FSInputFile(path=catalog_photo), caption="Вот наш каталог",
                               reply_markup=catalog_list)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(botik)

if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(bot.sending_key())

db.close()