from aiogram import Bot, Dispatcher, executor, types
import ariphmetika_kr
import main

token = "5024416065:AAHPIFc4zSkSorxbdmFllIbh_UE1SWdKrxU"
bot = Bot(token=token)
dp = Dispatcher(bot)



@dp.message_handler()
async def q1(message: types.Message):
    if '/start' in message.text:
        await message.reply("CMD:\n/q1\n/q2 a b\n/q3\n/q4 a b\n/q5")
    elif '/q2' in message.text:
        a, b = map(int, message.text.replace('/q2', '').strip().split())
        await message.reply(ariphmetika_kr.question_two(a, b))
    elif "/m" in message.text:
        await message.reply('https://books.ifmo.ru/file/pdf/638.pdf')
    elif '/q5' in message.text:
        for i in range(1, 5):
            await bot.send_photo(message.chat.id, open(f'{i}.png', 'rb'))
    elif '/q1' in message.text:
        await message.reply(ariphmetika_kr.question_one())
    elif '/q4' in message.text:
        a, b = map(int, message.text.replace('/q4', '').strip().split())
        res = ariphmetika_kr.question_four(a, b).split('splitplace')[:-1]
        for i in res:
            await message.reply(i)
    elif '/q3' in message.text:
        await message.reply(ariphmetika_kr.question_three())
    elif '/dz' in message.text:
        a, b, r, s = map(int, message.text.replace('/dz', '').strip().split())
        await message.reply(main.main(a, b, r, s))

if __name__ == "__main__":
    while True:
        try:
            executor.start_polling(dp, skip_updates=True)
        except:
            pass