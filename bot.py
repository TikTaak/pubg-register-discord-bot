import discord
from discord.ext import commands
from discord.utils import get

from asyncio import *

class Config():
    token = "OTYzNzQxMzkxMjUzNTY1NDQx.YlagHQ.IB3ZdPDYE-Ls6Cn9YuqUqvzry1A"
    prefix = "%"
    activity = "Artemis"
    admin = ""

scrim_status_array = ["close"]
registered_members_id = []

team_list = []


def add_team(team_info_array):
    team_list.append(team_info_array)

def scrim_status(sta):
    scrim_status_array.clear()
    scrim_status_array.append(sta)

def delete_team(innp):
    team_list.pop(int(innp) - 1)

client = commands.Bot(command_prefix = Config.prefix)
client.remove_command('help')

@client.event
async def on_ready():
    activeservers = client.guilds
    print("Bot ready")

@client.command()
async def help(ctx):
    await ctx.send(" for registe use '%add <team name>/<team tag>/<mention manager>'\n for see registered teams use %teams .")

@client.command()
async def set(ctx, st):
    if (st == "open"):
        scrim_status("open")
        await ctx.send("scrim is open :white_check_mark: ")
    elif(st == "close"):
        scrim_status("close")
        await ctx.send("Scrim closed :no_entry_sign: ")
    else:
        await ctx.send("please send 'set open' for make a scrim \n or 'set close' for close scrim ")


@client.command()
async def add(ctx, * , team_info):
    for sc_st in scrim_status_array:
        if (sc_st == "open"):
            if (len(team_info.split("/")) == 3):
                if (len(team_list) == 4):
                    await ctx.send("<@{}> Register is Close ! :no_entry_sign: ".format(member))
                else:
                    "arman/play team/@ॠ arman ellaЯӨS#5334"
                    member = ctx.message.author.id
                    user = ctx.message.author
                    print(member)
                    print(user)
                    inp = team_info.split("/")
                    print(inp[2])
                    inp.append(str(member))
                    add_team(inp)
                    #  role
                    role = ctx.guild.get_role(1007299535917293568)
                    await user.add_roles(role)
                    
                    await ctx.send("<@{}> You registered ! :white_check_mark: ".format(member))
                    if (len(team_list) == 18):
                        await ctx.send("@everyone Register Closed !! :no_entry_sign: ")
            else:
                await ctx.send("<@{}> your input team informations ins not match with template !! please try again :x: .".format(member))
        else:
            await ctx.send("<@{}>no scrim started !".format(member))



@client.command()
async def teams(ctx):
    embed=discord.Embed(title="Scrim")
    embed_team_list = ""
    counter = 1
    for i in team_list:
        #embed_team_list = embed_team_list + i[1] + "{}\n".format(str(team_list.index(i)))
        embed_team_list = embed_team_list + "{} - {}".format(str(team_list.index(i) + 1), i[1]) + "\n"
    embed.add_field(name="Team's Registered : ", value=embed_team_list, inline=False)
    await ctx.send(embed=embed)

@client.command()
async def delete(ctx, inn):
    try:
        if (0 < int(inn) <= len(team_list)):

            delete_team(int(inn))

            embed=discord.Embed(title="Scrim")
            embed_team_list = ""
            counter = 1
            for i in team_list:
                #embed_team_list = embed_team_list + i[1] + "{}\n".format(str(team_list.index(i)))
                embed_team_list = embed_team_list + "{} - {}".format(str(team_list.index(i) + 1), i[1]) + "\n"
            embed.add_field(name="Team's Registered : ", value=embed_team_list, inline=False)
            await ctx.send(embed=embed)
            # delete_team(1)
        else:
            await ctx.send("i can't find your target team !")
    except:
        pass
client.run(Config.token)
