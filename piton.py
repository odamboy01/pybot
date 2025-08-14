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

@dp.message(F.text.lower() == 'Assalomu alaykum')
async def cmd_na_gap(message: Message):
    await message.reply('Valeykum Assalom!')

@dp.message(F.photo)
async def photo(message: Message):
    if message.photo:
        await message.answer(f'Foto ID si: {message.photo[-1].file_id}')
    else:
        await message.answer('Hech qanday foto topilmadi.')

# 100 simple project ideas
IDEAS = [
    "Weather app",
    "To-do list",
    "Calculator",
    "Currency converter",
    "Quiz game",
    "Flashcard app",
    "Notes app",
    "Expense tracker",
    "Password generator",
    "Pomodoro timer",
    "Unit converter",
    "Markdown editor",
    "Simple blog",
    "Portfolio website",
    "Recipe book",
    "Habit tracker",
    "Random joke bot",
    "Image gallery",
    "Contact manager",
    "Simple chat app",
    "File organizer",
    "Alarm clock",
    "Countdown timer",
    "BMI calculator",
    "Tip calculator",
    "QR code generator",
    "URL shortener",
    "Dictionary app",
    "Translator",
    "Calendar app",
    "Stopwatch",
    "Music player",
    "Movie database",
    "Book tracker",
    "Task reminder",
    "Simple poll bot",
    "Voting app",
    "Weather notifier",
    "Stock price checker",
    "News aggregator",
    "RSS reader",
    "Random quote bot",
    "Simple drawing app",
    "Meme generator",
    "Text encryptor",
    "Text analyzer",
    "Palindrome checker",
    "Prime number finder",
    "Tic-tac-toe game",
    "Hangman game",
    "Rock-paper-scissors",
    "Simple survey bot",
    "Feedback collector",
    "Simple e-commerce",
    "Shopping list",
    "Budget planner",
    "Simple forum",
    "Guestbook",
    "Simple wiki",
    "File uploader",
    "Image resizer",
    "PDF merger",
    "Simple calendar",
    "Event scheduler",
    "Birthday reminder",
    "Simple messenger",
    "Simple API",
    "Random name generator",
    "Simple chatbot",
    "Simple search engine",
    "Simple web scraper",
    "Simple dashboard",
    "Simple analytics",
    "Simple leaderboard",
    "Simple game leaderboard",
    "Simple multiplayer game",
    "Simple puzzle game",
    "Simple maze game",
    "Simple matching game",
    "Simple memory game",
    "Simple card game",
    "Simple dice roller",
    "Simple lottery picker",
    "Simple voting system",
    "Simple ticket system",
    "Simple booking system",
    "Simple reservation system",
    "Simple calendar sync",
    "Simple email sender",
    "Simple SMS sender",
    "Simple notification bot",
    "Simple reminder bot",
    "Simple timer bot",
    "Simple stopwatch bot",
    "Simple countdown bot",
    "Simple weather bot",
    "Simple news bot",
    "Simple RSS bot",
    "Simple quote bot",
    "Simple joke bot",
    "Simple trivia bot",
    "Simple quiz bot",
    "Simple poll bot",
    "Simple survey bot",
    "Simple feedback bot",
    "Simple suggestion bot"
]

@dp.message(Command('idea'))
async def cmd_idea(message: Message):
    idea_list = "\n".join([f"{i+1}. {IDEAS[i]}" for i in range(len(IDEAS))])
    await message.answer(f"100 Simple Project Ideas:\n{idea_list}\n\nSend /choose <number> to select an idea.")

@dp.message(Command('choose'))
async def cmd_choose(message: Message):
    if not message.text:
        await message.reply("Usage: /choose <number>")
        return
    args = message.text.split()
    if len(args) != 2 or not args[1].isdigit():
        await message.reply("Usage: /choose <number>")
        return
    idx = int(args[1]) - 1
    if 0 <= idx < len(IDEAS):
        await message.reply(f"You chose: {IDEAS[idx]}")
    else:
        await message.reply("Invalid number. Please choose a number between 1 and 100.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\nGoodbye')