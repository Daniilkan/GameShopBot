from aiogram import Bot, Dispatcher, types, filters, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from pyqiwip2p import QiwiP2P
import config
import sqlite3
import logging
import asyncio

minecraft_products = [["Minecraft Standart Edition", 1550, "o_mine_std"],
                      ["Minecraft Deluxe Edition", 2000, "o_mine_del"],
                      ["Minecraft Dungeons", 750, "o_dun_std"],
                      ["Minecraft Dungeons + DLC", 1950, "o_dun_dlc"]]
rcl_products = [["Red Dead Redemption 2", 3150, "o_rdr2"], ["Grand Theft Auto 5 + WhiteShark", 2650, "o_gta5_ws"]]

# minecraft_st_b = InlineKeyboardButton(text="Minecraft Standart Edition - 1550p", callback_data="o_mine_std")
# minecraft_de_b = InlineKeyboardButton(text="Minecraft Deluxe Edition - 2000p", callback_data="o_mine_del")
# minecraft_du_b = InlineKeyboardButton(text="Minecraft Dungeons - 750p", callback_data="o_dun_std")
# minecraft_du_dlc_b = InlineKeyboardButton(text="Minecraft Dungeons + DLC - 1950p", callback_data="o_dun_dlc")
back_b = InlineKeyboardButton(text="Назад⬅️", callback_data="catalog")
def prod_catalog(products: str):
    product_list = InlineKeyboardMarkup(inline_keyboard=[[back_b]])
    product_list.inline_keyboard.clear()
    if(products == "minecraft"):
        for i in range(len(minecraft_products)):
            product_list.inline_keyboard.append([InlineKeyboardButton(text=f"{str(minecraft_products[i][0])} - {int(minecraft_products[i][1])}P",
                                                                    callback_data=minecraft_products[i][2])])
    elif(products == "rcl"):
        for i in range(len(rcl_products)):
            product_list.inline_keyboard.append([InlineKeyboardButton(text=f"{str(rcl_products[i][0])} - {int(rcl_products[i][1])}P",
                                                                    callback_data=rcl_products[i][2])])
    product_list.inline_keyboard.append([back_b])
    return product_list