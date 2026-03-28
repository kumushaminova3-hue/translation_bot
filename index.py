import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from deep_translator import GoogleTranslator

# 1. Sozlamalar
API_TOKEN = "8774576374:AAFpLUZ1YkzKJo0tFmnCWhnkDwUUckbZBSE"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# 2. Start buyrug'i uchun handler
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    welcome_text = (
        "👋 **Assalomu alaykum!**\n\n"
        "Men kreativ tarjimon botman. Menga o'zbekcha so'z yoki matn yuboring, "
        "men uni darhol **Ingliz tiliga** o'girib beraman! 🇺🇿 ➡️ 🇺🇸"
    )
    await message.answer(welcome_text, parse_mode="Markdown")

# 3. Tarjima qilish qismi (Asosiy mantiq)
@dp.message(F.text)
async def translate_text(message: types.Message):
    # Foydalanuvchiga "o'ylayotgan" statusini ko'rsatish
    await bot.send_chat_action(message.chat.id, action="typing")
    
    try:
        # O'zbekchadan Inglizchaga tarjima
        translated = GoogleTranslator(source='uz', target='en').translate(message.text)
        
        # Kreativ javob ko'rinishi
        response_template = (
            f"🔍 **Asl matn:** {message.text}\n"
            f"✨ **Tarjima:** `{translated}`\n\n"
            f"💡 _Yana biror nima tarjima qilamizmi?_"
        )
        
        await message.reply(response_template, parse_mode="Markdown")
        
    except Exception as e:
        await message.answer("⚠️ Kechirasiz, tarjima qilishda xatolik yuz berdi. Birozdan so'ng urinib ko'ring.")
        logging.error(f"Xatolik: {e}")

# 4. Botni ishga tushirish
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtatildi")