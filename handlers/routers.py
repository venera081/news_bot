from aiogram import Router, F
from aiogram.types import Message
from handlers.keyboards import lang_kb
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Hi I'm bot for _news_. \n\n🌍 *Choose* *language* in your keyboard",
          reply_markup=lang_kb,
          parse_mode="Markdown")

@router.message(Command("help"))
async def help(message: Message):
    await message.answer("Commands:\n/start - launch bot\n/help - list of commands")
    
@router.message()
async def misunderstand(message: Message):
    await message.answer("Sorry, I can't understand write /help to watch comands")
