import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiohttp import web

# Tokenni hech qanday probelsiz, toppa-toʻgʻri shu yerga yozdik:
TOKEN = "8678456257:AAEto_KQibg7CTF0sV0-2FjFdIIQXnGP60c"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}! Botimiz Render serveridan muvaffaqiyatli, xatoliksiz ishga tushdi! 🚀")

@dp.message()
async def echo_message(message: types.Message):
    await message.answer(f"Siz yozdingiz: {message.text}")

# Render oʻchrib yubormasligi uchun port ochamiz:
async def handle(request):
    return web.Response(text="Bot is running alive!")

async def main():
    port = int(os.environ.get("PORT", 10000))
    app = web.Application()
    app.router.add_get("/", handle)
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    
    await asyncio.gather(
        site.start(),
        dp.start_polling(bot)
    )

if __name__ == "__main__":
    asyncio.run(main())
