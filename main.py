import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode

# ➤ Заміни ці значення:
BOT_TOKEN = os.getenv("7676603214:AAGDNVjOjOh2kbG8jqfLRBcctBiNe-HQb-s")  # токен з BotFather
GROUP_ID = os.getenv("1002352802922")    # ID твоєї групи в Telegram (має бути типу: -1001234567890)

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

# Стан машини для оголошення
class AdForm(StatesGroup):
    text = State()

@dp.message(F.text == "/додати")
async def start_add(message: Message, state: FSMContext):
    await message.answer("✍️ Введіть текст оголошення:")
    await state.set_state(AdForm.text)

@dp.message(AdForm.text)
async def receive_ad(message: Message, state: FSMContext):
    ad_text = message.text
    user = message.from_user.full_name
    final_text = f"<b>📢 Оголошення від {user}:</b>\n\n{ad_text}"
    
    # Надсилаємо в групу
    await bot.send_message(chat_id=int(GROUP_ID), text=final_text)
    await message.answer("✅ Оголошення надіслано!")
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
