import discord

client = discord.Client()


token = '★봇토큰★'


@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game('고객센터 봇🤖')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.guild is None:
        if message.author.bot:
            return
        else:
            embed = discord.Embed(colour=discord.Colour.blue(), timestamp=message.created_at)
            embed.add_field(name='문의 관리자', value=message.author, inline=False)
            embed.add_field(name='문의 DM고객센터', value=message.content, inline=False)
            embed.set_footer(text=f'!디엠 <@{message.author.id}> [할말] 을 통해 답장을 보내주세요!')
            await client.get_channel(★디엠 내용 보내질 채널ID★).send(f"`{message.author.name}({message.author.id})`", embed=embed)

    if message.content.startswith('!디엠'):
        if message.author.guild_permissions.manage_messages:
            msg = message.content[26:]
            await message.mentions[0].send(f"**{message.author.name}** 님의 답장: {msg}")
            await message.channel.send(f'`{message.mentions[0]}`에게 DM을 보냈습니다')
        else:
            return
        
client.run(token)
