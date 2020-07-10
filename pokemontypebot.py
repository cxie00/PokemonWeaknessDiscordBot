import pokebase as pb
import os # to access .env vars
import random 
from dotenv import load_dotenv
import requests
import discord
from discord.ext import commands, tasks

# Chloe Xie 2020 Pokemon weakness discord bot
# Used pokebase library for weakness info 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='about', help='Displays info about the bot')
async def about(ctx):
    await ctx.send("```The weakness command has some shortcomings for Pokemon with different forms." +
    "\nFor example, Giratina can be giratina-altered and giratina-origin." +
    "\nI'll give the documentation a closer look some time to see what I can do about that.```")

@bot.command(name='random', help='Displays a random Pokemon')
async def randomMon(ctx):
    pokemonID =  random.randint(1, 807)
    pokemon = pb.pokemon(pokemonID)
    typing = str(pokemon.types[0].type)
    if len(pokemon.types) > 1:
        typing += f'/{pokemon.types[1].type}'
    await ctx.send(f'https://pokeres.bastionbot.org/images/pokemon/{pokemonID}.png' + f'\n{str(pokemon)} \n type: {typing}')

@bot.command(name='weakness', help='Calculates the weakness of a Pokemon')
async def weaknesscalc(ctx, user_input):
    userPokemon = pb.pokemon(str(user_input).lower())
    immunities = []
    double_damage = []
    quad_damage = []
    for slot in userPokemon.types:
        for weaknessobj in slot.type.damage_relations.double_damage_from:
            weakness = weaknessobj.get('name')
            if weakness in double_damage:
                double_damage.remove(weakness)
                quad_damage.append(weakness)
            else:
                double_damage.append(weakness)
    for slot in userPokemon.types:        
        for resistanceobj in slot.type.damage_relations.half_damage_from:
            resistance = resistanceobj.get('name')
            while resistance in double_damage:
                double_damage.remove(resistance)
        for immunityobj in slot.type.damage_relations.no_damage_from:
            immunity = immunityobj.get('name')
            while immunity in double_damage:
                double_damage.remove(immunity)
            immunities.append(immunity)
    result0 = ""
    if len(immunities) > 0:
        result0 = f'\n {userPokemon} is immune to: \n'
        for i in immunities:
            result0 += f'{i} \n'
    result0 += "\n"
    if len(double_damage) > 0:
        result0 += f'{userPokemon} is 1x weak to: \n'
        for w1 in double_damage:
            result0 += f'{w1} \n'
        result0 += "\n"
    if len(quad_damage) > 0:
        result0 += f'{userPokemon} is 2x weak to: \n'
        for w2 in quad_damage:
            result0 += f'{w2} \n'
    await ctx.send(f'https://pokeres.bastionbot.org/images/pokemon/{userPokemon.id}.png' + result0 )
bot.run(TOKEN)