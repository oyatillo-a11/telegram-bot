import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiohttp import web

TOKEN = "8678456257:AAGPBLpsSyuArYiSPGgGUy8S4a4EnfuV" # Sizning tokeningiz

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}! Botimizga xush kelibsiz!")

@dp.message()
async def echo_message(message: types.Message):
    await message.answer(f"Siz yozdingiz: {message.text}")
async def handle(request):
    return web.Response(text="Bot is running smoothly!")
async def main():
    app = web.Application()
    app.router.add_get("/", handle)
    port = int(os.environ.get("PORT", 10000))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    asyncio.create_task(site.start())
    print(f"Web server started on port {port}")
    print("Bot is polling...")
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
