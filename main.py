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

def replace_twitter_links(msg):
    #This function finds and replaces any twitter or x.com links with "fixvx.com"
    pattern = r"(https://)(twitter\.com|x\.com|t\.co)([^\s]*)"

    def replace_domain(msg):
        #Splitting message into the three match groups
        protocol = msg.group(1)
        domain = msg.group(2)
        rest = msg.group(3)
        
        #Replacing the domain
        new_domain = "fixvx.com"
        return f"{protocol}{new_domain}{rest}"
    
    return re.sub(pattern, replace_domain, msg) #Applying the replacement function on the message with the pattern, returns the same string if it doesnt match the pattern

@client.event
async def on_ready():
    print(F"✅ Logged in as {client.user}")

@client.event
async def on_message(message): #This function runs every time a message is sent anywhere the bot can see.
    if message.author.bot:
        return #Ignore messages sent by bots
    
    fixed_link = replace_twitter_links(message.content) #Call to replace the domain

    if fixed_link != message.content: #If the message is the same as the result after replacement, that means it didn't contain a twitter link and it does nothing.
        await message.delete() #Delete the original message
        await message.channel.send(f"{message.author.mention}: {fixed_link}")

client.run(TOKEN)