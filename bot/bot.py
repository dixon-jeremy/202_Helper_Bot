from random import random

import discord
import random
from globals import get_globals

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('!help'):
        await message.channel.send('It appears that you have requested help.\n \
        !info - Will tell you how to use this office hour system\n \
        !office - Will provide you with the current office hours schedule\n \
        !due - Will provide you with due dates of current assignments\n')
    if message.content.startswith('!grade_worry'):
        await message.channel.send("We're worried about your grade too.")
    if message.content.startswith('!meow'):
        await message.channel.send('meow!')
    if message.content.startswith('!due'):
        await message.channel.send('CMSC 202 Due Dates:\n \
        Lab 8 - Thursday, March 26th on GL\n \
        Project 3 - Thursday, April 2nd @8:59pm on GL\n \
        Exam 2 - Thursday, April 9th on Blackboard\n')
    if message.content.startswith('!info'):
        await message.channel.send('CMSC 202 Office Hours:\n \
        When office hours are available, you can request help\n \
        You go to the waiting room and type !request **a bit about the help you need*\n \
        When an Instructor or TA is available, they will accept your request\n')
    if message.content.startswith('!ta'):
        await message.channel.send('Office Hours and Lab Instructions:\n \
        To create a set of special private rooms for lab use:\n \
        @202Bot lab start\n \
        @202Bot lab end\n \
        To start and stop office hours use:\n \
        @202Bot oh start\n \
        @202Bot end oh\n')
    if message.content.startswith('!office'):
        file = discord.File("bot/img/office2.png", filename="bot/img/office2.png")
        await message.channel.send("CMSC 202 Spring 2020 Office Hours", file=file)
    if message.content.startswith('!grade'):
        random.seed()
        grade = random.randint(0, 100)
        await message.channel.send('Your current grade is ' + str(grade) + '\nAlso, these are random.')
    if message.content.startswith('!drop'):
        await message.channel.send('Attempting withdraw from course...')
        await message.channel.send('Failed. You can withdraw until Monday, April 6th')
    if message.content.startswith('!runt'):
        random.seed()
        choice = random.randint(0,4)
        runt = ["red", "yellow", "purple", "orange", "green"]
        file = discord.File("bot/img/"+runt[choice]+".png", filename="bot/img/"+runt[choice]+".png")
        await message.channel.send("You got a " + runt[choice] + " Runt!", file=file)

if __name__ == '__main__':
    info = get_globals()
    if info:
        token = info['props']['token']
        prefix = info['props']['prefix']
        client.run(token)