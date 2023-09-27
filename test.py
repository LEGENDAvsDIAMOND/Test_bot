import telebot
import random


TOKEN = '6518779627:AAFbGiUhVkjNDAOZZeuRX1alp4RViqs7uf4'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Assalomu alaykum! Matematik amallardan iborat botimizga xush kelibsiz!😊")

@bot.message_handler(commands=['test'])
def test(message):
    operations = {
        '187 + 89': 276,
        '12 * 3': 36,
        '175 - 108': 67,
        '98 / 16': 6.125,
        '3 ** 2': 9
    }

    question = random.choice(list(operations.keys()))
    correct_answer = operations[question]

    bot.send_message(message.chat.id, f"Question: {question} = ?")

    @bot.message_handler(func=lambda message: True)
    def check_answer(message):
        user_answer = message.text.strip()
        if user_answer.isdigit() and int(user_answer) == correct_answer:
            bot.send_message(message.chat.id, "Barakalla! Javobingiz to'g'ri👍")
        else:
            bot.send_message(message.chat.id, f"Afsus, javobingiz noto'g'ri😞 To'g'ri javob {correct_answer}.")

    bot.register_next_step_handler(message, check_answer)

bot.polling()


