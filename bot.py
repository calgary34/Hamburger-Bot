from discord.ext import commands
import discord
import random
import os
from keep_alive import keep_alive
client = commands.Bot(command_prefix=";")
client.remove_command("help")

@client.event
async def on_ready():
	print(client.user, "Is Ready")

@client.command(aliases=['random-integer'])
async def random_integer( ctx,startnum:int,endnum:int):
	answer=f'Your random integer between {str(startnum)} and {str(endnum)} is {str(random.randint(int(startnum),int(endnum)))}.'
	em = discord.Embed(title="Random Integer", description=answer, color=0x275ef4)
	await ctx.send(embed=em)


@client.command(aliases=['random-float'])
async def random_float(ctx,startnum:float,endnum:float):
  answer=f"Your random floating point number between {str(startnum)} and {str(endnum)} is {str(random.uniform(float(startnum),float(endnum)))}"
  em=discord.Embed(title="Random Float",description=answer,color=0x275ef4)
  await ctx.send(embed=em)

@client.command(aliases=['random-letter'])
async def random_letter( ctx):
	letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	answer=f'{ctx.author.mention}, your random letter is `{random.choice(letters)}`.'
	em = discord.Embed(title="Random Letter", description=answer, color=0x275ef4)
	await ctx.send(embed=em)


@client.command(aliases=['random-shuffle','shuffle'])
async def random_shuffle(ctx,*args):
  arr=list(args)
  random.shuffle(arr)
  printedlist=''
  for r in arr:
    printedlist=printedlist+str(r)+'\n'
    answer=f'Your randomly reoganized list now looks like this:\n'+printedlist
  em = discord.Embed(title="Shuffled List", description=answer, color=0x275ef4)
  await ctx.send(embed=em)

@client.command(name='random_choice',aliases=['random-choice'])
async def random_choice( ctx,*args):
  x=random.choice(args)
  answer=f'Your randomly chosen item now is:\n'+x
  em = discord.Embed(title="Random Choice from list",description=answer, color=0x275ef4)
  await ctx.send(embed=em)

@client.command()
async def info(ctx):
  em = discord.Embed(title="Info about bot",description='Hamburger Bot is a Discord bot created by [Spot Sign](https:repl.it/@SpotSign) and [The Peeps191](https:repl.it/@ThePeeps191). The code is open-source and can be found [here](https://github.com/calgary34/Hamburger-Bot).', color=0x275ef4)
  await ctx.send(embed=em)

@client.command(aliases=['8ball'])
async def eightball( ctx,*,question):
  answers=["It is certain.","It is decidedly so.","Without a doubt.","Yes - definitely","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.",'Better not tell you now.','Cannot predict now.','Concentrate and ask again.',"Don't count on it.",'My reply is no.','My sources say no.','Outlook not so good.','Very doubtful.']
  em = discord.Embed(title="8ball",description=f'You question: {question}\n8ball says: {random.choice(answers)}', color=0x275ef4)
  await ctx.send(embed=em)

@client.group(invoke_without_command=True)
async def help(ctx):
	em = discord.Embed(title="Help", description="Hamburger Bot - Help Command. You can use `;help <command>` for information on a certain command. `;info` also gives you information on the bot. Remember to use `;` before each command!", color=0x275ef4)
	em.add_field(name="Random Commands", value="`random-integer`, `random-float`, `random-letter`, `random-shuffle`, `random-choice`, `8ball`")
	await ctx.send(embed=em)
class HelpCommand:
  def __init__(self, title, desc, usage,aliases):
    self.title = title
    self.desc = desc
    self.color = 0x275ef4
    self.desc = desc
    self.aliases=aliases
    self.usage=usage
    self.em = discord.Embed(title=self.title, description=self.desc, color=self.color)
    self.em.add_field(name="Description", value=desc)
    self.em.add_field(name="Usage", value=usage)
    self.em.add_field(name='Aliases',value=aliases)
@help.command(name='random-integer',aliases=['random_integer'],pass_context=True)
async def help_random_integer(ctx):
  cmd=HelpCommand('Help on `random-integer`',"Outputs a random integer between two specified numbers.","`;random-integer <start> <stop>`","`random_integer`")
  await ctx.send(embed=cmd.em)
@help.command(name='random-float',aliases=['random_float'])
async def help_random_float(ctx):
  cmd=HelpCommand("Help on `random-float`","Outputs a random floating point number between two specified numbers.","`;random-float <start> <stop>`","`random_float`")
  await ctx.send(embed=cmd.em)
@help.command(name='random-letter',aliases=['random_letter'])
async def help_random_letter(ctx):
  cmd=HelpCommand("Help on `random-letter`","Outputs a random letter from the english alphabet.","`;random-letter`","`random_letter`")
  await ctx.send(embed=cmd.em)
@help.command(name='random-shuffle',aliases=['random_shuffle'])
async def help_random_shuffle(ctx):
  cmd=HelpCommand("Help on `random-shuffle`","Randomly reogranizes a specified list. Enter the list, with items seperated by spaces, and to add an item with spaces, add quotes around it.","`;random-shuffle <your list>`","`random_shuffle`,`shuffle`")
  await ctx.send(embed=cmd.em)
@help.command(name='random-choice',aliases=['random_choice'],pass_context=True)
async def help_random_choice(ctx):
  cmd=HelpCommand("Help on `random-choice`","Randomly picks an item from a specified list. Enter the list, with items seperated by spaces, and to add an item with spaces, add quotes around it.","`;random-choice <your list>`","`random_choice`")
  await ctx.send(embed=cmd.em)
@help.command(name='8ball',aliases=['eightball'],pass_context=True)
async def help_eightball(ctx):
  cmd=HelpCommand("Help on `8ball`","Outputs a random choice from a list of possible responses.","`;8ball`","`eightball`")
  await ctx.send(embed=cmd.em)
@help.command(name='info',pass_context=True)
async def help_info(ctx):
  cmd=HelpCommand("Help on `info`","Gives info on the bot.","`;info`","None")
  await ctx.send(embed=cmd.em)
@help.command(name='help',pass_context=True)
async def help_help(ctx):
  cmd=HelpCommand("Help on `help`","Help for the bot. You can also enter a command, giving help on that command.","`;help <command (optional)>`","None")
  await ctx.send(embed=cmd.em)
keep_alive()
# Run The Bot
client.run(os.getenv("DISCORD_BOT_SECRET"))