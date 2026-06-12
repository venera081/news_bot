from deep_translator import GoogleTranslator


def t(text: str, lang: str):
    try:
        return GoogleTranslator(source="auto", target=lang).translate(text)
    except:
        return text