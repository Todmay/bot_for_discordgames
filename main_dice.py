import discord
from discord.ext import commands
import random

from botconfig import bot_id

description = '''Кубики кидаем да и все тут, броски написаны для системы Savage Worlds'''

bot = commands.Bot(intents=discord.Intents.default(), command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def roll(ctx, dices: str):

    try:
        dice = dices
        rolls, limit = map(int, dice.split('d'))
        if limit < 2: 
            await ctx.send('Число граней кубики не может быть меньше 2')
            return

       
    except Exception:
        await ctx.send('Формат указывается как NdN, где первая N число кубиков, а вторая число их граней')
        return
    result = ''
    resultSUM = 0
    for r in range(rolls):
        roll = (random.randint(1, limit))
        if result == '': result = str(roll)
        else: result += ', '  + str(roll)
        resultSUM += roll
    message = 'Броски - ' + result + '\n' + 'Сумма - ' + str(resultSUM)
    await ctx.send(message)

@bot.command()
async def swroll(ctx, dices: str):
    try:
        fdice, sdice = dices.split('+')
        flimit = int(fdice[(fdice.find('d')+1)::])
        slimit = int(sdice[(fdice.find('d')+1)::])
        if slimit < 2 or flimit < 2: 
            await ctx.send('Число граней кубики не может быть меньше 2')
            return

       
    except Exception:
        await ctx.send('Формат указывается как dN+dN, кидается два кубика')
        return

    froll = (random.randint(1, flimit))
    fresult = str(froll)   
    fresultSUM = froll

    while (froll == flimit):
        froll = (random.randint(1, flimit))
        fresult += ', '  + str(froll)
        fresultSUM += froll
    
    sroll = (random.randint(1, slimit))
    sresult = str(sroll)   
    sresultSUM = sroll

    while (sroll == slimit):
        sroll = (random.randint(1, slimit))
        sresult += ', ' +  str(sroll) 
        sresultSUM += sroll
    message = 'Броски первого кубика  - ' + fresult + '\n' + 'Сумма - ' + str(fresultSUM) + '\n' + 'Броски второго кубика  - ' + sresult + '\n' + 'Сумма - ' + str(sresultSUM)
    await ctx.send(message)

@bot.command()
async def command_list(ctx):

    command_list = '\n' + 'Доступны следующие команды: ' + '\n' + '\n'+ '?roll NdN - делает бросок кубиков одинаковых граней, например ?roll 4d6, для броска одного кубика ?roll 1d8' + '\n' + '\n' +'?swroll dN+dN - бросает два кубика, которые ВЗРЫВАЮТСЯ, пример команды - ?swroll d6+d4' + '\n' + '\n' + '?command_list - отображате список команд' + '\n' 
    await ctx.send(command_list)




bot.run(bot_id)