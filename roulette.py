from discord.ext import commands
import discord
import random

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is online and ready to use")

#gold-FFFB00
#purple-FFFB00
#redish-FF0078
@bot.command()
async def roulette(ctx, round_id):
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length == 36:
        predictions = ['red','red','red','purple','purple','purple','gold']
        prediction = random.choice(predictions)
        if prediction == 'red':
            embed_color = 0xFF0036
            color_text = 'Red'
            prediction = ":red_square:"
        elif prediction == 'purple':
            embed_color = 0xAE00FF
            color_text = 'Purple'
            prediction = ":purple_square:"
        elif prediction == 'purple':
            embed_color = 0xFFFB00
            color_text = 'Gold'
            prediction = ":yellow_square:"
        em = discord.Embed(color=embed_color)
        em.add_field(name="Roulette Predictor", value=color_text + "\n" + prediction)
        em.set_footer(text="Made by geek")
        await ctx.send(embed=em)
    else:
        await ctx.send("Invalid round id")

bot.run('')