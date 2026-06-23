from aiogram import Router, F
from aiogram.types import Message
from handlers.keyboards import lang_kb
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message,
    CallbackQuery,
    ReplyKeyboardMarkup, 
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


router = Router()

def get_main_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="AboutBot")],
            [KeyboardButton(text="Start"), KeyboardButton(text="Help")]
        ],
        resize_keyboard=True
    )

    return keyboard

def get_main_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Open website", url="https://www.bbc.com/news")]
            [InlineKeyboardButton(text="learn more", callback_data="info_more")]
        ]
    )

    return keyboard

@router.callback_query(lambda c: c.data == "info_more")
async def proccess_more_info(callback: CallbackQuery):
    await callback.message.answer("More detail info....")
    await callback.answer()

@router.message(CommandStart())
@router.message(F.text.lower() == "старт")
async def start(message: Message):
    await message.answer(
        "Hi I'm bot for _news_. \n\n🌍 *Choose* *language* in your keyboard",
          reply_markup=lang_kb,
          parse_mode="Markdown",
          reply_markup=get_main_inline_keyboard())

@router.message(Command("help"))
async def help(message: Message):
    await message.answer("Commands:\n/start - launch bot\n/help - list of commands",
                         reply_markup=get_main_reply_keyboard())
    
@router.message()
async def misunderstand(message: Message):
    await message.answer("Sorry, I can't understand write /help to watch comands")
