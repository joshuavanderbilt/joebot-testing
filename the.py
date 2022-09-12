import discord
import random
from discord.ext import commands
import os
import sys
import psutil
import logging
import time
import string
import git
from git import Repo

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
token_file = open('token.txt', 'r')
token = token_file.read()

def arestart():
    import sys
    print("argv was",sys.argv)
    print("sys.executable was", sys.executable)
    print("restart now")

def restartApp():
    python = sys.executable
    os.execl(python, python, *sys.argv)

@bot.command(help='Displays Rule 11')
async def r11(ctx):
    await ctx.send('Please refrain from asking for or giving assistance with installing, using, or obtaining pirated software.')
    
@bot.command(help='Displays Rule 11')
async def rule11(ctx):
    await ctx.send('Please refrain from asking for or giving assistance with installing, using, or obtaining pirated software.')

@bot.command(help="dispways wuwe 11")
async def wuwe11(ctx):
    await ctx.send('pwease wefwain fwom asking fow ow giving assistance with instawwing, using, ow obtaining piwated softwawe')

@bot.command(help="dispways wuwe 11")
async def w11(ctx):
    await ctx.send('pwease wefwain fwom asking fow ow giving assistance with instawwing, using, ow obtaining piwated softwawe')

@bot.command(help="Bans a member.")
async def ban(ctx, member : discord.Member):
    if member.name == 'Joe Bot':
        await ctx.send('no')
    else:
        thing = [':hammer: ', member.mention, ' has been banned.']
        x = ''.join(thing)
        await ctx.send(x)

@bot.command(help="Kills a member.")
async def kill(ctx, member : discord.Member):
    if member.name == 'Joe Bot':
        await ctx.send('no')
    else:
        thing = [':knife: ', member.mention, ' has been killed.']
        x = ''.join(thing)
        await ctx.send(x)

@bot.command(help="Super bans a member.")
async def superban(ctx, member : discord.Member):
    if member.name == 'Joe Bot':
        await ctx.send('no')
    else:
        thing = [member.mention, ' is now SUPER BANNED. :thumbup: https://nintendohomebrew.com/assets/img/banned.gif']
        x = ''.join(thing)
        await ctx.send(x)

@bot.command(help="Takes away help from a member.")
async def takehelp(ctx, member : discord.Member):
        thing = [member.mention, ' can no longer access the help channels.']
        x = ''.join(thing)
        await ctx.send(x)
        print("I took help from", member.mention,".")

@bot.command(help="Displays information about the bot.", )
async def about(ctx):
    await ctx.send('Joe Bot Version j6.1 testing')
    await ctx.send('--------------------------------')
    await ctx.send('This is a JOE Bot, all hail Joe!')
    await ctx.send('Contributors: JoshuaMV')
    await ctx.send('--------------------------------')
    await ctx.send('This bot is a fork of Joe Bot for testing.')
    await ctx.send('All birbs birbserved.')
    print("User called the about message.")

@bot.command(help="Sends a random image from the furry folder.")
async def furryfolder(ctx):
    furryfile = random.choice(os.listdir("/FURRY"))
    furrytable = ["/FURRY/",furryfile]
    furrysend = ''.join(furrytable)
    await ctx.send(file=discord.File(furrysend))
    print("I sent", furrysend, "from the /FURRY directory.")

# The command below requires the string library.

@bot.command(help="Sends a random LightShot image. (Use at your own risk!)")
async def lightshot(ctx):
    lslink = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    lstable = ["https://prnt.sc/", lslink]
    lssend = ''.join(lstable)
    await ctx.send(lssend)
    print("User generated this link from LightShot:", lssend)


@bot.command(help="Make the Joe Bot say what you want it to!")
async def say(ctx, *args):
    arguments = ' '.join(args)
    await ctx.send(arguments)
    print("I said '",arguments,"'.")

@bot.command(help="Birb image.")
async def birb(ctx):
    await ctx.send('https://files.catbox.moe/s1g67r.png')

@bot.command(help='Update the bot via GIT.')
async def update(ctx):
    print("User attempted to update bot.")
    await ctx.send('Software updates are not available in your region. (000-0001)')
#	os.system("rm -rf /root/test/")
#	os.system("mkdir /root/test/")
#	Repo.clone_from("https://www.github.com/Evanzap/joebot.git", "/root/test/")
#	os.system("mv /root/test/the.py /root/the.py")
#	await ctx.send('Updating software, please type .update after a few seconds.')
	
@bot.command(help='Restart the bot after updating')
async def restart(ctx):
	ctx.send('Restarting...')
	restartApp()

bot.run(str(token))
