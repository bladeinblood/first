import discord
from discord.ext import commands
from discord.ext.commands.core import command
import asyncio
import datetime

PREFIX = '$'

client = commands.Bot(PREFIX) # $help
client.remove_command('help')


@client.event

async def on_ready():
    print('BOT connected')


#warn
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def warn1(ctx, member: discord.Member, *, reason = None):
    await member.send('Тебе кинули варн Еще 2 улетишь в бан')
    await ctx.send(f'{member.mention} кинули варн')
    if member is None:
        await ctx.send('Укажи пользователя')
    print(f'{member.mention} ему кинули варн')
    with open("base/warns/warns.txt", "w") as f:
        f.write(f'{member.mention} was warn1') 

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def warn2(ctx, member: discord.Member, *, reason = None):
    await member.send('Тебе кинули варн Еще 1 улетишь в бан')
    await ctx.send(f'{member.mention} кинули варн')
    if member is None:
        await ctx.send('Укажи пользователя')
    print(f'{member.mention} ему кинули варн')
    with open("base/warns/warns.txt", "w") as f:
        f.write(f'{member.mention} was warn2') 

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def warn3(ctx, member: discord.Member, *, reason = None):
    await member.send('Соррян но ты летишь в бан')
    await ctx.send(f'{member.mention} кинули варн')
    if member is None:
        await ctx.send('Укажи пользователя')
    print(f'{member.mention} ему кинули варн')
    with open("base/warns/warns.txt", "w") as f:
        f.write(f'{member.mention} was warn3 and banned') 
    await member.ban(reason = reason)


#$help
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def help(ctx):
    emb = discord.Embed(title = 'help', colour = discord.Color.blue())
    
    emb.add_field(name = '{}kick'.format(PREFIX), value = 'Кик участника с сервера')
    emb.add_field(name = '{}ban'.format(PREFIX), value = 'Бан участника с сервера')
    emb.add_field(name = '{}mute'.format(PREFIX), value = 'Мут участника')
    emb.add_field(name = '{}unban'.format(PREFIX), value = 'Анбан участника ')
    emb.add_field(name = '{}tempmute1h'.format(PREFIX), value = 'Временный мут на 1 час')

    await ctx.send(embed = emb)
    print("Help выведено")

#tempmute
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
#947102409665163284
async def tempmute1h(ctx, member: discord.Member, *, reason = None):
    if member is None:
        print('Укажи пользователя')
    role = discord.utils.get(ctx.guild.roles, id=947102409665163284)
    await member.add_roles(role, reason = reason)
    print(f"muted {member.mention}")
    await asyncio.sleep(3600)
    await member.remove_roles(role)
    print(f"unmuted {member.mention}")
    

#hello
@client.command(pass_context = True)

async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f' Привет {author.mention}')
    print(f'Hello {member.mention}')

#embed_time
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def time(ctx):
    emb = discord.Embed(title = 'Time', colour = discord.Color.blue(), url = 'https://time.is/uk/')

    emb.set_author(name = client.user.name, icon_url = client.user.avatar_url)
    emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
    emb.set_image(url = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fapps.apple.com%2Fru%2Fapp%2Ftime-timer%2Fid332520417%3Fl%3Duk&psig=AOvVaw1UYDIwoQ7XQLjFIBendMew&ust=1646218563412000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCMi5kpngpPYCFQAAAAAdAAAAABAD')

    now_date = datetime.datetime.now()
    emb.add_field(name = 'Time', value = 'Time : {}'.format(now_date))

    await ctx.send(embed = emb)

#kick
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def kick(ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge(limit = 1)

    await member.kick(reason = reason)
    await ctx.send(f'kick user {member.mention}')
    print(f'Kicked {member.mention}')

    with open("base/kicks/kick.txt", "w") as f:
        f.write(f'{user.mention} kicked') 

#ban
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def ban(ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge(limit = 1)

    await member.ban(reason = reason)
    await ctx.send(f'ban user {member.mention}')
    print(f'Banned {member.mention}')

    with open("base/bans/bans.txt", "w") as f:
        f.write(f'{user.mention} was banned')

#mute
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
#947102409665163284
async def mute(ctx, member: discord.Member, *, reason = None):
    role = discord.utils.get(ctx.guild.roles, id=947102409665163284)
    await member.add_roles(role, reason = reason)
    print(f"muted {member.mention}")

    with open("base/mute/mutes.txt", "w") as f:
        f.write(f'{member.mention} mute')    

#unmute
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
#947102409665163284
async def unmute(ctx, member: discord.Member, *, reason = None):
    role = discord.utils.get(ctx.guild.roles, id=947102409665163284)
    await member.remove_roles(role)
    await ctx.send(f'unmuted user {member.mention}')
    print(f'Unmuted {member.mention}')

    with open("base/mute/unmute.txt", "w") as f:
        f.write(f'{member.mention} unmuted') 

#unban
@client.command(pass_context = True)

async def unban(ctx, *, member):
    await ctx.channel.purge(limit = 1)
    
    banned_users = await ctx.guild.bans()

    for ban_entry in banned_users:
        user = ban_entry.user

        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned user {user.mention}')
        print(f'{user.mention} unbanned')
        with open("base/bans/unbans.txt", "w") as f:
            f.write(f'{user.mention} unbanned') 

        return

        

# Connect

token = open('token.txt', 'r').readline()

client.run(token)