from aiogram import executor
from create_bot import dp
from handlers.admin_handlers import register_admin_handlers

register_admin_handlers()
if __name__ == '__main__':
    executor.start_polling(skip_updates=True,dispatcher=dp)
