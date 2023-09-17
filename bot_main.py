from pyrogram import Client, filters
import random


API_TOKEN = "6518779627:AAFbGiUhVkjNDAOZZeuRX1alp4RViqs7uf4"

one_bot = Client("Test_bot", api_id=12345, api_hash="API_HASHINGIZ", bot_token=API_TOKEN)

@one_bot.on_message(filters.command("start"))
def start_command(client, message):
    message.reply_text("Assalomu alaykum! Matematikaga oid testimizga xush kelibsiz!")

@one_bot.on_message(filters.command("test"))
def test_command(client, message):
    amallar = {
        '90 + 45': 135,
        '2 * 3': 6,
        '99 - 80': 19,
        '175 / 5': 35,
        '10 ** 2': 20
    }

    savol = random.choice(list(amallar.keys()))
    answer = amallar[savol]

    message.reply_text(f"{savol} = ?")

    @one_bot.on_message(filters.text)
    def check_answer(client, message):
        javob = message.text.strip()
        if javob.isdigit() and int(javob) == answer:
            message.reply_text("To'g'ri javob!")
        else:
            message.reply_text(f"Noto'g'ri javob. To'g'ri javob {answer} bo'lishi kerak.")

one_bot.run()