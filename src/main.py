import discord
import configparser
import random

config_ini = configparser.ConfigParser()
config_ini.read("config.ini", encoding="UTF-8")

token = config_ini["DEFAULT"]["Token"]

client = discord.Client()

random_comments=[
    "にゃーん",
    "わん!",
    "コケコッコー",
]
emoji_digits = [
    '\N{DIGIT ONE}\N{VARIATION SELECTOR-16}\N{COMBINING ENCLOSING KEYCAP}'
    '\N{DIGIT TWO}\N{VARIATION SELECTOR-16}\N{COMBINING ENCLOSING KEYCAP}'
    '\N{DIGIT THREE}\N{VARIATION SELECTOR-16}\N{COMBINING ENCLOSING KEYCAP}'
    '\N{DIGIT FOUR}\N{VARIATION SELECTOR-16}\N{COMBINING ENCLOSING KEYCAP}'
    '\N{DIGIT FIVE}\N{VARIATION SELECTOR-16}\N{COMBINING ENCLOSING KEYCAP}'
    '\N{DIGIT SIX}\N{VARIATION SELECTOR-16}\N{COMBINING ENCLOSING KEYCAP}'
    '\N{DIGIT SEVEN}\N{VARIATION SELECTOR-16}\N{COMBINING ENCLOSING KEYCAP}'
    '\N{DIGIT EIGHT}\N{VARIATION SELECTOR-16}\N{COMBINING ENCLOSING KEYCAP}'
    '\N{DIGIT NINE}\N{VARIATION SELECTOR-16}\N{COMBINING ENCLOSING KEYCAP}'
]

@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)
    await

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "鳴いて":
        content = random.choice(random_comments)
        await message.channel.send(content)
    elif message.content == "おはよう":
        await message.channel.send("おはよう！！！")

client.run(token)