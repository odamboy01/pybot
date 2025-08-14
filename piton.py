import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Assalomu alaykum\nNa gap?')

@dp.message(Command('salom'))  # /salom
async def cmd_salom(message: Message):
    await message.reply('Vaaleykum Assalom!')

@dp.message(F.text == 'Assalomu alaykum')
async def cmd_na_gap(message: Message):
    await message.reply('Valeykum Assalom!')

@dp.message(F.photo)
async def photo(message: Message):
    await message.answer(f'Foto ID si: {message.photo[-1].file_id}')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\nGoodbye')