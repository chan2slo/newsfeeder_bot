from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('안녕하세요! 에코 봇입니당!!!!!!')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

def main() -> None:
    app = Application.builder().token('7065509074:AAGF2BwkxIK7zBEWfsBH29Ml7DXYPGEd03k').build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    app.run_polling()

if __name__ == '__main__':
    main()