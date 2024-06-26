# import asyncio
from aiogram import Router, F
# from aiogram.types import Message
# from aiogram.filters import CommandStart
# from aiogram.filters import Command
# from aiogram.fsm.context import FSMContext
#
# from src.bot.keyboards.builders.user import form_btn
# from src import db
# # from src.bot.keyboards.reply import main_kb, rmk
# # from .utils.city import check
# #
# # from data.database import DataBase
# from src.bot.utils.states import Form
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
#
router = Router()
#
#
# @router.message(Command('reg'))
# async def my_form(message: Message, state: FSMContext, db: db = db):
#
#     if not await asyncio.gather(db.select.user_exists(message.from_user.id)):
#         data = await db.select.get_users(message.from_user.id)
#         usr = data.one()
#         pattern = {
#             "photo": usr.photo,
#             "caption": f"{usr.name} {usr.age}, {usr.city}\n{usr.bio}"
#         }
#
#         await message.answer_photo(**pattern, reply_markup=main)
#     else:
#         await state.set_state(Form.name)
#         await message.answer(
#             "Отлично, введи своё имя",
#             reply_markup=form_btn(message.from_user.first_name)
#         )
#
#
# @router.message(Form.name)
# async def form_name(message: Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     # await state.set_state(Form.age)
#     await state.set_state(Form.sex)
#     await message.answer(
#                 "Теперь давай определимся с полом",
#                 reply_markup=form_btn(["Парень", "Девушка"])
#             )
#     # await message.answer("Теперь укажи свой возраст", reply_markup=rmk)
#
#
# # @profile.message(Form.age)
# # async def form_age(message: Message, state: FSMContext):
# #     if str(message.text).isdigit():
# #         await state.update_data(age=int(message.text))
# #         await state.set_state(Form.city)
# #         await message.answer("Теперь укажи свой город")
# #     else:
# #         await message.answer("Попробуй еще раз!")
# #
# #
# # @profile.message(Form.city)
# # async def form_city(message: Message, state: FSMContext):
# #     city_exists = await check(message.text)
# #     if city_exists:
# #         await state.update_data(city=message.text)
# #         await state.set_state(Form.sex)
# #         await message.answer(
# #             "Теперь давай определимся с полом",
# #             reply_markup=form_btn(["Парень", "Девушка"])
# #         )
# #     else:
# #         await message.answer("Попробуй еще раз!")
#
#
# @router.message(Form.sex, F.text.casefold().in_(["парень", "девушка"]))
# async def form_sex(message: Message, state: FSMContext):
#     await state.update_data(sex=message.text)
#     # await state.set_state(Form.look_for)
#     await state.set_state(Form.photo)
#     # await message.answer(
#     #     "Кого ты предпочитаешь искать?",
#     #     reply_markup=form_btn(["Парни", "Девушки", "Мне все равно"])
#     # )
#
#
# @router.message(Form.sex)
# async def incorrect_form_sex(message: Message, state: FSMContext):
#     await message.answer("Выбери один вариант!")
#
#
# @router.message(
#     Form.look_for,
#     F.text.casefold().in_(["девушки", "парни", "мне все равно"])
# )
# # async def form_look_for(message: Message, state: FSMContext):
# #     await state.update_data(look_for=message.text)
# #     await state.set_state(Form.about)
# #     await message.answer("Теперь расскажи о себе", reply_markup=rmk)
# #
# #
# # @profile.message(Form.look_for)
# # async def incorrect_form_look_for(message: Message, state: FSMContext):
# #     await message.answer("Выбери один вариант!")
# #
# #
# # @profile.message(Form.about)
# # async def form_about(message: Message, state: FSMContext):
# #     await state.update_data(bio=message.text)
# #     await state.set_state(Form.photo)
# #     await message.answer("Теперь отправь фото")
#
#
# @router.message(Form.photo, F.photo)
# async def form_photo(message: Message, state: FSMContext, db: db = db):
#     phid = message.photo[-1].file_id
#     print(message)
#     data = await state.get_data()
#     # data["user_id"] = message.from_user.id
#     # data["photo"] = phid
#     print(phid)
#     await db.update.edit_user(message)
#     # await db.insert(**data)
#     await state.clear()
#     frm_text = []
#     [
#         frm_text.append(f"{value}")
#         for key, value in data.items()
#         if key not in ["user_id", "photo"]
#     ]
#     await message.answer_photo(phid, "\n".join(frm_text))
#
#
# @router.message(Form.photo, ~F.photo)
# async def form_photo(message: Message, state: FSMContext):
#     await message.answer("Отправь фото!")