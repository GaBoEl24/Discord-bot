import discord
from discord.ext import commands
from main2 import *
from Token import *
Permission = discord.Intents.default()
Permission.message_content = True
Daybot = commands.Bot(command_prefix="<",intents=Permission)
@Daybot.event
async def on_ready():
    print(f"The bot {Daybot.user} has been initialized correctly")
@Daybot.command()
async def Hi(ctx):
    await ctx.send(f"Hello {ctx.author}!")
@Daybot.command()
async def Password(ctx,lenght:int):       
    await ctx.send(f"The password is {gen_pass(lenght)}")
@Daybot.command()
async def SeeCommands(ctx):
    C_L = ", ".join([command.name for command in Daybot.commands])
    await ctx.send(f"The active commands are {C_L}")
@Daybot.command()
async def Down(ctx, *args):
    if len(args) != 2:
        await ctx.send("Please insert only two names")
        print("Funtion 'Down' argument error")
        return
    a, b = args
    result = choose_btw(a,b)
    await ctx.send(f"{result} is the real down")
    #await ctx.send(
        #f"Disclaimer: This is just a joke! According to the bot, {result} is the chosen one."
    #)
@Daybot.command()
async def Gay(ctx, *args):
    if len(args) != 2:
        await ctx.send("Please provide exactly two names.")
        print("Function 'Gay' argument error")
        return
    
    a, b = args
    result = choose_btw(a, b)
    await ctx.send(f"{result} is the real gay")
    #await ctx.send(
        #f"Disclaimer: This is just a joke! According to the bot, {result} is the chosen one."
    #)
    
@Daybot.command()
async def Desease(ctx, *args):
    if len(args) != 2:
        await ctx.send("Please insert only one name and one factor")
        print("Funtion 'Desease' argument error")
        return
    a, b = args
    result = check(a,b)
    if result == 1:
        await ctx.send(f"{a} haves {b}")
    else:
        await ctx.send(f"{a} doesn´t have {b}")
@Daybot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"Command doesn´t exist")
        print("'Command doesn´t exists' error")
Daybot.run(token())