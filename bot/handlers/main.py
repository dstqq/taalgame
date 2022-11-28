from aiogram import Dispatcher

from bot.handlers.user import register_users_handlers
# from bot.handlers.admin import register_admin_handlers


def register_all_handlers(dp: Dispatcher) -> None:
    # handlers = (
    #     # register_admin_handlers,
    #     register_users_handlers
    # )
    # for handler in handlers:
    #     handler(dp)
    register_users_handlers(dp)