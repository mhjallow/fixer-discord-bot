import discord
import os
from dotenv import load_dotenv
import re
from keep_alive import keep_alive

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

@client.event #This is how you register events
async def on_ready(): #This function runs when the bot is ready
    print(F"✅ Logged in as {client.user}")

@client.event
async def on_message(message): #This function runs every time a message is sent anywhere the bot can see.
    if message.author.bot:
        return #Ignore messages sent by bots
    
    fixed_link = replace_twitter_links(message.content) #Call to replace the domain

    if fixed_link != message.content: #If the message is the same as the result after replacement, that means it didn't contain a twitter link and it does nothing.
        await message.delete() #Delete the original message
        # Create an embed to credit the user
        embed = discord.Embed(
            description=fixed_link,
            color=discord.Color.blue()
        )
        embed.set_author(name=f"{message.author.mention}", icon_url=message.author.avatar.url if message.author.avatar else discord.Embed.Empty)

        await message.channel.send(embed=embed)
        await message.channel.send(fixed_link)

keep_alive() #Runs the webserver to keep the bot on if using Replit
client.run(TOKEN)