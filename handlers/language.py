from aiogram import Router, F
from aiogram.types import Message
from handlers.db import set_lang

router = Router()

LANG_MAP = {
    "🇷🇺 Русский": "ru",
    "🇬🇧 English": "en",
    "🇰🇬 Кыргызча": "ky",
    "🇰🇿 Қазақша": "kk",
    "🇺🇿 O'zbek": "uz",
    "🇹🇯 Тоҷикӣ": "tg",
    "🇸🇦 العربية": "ar",
    "🇫🇷 Français": "fr",
    "🇩🇪 Deutsch": "de",
    "🇮🇹 Italiano": "it",
    "🇰🇷 한국어": "ko",
    "🇯🇵 日本語": "ja",
    "🇨🇳 中文": "zh",
    "🇪🇸 Español": "es",
}


@router.message(F.text.in_(LANG_MAP.keys()))
async def choose_lang(message: Message):
    lang_code = LANG_MAP[message.text]
    print("LANG ROUTER LOADED")

    await set_lang(message.from_user.id, lang_code)

    await message.answer(f"🌍 Language set: {lang_code}")