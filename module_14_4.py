from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import TOKEN
from my_keyboards import *
from crud_functions import *
import logging

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

get_all_products()

logging.basicConfig(level=logging.INFO, filename="calories_index_inline.log", encoding="UTF-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")


class UserState(StatesGroup):
    age = State()
    gender = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name or ""
    await message.reply(f"Привет, {first_name} {last_name}. Хотите рассчитать суточную норму калорий?"
                        f"Нажмите на кнопку 'Рассчитать'", reply_markup=kb)
    logging.info(f"Производится расчет для {first_name} {last_name}")


@dp.message_handler(text=["Информация"])
async def info(message):
    await message.answer("Этот бот рассчитает необходимую норму калорий в сутки, а также индекс массы вашего тела.\n"
                         "Для начала работы нажмите кнопку 'Рассчитать'")


@dp.message_handler(text=["Рассчитать"])
async def main_menu(message):
    await message.answer("Выберите опцию", reply_markup=kb_inline)


@dp.message_handler(text=["Купить витамины"])
async def buying_list(message):
    for i in range(0, 4):
        vitamins = get_all_products()[i]
        await message.answer(f'Название: {vitamins[1]} | Описание: {vitamins[2]} | Цена: {vitamins[3]}')
        with open(f"{i+1}.png", "rb") as img:
            await message.answer_photo(img)
    await message.answer("Выберите продукт для покупки", reply_markup=kb_inline_buy)


@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer("Упрощенная формула Миффлина - Сан Жеора\n"
                              "для женщин:\n"
                              "вес(кг) х 10 + рост(см) х 6.25 - возраст(лет) х 5 - 161\n"
                              "для мужчин:\n"
                              "вес(кг) х 10 + рост(см) х 6.25 - возраст(лет) х 5 + 5\n"
                              "Индекс массы тела (BMI):\n"
                              " вес(кг) : (рост(м)²)")
    await call.answer()


@dp.callback_query_handler(text=["calories"])
async def set_age(call):
    await call.message.answer("Введите свой возраст, пожалуйста")
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_gender(message, state):
    await state.update_data(age=message.text)
    await message.answer("Укажите ваш пол (м/ж)")
    await UserState.gender.set()


@dp.message_handler(state=UserState.gender)
async def set_growth(message, state):
    await state.update_data(gender=message.text.lower())
    await message.answer("Введите свой рост в см")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    index = round(float(data['weight']) * 10000 / float(data['growth']) ** 2, 1)
    calories = int(data['weight']) * 10 + float(data['growth']) * 6.25 - int(data['age']) * 5
    if index <= 16:
        bmi = "выраженный дефицит массы тела"
    elif 16 < index <= 18.5:
        bmi = "дефицит массы тела"
    elif 18.5 < index <= 25:
        bmi = "норма"
    elif 25 < index <= 30:
        bmi = "избыточная масса тела"
    elif 30 < index <= 35:
        bmi = "ожирение первой степени"
    elif 35 < index <= 40:
        bmi = "ожирение второй степени"
    elif 40 < index:
        bmi = "ожирение третьей степени"
    if data["gender"] == "м":
        await message.answer(f"Необходимый рацион килокалорий в день для мужчин: {calories + 5}\n"
                             f"Расчет калорийности производится по упрощенной формуле Миффлина - Сан Жеора.\n"
                             f"Индекс массы тела {index} - у вас {bmi}.")
    else:
        await message.answer(f"Необходимый рацион килокалорий в день для женщин: {calories - 161}\n"
                             f"Расчет калорийности производится по упрощенной формуле Миффлина - Сан Жеора.\n"
                             f"Индекс массы тела {index} - у вас {bmi}.")

    logging.info(f"Расчет произведен")

    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
