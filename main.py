import discord
from discord.ext import commands
from discord.ext import *
import random
import os

client = commands.Bot(command_prefix="")


@client.event
async def on_ready():   
    print("Ready to rock and roll")
    await client.change_presence(status=discord.Status.online,activity=discord.Game('Reading Art of War'))

@client.event
async def on_member_join(member):
    print('(member) is ready to start thinking very hardly and in a big brain manner')

@client.event
async def on_member_remove(member):
    print('(member) is now a very dumb ape')

@client.command()
async def biography(ctx):
    await ctx.send(f'I, Sun Tzu, is very intelligent, also Aaron is cool')

@client.command(aliases=['sun tzu is bad ', 'I hate sun tzu ', 'sun tzu is trash '])
async def suntzuistrash(ctx):
    quotes2 = ['"Bruh look at whos talking", ""Pretend inferiority and encourage his arrogance." - Sun Tzu, The Art of War" "Do you have years and years of military experience? Didnt think so..."']
    await ctx.send(f'{random.choice(quotes2)}')

@client.command()
async def commands(ctx):
    await ctx.send(f'Type in quote or quotes to get a random quote. Type "who is Sun Tzu" to get to know me better. There are also some hidden features that I kind of want to leave you guys to find out for yourself.')


@client.command(aliases=['quotes', 'quote'])
async def randomquote(ctx):
    quotes = [
                '”Appear weak when you are strong, and strong when you are weak.” ― Sun Tzu, The Art of War',
                '“The supreme art of war is to subdue the enemy without fighting.” ― Sun Tzu, The Art of War',
                '“Let your plans be dark and impenetrable as night, and when you move, fall like a thunderbolt.”',
                '“Supreme excellence consists of breaking the enemys resistance without fighting.”',
                '“Let your plans be dark and impenetrable as night, and when you move, fall like a thunderbolt.” ― Sun Tzu, The Art of War',
                '“Supreme excellence consists of breaking the enemy\'s resistance without fighting.”',
                '“All warfare is based on deception. Hence, when we are able to attack, we must seem unable; when using our forces, we must appear inactive; when we are near, we must make the enemy believe we are far away; when far away, we must make him believe we are near.” ― Sun Tzu, The Art of War',
                '“In the midst of chaos, there is also opportunity” ― Sun Tzu, A Arte da Guerra',
                '“The greatest victory is that which requires no battle.” ― Sun Tzu, The Art of War',
                '“Engage people with what they expect; it is what they are able to discern and confirms their projections. It settles them into predictable patterns of response, occupying their minds while you wait for the extraordinary moment — that which they cannot anticipate.” ― Sun Tzu, The Art of War',
                '“Move swift as the Wind and closely-formed as the Wood. Attack like the Fire and be still as the Mountain.” ― Sun Tzu, The Art of War',
                '“Treat your men as you would your own beloved sons. And they will follow you into the deepest valley.” ― Sun Tzu, The Art of War',
                '“When you surround an army, leave an outlet free. Do not press a desperate foe too hard.” ― Sun Tzu, The Art of War',
                '“When the enemy is relaxed, make them toil. When full, starve them. When settled, make them move.” ― Sun Tzu, The Art of War',
                '“So in war, the way is to avoid what is strong, and strike at what is weak.” ― Sun Tzu, The Art of War',
                '“To win one hundred victories in one hundred battles is not the acme of skill. To subdue the enemy without fighting is the acme of skill.” ― Sun Tzu, The Art of War',
                '“Be extremely subtle even to the point of formlessness. Be extremely mysterious even to the point of soundlessness. Thereby you can be the director of the opponent\'s fate.” ― Sun Tzu, The Art of War',
                '“One may know how to conquer without being able to do it. ” ― Sun Tzu, The Art of War',
                '“He who is prudent and lies in wait for an enemy who is not, will be victorious.” ― Sun Tzu, The Art of War',
                '"Build your opponent a golden bridge to retreat across"']
    await ctx.send(f'{random.choice(quotes)}')

elosayings = ['"Should have read Art of War" - Sun Tzu, Art of War', '"Naw man you are just trash" - Sun Tzu, Art of War', '"Brooo imagine losing, could not be me" - Sun Tzu, Art of War', '"No, I think you just deserved it" - Sun Tzu, Art of War', '"Just git gud kid, friggin rat" - Sun Tzu, Art of War']
winsayings = ['Courtesy of yours truly', 'Congrats', 'Remember who brought you here']

@client.event
async def on_message(message):
    id = client.get_guild(711788514915778622)
    if message.author == client.user:
        return
    if 'rollback' in message.content:
        await message.channel.send(f'{random.choice(elosayings)}')
    elif 'lost elo' in message.content:
        await message.channel.send(f'{random.choice(elosayings)}')
    elif 'lost so much elo' in message.content:
        await message.channel.send(f'{random.choice(elosayings)}')
    elif 'demoted' in message.content:
        await message.channel.send(f'{random.choice(elosayings)}')
    elif 'lost' in message.content:
        await message.channel.send(f'{random.choice(elosayings)}')
    elif 'losing' in message.content:
        await message.channel.send(f'{random.choice(elosayings)}')
    elif 'win ' in message.content:
        await message.channel.send(f'{random.choice(winsayings)}')
    elif 'won ' in message.content:
        await message.channel.send(f'{random.choice(winsayings)}')
    elif 'winning ' in message.content:
        await message.channel.send(f'{random.choice(winsayings)}')
    elif 'who is Sun Tzu?' in message.content:
        await message.channel.send(f'{"Sun Tzu (l. c. 500 BCE) was a Chinese military strategist and general best known as the author of the work The Art of War, a treatise on military strategy, which advocated military preparedness in maintaining peace and social order. No pronouns are required for my commands, cuz I am just built different. There are many other functions besides random quotes that I have. Built by Aaron Tse."}')
    await client.process_commands(message)






client.run(os.environ['DISCORD_TOKEN'])

#not including bot key as discord freaks out and stops bot from working if I push it to github with public permissions :( 
