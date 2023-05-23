import telegram
from telegram.ext import Updater, MessageHandler, Filters

def process_message(update, context):
    message_text = update.message.text
    
    # Check if the message matches the desired pattern
    if "Sell entry" in message_text:
        lines = message_text.split("\n")
        
        # Extract relevant information
        entry = lines[0].split("Sell entry at ")[1]
        take_profit_1 = lines[1].split("Takeprofit 1 = ")[1]
        take_profit_2 = lines[2].split("Takeprofit 2 = ")[1]
        take_profit_3 = lines[3].split("Takeprofit 3 = ")[1]
        stop_loss = lines[4].split("Stoploss = ")[1]
        
        # Format the extracted information
        response = f"SELL LIMIT EURUSD\nEntry {entry}\nSL {stop_loss}\nTP {take_profit_1}\nTP {take_profit_2}\nTP {take_profit_3}"
        
        # Send the formatted message to the user
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def main():
    # Enter your Telegram bot token here
    token = '6289400535:AAHg3UrXFlhQltk5cw8Qi9YvD8l-x_p6dIM'
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher
    
    # Register the message handler
    message_handler = MessageHandler(Filters.text, process_message)
    dispatcher.add_handler(message_handler)
    
    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
