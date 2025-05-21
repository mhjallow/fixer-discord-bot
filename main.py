import discord
import os
from dotenv import load_dotenv
import re

#Load .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

#Set up bot with permission to parse message content
intents = discord.Intents.default()
intents.message_content = True

#Create the bot client
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(F"✅ Logged in as {client.user}")

@client.event
async def on_message(message): #This function runs every time a message is sent anywhere the bot can see.
    if message.author.bot:
        return #Ignore messages sent by bots
    print(f"Message from {message.author}: {message.content}")

client.run(TOKEN)