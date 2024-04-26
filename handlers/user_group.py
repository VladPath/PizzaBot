from string import punctuation

from aiogram import F, types, Router
from handlers.restricted import restricted_words
from filters.chat_types import ChatTypeFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))

def clean_text(text:str):
    return text.translate(str.maketrans('','',punctuation))

    

@user_group_router.edited_message()
@user_group_router.message()
async def cleaner(message: types.Message):
    if restricted_words.intersection(clean_text(message.text.lower()).split()):
        await message.answer(f'{message.from_user.first_name} Соблюдайте порядок в чате!')
        await message.delete()
    




