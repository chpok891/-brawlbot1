from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "7314156880:AAFkiUyDKce4QzNm12DKG4i9Id6acMg9MDU"

# Старт
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Профиль", "Помощь"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Привет! Я бот с базовыми функциями.", reply_markup=reply_markup)

# Хелп
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Список команд:
/start — запустить бота
/help — помощь")

# Ответ на кнопки
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "профиль" in text:
        await update.message.reply_text("🔐 Это твой профиль. (Заглушка)")
    elif "помощь" in text:
        await help_command(update, context)
    else:
        await update.message.reply_text("Я не понял сообщение. Нажми одну из кнопок ниже.")

# Запуск
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
