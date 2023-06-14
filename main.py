from discord.ext import commands
import discord
from asyncio import sleep
from datetime import datetime as dt
import requests
import json



TOKEN = 'MTA4NTE1MTA0MjI4ODc1MDY5NA.GL3a_u.gp4SPSxj8DjBLu7RfdaOWGSGxFexkb-oeN72Ic'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)
today_date = dt.now()


class MockContext:
    def __init__(self):
        self.message = MockMessage()

class MockMessage:
    def __init__(self):
        self.author = MockAuthor()

class MockAuthor:
    def __init__(self):
        # Add necessary attributes for the author (e.g., id, name, etc.)
        pass




class Menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.option = None


    @discord.ui.button(label='Sprawdzian', style=discord.ButtonStyle.primary)
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.option = 'Sprawdzian'
        self.value = '1'
        self.stop()
        await interaction.response.defer()


    @discord.ui.button(label='Kartkowka', style=discord.ButtonStyle.primary)
    async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.option = 'Kartkowka'
        self.value = '2'
        self.stop()
        await interaction.response.defer()

    @discord.ui.button(label='Praca Domowa', style=discord.ButtonStyle.primary)
    async def menu3(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.option = 'Praca Domowa'
        self.value = '3'
        self.stop()
        await interaction.response.defer()

    @discord.ui.button(label='Project', style=discord.ButtonStyle.primary)
    async def menu4(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.option = 'Project jebany'
        self.value = '4'
        self.stop()
        await interaction.response.defer()

    @discord.ui.button(label='Custom', style=discord.ButtonStyle.primary)
    async def menu5(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = '5'
        self.stop()
        await interaction.response.defer()

    async def wait_for_response(self):
        await self.wait()
        return self.value


@bot.command()
async def remind(ctx):

    await ctx.send("When do you want to be reminded?")
    remind_date = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    remind_date_str = remind_date.content
    await ctx.send(f"Okay, I will remind you at {remind_date_str}! What do you want me to remind you about?")
    view = Menu()
    view.menu1
    view.menu2
    view.menu3
    view.menu4
    view.menu5

    await ctx.send(view=view)
    response = await view.wait_for_response()

    list = ['1','2','3','4']
    if response in list:

        await ctx.send(f"What subject?")
        subject = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
        await ctx.send(f"What is it about?")
        details = await bot.wait_for('message', check=lambda message: message.author == ctx.author)

    else:
        await ctx.send("What do you want to be reminded about?")
        reminder = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
        await ctx.send("Any details")
        extra_info = await bot.wait_for('message', check=lambda message: message.author == ctx.author)

    await ctx.send(f"I will remind you at {remind_date_str}")



    date_object = dt.strptime(remind_date_str, '%d-%m-%Y-%H-%M')
    date1 = (today_date - date_object) * (-1)
    date_without_time = date_object.date()

    embed = discord.Embed(
        colour=discord.Colour.dark_red(),
        title="Reminder",
        description="Some shit you need to do"
    )

    if response in ['1', '2', '3', '4']:
        embed.insert_field_at(1, name=f"{subject.content} {view.option} ", value=details.content)
        option = 1
    else:
        embed.insert_field_at(1, name=reminder.content, value=extra_info.content)



    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1086270045853847592/1092742274275872808/Daco_4228969.png")
    embed.set_footer(text=f"Reminder date {remind_date_str}")


    while True:
        print(date1.total_seconds())
        await sleep(date1.total_seconds())
        member = ctx.message.author
        await member.send(embed=embed)
        break


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await send_notion_reminders()

async def send_notion_reminders():
    notion_token = "secret_bKrCxad0LUjcrJaBRXBHguMhXTMozmfypoJ24EJPrrv"
    database_id = "028e6cf3082043c3a140e3de354abf52"
    url = f"https://api.notion.com/v1/databases/{database_id}/query"

    payload = {"page_size": 100}
    headers = {
        "Authorization": f"Bearer {notion_token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = json.loads(response.text)

    for result in data["results"]:
        if "Date" in result["properties"] and result["properties"]["Date"].get("date"):
            date = result["properties"]["Date"]["date"]["start"]
        else:
            date = "N/A"
        # remind_date_str = dt.strftime('%d-%m-%Y-%H-%M')
        # print(remind_date_str)
        print(date)

# Run the bot
bot.run(TOKEN)


bot.run(TOKEN)