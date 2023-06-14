import disnake
from disnake.ext import commands
import random

intents = disnake.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.command()
async def mmr(ctx):
    user = ctx.author
    if user.discriminator == '1200':
        random_mmr = random.randint(500, 12000)
    else:
        chance = random.random()
        if chance <= 0.6:
            random_mmr = random.randint(500, 1500)
        elif chance <= 0.9:
            random_mmr = random.randint(2000, 4000)
        else:
            random_mmr = random.randint(5000, 12000)

    if 500 <= random_mmr <= 1500:
        response = "Жаль, что ты мусор"
    elif 2000 <= random_mmr <= 4000:
        response = "Неплохо играешь, браток"
    elif 5000 <= random_mmr <= 12000:
        response = "Ну ты скилловый мужичок"
    else:
        response = "Что-то пошло не так"

    await ctx.send(f'{user.mention}, твой MMR: {random_mmr}\n{response}')

bot.run('MTExODMxMjQ4OTI3MzI3ODUxNA.GKG2n0.9JtR020XGg2FteqfbHTh8icCcO70uDGq5xO9SM')
