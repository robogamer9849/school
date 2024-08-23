from bale import *
from botoken import *
from pathlib import Path

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
        keyboardMarkup = MenuKeyboardMarkup()
        keyboardMarkup.add(keyboard_button = MenuKeyboardButton(text = 'send my location', request_location=True))
        keyboardMarkup.add(keyboard_button = MenuKeyboardButton(text = 'send my contact', request_contact=True))
        await message.reply(f'Hi, {message.author.first_name}!\nuse /help for command list',
                            components= keyboardMarkup)



    elif message.content == '/help':
        try:
            path = Path(__file__).parent.resolve()/'images.png'
            file = open(file = path,mode = 'rb').read()
            img = InputFile(file = file, file_name = 'images.png')
            await message.reply_photo(photo = img, caption = '/start\n/help\n/name\n/about\n/my_info')
        except APIError as e:
            print(f"Error sending photo: {e}")
            await message.reply('/start\n/help\n/name\n/about\n/my_info\n\ncant send photo')

    elif message.content == '/name':
        reply_markup = InlineKeyboardMarkup()
        reply_markup.add(inline_keyboard_button = InlineKeyboardButton(text="github", url="https://github.com/robogamer9849"), row = 1)
        reply_markup.add(inline_keyboard_button = InlineKeyboardButton(text="API", url="python-bale-bot.ir"), row = 2)
        await message.reply('im taha, a student from mofid\n',
        components=reply_markup
        )

    elif message.content == '/about':
        await message.reply('a bot that can help you with a lot of things!')

    elif message.content == '/my_info' :
        await message.reply(f'here is your bale account info:\n{message.author}')

    else:
        await message.reply('no command found')

client.run()
