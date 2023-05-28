import telegram
from telegram.ext import Updater, CommandHandler

# Define your Telegram bot token
TOKEN = '6289400535:AAHg3UrXFlhQltk5cw8Qi9YvD8l-x_p6dIM'

# Create an instance of the Updater class
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bot started!")

# Define a function to handle incoming messages
def handle_message(update, context):
    # Extract the message text
    message_text = update.message.text

    # Parse the message text and extract relevant information
    entry = ''
    stoploss = ''
    takeprofits = []
    
    lines = message_text.strip().split('\n')
    for line in lines:
        if line.startswith('EURUSD Sell entry at'):
            entry = line.split('=')[1].strip()
        elif line.startswith('Stoploss ='):
            stoploss = line.split('=')[1].strip()
        elif line.startswith('Takeprofit'):
            parts = line.split('=')
            takeprofit = parts[1].strip()
            takeprofits.append(takeprofit)
    
    # Format the extracted information
    formatted_message = f"SELL LIMIT EURUSD\nEntry {entry}\nSL {stoploss}\n"
    formatted_message += '\n'.join([f"TP {tp}" for tp in takeprofits])

    # Send the formatted message back to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=formatted_message)

# Register the handlers
start_handler = CommandHandler('start', start)
message_handler = telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()
updater.idle()
