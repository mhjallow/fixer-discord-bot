import discord
import os
from dotenv import load_dotenv

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

client.run(TOKEN)