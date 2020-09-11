import discord
from discord.ext import commands
import asyncio

clopper = commands.Bot(command_prefix='c!', description='A multipurpose bot written in Python.')

cogs = ['modules.audio', 'modules.mod', 'modules.profiles', 'modules.fun', 'modules.general']

@clopper.event
async def on_ready():
  await clopper.change_presence(game=discord.Game(name=str(len(clopper.servers)) + ' servers'))

for cog in cogs: clopper.load_extension(cog)

clopper.run('NzMyODI4NjEzMjA4MDQ3Njg3.Xw6R1A.SCUQd-0A2dkfszjpdqGLYHAMVRM')
