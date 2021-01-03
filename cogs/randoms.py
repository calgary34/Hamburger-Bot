from discord.ext import commands
import random
class RandomGenerators(commands.Cog,name="Random Generators"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='random_integer',aliases=['random-integer'],help="Outputs a random integer between two specified numbers.")
    async def random_integer(self, ctx,startnum:int,endnum:int):
        answer=f'Your random integer between {str(startnum)} and {str(endnum)} is {str(random.randint(int(startnum),int(endnum)))}.'
        await ctx.send(answer)   
    @commands.command(name='random_float',aliases=['random-float'],help="Outputs a random floating point number between two specified numbers.")
    async def random_float(self, ctx,startnum:float,endnum:float):
        answer=f'Your random floating point number between {str(startnum)} and {str(endnum)} is {str(random.uniform(float(startnum),float(endnum)))}.'
        await ctx.send(answer) 
    @commands.command(name='random_letter',aliases=['random-letter'],help="Outputs a random English letter.")
    async def random_letter(self, ctx):
        letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        answer=f'Your letter is {random.choice(letters)}.'
        await ctx.send(answer)   
    @commands.command(name='random_shuffle',aliases=['random-shuffle','shuffle'],help="Randomly reoganizes a specified list.")
    async def random_shuffle(self, ctx,*args):
        arr=list(args)
        random.shuffle(arr)
        printedlist=''
        for r in arr:
          printedlist=printedlist+str(r)+'\n'
        answer=f'Your randomly reoganized list now looks like this:\n'+printedlist
        await ctx.send(answer)   
    @commands.command(name='random_choice',aliases=['random-choice'],help="Randomly picks an item from a specified list.")
    async def random_choice(self, ctx,*args):
        x=random.choice(args)
        answer=f'Your randomly chosen item now is:\n'+x
        await ctx.send(answer) 


def setup(bot):
    bot.add_cog(RandomGenerators(bot))