import random

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message


async def user_start(message: Message):
    await message.reply("Hello, users!")


async def new_random(message: Message, state: FSMContext):
    await message.reply("Пришли мне список из которого надо выбрать рандомным образом\n\n"
                        "В первой строчке то что надо указать перед выбранным юнитом, пример:\n\n"
                        "<code>Что буду делать\nПроект\nСтатью\nУчить текст\nУзнавать новую информацию</code>")
    await state.set_state("get_random_list")


async def get_random_list(message: Message, state: FSMContext):
    random_list = message.text.split("\n")
    text_answer = random_list[0] + ": "
    random_id = random.randint(1, len(random_list) - 1)
    text_answer += random_list[random_id]
    await message.answer(text_answer)
    await state.reset_state(with_data=False)


def register_user(dp: Dispatcher):
    dp.register_message_handler(get_random_list, state="get_random_list")

    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(new_random, commands=["new_random"], state="*")
