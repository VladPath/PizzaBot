активация venv 'source venv/bin/activate'

Создаю телеграм бота 
типы ответов: 
пишет в личку - await bot.send_message(message.from_user.id, 'Сейчас будет Эхо'
отвечает в чат(группу) - await message.answer(message.text)

шаг 1:
    создать через FatherBot
    создать venv 'python3 -m venv venv'
    
    Создается файл (name).py 
    импортируется:
    import asyncio - для ассинхроного программирования 
    import os
    from aiogram import Bot, types, Dispatcher - для вводных данных
    from  aiogram.filters import CommandStart - для /start

# PizzaBot
