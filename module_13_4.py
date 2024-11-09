from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import TOKEN
import logging


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO, filemode="a", filename="calories.log", encoding="UTF-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name or ""
    await message.reply(f"Привет, {first_name} {last_name}. Хотите рассчитать суточную норму калорий?"
                        f"Отправьте мне запрос 'Calories'")
    logging.info(f"Производится расчет для {first_name} {last_name}")


@dp.message_handler(text=["Calories"])
async def set_age(message):
    await message.answer("Введите свой возраст, пожалуйста")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
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
    await message.answer(f"Необходимый рацион килокалорий в день для женщин:"
                         f"{int(data['weight']) * 10 + float(data['growth']) * 6.25 - int(data['age']) * 5 - 161}\n"
                         f"для мужчин:"
                         f"{int(data['weight']) * 10 + float(data['growth']) * 6.25 - int(data['age']) * 5 + 5}\n"
                         f"Расчет калорийности производится по упрощенной формуле Миффлина - Сан Жеора.")
    logging.info(f"Расчет произведен ")

    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
