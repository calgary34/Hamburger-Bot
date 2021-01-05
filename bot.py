from discord.ext import commands
import discord
import random
import os
client = commands.Bot(command_prefix=";")
client.remove_command("help")

@client.event
async def on_ready():
	print(client.user, "Is Ready")

@client.command(aliases=['random-integer'],pass_context=True)
async def random_integer( ctx,startnum:int,endnum:int):
	answer=f'Your random integer between {str(startnum)} and {str(endnum)} is {str(random.randint(int(startnum),int(endnum)))}.'
	em = discord.Embed(title="Random Integer", description=answer, color=0x275ef4)
	await ctx.send(embed=em)


@client.command(aliases=['random-float'],pass_context=True)
async def random_float(ctx,startnum:float,endnum:float):
  answer=f"Your random floating point number between {str(startnum)} and {str(endnum)} is {str(random.uniform(float(startnum),float(endnum)))}"
  em=discord.Embed(title="Random Float",description=answer,color=0x275ef4)
  await ctx.send(embed=em)
@client.command(aliases=['random-letter'],pass_context=True)
async def random_letter( ctx):
	letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	answer=f'{ctx.author.mention}, your random letter is `{random.choice(letters)}`.'
	em = discord.Embed(title="Random Letter", description=answer, color=0x275ef4)
	await ctx.send(embed=em)


@client.command(aliases=['random-shuffle','shuffle'],pass_context=True)
async def random_shuffle(ctx,*args):
  arr=list(args)
  random.shuffle(arr)
  printedlist=''
  for r in arr:
    printedlist=printedlist+str(r)+'\n'
    answer=f'Your randomly reoganized list now looks like this:\n'+printedlist
  em = discord.Embed(title="Shuffled List", description=answer, color=0x275ef4)
  await ctx.send(embed=em)
@client.command(name='random_choice',aliases=['random-choice'],pass_context=True)
async def random_choice( ctx,*args,pass_context=True):
  x=random.choice(args)
  answer=f'Your randomly chosen item now is:\n'+x
  em = discord.Embed(title="Random Choice from list",description=answer, color=0x275ef4)
  await ctx.send(embed=em)

@client.command()
async def info( ctx):
  em = discord.Embed(title="Info about bot",description='Hamburger Bot is a Discord bot created by [Spot Sign](https:repl.it/@SpotSign) and [The Peeps191](https:repl.it/@ThePeeps191). The code is open-source and can be found [here](https://github.com/calgary34/Hamburger-Bot).', color=0x275ef4)
  await ctx.send(embed=em)

@client.command(aliases=['8ball'],pass_context=True)
async def eightball( ctx,*,question):
  answers=["It is certain.","It is decidedly so.","Without a doubt.","Yes - definitely","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.",'Better not tell you now.','Cannot predict now.','Concentrate and ask again.',"Don't count on it.",'My reply is no.','My sources say no.','Outlook not so good.','Very doubtful.']
  em = discord.Embed(title="8ball",description=f'You question: {question}\n8ball says: {random.choice(answers)}', color=0x275ef4)
  await ctx.send(embed=em)

@client.group(invoke_without_command=True,pass_context=True)
async def help(ctx):
	em = discord.Embed(title="Help", description="Hamburger Bot - Help Command. You can use `;help <command>` for information on a certain command. `;info` also gives you information on the bot.", color=0x275ef4)
	em.add_field(name="Random Commands", value="`random-integer`, `random-float`, `random-letter`, `random-shuffle`, `random-choice`, `eightball`")
	await ctx.send(embed=em)

class HelpCommand:
	def __init__(self, title, desc, color, info):
		self.title = title
		self.desc = desc
		self.color = color
		self.info = info
		self.em = discord.Embed(title=self.title, description=self.desc, color=self.color)
		self.em.add_field(name="INFO", value=info)

# Run The Bot
client.run(os.getenv("DISCORD_BOT_SECRET"))