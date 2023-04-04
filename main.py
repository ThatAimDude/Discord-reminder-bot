
from discord.ext import commands
import discord
from asyncio import sleep
from datetime import datetime as dt


TOKEN = 'MTA4NTE1MTA0MjI4ODc1MDY5NA.Ga5db4.Xm9QDtndOompX90AKey8adA4x_f_y_iNqTkKg8'


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)
today_date = dt.now()


@bot.command()
async def remind(ctx):
    await ctx.send("When do you want to be reminded?")
    remind_date = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    remind_date_str = remind_date.content
    await ctx.send(f"Okay, I will remind you at {remind_date_str}! What do you want me to remind you about?")
    reminder = await bot.wait_for('message', check=lambda message: message.author == ctx.author)

    if reminder.content.lower() in ['sprawdzian', 'kartkowka','praca domowa', 'homework','test']:
        global subject
        global details
        await ctx.send(f"What subject? ")
        subject = await bot.wait_for('message',check=lambda message: message.author == ctx.author)
        await ctx.send(f"What is it about?")
        details = await bot.wait_for('message',check=lambda message: message.author == ctx.author)

    else:
        subject = ''
        details = ''

    await ctx.send(f"I will remind you at {remind_date_str} about {reminder.content}")

    date_object = dt.strptime(remind_date_str, '%d-%m-%Y-%H-%M')
    date1 = (today_date - date_object) * (-1)
    date_without_time = date_object.date()

    embed = discord.Embed(
        colour=discord.Colour.dark_teal(),
        description="Some shit you have to do",
        title="Reminder Kurwa"
    )

    embed.add_field(name='Remind date', value=remind_date_str, inline=False)
    try:
        embed.insert_field_at(1, name=subject.content, value=details.content)
    except Exception as e:
        embed.insert_field_at(1, name=reminder.content, value='')
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1086270045853847592/1092742274275872808/Daco_4228969.png")
    embed.set_footer(text="This is a message from annonymous")

    while True:
        print(date1.total_seconds())
        await sleep(date1.total_seconds())
        member = ctx.message.author
        await member.send(embed=embed)
        break

bot.run(TOKEN)