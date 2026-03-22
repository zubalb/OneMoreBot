#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import asyncio
import os
from telebot import apihelper
from dotenv import load_dotenv
from telebot.async_telebot import AsyncTeleBot

load_dotenv()

apihelper.proxy = {'https': 'http://127.0.0.1:12334'}

bot = AsyncTeleBot(os.environ["tgtokendev"])

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print("Вебхук удален, старые сообщения очищены.")
    print("Бот запущен и ожидает новых сообщений...")
    await bot.polling(non_stop=True)
    
# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Привет! Я Бот для тестирования!.\nПросто напиши мне что-нибудь, и я это повторю!'
    await bot.reply_to(message, text)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    print(f"Пришло сообщение: {message.text}")
    await bot.reply_to(message, message.text)

if __name__ == '__main__':  
    print("Бот запущен и ожидает сообщений...")
    asyncio.run(bot.polling())