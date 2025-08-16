import asyncio
import logging
import os
from datetime import datetime

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN

# --- Bot bootstrap ---
bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- Storage for downloaded media ---
SAVE_PATH = "downloads"
os.makedirs(SAVE_PATH, exist_ok=True)

# --- Number → description mapping (1..106) ---
RESPONSES = {
    1: "Weather app — A simple tool to check current weather and forecasts using an online API.",
    2: "To-do list — A basic application to manage tasks, allowing users to add, remove, and check off items.",
    3: "Calculator — A simple calculator that can perform basic arithmetic operations like addition, subtraction, multiplication, and division.",
    4: "Currency converter — An application that converts amounts between different currencies using real-time exchange rates.",
    5: "Quiz game — A simple quiz game where users can answer questions and get scores based on their answers.",
    6: "Flashcard app — An application to create and study flashcards for learning new concepts or languages.",
    7: "Notes app — A simple application to take and manage notes, allowing users to create, edit, and delete notes.",
    8: "Expense tracker — An application to track daily expenses, allowing users to categorize and analyze their spending.",
    9: "Password generator — A tool to generate strong and secure passwords based on user-defined criteria.",
    10: "Pomodoro timer — A productivity tool that uses the Pomodoro Technique to help users manage time effectively by breaking work into intervals.",
    11: "Unit converter — An application to convert between different units of measurement, such as length, weight, and temperature.",
    12: "Markdown editor — A simple text editor that supports Markdown syntax for formatting text.",
    13: "Simple blog — A basic blogging platform where users can create, edit, and publish blog posts.",
    14: "Portfolio website — A personal website to showcase projects, skills, and experiences.",
    15: "Recipe book — An application to store and manage recipes with ingredients, instructions, and photos.",
    16: "Habit tracker — An application to track daily habits and help maintain good ones.",
    17: "Random joke bot — A bot that sends random jokes to users.",
    18: "Image gallery — A simple application to display and manage a collection of images.",
    19: "Contact manager — An application to store and manage contact information.",
    20: "Simple chat app — A basic chat application that allows real-time messaging.",
    21: "File organizer — An application to help organize files and folders.",
    22: "Alarm clock — A simple alarm clock application.",
    23: "Countdown timer — An application to count down to specific events.",
    24: "BMI calculator — A tool to calculate Body Mass Index.",
    25: "Tip calculator — An application to calculate tips based on bill amount.",
    26: "QR code generator — A tool to create QR codes.",
    27: "URL shortener — A tool to shorten long URLs.",
    28: "Dictionary app — A simple application that provides word definitions and synonyms.",
    29: "Translator — An application that translates text between different languages.",
    30: "Calendar app — A simple calendar to manage events.",
    31: "Stopwatch — A tool to measure elapsed time.",
    32: "Music player — A simple application to play audio files.",
    33: "Movie database — An app that shows movie info, ratings, and reviews.",
    34: "Book tracker — An application to track books read.",
    35: "Task reminder — An application to send reminders for tasks.",
    36: "Simple poll bot — A bot for creating and answering polls.",
    37: "Voting app — An application to conduct votes and elections.",
    38: "Weather notifier — A bot that sends weather updates.",
    39: "Stock price checker — An app to track stock prices.",
    40: "News aggregator — An app that collects and shows news articles.",
    41: "RSS reader — An app to read RSS feeds.",
    42: "Random quote bot — A bot that sends random quotes.",
    43: "Simple drawing app — A basic drawing application.",
    44: "Meme generator — A tool to create memes by adding text to images.",
    45: "Text encryptor — A tool to encrypt and decrypt text.",
    46: "Text analyzer — A tool to analyze text for readability and word count.",
    47: "Palindrome checker — A tool to check if a text is a palindrome.",
    48: "Prime number finder — A tool to find prime numbers in a range.",
    49: "Tic-tac-toe game — A simple two-player game.",
    50: "Hangman game — A word guessing game.",
    51: "Rock-paper-scissors — A simple game against the computer.",
    52: "Simple survey bot — A bot for creating and taking surveys.",
    53: "Feedback collector — An app to gather user feedback.",
    54: "Simple e-commerce — A basic online store.",
    55: "Shopping list — An app to manage shopping lists.",
    56: "Budget planner — An app to track and plan budgets.",
    57: "Simple forum — A basic discussion board.",
    58: "Guestbook — A digital guestbook for messages.",
    59: "Simple wiki — A collaborative article system.",
    60: "File uploader — An app to upload and share files.",
    61: "Image resizer — A tool to resize images.",
    62: "PDF merger — A tool to combine PDF files.",
    63: "Simple calendar — A basic calendar.",
    64: "Event scheduler — An app to schedule events.",
    65: "Birthday reminder — A reminder for birthdays.",
    66: "Simple messenger — A basic messaging app.",
    67: "Simple API — A basic API for developers.",
    68: "Random name generator — A tool to generate random names.",
    69: "Simple chatbot — A basic chatbot app.",
    70: "Simple search engine — A basic web search app.",
    71: "Simple web scraper — An app to extract data from websites.",
    72: "Simple dashboard — A dashboard for metrics.",
    73: "Simple analytics — An analytics tool for data.",
    74: "Simple leaderboard — A ranking display system.",
    75: "Simple game leaderboard — A leaderboard for games.",
    76: "Simple multiplayer game — A basic online multiplayer game.",
    77: "Simple puzzle game — A basic puzzle challenge.",
    78: "Simple maze game — A maze navigation game.",
    79: "Simple matching game — A memory matching game.",
    80: "Simple memory game — A memory training game.",
    81: "Simple card game — A basic card game.",
    82: "Simple dice roller — A dice rolling tool.",
    83: "Simple lottery picker — A random lottery number picker.",
    84: "Simple voting system — A voting system app.",
    85: "Simple ticket system — A ticket tracking system.",
    86: "Simple booking system — An appointment booking app.",
    87: "Simple reservation system — A reservation management app.",
    88: "Simple calendar sync — A tool to sync events with calendars.",
    89: "Simple email sender — A basic email sending tool.",
    90: "Simple SMS sender — A tool to send SMS messages.",
    91: "Simple notification bot — A bot for sending notifications.",
    92: "Simple reminder bot — A reminder sending bot.",
    93: "Simple timer bot — A countdown timer bot.",
    94: "Simple stopwatch bot — A stopwatch bot.",
    95: "Simple countdown bot — A bot to count down to events.",
    96: "Simple weather bot — A weather update bot.",
    97: "Simple news bot — A bot for sending news updates.",
    98: "Simple RSS bot — A bot for RSS updates.",
    99: "Simple quote bot — A bot for random quotes.",
    100: "Simple joke bot — A bot for random jokes.",
    101: "Simple trivia bot — A trivia question bot.",
    102: "Simple quiz bot — A quiz-taking bot.",
    103: "Simple poll bot — A polling bot.",
    104: "Simple survey bot — A survey-taking bot.",
    105: "Simple feedback bot — A feedback collection bot.",
    106: "Simple suggestion bot — A suggestion collection bot."
}

# --- Commands & Handlers ---

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Assalomu alaykum\nNa gap?")

@dp.message(Command("salom"))
async def cmd_salom(message: Message):
    await message.reply("Vaaleykum Assalom!")

@dp.message(F.text.lower() == "assalomu alaykum")
async def cmd_na_gap(message: Message):
    await message.reply("Valeykum Assalom!")

# Save any photo to ./downloads with username + timestamp
@dp.message(F.photo)
async def photo_handler(message: Message):
    photo = message.photo[-1]  # largest size
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    username = message.from_user.username or str(message.from_user.id)
    filename = f"{username}_{photo.file_unique_id}_{timestamp}.jpg"
    path = os.path.join(SAVE_PATH, filename)

    await bot.download(photo, destination=path)
    await message.answer(f"✅ Rasm saqlandi: {path}")

# List all ideas (1..106)
@dp.message(Command("idea"))
async def cmd_idea(message: Message):
    lines = []
    # print in numeric order
    for i in range(1, len(RESPONSES) + 1):
        name = RESPONSES[i].split(" — ")[0]
        lines.append(f"{i}. {name}")
    await message.answer(
        "100+ Simple Project Ideas:\n" + "\n".join(lines) + "\n\nSend /choose <number> to select an idea."
    )

# /choose NUMBER → same text as sending NUMBER
@dp.message(Command("choose"))
async def cmd_choose(message: Message):
    parts = message.text.split()
    if len(parts) != 2 or not parts[1].isdigit():
        await message.reply("Usage: /choose <number>")
        return

    num = int(parts[1])
    text = RESPONSES.get(num)
    if text:
        await message.reply(text)
    else:
        await message.reply(f"Invalid number. Please choose between 1 and {len(RESPONSES)}.")

# Plain number messages (e.g. "5")
@dp.message(F.text.regexp(r"^\d+$"))
async def number_handler(message: Message):
    num = int(message.text)
    text = RESPONSES.get(num)
    if text:
        await message.reply(text)
    else:
        await message.reply(f"Noto‘g‘ri raqam. 1..{len(RESPONSES)} orasidan tanlang.")

# --- Runner ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nGoodbye")
