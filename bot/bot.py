import constants as keys
import responses as r
from telegram import Update
from telegram.ext import *
from views import *

print("Bot is waking up.")

async def start_command(update: Update, context: CallbackContext):
    await update.message.reply_text('Type something to get started')

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text('I will do my best!')

async def end_command(update: Update, context: CallbackContext):
    await update.message.reply_text('Goodbye')
    return ConversationHandler.END

async def echo_command(update: Update, context: CallbackContext) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def error_handler(update: Update, context: CallbackContext):
    print(f"Update {update} caused an error {context.error}")

def main():
    application = Application.builder().token(keys.API_KEY).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start_command)],
        states={
        },
        fallbacks=[CommandHandler("end", end_command)],
        run_async=True
    )

    # application.add_handler(CommandHandler("start", start_command))
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("end", end_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_command))
    application.add_handler(MessageHandler(filters.TEXT, handle_command))
    application.add_error_handler(error_handler)
    application.run_polling(stop_signals=None)

if __name__ == "__main__":
    main()
