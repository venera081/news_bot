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
from forms.user import Form
from aiogram.fsm.context import FSMContext

router = Router()

@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer("Let's start filling in the form!\nFirst of all enter your name:")
    await state.set_state(Form.name)

@router.message(Command("cancel"))
async def cancel_form(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Bio canceled!")

@router.message(Form.name, F.text)
async def proccess_name(message: Message, state:FSMContext):
    await state.update_data(name=message.text)

    await message.answer("Amazing!\n And enter your age:")
    await state.set_state(Form.age)

@router.message(Form.age, F.text)
async def proccess_age(message: Message, state:FSMContext):
    if not message.text.isdigit():
        await message.answer("Age must be digit")
        return
        
    if int(message.text) < 12 or int(message.text) > 100:
        await message.answer("Age must be from 12 to 100")
        return
    
    await state.update_data(age=int(message.text))

    await message.answer("Excellent!\n Then enter your email:")
    await state.set_state(Form.email)

@router.message(Form.email, F.text)
async def proccess_email(message: Message, state:FSMContext):
    email_text = message.text
    if "@" not in email_text or "gmail.com" not in email_text:
        await message.answer("Email doesn't correct")
        return
    
    await state.update_data(email=email_text)

    data = await state.get_data()
    name = data["name"]
    age = data["age"]
    email = data["email"]

    await message.answer(f"Your bio is ready\nName: {name}\nAge: {age}\nEmail: {email}")
    await state.clear()

