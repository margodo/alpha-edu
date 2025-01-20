import requests
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
from sql_db import QuoteDB
from secret_key import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

database = QuoteDB()
message_quote_data = {}

async def get_random_quote():
    response = requests.get('https://zenquotes.io/api/random')
    quote_data = response.json()
    quote = quote_data[0]['q']
    author = quote_data[0]['a']
    return quote, author

def get_quote_buttons():
    markup = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text='👍 Like', callback_data='like')],
        [types.InlineKeyboardButton(text='👎 Dislike', callback_data='dislike')]
    ])
    return markup

@dp.message(Command("random-quote"))
async def send_welcome(message: types.Message):
    quote, author = await get_random_quote()
    markup = get_quote_buttons()
    message_quote_data['author'] = author
    message_quote_data['quote'] = quote
    await message.reply("Here's a quote for you:")
    await message.answer(f"\"{quote}\"\n\n- {author}", reply_markup=markup)

@dp.callback_query(F.data == 'like')
async def handle_like(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    author, quote = message_quote_data['author'], message_quote_data['quote']
    database.save_quote(user_id, quote, author)
    await callback_query.answer("Quote saved!")

@dp.callback_query(F.data == 'dislike')
async def handle_dislike(callback_query: types.CallbackQuery):
    await callback_query.answer("Quote removed.")
    await callback_query.message.delete()

@dp.message(Command("saved-quotes"))
async def show_saved_quotes(message: types.Message):
    user_id = message.from_user.id
    saved_quotes = database.get_saved_quotes(user_id)
    
    if saved_quotes:
        formatted_quotes = "\n\n".join([f"\"{quote[0]}\" - {quote[1]}" for quote in saved_quotes])
        await message.answer(f"Here are your saved quotes:\n\n{formatted_quotes}")
    else:
        await message.answer("You haven't saved any quotes yet.")

async def main():
    print('Started the bot')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())