from aiogram import F, types, Router
from  aiogram.filters import CommandStart, Command, or_f
from filters.chat_types import ChatTypeFilter

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))



@user_private_router.message(or_f(CommandStart(), F.text.lower().contains('старт') ))
async def start_cmd(message: types.Message):
    await message.answer('Это была команда старт')


@user_private_router.message(or_f(Command('menu'), F.text.lower().contains('меню') ))
async def menu(message: types.Message):
    await message.answer('Вот меню:')


@user_private_router.message(or_f(Command('about'), F.text.lower().contains('о нас') | F.text.lower().contains('о вас')))
async def about(message: types.Message):
    await message.answer('Вот информация о нас')
    
@user_private_router.message(or_f(Command('payment'), F.text.lower().contains('оплат') ))
async def about(message: types.Message):
    await message.answer('Варианты оплаты:')

# через or_f или можно так!
@user_private_router.message((F.text.lower().contains('доставк')) | F.text.lower().contains('варианты доставки'))
@user_private_router.message(Command('shipping'))
async def about(message: types.Message):
    await message.answer('Варианты доставки:')