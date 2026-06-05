import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiohttp import web
TOKEN = "8678456257:AAGPBLpsSyuArYiSPgGGuY8S4a4E"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}! SlaydTop botiga xush kelibsiz.")

@dp.message()
async def echo_message(message: types.Message):
    await message.answer(f"Siz yozdingiz: {message.text}")
async def handle(request):
    return web.Response(text="Bot is running alive!")

async def main():
    app = web.Application()
    app.router.add_get("/", handle)
    
    port = int(os.environ.get("PORT", 10000))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 
    await site.start()
    print(f"Veb-server {port}-portda ishga tushdi")
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

    
