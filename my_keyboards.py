from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text="Рассчитать")
button_2 = KeyboardButton(text="Информация")
button_buy = KeyboardButton(text="Купить витамины")
kb.add(button, button_2)
kb.add(button_buy)

kb_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories"),
     InlineKeyboardButton(text="Формулы расчета", callback_data="formulas")]
], resize_keyboard=True)

kb_inline_buy = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Продукт1", callback_data="product_buying"),
     InlineKeyboardButton(text="Продукт2", callback_data="product_buying")],
    [InlineKeyboardButton(text="Продукт3", callback_data="product_buying"),
     InlineKeyboardButton(text="Продукт4", callback_data="product_buying")]
], resize_keyboard=True)
