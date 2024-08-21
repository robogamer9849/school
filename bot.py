from bale import *
from botoken import *

client = Bot(token=taha)

@client.event
async def on_ready():
    print(client.user.username, "is Ready!")

@client.event
async def on_update(update: Update):
    print(update.update_id)

@client.event
async def on_message(message: Message):
    if message.content == '/start':
        file = open('images.png', 'rb').read()
        photo = InputFile(file)
        return await message.reply_photo(photo = photo, caption= f'Hi, {message.author.first_name}!\nuse /help for command list')

    elif message.content == '/help':
        await message.reply('/start\n/help\n/name\n/about\n/my_info')

    elif message.content == '/name':
        reply_markup = InlineKeyboardMarkup()
        reply_markup.add(InlineKeyboardButton(text="github", url="https://github.com/robogamer9849"))
        await message.reply('im taha\n',
        components=reply_markup
        )

    elif message.content == '/about':
        await message.reply('a bot that can help you with everything')

    elif message.contact == '/my_info' :
        await message.reply(f'here is your bale account info:\n{message.author}')

    else:
        await message.reply('no command found')

client.run()
