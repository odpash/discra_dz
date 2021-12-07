from aiogram import Bot, Dispatcher, executor, types
import ariphmetika_kr

token = "5024416065:AAHPIFc4zSkSorxbdmFllIbh_UE1SWdKrxU"
bot = Bot(token=token)
dp = Dispatcher(bot)



@dp.message_handler()
async def q1(message: types.Message):
    if '/q2' in message.text:
        a, b = map(int, message.text.replace('/q2', '').strip().split())
        await message.reply(ariphmetika_kr.question_two(a, b))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
