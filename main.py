import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "hai" in message.content.lower():
        await message.channel.send("Halo, pengguna Discord! Untuk memulai interaksi, silahkan ketik !mulai")
    await bot.process_commands(message)

@bot.command()
async def mulai(ctx):
    with open('interaksi.txt', 'r', encoding='utf-8') as f:
        await ctx.send(f.read())

@bot.command()
async def definisi(ctx):
    with open('definisi.txt', 'r', encoding='utf-8') as f:
        await ctx.send(f.read())
@bot.command()
async def penyebab(ctx):
    with open('penyebab.txt', 'r', encoding='utf-8') as f:
        await ctx.send(f.read())
        
@bot.command()
async def dampak(ctx):
    with open('dampak.txt', 'r', encoding='utf-8') as f:
        await ctx.send(f.read())

@bot.command()
async def solusi(ctx):
    with open('source.txt', 'r', encoding='utf-8') as f:
        await ctx.send(f.read())
        
    with open('kincir angin.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
        
    with open('solar panel.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    
    with open('pertanian bertingkat.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    
    with open('electric vehicle.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    
    with open('vertical garden.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("TOKEN BOT") 