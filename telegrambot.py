import telegram

text = "Hello"
bot = telegram.Bot(token="TELEGRAM_BOT_TOKEN")
bot.send_message(chat_id="TELEGRAM_CHAT_ID", text=(f'Your Text: {text}'))