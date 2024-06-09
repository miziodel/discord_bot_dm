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

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_message(message):
    if message.author == bot.user:  # Controlla se il messaggio è stato inviato dal bot stesso 
        return  # Ignora i messaggi inviati dal bot per evitare loop infiniti

    await bot.process_commands(message)  # Assicura che i comandi siano ancora processati normalmente

    # Traccia i messaggi ricevuti nel log
    print(f"Message received from {message.author}: {message.content}")


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def send_dm(ctx, user: discord.User, *, message=None):
    """invia un messaggio diretto tramite comando !send_dm username messaggio 
    """

    if message is None:
        await ctx.send("You need to provide a message to send.")
    else:
        try:
            await user.send(message)
            await ctx.send(f"Sent message to {user.name}")
        except discord.Forbidden:
            await ctx.send("I cannot send messages to this user.")


if __name__ == "__main__":
    bot.run(token_bot)