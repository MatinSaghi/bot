import discord
from discord.ext import commands

intents=discord.Intents.default()
intents.message_content=True
intents.members=True
intents.presences=True

Bot= commands.Bot (command_prefix="+" , intents=intents)

@Bot.event
async def on_member_join(member):
    log_channel = Bot.get_channel(1518192110770196630)     # چنل لاگ
    welcome_channel = Bot.get_channel(1518198846436413573) # چنل ولکام

    # لاگ ساده
    if log_channel:
        await log_channel.send(f"{member.name} join shod")

    # امبد خوشگل
    if welcome_channel:
        embed = discord.Embed(
            title="Welcome To Aqua server",
            description=f"salam {member.mention} Khosh Omadi.",
            color=discord.Color.green()
        )

        embed.set_thumbnail(url=member.avatar.url)  # عکس پروفایل
        embed.set_footer(text=f"ID: {member.id}")

        await welcome_channel.send(embed=embed)

@Bot.event
async def on_member_remove(member):
    channel =  Bot.get_channel(1518192110770196630)
    if channel:
        await channel.send(f"{member.mention}left the server")  

@Bot.event
async def on_member_ban(guild , user):
  channel = Bot.get_channel(1518197129657716777)
  if channel:
    await channel.send(f"{user.name}ban shod")

@Bot.event
async def on_member_unban(guild , user):
  channel = Bot.get_channel(1518197129657716777)
  if channel:
    await channel.send(f"{user.name}unban shod")

Token= "MTQzMjMwOTU5MDQ4NTI0MTg3Ng.GQAuW7.If3qs32BWmj3lcJwI59Rh20t84p6thS_ucwp7Q"
Bot.run(Token)
