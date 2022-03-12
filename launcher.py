import json

from discord.ext.commands import Bot

version = 'v0.1.0'

bot = Bot(command_prefix="~/", self_bot=True)

with open('data/config.json', 'r') as file:
    info = json.loads(file.read())
    user_token = info['user_token']

bot.load_extension('cogs.catch')
bot.load_extension('cogs.utils')

@bot.event
async def on_message(message):
    if not message.author.bot:
        await bot.process_commands(message)

print(f'Persona\nA modularized Discord userbot\nBy Rod of Discord https://github.com/rodofdiscord')
bot.run(f"{user_token}")