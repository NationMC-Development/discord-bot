import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="h:", help_command=None)

@bot.command()
async def help(ctx):#コマンドを定義するときの関数は必ずContextという引数が渡される。つまり引数を最低一つだけでも書いておかないと動かないので注意
    embed = discord.Embed(title="ヘルプ", description="このヘルプコマンドにはプレフィックスを書いていないため、\n実行には全て`h:コマンド名`とする必要があります。",color=0x4169e1)
    #↑ここのテキストは自分で修正よろしく
    embed.add_field(name="**help**", value="このコマンドです。",inline=False)
    embed.add_field(name="**about**", value="botについてや、botの招待リンク、サポートサーバーを確認できます。",inline=False)
    embed.add_field(name="**globalch**", value="「humi-global」というチャンネルを作成するとグローバルチャットに接続できます。",inline=False)
    await ctx.send(embed=embed)#Contextにはいろいろな情報が入っており、そこから様々な関数、情報にアクセスできる。ctx.sendがその一つ

@bot.command()
async def about(ctx):
    embed = discord.Embed(title="このbotについて...", description="humi server",color=0x4169e1)
    embed.add_field(name="製作者", value="Mumeinosato#7252 \n[無名の里](https://www.youtube.com/channel/UCpb92184AP2Ffhyf7u2bD3w?view_as=subscriber) [@mumeinosato](https://mobile.twitter.com/mumeinosato)",inline=False)
    embed.add_field(name="このbotを招待", value="[こちら](https://discord.com/api/oauth2/authorize?client_id=936868771371569203&permissions=8&scope=bot)から招待できます",inline=False)
    await ctx.send(embed=embed)


@bot.event
async def on_message(message):
    """
    if message.author == bot.user:
        return
    """#Bot判定は下のif文で十分。ちなみにこれは複数行コメントアウト
    if message.author.bot:
        return
    
    GLOBAL_CH_NAME = "humi-global"
    
    if message.channel.name == GLOBAL_CH_NAME:                                                          
        print("success")
        await message.delete() # 元のメッセージは削除しておく
        channels = bot.get_all_channels()
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]
        embed = discord.Embed(
            description=message.content, color=0x00bfff)
        embed.set_author(name=message.author.display_name,                                                                            
            icon_url=message.author.avatar_url_as(format="png"))
        embed.set_footer(text=f"{message.guild.name}",
            icon_url=message.guild.icon_url_as(format="png"))# Embedインスタンスを生成、投稿者、投稿場所などの設定
        for channel in global_channels:# メッセージを埋め込み形式で転送
            await channel.send(embed=embed)

    await bot.process_commands(message)

bot.run("token")            