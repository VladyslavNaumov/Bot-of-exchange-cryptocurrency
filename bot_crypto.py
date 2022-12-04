import os
from dotenv import load_dotenv
from pycoingecko import CoinGeckoAPI
from telebot import TeleBot

load_dotenv()  # take environment variables from .env.
"""Insert your token (from BotFather) into the .env file
after it is created, name of the variable is "BOT_TOKEN" """ 

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = TeleBot(token = BOT_TOKEN)
coin_client = CoinGeckoAPI()

"""The user enters the name of the cryptocurrency, 
the function takes the name and looks it up from the 
dictionary key passed from the json from coingeco """
@bot.message_handler(content_types = ['text'])
def message_of_crypto(message):
    crypto_id = message.text
    try:
        price_response = coin_client.get_price(ids = crypto_id, vs_currencies='usd')
        price = price_response[crypto_id]['usd']
        bot.send_message(chat_id=message.chat.id, text= f'Price of {crypto_id} is {price} usd' )       
    except KeyError:
            if crypto_id == '/start': #
                bot.send_message(chat_id = message.chat.id,
                        text = 'If you want to find out the rate of cryptocurrency to USD, \n plese print name of cryptocurrency in lower case')
            else:
                bot.send_message(chat_id=message.chat.id, text= f'CryptoCoin: {crypto_id} wasn`t found')
              
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=1)  # type: ignore