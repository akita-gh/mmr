from disnake.ext import commands
import disnake
import random
import os
from dotenv import load_dotenv
load_dotenv()


intents = disnake.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Вошел как {bot.user.name}')


@bot.command()
async def mmr(ctx):
    user = ctx.author
    if str(user) == 'akita#1200':
        # Выдаем большое число пользователю akita#1200
        number = random.randint(5000, 12000)
    else:
        # Генерируем случайное число в соответствии с заданными вероятностями
        chance = random.randint(1, 100)
        if chance <= 60:
            number = random.randint(500, 1500)
        elif chance <= 90:
            number = random.randint(2000, 4000)
        else:
            number = random.randint(5000, 12000)

    if number <= 1500:
        message = "Жаль, что ты мусор"
    elif number <= 4000:
        message = "Неплохо играешь, браток"
    else:
        message = "Ну ты скилловый мужичок"

    await ctx.send(f'{user.mention}, твой MMR: {number}\n{message}')

# Получаем токен бота из переменной окружения
bot_token = os.environ['BOT_TOKEN']
bot.run(bot_token)
