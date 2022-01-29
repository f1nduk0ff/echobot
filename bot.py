import config
import logging

from aiogram import Bot, Dispatcher, executor, types

# log level
logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# echo messages
@dp.message_handler()
async def echo(message: types.Message):
	print("INFO:aiogram.bot:New echo_message was sent!")
	await message.answer(message.text)

# run long-poll
if __name__== "__main__":
    executor.start_polling(dp, skip_updates=True)