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
    if '/q1' in message.text:
        await message.reply(ariphmetika_kr.question_one())
    if '/q5' in message.text:
        a, b = map(int, message.text.replace('/q5', '').strip().split())
        res = ariphmetika_kr.question_five(a, b).split('splitplace')[:-1]
        for i in res:
            await message.reply(i)
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
