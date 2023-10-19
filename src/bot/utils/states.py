from aiogram.filters.state import State, StatesGroup
# from aiogram.fsm.context import FSMContext


# State Machine
class Form(StatesGroup):
    telegram_id = State()
    event_id = State()
    event_is_now = State()
    name = State()
    age = State()
    city = State()
    sex = State()
    look_for = State()
    about = State()
    photo = State()

