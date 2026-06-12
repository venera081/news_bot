from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

lang_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇷🇺 Русский"), KeyboardButton(text="🇬🇧 English")],
        [KeyboardButton(text="🇰🇬 Кыргызча"), KeyboardButton(text="🇰🇿 Қазақша")],
        [KeyboardButton(text="🇺🇿 O'zbek"), KeyboardButton(text="🇹🇯 Тоҷикӣ")],
        [KeyboardButton(text="🇸🇦 العربية"), KeyboardButton(text="🇫🇷 Français")],
        [KeyboardButton(text="🇩🇪 Deutsch"), KeyboardButton(text="🇮🇹 Italiano")],
        [KeyboardButton(text="🇰🇷 한국어"), KeyboardButton(text="🇯🇵 日本語")],
        [KeyboardButton(text="🇨🇳 中文"), KeyboardButton(text="🇪🇸 Español")]
    ],
    resize_keyboard=True
)