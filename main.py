import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Sizning botingiz uchun to'g'ri token o'rnatildi:
TOKEN = "8678456257:AAEto_KQibg7CTF0sV0-2FjFdIIQXnGP60c"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}! Botimiz bulutli serverdan muvaffaqiyatli ishga tushdi! 🚀")

@dp.message()
async def echo_message(message: types.Message):
    await message.answer(f"Siz yozdingiz: {message.text}")

async def main():
    print("Bot ishlamoqda...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

