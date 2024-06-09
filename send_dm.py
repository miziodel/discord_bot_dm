import discord
from discord.ext import commands

import sys
import asyncio


# secret.py contiene token_bot = <token del bot>
from secret import token_bot

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)

async def send_private_message(username, message):
    await client.wait_until_ready()
    user = discord.utils.get(client.get_all_members(), name=username)
    if user:
        await user.send(message)
    else:
        print(f"User {username} not found.")

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    if len(sys.argv) != 3:
        print("Usage: python send_message.py <username> <message>")
        await client.close()
        return

    username = sys.argv[1]
    message = sys.argv[2]
    await send_private_message(username, message)
    await client.close()

client.run(token_bot)