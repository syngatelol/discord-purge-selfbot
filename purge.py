import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.' ,self_bot = True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def purge(ctx, amount: int):
    if isinstance(ctx.channel, discord.TextChannel):
        def is_author(message):
            return message.author == ctx.author

        deleted_messages = await ctx.channel.purge(limit=amount + 1, check=is_author, bulk=True)

        await ctx.send(f'Deleted {len(deleted_messages) - 1} messages in this channel.')
    elif isinstance(ctx.channel, discord.DMChannel):
        def is_author(message):
            return message.author == ctx.author

        deleted_messages = []
        async for message in ctx.channel.history(limit=amount + 1):
            if is_author(message):
                await message.delete()
                deleted_messages.append(message)

        await ctx.send(f'Deleted {len(deleted_messages) - 1} messages in this DM.')

bot.run('Token' ,bot = False)
