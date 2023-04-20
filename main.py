import telebot
from pytube import YouTube


bot = telebot.TeleBot('6168292227:AAGtmg4vcdt91v5NqodA_zb5QbtRA11wXUk')


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привіт! Відправ мені посилання на відео на YouTube і я скачаю його для тебе.")
    bot.register_next_step_handler(message,download_video)

def download_video(message):
    try:
        yt = YouTube(message.text)
        video = yt.streams.get_highest_resolution()
        video.download()
        # Скачане відео, відкриваєм і висилаєм в бота
        with open(video.default_filename, 'rb') as video_file:
            bot.send_video(message.chat.id, video_file)

        bot.reply_to(message, "Відео успішно завантажено та відправлено в чат!")
    except Exception as e:
        bot.reply_to(message, f"Error, попробуйте ще раз /start")


bot.polling(none_stop=True)


