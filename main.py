from pyrogram import Client
import config

bot = Client(
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    name='my bot'
)

@bot.on_message()
async def echo(bot, message):
    await message.reply(f'u wrote {message.text}')

bot.run()