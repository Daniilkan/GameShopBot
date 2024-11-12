from main import botik, dp
from aiogram import types
import sqlite3

db = sqlite3.connect('orders.db')
c = db.cursor()

async def sending_key():
    orders_count = 0
    ids = c.execute("SELECT id FROM orders")
    for i in ids:
        orders_count += 1
    while orders_count > 0:
        c.execute("SELECT id FROM orders")
        id = str(c.fetchone())
        id = id.replace("(", "")
        id = id.replace(")", "")
        id = id.replace(",", "")
        id = id.replace("'", "")
        key_to_send = "hz"
        chat_id = "hz"
        prName = "hz"
        c.execute(f"SELECT prName FROM orders WHERE id={int(id)}")
        prName = str(c.fetchone())
        c.execute(f"SELECT chatID FROM orders WHERE id={int(id)}")
        chat_id = str(c.fetchone())
        prName = prName.replace("(", "", 1)
        prName = prName.replace(")", "", 1)
        prName = prName.replace("'", "", 2)
        prName = prName.replace(",", "", 2)
        chat_id = chat_id.replace("(", "", 1)
        chat_id = chat_id.replace(")", "", 1)
        chat_id = chat_id.replace("'", "", 2)
        chat_id = chat_id.replace(",", "", 2)
        if prName == "Minecraft Standart Edition":
            file_keys = open('mine_std_keys.txt', 'r')
            key_to_send = file_keys.readline()
        with open('mine_std_keys.txt', 'r') as f:
            lines = f.readlines()
        with open('mine_std_keys.txt', 'w') as f:
            f.writelines(lines[1:])
        orders_count -= 1
        await botik.send_message(chat_id, f"Ваш ключ к {prName}: {key_to_send}")
        c.execute(f'DELETE FROM orders WHERE id={int(id)}')
        db.commit()