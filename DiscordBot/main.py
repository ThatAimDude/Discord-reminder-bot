import os
import random
from discord.ext import commands
import discord
import time
from asyncio import sleep as s
from datetime import datetime as dt, timedelta, time


TOKEN = 'MTA4NTE1MTA0MjI4ODc1MDY5NA.G_c8e1.Z8NZ682cNqLW4mQLI6BXcIZuQ_DQauVyUGERTQ'


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)
today_date = dt.now()


@bot.command()
async def remind(ctx , remind_date, msg, msg2):
    date_object = dt.strptime(remind_date, '%d-%m-%Y-%H-%M')
    date1 = (today_date - date_object) * (-1)
    date_without_time = date_object.date()


    while True:

        print(date1.total_seconds())
        await s(date1.total_seconds())
        member = ctx.message.author
        await member.send(f"**{msg}**, {msg2}, {date_without_time}, {ctx.author.mention}")
        break


bot.run(TOKEN)


