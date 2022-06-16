import re, asyncio, json, random, string, discord

from discord.ext.commands import Cog, command

with open('data/config.json', 'r') as file:
    info = json.loads(file.read())
    user_token = info['user_token']
    catch_id = info['channel_id']

with open('data/poketwo/pokemon', 'r', encoding='utf8') as file:
    pokemon_list = file.read()
with open('data/poketwo/legendary', 'r') as file:
    legendary_list = file.read()
with open('data/poketwo/mythical', 'r') as file:
    mythical_list = file.read()

class Catching(Cog):
    def __init__(self, bot):
        self.bot = bot

        self.cnum = 0
        self.shiny = 0
        self.legendary = 0
        self.mythical = 0

        self.poketwo = 716390085896962058

    def solve(self, message):
        hint = []
        for i in range(15, len(message) - 1):
            if message[i] != '\\':
                hint.append(message[i])
        hint_string = ''
        for i in hint:
            hint_string += i
        hint_replaced = hint_string.replace('_', '.')
        hint_replaced = hint_replaced.split(' ')[-1]
        solution = re.findall('^'+hint_replaced+'$', pokemon_list, re.MULTILINE)
        return solution

    async def spam(self, channel: discord.TextChannel):
        while True:
            await channel.send("".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=random.randint(20, 30))))
            await asyncio.sleep(random.uniform(1.45, 1.6))

    @command(name="start", aliases=["st"])
    async def start_spam(self, ctx, channel: discord.TextChannel):
        try:
            self.task = self.bot.loop.create_task(self.spam(channel))
            await ctx.send(f'Bot now spamming in channel:\n<#{channel.id}>')
        except:
            await ctx.send(f"The autocatcher cannot start spamming.\n Consider sending `~/stop` and try again.")

    @command(name="stop", aliases=["sp"])
    async def stop_spam(self, ctx):
        try:
            self.task.cancel()
            await ctx.send(f'Bot stopped spamming.')
        except:
            await ctx.send(f"The autocatcher couldn't stop spamming. Try stopping the autocatcher directly.")

    @Cog.listener()
    async def on_ready(self):
        print(f'Logged into account: {self.bot.user.name}')

    @Cog.listener()
    async def on_message(self, message):
        channel_ids = [int(x) for x in catch_id.split(',')]
        if message.channel.id in channel_ids:

            channel = self.bot.get_channel(message.channel.id)
            if message.author.id == self.poketwo:
                if message.embeds:
                    embed_title = message.embeds[0].title
                    if 'wild pokémon has appeared!' in embed_title:
                        await asyncio.sleep(random.uniform(0.45, 0.65))
                        await channel.send('p!h')
                        await asyncio.sleep(random.uniform(1.45, 1.65))
                else:
                    content = message.content
                    if 'The pokémon is ' in content:
                        if not len(self.solve(content)):
                            print('Pokemon not found.')
                        else:
                            for i in self.solve(content):
                                await channel.send(f'p!c {i.lower()}')
                        checked = random.randint(1, 240)
                        if checked == 1:
                            await asyncio.sleep(900)

                    elif 'Congratulations' in content:
                        print(message.content)
                        self.cnum += 1
                        split = content.split(' ')
                        pokemon = split[7].replace('!', '')
                        if 'seem unusual...' in content:
                            self.shiny += 1
                            print(f'Shiny Pokémon caught! Pokémon: {pokemon}')
                            print(f'Shiny - {self.shiny} | Legendary - {self.legendary} | Mythical - {self.mythical}')
                        elif re.findall('^'+pokemon+'$', legendary_list, re.MULTILINE):
                            self.legendary += 1
                            print(f'Legendary Pokémon caught! Pokémon: {pokemon}')
                            print(f'Shiny - {self.shiny} | Legendary - {self.legendary} | Mythical - {self.mythical}')
                        elif re.findall('^'+pokemon+'$', mythical_list, re.MULTILINE):
                            self.mythical += 1
                            print(f'Mythical Pokémon caught! Pokémon - {pokemon}')
                            print(f'Shiny - {self.shiny} | Legendary - {self.legendary} | Mythical - {self.mythical}')
                        else:
                            print(f'Total Pokémon Caught: {self.cnum}')
                    elif 'human' in content:
                        self.task.cancel()
                        print('Captcha detected; autocatcher paused. Press enter to restart, after solving captcha manually.')
                        input()
                        await channel.send('p!h')

def setup(bot):
    bot.add_cog(Catching(bot))