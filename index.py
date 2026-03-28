import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Update
from aiogram.filters import Command
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

# Sozlamalar
API_TOKEN = "8774576374:AAFpLUZ1YkzKJo0tFmnCWhnkDwUUckbZBSE"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Vercelda ishlayotgan kreativ tarjimon botga xush kelibsiz! 🚀")

@dp.message(F.text)
async def translate(message: types.Message):
    translated = GoogleTranslator(source='uz', target='en').translate(message.text)
    await message.reply(f"🇺🇸 Tarjima: `{translated}`", parse_mode="Markdown")

# Vercel uchun Handler funksiyasi
async def handler(request):
    if request.method == "POST":
        json_str = await request.json()
        update = Update.model_validate(json_str, context={"bot": bot})
        await dp.feed_update(bot, update)
    return {"statusCode": 200, "body": "ok"}