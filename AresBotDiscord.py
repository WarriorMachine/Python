# coding: utf-8

# mfa. K6S7Y_19aacsuhWTZSYgvS60HOnAY-_YqzCl5030j6YLB-3WPwo2wajzHz0UGGpwBKFjAISU-Y1MCXv2cHZr (my token)
import discord
import time
import aiohttp
import json
import math
import os
import random
import asyncio
import youtube_dl
import datetime
from discord.ext import commands
from itertools import cycle
from discord.utils import get
from mcstatus import MinecraftServer

os.system('title DISCORD BOT : Ares')

BOT_PREFIX = ("ARS ", "ars ", "ARES ", "ares ", "Ares ", "Ars ")
TOKEN = 'NTkwNjc1NDI2NjE2Mjc5MDUx.XQl34Q.0m7mGgzBtuGhe1zMZGBz6uu_C0E'

client = commands.Bot(command_prefix = BOT_PREFIX)
client.remove_command('help')

players = {}
queues = {}

async def change_status():
    i = 1000
    initi = 0
    await client.wait_until_ready()
    while not client.is_closed:
        try:
            current_status = next(msgs)
        except:
            pass
        if initi == 0:
            membernum = 0
            for server in client.servers:
                for member in server.members:
                    membernum = membernum+1
            status = ['utilise moi : ARS',"sur "+str(len(client.servers))+" serveurs","avec "+str(membernum)+" membres",'WarT®','ars help','new : triggered','new : NSFW']
            msgs = cycle(status)
            current_status = next(msgs)
            initi = 1
        await client.change_presence(status=discord.Status.dnd, game=discord.Game(name=current_status, type=1, url="https://www.twitch.tv/warriormachine_")) #online idle dnd invisible
        i = i+1
        await asyncio.sleep(10)
        if i >= 1000:
            print("\n\nAres est sur :")
            i = 0
            for server in client.servers:
                print("- "+str(server.name))

@client.event
async def on_ready():
    print("ID : "+str(client.user.id))
    print(str(client.user.name)+" en ligne !")
    client.loop.create_task(change_status())

@client.event
async def on_member_join(member):
    embed = discord.Embed(colour = discord.Colour.teal())
    embed.set_author(name='Bienvenue '+str(member.name)+' sur '+str(member.server),icon_url=member.server.icon_url)
    embed.add_field(name='Ecrit ARS help 🚩', value="pour obtenir de l'aide", inline=True)
    embed.add_field(name='Le Staff est à ta disposition', value="mentionne les :wink:", inline=True)
    embed.set_footer(text='Amuse toi bien')
    embed.set_image(url='https://www.artiref.com/wp-content/uploads/2016/02/welcome.png')
    await client.send_message(member, embed=embed)
    channel = discord.Object(id="597073417195225129")
    embed = discord.Embed(colour = discord.Colour.teal())
    embed.set_author(name='Bienvenue '+str(member.name)+' sur '+str(member.server),icon_url='https://static.wixstatic.com/media/0d48eb_69b87849b93e462195b27ea179d21063~mv2.gif')
    embed.add_field(name='Le Staff est à ta disposition', value="mentionne les :wink:", inline=True)
    embed.set_footer(text='Amuse toi bien')
    embed.set_image(url='https://www.artiref.com/wp-content/uploads/2016/02/welcome.png')
    await client.send_message(channel, embed=embed)
    role = discord.utils.get(member.server.roles, name='೩ Membre')
    await client.add_roles(member, role)

@client.event
async def on_server_join(server):
    channel = discord.Object(id="599952639353946123")
    embed = discord.Embed(colour = discord.Colour.dark_teal())
    embed.set_author(name='Arès rejoint le serveur '+str(server.name),icon_url=server.icon_url)
    embed.set_thumbnail(url=server.icon_url)
    embed.add_field(name=":information_source: Informations >",value="•Nombre de membres :\n"+str(len(server.members))+"\n•Nombre de channels :\n"+str(len(server.channels))+"\n•Nombre de rôles :\n"+str(len(server.roles))+"\n•Propriétaire du serveur :\n"+str(server.owner)+"\n•Serveur créer le :\n"+str(server.created_at.strftime("%d/%m/20%y à %H:%M:%S")))
    embed.set_footer(text="À "+str(time.strftime('%H:%M:%S')))
    await client.send_message(channel, embed=embed)

    emoji = get(client.get_all_emojis(), name="agape")
    embedF = discord.Embed(title="Arès à rejoin "+str(server.name),color=0x36ff1a)
    embedF.set_footer(text="À "+str(time.strftime('%H:%M:%S')))
    embedF.set_image(url='https://res.cloudinary.com/dsqzssrno/image/upload/v1523657121/tsol5czd7zz21sat2o28.gif')
    embedF.add_field(name=str(emoji)+" Pour m'utiliser tapez simplement : `ars ?`",value="*je vous enverai mes commandes*", inline=False)
    await client.send_message(server.owner, embed=embedF)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        pass
    if isinstance(error, commands.CommandNotFound):
        pass

@client.command(pass_context=True)
async def ping(ctx):
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    timePing = time.monotonic()
    await client.say("**Pong !**")
    ping = '%2f'%(1000*(time.monotonic()-timePing))
    embed = discord.Embed(title="Ping", color=discord.Colour.light_grey())
    embed.set_thumbnail(url='https://image.flaticon.com/icons/png/512/23/23644.png')
    embed.add_field(name="Latence :",value=str(ping)+"ms")
    embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    resultText = await client.send_message(channel, embed=embed)
    await client.add_reaction(resultText, "📶")

@client.command(aliases=['infobot', 'infosbot', 'botinfos'], pass_context=True)
async def botinfo(ctx):
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    embed = discord.Embed(title="Infos Arès", color=0x226fac)
    embed.set_thumbnail(url='https://images.discordapp.net/avatars/422087909634736160/ba3af9afe0ec8253149ac7f5f84a69f1.png?size=512')
    embed.add_field(name="Créer le :",value="22:53:15 le 18/06/2019")
    newmemberscore = 0
    for server in client.servers:
        for member in server.members:
            newmemberscore = newmemberscore+1
    embed.add_field(name="Nombre de membres cumulé :",value=str(newmemberscore))
    i=0
    listee = str()
    for server in client.servers:
        i=i+1
        listee = listee+str(i)+str(". `")+str(server.name)+str("` \n")
    embed.add_field(name="Liste de serveurs rejoint :",value=str(listee))
    embed.add_field(name="Nombre de serveurs rejoint :",value=str(len(client.servers)))
    embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    resultText = await client.send_message(channel, embed=embed)

@client.command(name='ball',aliases=['eight_ball', 'eightball', '8-ball', '8ball', 'random', '8b'],pass_context=True)
async def ball(ctx, nombre = -6537634684):
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    if nombre != -6537634684:
        if nombre < 0:
            embed = discord.Embed(title="essayez : ars 8ball {NOMBRE}", color=0xf85a5f)
            embed.set_author(name='Erreur')
            embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
            embed.set_footer(text="Votre nombre doit être supérieur à 0")
            reponseText = await client.send_message(channel, embed=embed)
            await client.add_reaction(reponseText, "✖")
        else:
            if nombre == 666:
                possible_responses = [
                "Mortel, nan ?",
                "Invocation !!",
                "You know what I am"
                ]
                embedF = discord.Embed(title="Nombre compris entre 0 et "+str(nombre),color=discord.Colour.default())
                embedF.add_field(name="🎲 Votre nombre aléatoire est : "+str(random.randint(0,nombre)),value=random.choice(possible_responses))
                embedF.set_image(url='https://i.gifer.com/1upi.gif')
                embedF.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
                messageF = await client.send_message(channel, embed=embedF)
                await client.add_reaction(messageF, "😈")
            else:   
                possible_responses = [
                "Franchement pourquoi est-il toujours question de boules ?",
                "Quoi, réellement ? un 8ball, je n'ai pas envie..",
                "C'est occupé merci de revenir..."
                ]
                embedF = discord.Embed(title="Nombre compris entre 0 et "+str(nombre),color=discord.Colour.default())
                embedF.add_field(name="🎲 Votre nombre aléatoire est : "+str(random.randint(0,nombre)),value=random.choice(possible_responses))
                embedF.set_image(url='https://cdn.dribbble.com/users/1910217/screenshots/4218363/casino-roulette.gif')
                embedF.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
                messageF = await client.send_message(channel, embed=embedF)
                await client.add_reaction(messageF, "🎱")
    else:
        embed = discord.Embed(title="essayez : ars 8ball {NOMBRE}", color=0xf85a5f)
        embed.set_author(name='Erreur')
        embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
        embed.set_footer(text="Il manque quelque chose..")
        reponseText = await client.send_message(channel, embed=embed)
        await client.add_reaction(reponseText, "✖")

@client.command(name='suicide',pass_context=True)
async def suicide(ctx):
    invitelinknew = await client.create_invite(destination = ctx.message.channel, xkcd = True, max_uses = 1)
    channel = ctx.message.channel
    choix = ["tombe1",
    "tombe2"]
    photo = ["https://discordemoji.com/assets/emoji/kys.png",
    "https://assets.change.org/photos/9/kg/hk/apkghKzQyVZjhzk-800x450-noPad.jpg",
    "https://cdn.icon-icons.com/icons2/1728/PNG/512/4003980-christmas-dead-death-emoji-santa_113002.png",
    "",
    ""]
    emoji1 = get(client.get_all_emojis(), name=random.choice(choix))
    await client.send_typing(channel)
    await asyncio.sleep(1)
    embedF = discord.Embed(title='Ouïe..', color=000000)
    embedF.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    embedF.set_thumbnail(url=random.choice(photo))
    embedF.add_field(name="Nous venons de perdre", value=str(ctx.message.author), inline=False)
    messageF = await client.send_message(channel, embed=embedF)
    await client.add_reaction(messageF, emoji1)

    author = ctx.message.author
    embed = discord.Embed(title='Envie de resurection ?', color=0xffffff)
    embed.set_thumbnail(url='http://clipart-library.com/images_k/angel-emoji-transparent/angel-emoji-transparent-21.png')
    embed.add_field(name='Clique :', value=invitelinknew, inline=False)
    embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    message = await client.send_message(author, embed=embed)

    await client.kick(ctx.message.author)

@client.command(name='chat',aliases=['cat', 'miaou'],pass_context=True)
async def chat(ctx):
    possible_responses = [
        "https://data.photofunky.net/output/image/e/b/c/c/ebcc2e/photofunky.gif",
        "https://file1.grazia.fr/var/grazia/storage/images/media/images/what-s-the-buzz/gifs-chats/gif4/13466161-1-fre-FR/Gif4_width545.gif",
        "https://lehollandaisvolant.net/img/5c/cat-gifs.gif",
        "https://p7.storage.canalblog.com/79/27/833312/83114448_p.gif",
        "https://medias.francoischarron.com/thumbnail/medias.francoischarron.com/gifs/original/gifs-chats-chiens-87VVll2Sgw.gif",
        "https://media.tenor.com/images/82517b1fbf01e0db1c2636319e2c6965/tenor.gif",
        "https://static.mmzstatic.com/wp-content/uploads/2013/08/gifchat16.gif",
        "http://gifdrole.com/meilleurs_gifs_animes_droles_de_chats/Dancing_cats.gif",
        "https://www.legipermis.com/blog/wp-content/uploads/2014/04/tumblr_mxx1ed5Rmh1s02vreo1_400.gif",
        "https://media3.giphy.com/media/A0aEq3RE7OFbi/giphy.gif",
        "https://www.goldens.fr/wp-content/uploads/2018/11/81fa002536a762ca72e2db4aa887655d.gif",
        "https://i2.wp.com/www.droles-de-chats.fr/wp-content/uploads/2017/11/gif-chat-article-1.6.gif?fit=499%2C231",
        "https://thumbs.gfycat.com/ShabbyThankfulHyrax-size_restricted.gif",
        "https://cache.cosmopolitan.fr/data/fichiers/44/catshower.gif",
        "https://media1.tenor.com/images/5738658e35fa01ace094ce17ec2f4f9d/tenor.gif?itemid=9934420",
        "https://static.mmzstatic.com/wp-content/uploads/2013/08/gifchat11.gif",
        "https://www.espacebuzz.com/assets/ckeditor/2014/sep/1096/originale/740_espacebuzz540d6022d3bb2.gif",
        "https://media1.giphy.com/media/4uVyQiFGLicuI/giphy.gif",
        "https://www.numerama.com/discussions/uploads/default/original/2X/4/4371f377ec81e91675ab8d265bc2e7c9c7b595f2.gif",
        "http://animaals.com/wp-content/uploads/2016/08/chat-chien-marrer-journee-gif-12.gif",
        "https://www.onefm.ch/wp-content/uploads/2018/08/chat-a-l-affut.gif",
        "https://i2.wp.com/www.photos-a-la-con.fr/wp-content/uploads/2017/12/image-drole-chat5.gif?resize=354%2C266",
        "https://www.imparfaites.be/wp-content/uploads/2015/09/funny-cat-gif.gif",
        "https://www.focusur.fr/wp-content/uploads/2016/12/gif-chat.gif",
        "https://i2.wp.com/www.droles-de-chats.fr/wp-content/uploads/2017/11/gif-chat-article-1.7.gif?fit=346%2C177",
        "https://data.photofunky.net/output/image/b/1/9/a/b19aaf/photofunky.gif",
        "http://blog.pasqunpeu.fr/wp-content/uploads/2011/04/580475001302798635.gif",
        "https://i.makeagif.com/media/6-29-2015/1OdX-D.gif",
        "https://daks2k3a4ib2z.cloudfront.net/5677cfc11a207bc755d0295c/56cdac446bae02f154dcb625_amateur-de-biere-chat-potte.gif"
        "https://p1.storage.canalblog.com/15/44/943891/107080481.gif"
    ]
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    embedF = discord.Embed(title='Chat', color=discord.Colour.teal())
    embedF.set_image(url=random.choice(possible_responses))
    embedF.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    messageF = await client.send_message(channel, embed=embedF)
    await client.add_reaction(messageF, "🐱")

@client.command(name='triggered',aliases=['triger', 'trigger','randomtriggered'],pass_context=True)
async def triggered(ctx):
    possible_responses = [
        "https://media1.tenor.com/images/c5dd72c7443a2d62ceb22c4e4c672f4c/tenor.gif",
        "https://media1.tenor.com/images/ff9ac4b6c8071d9ddb28d0c40721074b/tenor.gif",
        "https://media.tenor.com/images/d213cc0fadd5b0aa5d088c2b8cd6dc47/tenor.gif",
        "https://i.gifer.com/origin/29/2950735d1b1435007bbf05b838232a23_w200.gif",
        "https://thumbs.gfycat.com/ThoroughTheseBluejay-size_restricted.gif",
        "https://media.tenor.com/images/376ad88d54d4e1f66caf8215802fc2f7/tenor.gif",
        "https://thumbs.gfycat.com/FineGenuineIggypops-size_restricted.gif",
        "https://thumbs.gfycat.com/DearestSpiffyAlpaca-small.gif",
        "https://thumbs.gfycat.com/RingedVacantEarthworm-size_restricted.gif",
        "https://dragon.best/media/img/gifs/triggered.gif",
        "https://i.kym-cdn.com/photos/images/original/001/276/514/6a5.gif",
        "https://www.wykop.pl/cdn/c3201142/comment_hzahW30fDetRdfHP3Np6GsfZ1ch4vvlS.gif",
        "https://orig10.deviantart.net/6f09/f/2016/259/f/a/commission__triggered_adventure_foxy_by_dangerdude991-dahtn2r.gif",
        "https://i2.wp.com/78.media.tumblr.com/ed39e57f526e62fe704540ced5263c07/tumblr_onnerdtEao1vdbl7uo1_r2_500.gif",
        "https://www.pixilart.com/images/art/16fbddead8cfec6.gif",
        "https://i.imgur.com/kuhYbg7.gif",
        "https://thumbs.gfycat.com/SlimyThickGuillemot-max-1mb.gif",
        "https://media1.tenor.com/images/bac5a118662ca717b23636f8083d3bfe/tenor.gif",
        "https://i.redd.it/euqf4wjagda11.gif",
        "https://media1.giphy.com/media/13gju7gQRjdM8E/source.gif",
        "https://i.kym-cdn.com/photos/images/newsfeed/001/401/904/56b.gif",
        "https://pa1.narvii.com/6353/032e34aed0fe230a5001ac19e7ba1d8438d0859c_hq.gif",
        "https://thumbs.gfycat.com/GregariousDefensiveBarebirdbat-size_restricted.gif",
        "https://aws1.discourse-cdn.com/pocketgems/uploads/episodeinteractive/original/4X/5/9/b/59bd9b2d96e9b6eb70bdfa6291c6f32e4b185311.gif",
        "https://i.kym-cdn.com/photos/images/original/001/238/907/8cb.gif",
        "https://i.pinimg.com/originals/1d/98/d1/1d98d1966f4df2383ccff2fba0b1eba3.gif",
        "https://thumbs.gfycat.com/AgitatedDelightfulIchidna-size_restricted.gif",
        "https://risibank.fr/cache/stickers/d1430/143026-full.gif",
        "https://i.pinimg.com/originals/c1/78/8b/c1788befbe92ee8a278e3930563173de.gif",
        "https://pa1.narvii.com/7023/5bef918a79ef955385070ce122b49e14af084d97r1-256-256_00.gif",
        "https://vignette.wikia.nocookie.net/random-memes/images/9/94/37BF8908-1349-4A5C-B12C-3F9061808267.gif",
        "https://media1.tenor.com/images/0ea3b27f9c436ee7a0c0550c3705ca6d/tenor.gif",
        "https://66.media.tumblr.com/d089d8d913f8d30496579008d7ed3e66/tumblr_inline_pbliks7i6r1v1upih_400.gif",
        "https://i.imgflip.com/1ep78f.gif",
        "https://media.giphy.com/media/XZOLSRM10XjJ9Zjrvh/giphy.gif"
    ]
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    embedF = discord.Embed(title='TRIGGERED', color=0xdb8228)
    embedF.set_image(url=random.choice(possible_responses))
    embedF.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    messageF = await client.send_message(channel, embed=embedF)

@client.command(name='chien',aliases=['dog', 'woof', 'wouaf'],pass_context=True)
async def chien(ctx):
    possible_responses = [
        "https://img.buzzfeed.com/buzzfeed-static/static/2013-12/enhanced/webdr06/3/12/anigif_enhanced-buzz-14140-1386090436-22.gif?downsize=700:*&output-format=auto&output-quality=auto",
        "https://img.buzzfeed.com/buzzfeed-static/static/2013-12/enhanced/webdr02/3/12/anigif_enhanced-buzz-2848-1386091343-4.gif?downsize=700:*&output-format=auto&output-quality=auto",
        "https://wamiz.com/uploads/additional/2010-09/thumbs/standard_chiens-tapis-de-course.gif",
        "https://media1.giphy.com/media/8wRy9PtdcCSXK/giphy.gif",
        "http://static.mmzstatic.com/wp-content/uploads/2015/08/journee-chien-corgi-wat.gif",
        "https://www.neonmag.fr/content/uploads/2016/12/chien.gif",
        "https://img.buzzfeed.com/buzzfeed-static/static/2013-12/enhanced/webdr07/3/12/anigif_enhanced-buzz-14001-1386091192-11.gif?downsize=700:*&output-format=auto&output-quality=auto",
        "http://i.imgur.com/t9BrRmr.gif",
        "https://i.pinimg.com/originals/81/29/6f/81296f50927605ec6b778abcdb733c27.gif",
        "https://data.photofunky.net/output/image/2/e/7/8/2e78d6/photofunky.gif",
        "https://thumbs.gfycat.com/GregariousEvilCygnet-size_restricted.gif",
        "https://data.photofunky.net/output/image/a/1/1/a/a11a8f/photofunky.gif",
        "https://s3-eu-west-1.amazonaws.com/sc-files.pjms.fr/p/pjms/282/000/211/750/036dd99707064122a634c2f48abdee1d.gif",
        "https://wamiz.com/uploads/images/1ultima.gif",
        "http://welikeit.fr/wp-content/uploads/2014/09/giphy.gif",
        "https://i.pinimg.com/originals/cb/46/67/cb4667eea17fdb06c658f2a5e9638fb1.gif",
        "http://aws-cf.imdoc.fr/prod/photos/3/5/5/8770355/23097022/img-23097022e27.gif?v=12",
        "https://data.photofunky.net/output/image/f/e/f/4/fef4e9/photofunky.gif",
        "http://24.media.tumblr.com/ee256bb8adfddd7236c9b9d8d6c44ed6/tumblr_mjwkq0yp7q1s3peh7o1_400.gif",
        "https://www.akenini.com/media/files/Imagesfun/Mini_animations/025.gif",
        "https://data.photofunky.net/output/image/d/f/1/6/df1609/photofunky.gif",
        "https://i.pinimg.com/originals/0e/7e/9a/0e7e9acb982874bd8b80b5fc62fa2295.gif",
        "http://www.lovethispic.com/uploaded_images/183690-Meet-My-New-Puppy.gif",
        "https://media.giphy.com/media/fteN9xUix9scHPWZcz/source.gif",
        "https://img.static-rmg.be/a/view/q75/w720/h480/1515940/dog1.gif",
        "https://www.woopets.fr/assets/ckeditor/News/dec_16/gifs_even/giphy_6.gif",
        "https://www.ipnoze.com/wordpress/wp-content/uploads/2018/03/retrievers-labradors-mignons-012.gif",
        "https://img.buzzfeed.com/buzzfeed-static/static/2014-06/14/15/enhanced/webdr08/anigif_enhanced-6098-1402774143-5.gif?downsize=700:*&output-format=auto&output-quality=auto",
        "https://www.woopets.fr/assets/ckeditor/News/jan_17/gifs_2001/17.gif",
        "http://38.media.tumblr.com/460788b998b7a371247d7590a72d410c/tumblr_mu8nq0zLz91skpqx1o1_400.gif",
        "https://www.woopets.fr/assets/ckeditor/News/Novembre_2017/9.gif",
        "https://media.tenor.com/images/bc77c36fb1c7dc2cb8b8922bb1b7b85f/tenor.gif",
        "https://media.tenor.com/images/65729ee29fe11faff167faf58a647318/tenor.gif",
        "https://files.sympa-sympa.com/files/news/part_70/702110/rqZKi4g-1553592040.gif",
        "https://data.photofunky.net/output/image/0/d/2/8/0d2810/photofunky.gif",
        "http://bichonmaltais.elevagedepetitschiens.fr/wp-content/uploads/2014/01/giphy.gif",
        "https://thumbs.gfycat.com/VigilantSeparateBorzoi-size_restricted.gif"
    ]
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    embedF = discord.Embed(title='Chien', color=discord.Colour.teal())
    embedF.set_image(url=random.choice(possible_responses))
    embedF.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    messageF = await client.send_message(channel, embed=embedF)
    await client.add_reaction(messageF, "🐶")

@client.command(name='dab',aliases=['DAB', 'Dab'],pass_context=True)
async def dab(ctx):
    possible_responses = [
        "https://media.giphy.com/media/A4R8sdUG7G9TG/giphy.gif",
        "https://media0.giphy.com/media/xUOwGmG2pRfFZUmdVe/giphy.gif",
        "https://thumbs.gfycat.com/MeaslySilkyFlounder-max-1mb.gif",
        "https://media0.giphy.com/media/3n69aDBlqGlCu10qZv/source.gif",
        "https://media.giphy.com/media/d4blihcFNkwE3fEI/giphy.gif",
        "https://media.giphy.com/media/3h5VTO6F1i2gU/giphy.gif",
        "https://media.giphy.com/media/rECzMG557PSMg/giphy.gif",
        "https://media1.giphy.com/media/xsVnZylYtPK1i/source.gif",
        "https://i.redd.it/kauz38ph36221.gif",
        "https://cdn125.picsart.com/212345420005202.gif",
        "https://media2.giphy.com/media/l2JhMMeXghvBnUpyg/giphy.gif",
        "https://media1.tenor.com/images/9b2147e6ad5a8c7f0ae0f39d37230a56/tenor.gif?itemid=9672617",
        "https://media3.giphy.com/media/eOOcHWaaJnTwc/giphy.gif",
        "https://media3.giphy.com/media/xiOJrpmZzHd9JgAJCh/giphy.gif",
        "https://media3.giphy.com/media/xThta6vYRKeX4D1b8Y/giphy.gif",
        "https://i.ya-webdesign.com/images/dab-gif-png-8.gif",
        "https://img.buzzfeed.com/buzzfeed-static/static/2016-08/17/3/asset/buzzfeed-prod-fastlane01/anigif_sub-buzz-9637-1471417722-2.gif?downsize=700:*&output-format=auto&output-quality=auto",
        "https://i.gifer.com/1ImD.gif",
        "https://i.redd.it/dj5w06oacxnz.gif",
        "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/027a23d1-26e7-4d2f-881f-48be2b7b04a0/dauf4p2-abc8994f-b3ec-4ffc-a5bc-29ef1c476029.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzAyN2EyM2QxLTI2ZTctNGQyZi04ODFmLTQ4YmUyYjdiMDRhMFwvZGF1ZjRwMi1hYmM4OTk0Zi1iM2VjLTRmZmMtYTViYy0yOWVmMWM0NzYwMjkuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.7Rgguzd3aVfcZR4OcG0aDooq8cXOxBO-6tGp7JHPB2w",
        "https://thumbs.gfycat.com/DizzyWhirlwindAlabamamapturtle-size_restricted.gif",
        "http://www.gifimili.com/gif/2019/02/dab-south-park.gif",
        "https://media.tenor.com/images/0743d25ff71846e7928fc7a1d2b5ec2b/tenor.gif",
        "https://media4.giphy.com/media/l3vR4Lx1KikchyFfW/giphy.gif"
    ]
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    embedF = discord.Embed(title='DAB', color=discord.Colour.blue())
    embedF.set_image(url=random.choice(possible_responses))
    embedF.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    messageF = await client.send_message(channel, embed=embedF)
    choix = ["dabbingdiscord",
    "CarloDab"]
    emoji = get(client.get_all_emojis(), name=random.choice(choix))
    await client.add_reaction(messageF, emoji)

@client.command(name='baffe',aliases=['slap'],pass_context=True)
async def baffe(ctx):
    possible_responses = [
        "https://www.gif-maniac.com/gifs/53/52956.gif",
        "https://www.gif-maniac.com/gifs/53/52955.gif",
        "https://www.gif-maniac.com/gifs/53/52962.gif",
        "https://www.gif-maniac.com/gifs/53/52959.gif",
        "https://www.gif-maniac.com/gifs/53/52960.gif",
        "https://www.gif-maniac.com/gifs/53/52961.gif",
        "https://media1.tenor.com/images/0057c0af7690c99e0a73028f3dfb817f/tenor.gif",
        "https://media.tenor.com/images/f2b2e5acd6b5cde9168062f6fc6ded11/tenor.gif",
        "http://nsa37.casimages.com/img/2017/02/02/170202071453575957.gif",
        "https://media1.tenor.com/images/49de17c6f21172b3abfaf5972fddf6d6/tenor.gif?itemid=10206784",
        "https://data.photofunky.net/output/image/3/4/3/5/34353e/photofunky.gif",
        "http://nsa38.casimages.com/img/2017/02/02/170202072349301594.gif",
        "http://i.imgur.com/fJlCweF.gif",
        "https://media.tenor.com/images/d3a424b670823f1a92ab8dbc35d1e935/tenor.gif",
        "http://legonepeint.e.l.f.unblog.fr/files/2015/01/8freehug1.gif",
        "https://cdn.weeb.sh/images/HJfXM0KYZ.gif",
        "https://cdn.weeb.sh/images/S1ylxxc1M.gif",
        "https://cdn.weeb.sh/images/SkZTQkKPZ.gif",
        "https://cdn.weeb.sh/images/HkskD56OG.gif",
        "https://cdn.weeb.sh/images/SkKn-xc1f.gif",
        "https://cdn.weeb.sh/images/SkdyfWCSf.gif",
        "https://cdn.weeb.sh/images/HkJ6-e91z.gif",
        "https://cdn.weeb.sh/images/rJYqQyKv-.gif",
        "https://cdn.weeb.sh/images/Hkw1VkYP-.gif",
        "https://cdn.weeb.sh/images/ryv3myFDZ.gif",
        "https://cdn.weeb.sh/images/r1siXJKw-.gif",
        "https://cdn.weeb.sh/images/B1fnQyKDW.gif"
    ]
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    embedF = discord.Embed(title='Baffe', color=0x1a0ae0)
    embedF.set_image(url=random.choice(possible_responses))
    embedF.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    messageF = await client.send_message(channel, embed=embedF)
    await client.add_reaction(messageF, "👊")

@client.command(name='poing',aliases=['frappe','punch'],pass_context=True)
async def poing(ctx):
    possible_responses = [
        "https://media1.giphy.com/media/l1J3G5lf06vi58EIE/giphy.gif",
        "https://media.giphy.com/media/l0IyouZhJkG0MG9Us/giphy.gif",
        "https://media2.giphy.com/media/GoN89WuFFqb2U/giphy.gif",
        "https://media.giphy.com/media/7Nsu3HCWLRVgQ/giphy.gif",
        "https://media3.giphy.com/media/l3V0D3RzZSeVDKGFa/source.gif",
        "https://media2.giphy.com/media/Ax6tX3pd7PCms/giphy.gif",
        "https://media0.giphy.com/media/3oEhmIiscXMRGgjqlq/source.gif",
        "https://media3.giphy.com/media/DViGV8rfVjw6Q/giphy.gif",
        "https://media.giphy.com/media/SzC42gUrhHopW/giphy.gif",
        "https://media0.giphy.com/media/dNRqxqr5eiy4g/giphy.gif",
        "https://media1.giphy.com/media/h0l165sEMU3pC/giphy.gif",
        "https://media.giphy.com/media/uidJNS3sWe85W/giphy.gif",
        "https://media2.giphy.com/media/arbHBoiUWUgmc/giphy.gif",
        "https://media1.tenor.com/images/67ba9eb3278bc0d57735e097fb3ae15a/tenor.gif",
        "https://media.giphy.com/media/R7TbTsGdsfkmQ/giphy.gif",
        "https://i.pinimg.com/originals/28/96/1c/28961c69fddcc0deac1dfdbc4db04819.gif",
        "https://i.pinimg.com/originals/99/7a/80/997a804ba20b96a9dc0af3543de4b3ca.gif",
        "https://thumbs.gfycat.com/EllipticalTatteredHarborseal-size_restricted.gif",
        "https://media1.tenor.com/images/64ff21140baffae8e00bbe0baf65c2b9/tenor.gif",
        "https://media2.giphy.com/media/tXV4SypzCogKs/giphy.gif",
        "https://66.media.tumblr.com/4362aa42db65b4ac15ab975f2cd6a867/tumblr_nqmaxz1QWn1twyezqo1_400.gif",
        "https://66.media.tumblr.com/e52837285c2eeb3c81e3d8fe331275d2/tumblr_nt5ah8u6DN1t89rpeo2_500.gif",
        "https://data.whicdn.com/images/244077564/original.gif",
        "https://cdn.weeb.sh/images/SJAfH5TOz.gif",
        "https://cdn.weeb.sh/images/SJR-PpZbM.gif",
        "https://cdn.weeb.sh/images/rJRUk2PLz.gif",
        "https://cdn.weeb.sh/images/BkdyPTZWz.gif",
        "https://cdn.weeb.sh/images/HJqSvaZ-f.gif",
        "https://cdn.weeb.sh/images/ByI7vTb-G.gif",
        "https://cdn.weeb.sh/images/rkkZP6Z-G.gif",
        "https://cdn.weeb.sh/images/BJg7wTbbM.gif",
        "https://cdn.weeb.sh/images/HkFlwpZZf.gif",
        "https://cdn.weeb.sh/images/B1-ND6WWM.gif"
    ]
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    embedF = discord.Embed(title='Poing', color=0x1a0ae0)
    embedF.set_image(url=random.choice(possible_responses))
    embedF.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    messageF = await client.send_message(channel, embed=embedF)
    await client.add_reaction(messageF, "👊")

@client.command(name='kiss',aliases=['bisou','embrasse','bisous'],pass_context=True)
async def kiss(ctx):
    possible_responses = [
        "http://mangapournous.m.a.pic.centerblog.net/to578785.gif",
        "https://media.giphy.com/media/FmB6UTdCj3G12/giphy.gif",
        "https://media1.giphy.com/media/iseq9MQgxo4aQ/giphy.gif",
        "https://media.giphy.com/media/QGc8RgRvMonFm/giphy.gif",
        "https://media.giphy.com/media/UuyMRM3Bazpcc/giphy.gif",
        "https://thumbs.gfycat.com/LegitimateAnnualGentoopenguin-small.gif",
        "https://thumbs.gfycat.com/WarpedSlightFrigatebird-size_restricted.gif",
        "https://media1.giphy.com/media/Vah0NhXAAceli/giphy.gif",
        "https://i.pinimg.com/originals/c2/1d/8b/c21d8bea83706009d0ab494a52076b08.gif",
        "https://media1.tenor.com/images/aa559ce009f9b2613fd9b567e8c6aacd/tenor.gif",
        "https://i.kym-cdn.com/photos/images/newsfeed/000/970/568/1a4.gif",
        "https://i.imgur.com/eisk88U.gif",
        "https://media0.giphy.com/media/flmwfIpFVrSKI/giphy.gif",
        "https://media.giphy.com/media/mGAzm47irxEpG/giphy.gif",
        "https://data.whicdn.com/images/276570515/original.gif",
        "https://media.giphy.com/media/vUrwEOLtBUnJe/giphy.gif",
        "https://media0.giphy.com/media/7gVZAy1iPgixa/giphy.gif",
        "https://i.skyrock.net/6517/89386517/pics/3189878693_1_2_bjyBvoeK.gif",
        "https://media3.giphy.com/media/Z2sivLSfN8FH2/giphy.gif",
        "http://33.media.tumblr.com/a8b3e9f706d5a509b09000fd736b9467/tumblr_n3qrm4N3S31siyfwio1_500.gif",
        "https://media3.giphy.com/media/ZRSGWtBJG4Tza/giphy.gif",
        "http://data.whicdn.com/images/191125508/large.gif",
        "http://31.media.tumblr.com/5862eaa08851f445f315dab997299a18/tumblr_n1iogwvsIH1tozm2ho1_250.gif",
        "https://i.pinimg.com/originals/0d/4f/bf/0d4fbfeef1d488a1ce1aea6b3455b190.gif",
        "http://lepassetempsderose.l.e.pic.centerblog.net/a1b51e46.gif",
        "http://i0.kym-cdn.com/photos/images/original/001/254/837/259.gif",
        "https://media2.giphy.com/media/ll5leTSPh4ocE/giphy.gif",
        "https://s-media-cache-ak0.pinimg.com/originals/f8/88/15/f88815fd60acb642622566fa6969ff5d.gif",
        "https://wir.skyrock.net/wir/v1/resize/?c=isi&im=%2F0508%2F85010508%2Fpics%2F3109660919_1_3_9R57Ip3P.gif",
        "https://media.giphy.com/media/bm2O3nXTcKJeU/giphy.gif",
        "https://steamuserimages-a.akamaihd.net/ugc/921418971829504655/A3C0D50C209F5B033A065A23F442D42D8F0687A4/",
        "https://i.pinimg.com/originals/1f/1c/a2/1f1ca2c09f171676503c2533319b354f.gif",
        "https://media0.giphy.com/media/uSHX6qYv1M7pC/giphy.gif"
    ]
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    embedF = discord.Embed(title='Bisous', color=0xf1a9f3)
    embedF.set_image(url=random.choice(possible_responses))
    embedF.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    messageF = await client.send_message(channel, embed=embedF)
    possible_emoji = [
        "💋",
        "💏",
        "😗",
        "😘",
        "😙",
        "😽"
    ]
    await client.add_reaction(messageF, random.choice(possible_emoji))

@client.command(name='smile',aliases=['sourrir','happy','content'],pass_context=True)
async def smile(ctx):
    possible_responses = [
        "https://media.giphy.com/media/4giCclqeKt0QM/giphy.gif",
        "https://media2.giphy.com/media/3Ugq7dfV3nQDC/giphy.gif",
        "https://media.giphy.com/media/3Cm8cxtSHqu6Q/giphy.gif",
        "https://i.kym-cdn.com/photos/images/original/001/103/137/7d4.gif",
        "https://i.gifer.com/5VA9.gif",
        "https://media.giphy.com/media/KsPC9t0ToZhqU/giphy.gif",
        "https://media.giphy.com/media/yd1p7Gp8EdauY/giphy.gif",
        "https://media1.giphy.com/media/EAOTD2L0qyvhm/giphy.gif",
        "https://i.pinimg.com/originals/18/94/8a/18948a1634f7cc51c86e2b4d914fc7fa.gif",
        "http://reve-of-manga.r.e.pic.centerblog.net/c5ec005f.gif",
        "https://media2.giphy.com/media/lPXNUrANOsMrTuK8Dw/giphy.gif",
        "https://i.imgur.com/he3uUsy.gif",
        "https://img.fireden.net/a/image/1529/41/1529412117471.gif",
        "https://media0.giphy.com/media/JG4iKdJamPHNK/giphy.gif",
        "https://media.giphy.com/media/PR7J3rrNCrFE4/giphy.gif",
        "https://thumbs.gfycat.com/HelplessAntiqueGonolek-size_restricted.gif",
        "https://data.whicdn.com/images/174338297/original.gif",
        "https://i.pinimg.com/originals/8c/98/e5/8c98e57bd4bb141b80a6dd631070a47e.gif",
        "https://uploads.disquscdn.com/images/81038ea6d7b1739a33b89c17016944b6a59c503331a34d516e6de0dde338d96d.gif",
        "https://data.whicdn.com/images/244172024/original.gif",
        "https://media1.tenor.com/images/63bfef9c1e6bb6713a17d7bf096e0e11/tenor.gif",
        "https://media0.giphy.com/media/7OWdOKaqtEYk5e1Uvj/giphy.gif",
        "https://i.pinimg.com/originals/1a/ba/5b/1aba5b3e40db2339aea920c6af9ffe13.gif",
        "https://media1.giphy.com/media/12fWcohsEln5V6/giphy.gif",
        "https://i.pinimg.com/originals/af/34/c6/af34c69ab0263fad464c0282989db537.gif",
        "http://s3-eu-central-1.amazonaws.com/heeboo-s3/wp-content/uploads/2017/09/20152755/t%C3%A9l%C3%A9chargement-3.gif",
        "https://66.media.tumblr.com/245e1dd0a0522ce16a011878726896e4/tumblr_nalod4huAl1rjsl9ao1_400.gif",
        "https://pa1.narvii.com/7044/b57938100f3de1aba5e097e8511be7c2c997e3d8r1-500-280_hq.gif",
        "https://cdn190.picsart.com/232320412069202.gif",
        "https://i.kym-cdn.com/photos/images/newsfeed/001/216/572/17a.gif",
        "http://media.giphy.com/media/HhTlerURUpnt6/giphy.gif",
        "https://media.tenor.com/images/d93523c4db7e20254c4dcd512029d51e/tenor.gif",
        "http://ekladata.com/L8Gldviq42TaIcys-M6xl1D5XXg.gif",
        "http://mrwgifs.com/wp-content/uploads/2013/05/Ash-Ketcum-Happy-Watery-Eyes-Reaction-Gif-On-Pokemon.gif",
        "https://media.giphy.com/media/amrNGnZUeWhZC/giphy.gif",
        "https://data.whicdn.com/images/329469798/original.gif"
    ]
    choix = [
        "smile1",
        "smile2", 
        "smile3",
        "smile4"
    ]
    emoji = get(client.get_all_emojis(), name=random.choice(choix))
    emoji2 = get(client.get_all_emojis(), name=random.choice(choix))
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    embedF = discord.Embed(title='Smile '+str(emoji2), color=0x2977ff)
    embedF.set_image(url=random.choice(possible_responses))
    embedF.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    messageF = await client.send_message(channel, embed=embedF)
    await client.add_reaction(messageF, emoji)

@client.command(name='hello',aliases=['hi','salut','coucou','hellow'],pass_context=True)
async def hello(ctx):
    possible_responses = [
        "https://image.myanimelist.net/ui/5LYzTBVoS196gvYvw3zjwFOLPQ0H-8MVJxpw6ht0cOA",
        "https://editorani.files.wordpress.com/2018/04/kanbaru-says-hello.gif?w=349",
        "https://image.myanimelist.net/ui/OK6W_koKDTOqqqLDbIoPAhGnoBZpVpPzzvjBBuwwe5g",
        "http://hokagoteatimehtt.weebly.com/uploads/1/0/1/9/10198562/8734154_orig.gif",
        "https://thumbs.gfycat.com/BlushingTartAngelwingmussel-size_restricted.gif",
        "https://image.myanimelist.net/ui/BQM6jEZ-UJLgGUuvrNkYUOpO1cW8D6B9kvhmyEeRa2yaHlS7thwemMakeHK-UhZPpN5Sp9kzAhbWbwmRrEThdg",
        "http://zupimages.net/up/16/03/0h6g.gif",
        "https://image.myanimelist.net/ui/tUy9QTY4RkAguovxW_qL175XQi-ZSYBbNm1nwuKul6sJA_0Z1No6WYjSTseoEwG-",
        "https://38.media.tumblr.com/5745a86960c660e9c7d3881616670a26/tumblr_n19rmxIwYG1tt3pduo1_500.gif",
        "https://redcdn.net/hpimg15/pics/837851bye.gif",
        "https://welcometothebebophome.files.wordpress.com/2019/01/gintoki-greeting.gif",
        "https://uploads.disquscdn.com/images/23b363df434fd2a93bd32c980a33cf334d837a9407992d06701e602edd7afeea.gif",
        "https://i.gifer.com/Q71.gif",
        "https://cdn.instructables.com/FWG/FAPR/IOYDFPVN/FWGFAPRIOYDFPVN.ANIMATED.SQUARE3.gif",
        "https://s-media-cache-ak0.pinimg.com/originals/b6/8e/6e/b68e6ea69d083462c6bfe7421d4ea732.gif",
        "https://steamuserimages-a.akamaihd.net/ugc/83720365537854886/CB7C3241160E761D41AD0315D8F47F1CCAFB9517/",
        "https://uploads.disquscdn.com/images/5d3635f126b05b1f6cd8998496ef065311433a7966edbdb111c561fdea6d8f9e.gif",
        "https://thumbs.gfycat.com/HatefulBlindFunnelweaverspider-size_restricted.gif",
        "https://i.skyrock.net/9955/93339955/pics/3248282026_1_3_Ibd5Xyvv.gif",
        "https://media1.tenor.com/images/8814d5c6ec4265fcc0525112c5814e59/tenor.gif",
        "https://gifimage.net/wp-content/uploads/2018/11/gif-bye-manga-6.gif",
        "http://good-winry-18.g.o.pic.centerblog.net/7b3abf38.gif",
        "https://media1.tenor.com/images/8b00c464465b4ad9ead8db11ccdbdba2/tenor.gif",
        "https://res.cloudinary.com/dsqzssrno/image/upload/v1523657121/tsol5czd7zz21sat2o28.gif",
        "https://pa1.narvii.com/5671/d655dc844f39461dfed4e1164e721e1a4a96012d_hq.gif",
        "https://thumbs.gfycat.com/FamiliarWickedKob-size_restricted.gif",
        "http://31.media.tumblr.com/tumblr_lvg795JjiI1qeweq9.gif",
        "https://img.fireden.net/a/image/1448/35/1448359577742.gif",
        "https://i.redd.it/9sijw39j2n321.gif"
    ]
    choix = [
        "smile1",
        "smile2", 
        "smile3",
        "smile4",
        "blinkheart",
        "mood",
        "enjoy",
        "bigsmile2"
    ]
    emoji = get(client.get_all_emojis(), name=random.choice(choix))
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    embedF = discord.Embed(title='Hello '+str(emoji), color=0x78bafc)
    embedF.set_image(url=random.choice(possible_responses))
    embedF.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    messageF = await client.send_message(channel, embed=embedF)
    await client.add_reaction(messageF, "👋")

@client.command(name='hug',aliases=['calin','câlin','calinou','hugg'],pass_context=True)
async def hug(ctx):
    possible_responses = [
        "https://media1.tenor.com/images/7e30687977c5db417e8424979c0dfa99/tenor.gif",
        "https://cdn.myanimelist.net/s/common/uploaded_files/1461073447-335af6bf0909c799149e1596b7170475.gif",
        "https://media.giphy.com/media/JLovyTOWK4cuc/giphy.gif",
        "https://media.giphy.com/media/143v0Z4767T15e/giphy.gif",
        "https://i.pinimg.com/originals/7b/3d/0a/7b3d0a10ae41cc26d7c2fffd9c7866dc.gif",
        "https://cdn.myanimelist.net/s/common/uploaded_files/1461071296-7451c05f5aae134e2cceb276b085a871.gif",
        "https://66.media.tumblr.com/0d0c8ad924fd2c9678be1d0986ce82a1/tumblr_oswddjkTku1v8tshbo1_400.gif",
        "https://data.whicdn.com/images/57068717/original.gif",
        "https://media1.tenor.com/images/506aa95bbb0a71351bcaa753eaa2a45c/tenor.gif",
        "https://i.kym-cdn.com/photos/images/original/000/935/627/3a5.gif",
        "https://37.media.tumblr.com/f2a878657add13aa09a5e089378ec43d/tumblr_n5uovjOi931tp7433o1_500.gif",
        "https://i.pinimg.com/originals/1a/d9/bd/1ad9bd9cb3113701e3ac039ca0e8cb04.gif",
        "https://66.media.tumblr.com/0b7bd9eba30dca747dde1fbbe9dc58bb/tumblr_pphyz47gep1ujrpx4_500.gif",
        "https://66.media.tumblr.com/16195b94d366cd3c4cb46de35b7c7d6b/tumblr_okuxnlEfV11slt45io3_500.gif",
        "https://66.media.tumblr.com/dfdc4dda019b539975e22c7f819cd2d3/tumblr_inline_p7qy7cCxYD1uz9xg9_540.gif",
        "https://media.tenor.com/images/aab83bd3725feeaccb9929f8ca964db9/tenor.gif",
        "https://thumbs.gfycat.com/GratefulComplexGlassfrog-size_restricted.gif",
        "http://peachy.p.e.pic.centerblog.net/dce0df37.gif",
        "https://uploads.disquscdn.com/images/c01af6913da5add6eea382083d2279510799e6f8fd99d0cfd5840589da345929.gif",
        "https://i.redd.it/m6twh6h7qxx11.gif",
        "https://media1.tenor.com/images/074d69c5afcc89f3f879ca473e003af2/tenor.gif",
        "https://animeforums.net/uploads/monthly_2017_10/b981f31e93532fefe3bc2879d17c475473b75158_hq.gif.0bd4502ab8610ea8382c811fe12c4576.gif",
        "https://i.imgur.com/r9aU2xv.gif",
        "https://cdn.myanimelist.net/s/common/uploaded_files/1461068547-d8d6dc7c2c74e02717c5decac5acd1c7.gif",
        "https://66.media.tumblr.com/18fdf4adcb5ad89f5469a91e860f80ba/tumblr_oltayyHynP1sy5k7wo1_400.gif",
        "https://uploads.disquscdn.com/images/55616436008c4e0ab6b985d64c0e1e90164636f7c51b7ad79f3610f8d12cb4ea.gif",
        "http://31.media.tumblr.com/938d02d040dab86b1b8b75ecc268da17/tumblr_mo9mrqmzVf1soljxao1_500.gif",
        "https://i.pinimg.com/originals/47/db/4d/47db4d25a9ff8b54cce4b5947804b847.gif",
        "https://media.tenor.com/images/7a3822d15e128bd4dbf529d3aea73caa/tenor.gif",
        "https://data.whicdn.com/images/236902451/original.gif",
        "https://cdn.myanimelist.net/s/common/uploaded_files/1460993069-9ac8eaae8cd4149af4510d0fed0796bf.gif",
        "https://media1.tenor.com/images/49a21e182fcdfb3e96cc9d9421f8ee3f/tenor.gif?itemid=3532079",
        "http://i.imgur.com/V2tjYJT.gif",
        "https://66.media.tumblr.com/8f3fe1665a33de3b3c25381b887c50a9/tumblr_ofe7gcwkbB1qehrvso1_540.gif",
        "https://66.media.tumblr.com/21651f48c4ad5fa8ce8aefd5fb346de4/tumblr_inline_p7qy5xMoA21uz9xg9_540.gif",
        "https://i.pinimg.com/originals/67/07/9a/67079aa7557447c45969dc5bb77f7533.gif",
        "http://25.media.tumblr.com/tumblr_m7caa594911ryjk8ao1_500.gif",
        "https://media.tenor.com/images/949b124d5b8cd0955d637dfb45352c7c/tenor.gif"
    ]
    choix = [
        "kiss1",
        "blinkheart",
        "mood",
        "smile2",
        "bigsmile2",
        "lucky"
    ]
    emoji = get(client.get_all_emojis(), name=random.choice(choix))
    emoji2 = get(client.get_all_emojis(), name=random.choice(choix))
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    embedF = discord.Embed(title='Câlin '+str(emoji), color=0x16f8cb)
    embedF.set_image(url=random.choice(possible_responses))
    embedF.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    messageF = await client.send_message(channel, embed=embedF)
    await client.add_reaction(messageF, emoji2)

@client.command(name='bang',aliases=['paw','pan'],pass_context=True)
async def bang(ctx):
    possible_responses = [
        "http://libertyinfinity.com/wp-content/uploads//2013/10/shot-gun.gif",
        "https://i.kym-cdn.com/photos/images/original/000/813/790/8c6.gif",
        "http://31.media.tumblr.com/8a2f58b420c39667cf5d0a0a5b6dbda8/tumblr_naa87wjS2q1r3rdh2o1_500.gif",
        "https://media1.giphy.com/media/zv3wgk0j5Bz2M/giphy.gif",
        "https://i.gifer.com/2IDv.gif",
        "https://cdn.myanimelist.net/s/common/uploaded_files/1458803246-9cf72763d1256c9ba4928f80b17baf88.gif",
        "https://i.kym-cdn.com/photos/images/original/000/978/568/24f.gif",
        "https://i.kym-cdn.com/photos/images/newsfeed/001/073/643/735.gif",
        "http://reve-of-manga.r.e.pic.centerblog.net/996fdb28.gif",
        "https://media0.giphy.com/media/ZgRibURMn7Ywdvzhd7/giphy.gif",
        "https://orig00.deviantart.net/94cc/f/2017/348/0/c/destroysgun_by_doctormoodb-dbwo7mz.gif",
        "https://media0.giphy.com/media/DEjWYYUn9ETny/source.gif",
        "https://data.whicdn.com/images/305309214/original.gif",
        "https://thumbs.gfycat.com/IckyColossalHoneycreeper-small.gif",
        "https://media1.giphy.com/media/9tZZoAy8HFNyo/giphy.gif",
        "https://33.media.tumblr.com/95cbb7c3d8532e9521c63abf26ff1c92/tumblr_nqiidtkgn81tophmdo1_500.gif",
        "https://thumbs.gfycat.com/FlimsyAngryKawala-small.gif",
        "https://media.giphy.com/media/XNx8oEOKGZTMc/giphy.gif",
        "https://66.media.tumblr.com/84f78c9e16d8b4daeb71fded4d7908d0/tumblr_mool0r7F9g1rtgwjbo1_r1_500.gif",
        "http://image.noelshack.com/fichiers/2018/16/2/1523964819-gundoh-musashi-quality.gif",
        "https://66.media.tumblr.com/8d7b7a31942a86070baff2aa4aadc5f0/tumblr_owmoen99M81ui7oe1o1_500.gif",
        "http://i.imgur.com/wDOrOCu.gif",
        "https://static1.fjcdn.com/thumbnails/comments/Anyone+wants+to+join+me+at+the+shooting+range+gun+_7d80693f937ddb899cccee28371b9bc6.gif",
        "https://i.pinimg.com/originals/9e/ff/1a/9eff1ae4d25cde54a78022af6768cf2e.gif",
        "https://i.kym-cdn.com/photos/images/original/000/978/571/9ab.gif",
        "https://jsjammersmith.files.wordpress.com/2018/06/mobile-gundam-2.gif?w=385&h=231",
        "https://66.media.tumblr.com/e097f7f2ba2d4f0338022fb3961d47f6/tumblr_mtjwgygoyo1qkxb1ko2_500.gif",
        "https://i.imgur.com/69myXih.gif",
        "https://thumbs.gfycat.com/HalfUnnaturalAmericanriverotter-size_restricted.gif",
        "https://i.pinimg.com/originals/2a/79/7d/2a797d20f714b6118382dfa21b94ff93.gif",
        "https://i.makeagif.com/media/6-11-2015/qNnqlu.gif",
        "https://i.pinimg.com/originals/40/52/82/40528293958ecc2e9571d9456a67765b.gif",
        "https://memestatic1.fjcdn.com/thumbnails/comments/+_2e88e89e8eecbdd9e7d0485e944cb669.gif",
        "https://cdn.weeb.sh/images/H1Gc74Fob.gif",
        "https://cdn.weeb.sh/images/BkvjZI7PW.gif",
        "https://cdn.weeb.sh/images/BkzSQVFoZ.gif",
        "https://cdn.weeb.sh/images/SkiIVEKsW.gif",
        "https://cdn.weeb.sh/images/HyZiWLmvb.gif",
        "https://cdn.weeb.sh/images/SkFub87DW.gif",
        "https://cdn.weeb.sh/images/BJDJ4VFoZ.gif",
        "https://cdn.weeb.sh/images/S1-RQVFjZ.gif",
        "https://cdn.weeb.sh/images/BJ3CENKiW.gif",
        "https://cdn.weeb.sh/images/rJmPWI7wW.gif",
        "https://cdn.weeb.sh/images/Sy_dXNts-.gif",
        "https://cdn.weeb.sh/images/Sk3v-LmD-.gif",
        "https://cdn.weeb.sh/images/B1bAfGHsW.gif",
        "https://cdn.weeb.sh/images/ryqfNEtj-.gif"
    ]
    choix = [
        "annoy2",
        "bigsmile2",
        "proud",
        "bother",
        "bigrage",
        "annoy1",
        "andry2",
        "andry1"
    ]
    emoji = get(client.get_all_emojis(), name=random.choice(choix))
    emoji2 = get(client.get_all_emojis(), name=random.choice(choix))
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    embedF = discord.Embed(title='Pan '+str(emoji), color=0xea4b24)
    embedF.set_image(url=random.choice(possible_responses))
    embedF.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    messageF = await client.send_message(channel, embed=embedF)
    await client.add_reaction(messageF, emoji2)

@client.command(name='hbd',aliases=['happybirthday','birthday','aniv','anniversaire'],pass_context=True)
async def hbd(ctx, member : discord.Member):
    possible_responses = [
        "https://uploads.disquscdn.com/images/1a3122c106c8e93703bfe6608f6e5e6c413cd79f363855502e5ff3e28ffcef4b.gif",
        "http://pa1.narvii.com/6543/f06d197a1c05f127dcc46994be750c85f8b7236e_hq.gif",
        "https://img.fireden.net/a/image/1485/38/1485385771348.gif",
        "https://img.fireden.net/a/image/1545/66/1545665867867.gif",
        "https://i.imgur.com/drP5fGR.gif",
        "https://uploads.disquscdn.com/images/b8efc59c51ebc661ac48e3831e5859bca539cd0adecd018cc4d9735e8ecabda6.gif",
        "https://i.imgur.com/XVH8fit.gif"
    ]
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    embedF = discord.Embed(title=f'🎉 Joyeux anniversaire {member} !', color=0xaa48a3)
    embedF.set_image(url=random.choice(possible_responses))
    embedF.set_footer(text="De la part de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    messageF = await client.send_message(channel, embed=embedF)

@client.command(aliases=['coloremoji', 'color'], pass_context=True)
async def emojicolor(ctx):
    possible_responses = [
        "Avec moi, le jour devient nuit, le sucre se change en sel, le bleu devient or et la mort l'emporte sur la vie",
        "Un peu de couleur ne fais pas de mal..",
        "Dans le noir, toutes les couleurs s’accordent",
        "Un peu de honte réchauffe et donne de belles couleurs",
        "Les hommes teintent le monde aux couleurs de leurs passions successives",
        "Les gens adorent les couleurs flamboyantes pas ceux qui les portent"
    ]
    possible_color = [
        0xff3636, #red
        0xf546ef, #rose
        0x7b0ac9, #violet
        0x3922fc, #bleu foncé
        0x2977ff, #bleu
        0x07af28, #vert foncé
        0x4df560, #vert
        0xedff4a, #jaune
        0xe47f00  #orange
    ]
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    embedF = discord.Embed(title=random.choice(possible_responses), color=random.choice(possible_color), url='https://htmlcolorcodes.com/fr/selecteur-de-couleur/')
    embedF.set_author(name='Couleurs Emoji')
    embedF.set_image(url='https://media.giphy.com/media/26BoDYDTteuyZCh3y/giphy-downsized-large.gif')
    embedF.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    message = await client.send_message(channel, embed=embedF)
    red = get(client.get_all_emojis(), name='colorred')
    rose = get(client.get_all_emojis(), name='colorpink')
    violet = get(client.get_all_emojis(), name='colorviolet')
    bleuf = get(client.get_all_emojis(), name='colordarkblue')
    bleu = get(client.get_all_emojis(), name='colorblue')
    vertf = get(client.get_all_emojis(), name='colordarkgreen')
    vert = get(client.get_all_emojis(), name='colorgreen')
    jaune = get(client.get_all_emojis(), name='coloryellow')
    orange = get(client.get_all_emojis(), name='colororange')
    await client.add_reaction(message, red)
    await client.add_reaction(message, rose)
    await client.add_reaction(message, violet)
    await client.add_reaction(message, bleuf)
    await client.add_reaction(message, bleu)
    await client.add_reaction(message, vertf)
    await client.add_reaction(message, vert)
    await client.add_reaction(message, jaune)
    await client.add_reaction(message, orange)

@client.command(aliases=['rouletterusse', 'russe','russeroulette'],pass_context=True)
async def roulette(ctx):
    bad = get(client.get_all_emojis(), name="bad")
    bruh1 = get(client.get_all_emojis(), name="bruh1")
    bruh2 = get(client.get_all_emojis(), name="bruh2")
    bother = get(client.get_all_emojis(), name="bother")
    sulk = get(client.get_all_emojis(), name="sulk")
    hiden = get(client.get_all_emojis(), name="hiden")
    possible_responses = [
        "http://66.media.tumblr.com/ea167b683088e3018d79392f3ad43404/tumblr_ngqnj3v0HI1sjwexto3_400.gif",
        "https://media.tenor.com/images/1dfeef23ee4a6b33b035b35b244f1080/tenor.gif",
        "https://i.kym-cdn.com/photos/images/original/001/296/147/2b8.gif"
    ]
    possible_say = [
        "Choisis bien.. "+str(bruh1),
        "Ne faîtes pas ça à la maison "+str(bad),
        "Attention "+str(bruh2),
        "J'ai chargé la roulette ! "+str(sulk),
        "Ne regardez pas.. ça riste d'être sale.. "+str(bother)
    ]
    possible_roulette = [
        "(*clique sur les carrés noir et découvre*)\n__Choisis__ :\n"+str(hiden)+" /  ||:skull_crossbones:||   ||:hole:|| \ \n"+str(hiden)+"| ||:hole:||   o   ||:hole:|| | \n"+str(hiden)+" \  ||:hole:||   ||:hole:|| /",
        "(*clique sur les carrés noir et découvre*)\n__Choisis__ :\n"+str(hiden)+" /  ||:hole:||   ||:skull_crossbones:|| \ \n"+str(hiden)+"| ||:hole:||   o   ||:hole:|| | \n"+str(hiden)+" \  ||:hole:||   ||:hole:|| /",
        "(*clique sur les carrés noir et découvre*)\n__Choisis__ :\n"+str(hiden)+" /  ||:hole:||   ||:hole:|| \ \n"+str(hiden)+"| ||:skull_crossbones:||   o   ||:hole:|| | \n"+str(hiden)+" \  ||:hole:||   ||:hole:|| /",
        "(*clique sur les carrés noir et découvre*)\n__Choisis__ :\n"+str(hiden)+" /  ||:hole:||   ||:hole:|| \ \n"+str(hiden)+"| ||:hole:||   o   ||:skull_crossbones:|| | \n"+str(hiden)+" \  ||:hole:||   ||:hole:|| /",
        "(*clique sur les carrés noir et découvre*)\n__Choisis__ :\n"+str(hiden)+" /  ||:hole:||   ||:hole:|| \ \n"+str(hiden)+"| ||:hole:||   o   ||:hole:|| | \n"+str(hiden)+" \  ||:skull_crossbones:||   ||:hole:|| /",
        "(*clique sur les carrés noir et découvre*)\n__Choisis__ :\n"+str(hiden)+" /  ||:hole:||   ||:hole:|| \ \n"+str(hiden)+"| ||:hole:||   o   ||:hole:|| | \n"+str(hiden)+" \  ||:hole:||   ||:skull_crossbones:|| /"
    ]
    roulette = get(client.get_all_emojis(), name='rouletterusseloaded')
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    embedF = discord.Embed(title=random.choice(possible_say), color=0x881518)
    embedF.set_author(name='Roulette Russe', icon_url='')
    embedF.set_image(url=random.choice(possible_responses))
    embedF.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    message = await client.send_message(channel, embed=embedF)
    roul = await client.send_message(channel, random.choice(possible_roulette))
    await client.add_reaction(roul, roulette)

@client.command(aliases=["playpiano"],pass_context=True)
async def piano(ctx, arg='zero'):
    channel = ctx.message.channel
    randompiano = [
        "https://youtu.be/eQ-eE8Ai_8g",
        "https://youtu.be/3gZC5763wYk"
    ]
    pianoemoji = get(client.get_all_emojis(), name='piano')
    await client.send_typing(channel)
    await asyncio.sleep(1)
    if arg == 'zero':
        message = await client.send_message(channel, str(pianoemoji)+"**Jouer du Piano**, __*PC Uniquement*__ !\n**1.** Cliquez sur le bouton play de la vidéo\n**2.** Puis recliquez 2 fois (asser lentement)\n**3.** Ensuite appuyez sur les touches `1` `2` `3` `4` `5` `6` `7` `8` `9` `0` pour jouer !\n"+str(random.choice(randompiano)))
        await client.add_reaction(message, pianoemoji)
    elif arg == '1':
        message = await client.send_message(channel, str(pianoemoji)+"**Jouer du Piano**, __*PC Uniquement*__ !\n**1.** Cliquez sur le bouton play de la vidéo\n**2.** Puis recliquez 2 fois (asser lentement)\n**3.** Ensuite appuyez sur les touches `1` `2` `3` `4` `5` `6` `7` `8` `9` `0` pour jouer !\nhttps://youtu.be/3gZC5763wYk")
        await client.add_reaction(message, pianoemoji)
    elif arg == '2':
        message = await client.send_message(channel, str(pianoemoji)+"**Jouer du Piano**, __*PC Uniquement*__ !\n**1.** Cliquez sur le bouton play de la vidéo\n**2.** Puis recliquez 2 fois (asser lentement)\n**3.** Ensuite appuyez sur les touches `1` `2` `3` `4` `5` `6` `7` `8` `9` `0` pour jouer !\nhttps://youtu.be/eQ-eE8Ai_8g")
        await client.add_reaction(message, pianoemoji)
    else:
        embed = discord.Embed(title="essayez : ars piano {1 ou 2}", color=0xf85a5f)
        embed.set_author(name='Erreur')
        embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
        embed.set_footer(text="Mauvais piano...")
        reponseText = await client.send_message(channel, embed=embed)
        await client.add_reaction(reponseText, "✖")

@client.command(aliases=['randomemoji', 'emoji'], pass_context=True)
async def emojirandom(ctx):
    choix = [
        "wondering",
        "weep",
        "vicious",
        "unsatisfied",
        "uncertain",
        "tongue1",
        "sulk",
        "stunned",
        "startled",
        "smilecorner",
        "smile4",
        "smile3",
        "smile2",
        "smile1",
        "sleep",
        "shy",
        "shock",
        "relieved1",
        "rage1",
        "proud",
        "neutral",
        "musickiss",
        "mournful",
        "mood",
        "minimouth",
        "depressed",
        "disappointed1",
        "disgusting",
        "enjoy",
        "expressionless1",
        "frustrate",
        "frustrated",
        "happy",
        "kiss1",
        "lucky",
        "deadly",
        "dead",
        "confused1",
        "bruh2",
        "bruh1",
        "bother",
        "blurp",
        "blinkheart",
        "blink",
        "bigsmile2",
        "bigsmile1",
        "bigrage",
        "badmood",
        "bad",
        "annoy2",
        "annoy1",
        "andry2",
        "andry1",
        "agape",
        "afflicted" 
    ]
    emoji = get(client.get_all_emojis(), name=random.choice(choix))
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    message = await client.send_message(channel, str(emoji))

@client.command(aliases=['emojis', 'allemojis', 'emojilist', 'listemoji', 'emojislist', 'listemojis'], pass_context=True)
async def allemoji(ctx):
    possible_responses = [
        "https://s5.eestatic.com/2018/09/21/social/La_Jungla_339728034_98112627_1706x1280.jpg",
        "https://s1.eestatic.com/2018/09/21/social/La_Jungla_339728043_98112331_1706x1280.jpg",
        "https://s2.eestatic.com/2018/09/21/social/La_Jungla_339728035_98112107_1706x1280.jpg",
        "https://s5.eestatic.com/2018/09/21/social/La_Jungla_339728036_98112135_1706x1280.jpg",
        "https://s6.eestatic.com/2018/09/21/social/La_Jungla_339728037_98112163_1706x1280.jpg",
        "https://s4.eestatic.com/2018/09/21/social/La_Jungla_339728053_98112611_1706x1280.jpg",
        "https://s1.eestatic.com/2018/09/21/social/La_Jungla_339728039_98112219_1706x1280.jpg",
        "https://s5.eestatic.com/2018/09/21/social/La_Jungla_339728040_98112247_1706x1280.jpg",
        "https://s1.eestatic.com/2018/09/21/social/La_Jungla_339728041_98112275_1706x1280.jpg",
        "https://s5.eestatic.com/2018/09/21/social/La_Jungla_339728042_98112291_1706x1280.jpg",
        "https://s5.eestatic.com/2018/09/21/social/La_Jungla_339728048_98112471_1706x1280.jpg",
        "https://s5.eestatic.com/2018/09/21/social/La_Jungla_339728044_98112359_1706x1280.jpg",
        "https://s2.eestatic.com/2018/09/21/social/La_Jungla_339728045_98112387_1706x1280.jpg",
        "https://s4.eestatic.com/2018/09/21/social/La_Jungla_339728046_98112415_1706x1280.jpg",
        "https://s6.eestatic.com/2018/09/21/social/La_Jungla_339728050_98112527_1706x1280.jpg",
        "https://s3.eestatic.com/2018/09/21/social/La_Jungla_339728047_98112443_1706x1280.jpg",
        "https://s4.eestatic.com/2018/09/21/social/La_Jungla_339728049_98112499_1706x1280.jpg",
        "https://s5.eestatic.com/2018/09/21/social/La_Jungla_339728051_98112555_1706x1280.jpg",
        "https://s6.eestatic.com/2018/09/21/social/La_Jungla_339728052_98112583_1706x1280.jpg",
        "https://s4.eestatic.com/2018/09/21/social/La_Jungla_339728073_98113174_1706x1280.jpg"
    ]
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    embedF = discord.Embed(title="Je t'ai envoyer la liste en PV",colour = 0xfaf783)
    embedF.set_author(name="Liste Emoji")
    embedF.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    embedF.set_image(url=random.choice(possible_responses))
    messageF = await client.send_message(channel, embed=embedF)

    wondering = get(client.get_all_emojis(), name="wondering")
    weep = get(client.get_all_emojis(), name="weep")
    vicious = get(client.get_all_emojis(), name="vicious")
    unsatisfied = get(client.get_all_emojis(), name="unsatisfied")
    uncertain = get(client.get_all_emojis(), name="uncertain")
    tongue = get(client.get_all_emojis(), name="tongue1")
    sulk = get(client.get_all_emojis(), name="sulk")
    stunned = get(client.get_all_emojis(), name="stunned")
    startled = get(client.get_all_emojis(), name="startled")
    smilecorner = get(client.get_all_emojis(), name="smilecorner")
    smile4 = get(client.get_all_emojis(), name="smile4")
    smile3 = get(client.get_all_emojis(), name="smile3")
    smile2 = get(client.get_all_emojis(), name="smile2")
    smile1 = get(client.get_all_emojis(), name="smile1")
    sleep = get(client.get_all_emojis(), name="sleep")
    shy = get(client.get_all_emojis(), name="shy")
    shock = get(client.get_all_emojis(), name="shock")
    relieved = get(client.get_all_emojis(), name="relieved1")
    rage = get(client.get_all_emojis(), name="rage1")
    proud = get(client.get_all_emojis(), name="proud")
    neutral = get(client.get_all_emojis(), name="neutral")
    musickiss = get(client.get_all_emojis(), name="musickiss")
    mournful = get(client.get_all_emojis(), name="mournful")
    mood = get(client.get_all_emojis(), name="mood")
    minimounth = get(client.get_all_emojis(), name="minimouth")
    depressed = get(client.get_all_emojis(), name="depressed")
    disappointed = get(client.get_all_emojis(), name="disappointed1")
    disgusting = get(client.get_all_emojis(), name="disgusting")
    enjoy = get(client.get_all_emojis(), name="enjoy")
    expressionless = get(client.get_all_emojis(), name="expressionless1")
    frustrate = get(client.get_all_emojis(), name="frustrate")
    frustrated = get(client.get_all_emojis(), name="frustrated")
    happy = get(client.get_all_emojis(), name="happy")
    kiss = get(client.get_all_emojis(), name="kiss1")
    lucky = get(client.get_all_emojis(), name="lucky")
    deadly = get(client.get_all_emojis(), name="deadly")
    dead = get(client.get_all_emojis(), name="dead")
    confused = get(client.get_all_emojis(), name="confused1")
    bruh2 = get(client.get_all_emojis(), name="bruh2")
    bruh1 = get(client.get_all_emojis(), name="bruh1")
    bother = get(client.get_all_emojis(), name="bother")
    blurp = get(client.get_all_emojis(), name="blurp")
    blinkheart = get(client.get_all_emojis(), name="blinkheart")
    blink = get(client.get_all_emojis(), name="blink")
    bigsmile2 = get(client.get_all_emojis(), name="bigsmile2")
    bigsmile1 = get(client.get_all_emojis(), name="bigsmile1")
    bigrage = get(client.get_all_emojis(), name="bigrage")
    badmood = get(client.get_all_emojis(), name="badmood")
    bad = get(client.get_all_emojis(), name="bad")
    annoy2 = get(client.get_all_emojis(), name="annoy2")
    annoy1 = get(client.get_all_emojis(), name="annoy1")
    andry2 = get(client.get_all_emojis(), name="andry2")
    andry1 = get(client.get_all_emojis(), name="andry1")
    agape = get(client.get_all_emojis(), name="agape")
    afflicted = get(client.get_all_emojis(), name="afflicted")
    author = ctx.message.author
    message = await client.send_message(author, "**__Liste des Emoji d'Arès__ :** (55)\n\n"+str(wondering)+"\t\t"+str(weep)+"\t\t"+str(vicious)+"\n\t\t"+str(unsatisfied)+"\t\t"+str(uncertain)+"\n"+str(tongue)+"\t\t"+str(sulk)+"\t\t"+str(stunned)+"\n\t\t"+str(startled)+"\t\t"+str(smilecorner)+"\n"+str(smile4)+"\t\t"+str(smile3)+"\t\t"+str(smile2)+"\n\t\t"+str(smile1)+"\t\t"+str(sleep)+"\n"+str(shy)+"\t\t"+str(shock)+"\t\t"+str(relieved)+"\n\t\t"+str(rage)+"\t\t"+str(proud)+"\n"+str(neutral)+"\t\t"+str(musickiss)+"\t\t"+str(mournful)+"\n\t\t"+str(mood)+"\t\t"+str(minimounth)+"\n"+str(depressed)+"\t\t"+str(disappointed)+"\t\t"+str(disgusting)+"\n\t\t"+str(enjoy)+"\t\t"+str(expressionless)+"\n"+str(frustrate)+"\t\t"+str(frustrated)+"\t\t"+str(happy)+"\n\t\t"+str(kiss)+"\t\t"+str(lucky)+"\n"+str(deadly)+"\t\t"+str(dead)+"\t\t"+str(confused)+"\n\t\t"+str(bruh2)+"\t\t"+str(bruh1)+"\n"+str(bother)+"\t\t"+str(blurp)+"\t\t"+str(blinkheart)+"\n\t\t"+str(blink)+"\t\t"+str(bigsmile2)+"\n"+str(bigsmile1)+"\t\t"+str(bigrage)+"\t\t"+str(badmood)+"\n\t\t"+str(bad)+"\t\t"+str(annoy2)+"\n"+str(annoy1)+"\t\t"+str(andry2)+"\t\t"+str(andry1)+"\n\t\t"+str(agape)+"\t\t"+str(afflicted))

@client.command(pass_context=True)
async def invite(ctx):
    possible_responses = [
        "Va check tes DM :smirk:",
        "Je viens de glisser un petit quelque chose en PV :smirk:",
        "Voyon voir, tu as une notif, nan ? :thinking:",
        "C'est envoyé ! :thumbsup:",
        "Je suis invité à la soirée ?"
    ]
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    embedF = discord.Embed(title='Invitation',colour = 0x6f7dff)
    embedF.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    embedF.set_image(url='http://discord-france.fr/wp-content/uploads/2018/07/longart.png')
    embedF.add_field(name="Je t'ai envoyer l'invitation", value=random.choice(possible_responses), inline=False)
    messageF = await client.send_message(channel, embed=embedF)

    author = ctx.message.author
    embed = discord.Embed(title='Clique ICI pour ajouter Ares à ton serveur !',colour = 0x6f7dff, url='https://discordapp.com/oauth2/authorize?client_id=590675426616279051&scope=bot&permissions=2146958847')
    embed.set_author(name='Ares',icon_url='https://www.mpadeco.com/thumb.php?zc=3&f=0&src=/sites/mpadeco/files/products/d9771.png&fl=none&w=360&h=360')
    embed.set_image(url='http://discord-france.fr/wp-content/uploads/2018/07/longart.png')

    embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    message = await client.send_message(author, embed=embed)

@client.command(aliases=['userinfo', 'user', 'info', 'infos'], pass_context=True)
async def userinfos(ctx, member : discord.Member):
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    roles = [role for role in member.roles]

    embed = discord.Embed(color=member.color)
    embed.set_author(name=f"Infos utilisateur : {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Pseudo :", value=member.display_name)
    embed.add_field(name="Identifiant :", value=member.id)
    embed.add_field(name="Créer à :", value=member.created_at.strftime("%H:%M:%S le %d/%m/20%y"))
    embed.add_field(name="À rejoint le :", value=member.joined_at.strftime("%H:%M:%S le %d/%m/20%y"))
    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Rôle le plus haut :", value=member.top_role.mention)
    if member.bot == False:
        isbot = 'Non'
    else:
        isbot = 'Oui'
    embed.add_field(name="Est-ce un Robot ?", value=isbot)
    embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)

    await client.send_message(channel, embed=embed)

@client.command(aliases=['picture', 'profil', 'photoprofil'], pass_context=True)
async def pp(ctx, member : discord.Member):
    channel = ctx.message.channel
    await client.send_typing(ctx.message.channel)
    await asyncio.sleep(1)

    embed = discord.Embed(color=member.color)
    embed.set_author(name=f"Photo de profil de : {member}")
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    await client.send_message(channel, embed=embed)

@client.command(aliases=['serveuricon', 'servicon', 'iconeserveur'], pass_context=True)
async def iconserv(ctx):
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    embed = discord.Embed(title="Icône du serveur", color=0x399587)
    embed.set_image(url=ctx.message.server.icon_url)
    embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    resultText = await client.send_message(channel, embed=embed)

@client.command(aliases=['delete','tm','suprime','messagetimer'], pass_context=True)
async def timermessage(ctx, timer : int):
    channel = ctx.message.channel
    if timer != None:
        try:
            await client.send_typing(channel)
            await asyncio.sleep(timer)
            await client.delete_message(ctx.message)
        except:
            embed = discord.Embed(title="essayez : ars timermessage {TEMPS} {MESSAGE}", color=0xf85a5f)
            embed.set_author(name='Erreur')
            embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
            embed.set_footer(text="Il manque quelque chose..")
            reponseText = await client.send_message(channel, embed=embed)
            await client.add_reaction(reponseText, "✖")
    else:
        embed = discord.Embed(title="essayez : ars timermessage {TEMPS} {MESSAGE}", color=0xf85a5f)
        embed.set_author(name='Erreur')
        embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
        embed.set_footer(text="Il manque quelque chose..")
        reponseText = await client.send_message(channel, embed=embed)
        await client.add_reaction(reponseText, "✖")

@client.command(aliases=['mc'],pass_context=True)
async def minecraft(ctx, arg='zero'):
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    if arg != 'zero':
        try:
            minecraft_server = MinecraftServer.lookup(str(arg))
            status = minecraft_server.status()
            embed = discord.Embed(title="Info serveur Minecraft : "+str(arg), colour=0x16c512)
            embed.set_thumbnail(url='https://cdn.freebiesupply.com/logos/large/2x/minecraft-1-logo-png-transparent.png')
            embed.add_field(name="Nombre de joueurs en ligne :",value="```python\n"+str(status.players.online)+"/"+str(status.players.max)+" joueurs"+"```",inline=False)
            embed.add_field(name="Version :",value="```python\n"+str(status.version.name)+"```")
            embed.add_field(name="Latence du serveur :",value="```python\n"+str(status.latency)+"ms"+"```",inline=False)
            embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
            resultText = await client.send_message(channel, embed=embed)
        except:
            embed = discord.Embed(title="essayez : ars minecraft {ADRESSE_IP}", color=0xf85a5f)
            embed.set_author(name='Erreur')
            embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
            embed.set_footer(text="Mauvaise adresse IP !")
            reponseText = await client.send_message(channel, embed=embed)
            await client.add_reaction(reponseText, "✖")
    else:
        embed = discord.Embed(title="essayez : ars minecraft {ADRESSE_IP}", color=0xf85a5f)
        embed.set_author(name='Erreur')
        embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
        embed.set_footer(text="Il manque quelque chose..")
        reponseText = await client.send_message(channel, embed=embed)
        await client.add_reaction(reponseText, "✖")


###HELP
@client.command(aliases=['?', 'aide'], pass_context=True)
async def help(ctx):
    possible_responses = [
        "Va check tes DM :smirk:",
        "Je viens de glisser un petit quelque chose en PV :smirk:",
        "Voyon voir, tu as une notif, nan ? :thinking:",
        "Liste complette des commandes envoyé chef ! :thumbsup:"
    ]
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    embedF = discord.Embed(title='Aide', color=0x36393f)
    embedF.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    embedF.set_thumbnail(url='https://cdn.pixabay.com/photo/2016/06/15/15/02/info-1459077_960_720.png')
    embedF.add_field(name="Je t'ai envoyer un message", value=random.choice(possible_responses), inline=False)
    messageF = await client.send_message(channel, embed=embedF)
    await client.add_reaction(messageF, "🚩")

    author = ctx.message.author
    embed = discord.Embed(title='Liste des commandes',colour = discord.Colour.red(), url='https://wariormachinebattl.wixsite.com/wart')
    embed.set_author(name='ARS est le prefix pour utiliser les commandes',icon_url='https://www.mpadeco.com/thumb.php?zc=3&f=0&src=/sites/mpadeco/files/products/d9771.png&fl=none&w=360&h=360')
    embed.set_thumbnail(url='https://cdn.pixabay.com/photo/2016/06/15/15/02/info-1459077_960_720.png')
    embed.add_field(name='Utile (**7**)', value="`botinfo` `help` `minecraft` `iconserv` `ping` `pp` `user`", inline=False)
    embed.add_field(name='Calcul (**13**)', value="`acos` `asin` `atan` `carre` `celtofar` `cos` `cube` `fartocel` `fois` `moins` `plus` `sin` `tan`", inline=False)
    embed.add_field(name='Fun & Images (**19**)', value="`baffe` `bang` `bitcoin` `chat` `chien` `color` `dab` `echo` `emojis` `hbd` `hello` `hug` `kiss` `poing` `randomemoji` `smile` `suicide` `timermessage` `triggered`", inline=False)
    embed.add_field(name='Jeux (**2**)', value="`piano` `roulette`", inline=False)
    embed.add_field(name='Musique (**2**)', value="`join` `leave` *En développement..*", inline=False)
    embed.add_field(name='NSFW (**15**)', value="ars x [CATEGORIE]\n`anal` `bdsm` `boobs` `biffle` `ciseaux` `dick` `facial` `fist` `gay` `hentai` `nude` `poils` `pussy` `squirt` `69`", inline=False)
    embed.add_field(name='Inviter Arès sur ton serveur', value="`invite`", inline=False)
    embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    message = await client.send_message(author, embed=embed)

###MUSIQUE
@client.command(pass_context=True)
async def join(ctx):
    channel1 = ctx.message.channel
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    embed = discord.Embed(title="Je rejoins le salon : "+str(channel), color=discord.Colour.dark_green())
    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/e/e0/Music_player_logo.png')
    embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')))
    resultText = await client.send_message(channel1, embed=embed)
    await client.add_reaction(resultText, "▶")

@client.command(pass_context=True)
async def leave(ctx):
    channel1 = ctx.message.channel
    server = ctx.message.server
    channel = ctx.message.author.voice.voice_channel
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()
    embed = discord.Embed(title="Je quitte le salon : "+str(channel), color=discord.Colour.dark_red())
    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/e/e0/Music_player_logo.png')
    embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')))
    resultText = await client.send_message(channel1, embed=embed)
    await client.add_reaction(resultText, "◀")

#CALCULS
@client.command(pass_context=True)
async def pi(ctx):
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    squared_value = math.pi
    embed = discord.Embed(title="Math calcul : pi")
    embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/550/PNG/512/business-color_calculator_icon-icons.com_53466.png')
    embed.add_field(name="Valeur",value="```python\n"+str(squared_value)+"```")
    embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
    resultText = await client.send_message(channel, embed=embed)
    await client.add_reaction(resultText, "✔")

@client.command(pass_context=True)
async def cube(ctx, number = -6537634684):
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    if number != -6537634684:
        squared_value = int(number) * int(number) * int(number)
        embed = discord.Embed(title="Math calcul : fonction cube")
        embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/550/PNG/512/business-color_calculator_icon-icons.com_53466.png')
        embed.add_field(name="Entré",value="```python\n"+str(number)+"**3"+"```")
        embed.add_field(name="Sortie",value="```python\n"+str(squared_value)+"```")
        embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
        resultText = await client.send_message(channel, embed=embed)
        await client.add_reaction(resultText, "✔")
    else:
        embed = discord.Embed(title="essayez : ars cube {NOMBRE}", color=0xf85a5f)
        embed.set_author(name='Erreur')
        embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
        embed.set_footer(text="Il manque quelque chose..")
        reponseText = await client.send_message(channel, embed=embed)
        await client.add_reaction(reponseText, "✖")

@client.command(aliases=['²', '**'],pass_context=True)
async def carre(ctx, number = -6537634684):
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    if number != -6537634684:
        squared_value = int(number) * int(number)
        embed = discord.Embed(title="Math calcul : fonction carré")
        embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/550/PNG/512/business-color_calculator_icon-icons.com_53466.png')
        embed.add_field(name="Entré",value="```python\n"+str(number)+"**2"+"```")
        embed.add_field(name="Sortie",value="```python\n"+str(squared_value)+"```")
        embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
        resultText = await client.send_message(channel, embed=embed)
        await client.add_reaction(resultText, "✔")
    else:
        embed = discord.Embed(title="essayez : ars carre {NOMBRE}", color=0xf85a5f)
        embed.set_author(name='Erreur')
        embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
        embed.set_footer(text="Il manque quelque chose..")
        reponseText = await client.send_message(channel, embed=embed)
        await client.add_reaction(reponseText, "✖")

@client.command(aliases=['par', '*'], pass_context=True)
async def fois(ctx, number1 = -6537634684, number2 = -6537634684):
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    if number1 != -6537634684 and number2 != -6537634684:
        squared_value = int(number1) * int(number2)
        embed = discord.Embed(title="Math calcul : multiplication")
        embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/550/PNG/512/business-color_calculator_icon-icons.com_53466.png')
        embed.add_field(name="Entré",value="```python\n"+str(number1)+"*"+str(number2)+"```")
        embed.add_field(name="Sortie",value="```python\n"+str(squared_value)+"```")
        embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
        resultText = await client.send_message(channel, embed=embed)
        await client.add_reaction(resultText, "✔")
    else:
        embed = discord.Embed(title="essayez : ars fois {NOMBRE} {NOMBRE}", color=0xf85a5f)
        embed.set_author(name='Erreur')
        embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
        embed.set_footer(text="Il manque quelque chose..")
        reponseText = await client.send_message(channel, embed=embed)
        await client.add_reaction(reponseText, "✖")

@client.command(aliases=['+'], pass_context=True)
async def plus(ctx, number1 = -6537634684, number2 = -6537634684):
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    if number1 != -6537634684 and number2 != -6537634684:
        squared_value = int(number1) + int(number2)
        embed = discord.Embed(title="Math calcul : addition")
        embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/550/PNG/512/business-color_calculator_icon-icons.com_53466.png')
        embed.add_field(name="Entré",value="```python\n"+str(number1)+"+"+str(number2)+"```")
        embed.add_field(name="Sortie",value="```python\n"+str(squared_value)+"```")
        embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
        resultText = await client.send_message(channel, embed=embed)
        await client.add_reaction(resultText, "✔")
    else:
        embed = discord.Embed(title="essayez : ars plus {NOMBRE} {NOMBRE}", color=0xf85a5f)
        embed.set_author(name='Erreur')
        embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
        embed.set_footer(text="Il manque quelque chose..")
        reponseText = await client.send_message(channel, embed=embed)
        await client.add_reaction(reponseText, "✖")

@client.command(aliases=['-'], pass_context=True)
async def moins(ctx, number1 = -6537634684, number2 = -6537634684):
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    if number1 != -6537634684 and number2 != -6537634684:
        squared_value = int(number1) - int(number2)
        embed = discord.Embed(title="Math calcul : soustraction")
        embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/550/PNG/512/business-color_calculator_icon-icons.com_53466.png')
        embed.add_field(name="Entré",value="```python\n"+str(number1)+"-"+str(number2)+"```")
        embed.add_field(name="Sortie",value="```python\n"+str(squared_value)+"```")
        embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
        resultText = await client.send_message(channel, embed=embed)
        await client.add_reaction(resultText, "✔")
    else:
        embed = discord.Embed(title="essayez : ars moins {NOMBRE} {NOMBRE}", color=0xf85a5f)
        embed.set_author(name='Erreur')
        embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
        embed.set_footer(text="Il manque quelque chose..")
        reponseText = await client.send_message(channel, embed=embed)
        await client.add_reaction(reponseText, "✖")

@client.command(aliases=['cosinus'], pass_context=True)
async def cos(ctx, number = -6537634684):
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    if number != -6537634684:
        squared_value = math.cos(number)
        embed = discord.Embed(title="Math calcul : sinus")
        embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/550/PNG/512/business-color_calculator_icon-icons.com_53466.png')
        embed.add_field(name="Entré",value="```python\n"+"math.cos("+str(number)+")"+"```")
        embed.add_field(name="Sortie",value="```python\n"+str(squared_value)+"```")
        embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
        resultText = await client.send_message(channel, embed=embed)
        await client.add_reaction(resultText, "✔")
    else:
        embed = discord.Embed(title="essayez : ars sin {NOMBRE} {NOMBRE}", color=0xf85a5f)
        embed.set_author(name='Erreur')
        embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
        embed.set_footer(text="Il manque quelque chose..")
        reponseText = await client.send_message(channel, embed=embed)
        await client.add_reaction(reponseText, "✖")

@client.command(aliases=['sinus'], pass_context=True)
async def sin(ctx, number = -6537634684):
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    if number != -6537634684:
        squared_value = math.sin(number)
        embed = discord.Embed(title="Math calcul : sinus")
        embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/550/PNG/512/business-color_calculator_icon-icons.com_53466.png')
        embed.add_field(name="Entré",value="```python\n"+"math.sin("+str(number)+")"+"```")
        embed.add_field(name="Sortie",value="```python\n"+str(squared_value)+"```")
        embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
        resultText = await client.send_message(channel, embed=embed)
        await client.add_reaction(resultText, "✔")
    else:
        embed = discord.Embed(title="essayez : ars sin {NOMBRE} {NOMBRE}", color=0xf85a5f)
        embed.set_author(name='Erreur')
        embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
        embed.set_footer(text="Il manque quelque chose..")
        reponseText = await client.send_message(channel, embed=embed)
        await client.add_reaction(reponseText, "✖")

@client.command(aliases=['tangente'], pass_context=True)
async def tan(ctx, number = -6537634684):
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    if number != -6537634684:
        squared_value = math.tan(number)
        embed = discord.Embed(title="Math calcul : sinus")
        embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/550/PNG/512/business-color_calculator_icon-icons.com_53466.png')
        embed.add_field(name="Entré",value="```python\n"+"math.tan("+str(number)+")"+"```")
        embed.add_field(name="Sortie",value="```python\n"+str(squared_value)+"```")
        embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
        resultText = await client.send_message(channel, embed=embed)
        await client.add_reaction(resultText, "✔")
    else:
        embed = discord.Embed(title="essayez : ars sin {NOMBRE} {NOMBRE}", color=0xf85a5f)
        embed.set_author(name='Erreur')
        embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
        embed.set_footer(text="Il manque quelque chose..")
        reponseText = await client.send_message(channel, embed=embed)
        await client.add_reaction(reponseText, "✖")

@client.command(aliases=['arccosinus','acos'], pass_context=True)
async def arccos(ctx, number = -6537634684):
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    if number != -6537634684:
        squared_value = math.acos(number)
        embed = discord.Embed(title="Math calcul : sinus")
        embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/550/PNG/512/business-color_calculator_icon-icons.com_53466.png')
        embed.add_field(name="Entré",value="```python\n"+"math.acos("+str(number)+")"+"```")
        embed.add_field(name="Sortie",value="```python\n"+str(squared_value)+"```")
        embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
        resultText = await client.send_message(channel, embed=embed)
        await client.add_reaction(resultText, "✔")
    else:
        embed = discord.Embed(title="essayez : ars sin {NOMBRE} {NOMBRE}", color=0xf85a5f)
        embed.set_author(name='Erreur')
        embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
        embed.set_footer(text="Il manque quelque chose..")
        reponseText = await client.send_message(channel, embed=embed)
        await client.add_reaction(reponseText, "✖")

@client.command(aliases=['arcsinus','asin'], pass_context=True)
async def arcsin(ctx, number = -6537634684):
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    if number != -6537634684:
        squared_value = math.asin(number)
        embed = discord.Embed(title="Math calcul : sinus")
        embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/550/PNG/512/business-color_calculator_icon-icons.com_53466.png')
        embed.add_field(name="Entré",value="```python\n"+"math.asin("+str(number)+")"+"```")
        embed.add_field(name="Sortie",value="```python\n"+str(squared_value)+"```")
        embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
        resultText = await client.send_message(channel, embed=embed)
        await client.add_reaction(resultText, "✔")
    else:
        embed = discord.Embed(title="essayez : ars sin {NOMBRE} {NOMBRE}", color=0xf85a5f)
        embed.set_author(name='Erreur')
        embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
        embed.set_footer(text="Il manque quelque chose..")
        reponseText = await client.send_message(channel, embed=embed)
        await client.add_reaction(reponseText, "✖")

@client.command(aliases=['arctangente','atan'], pass_context=True)
async def arctan(ctx, number = -6537634684):
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    if number != -6537634684:
        squared_value = math.atan(number)
        embed = discord.Embed(title="Math calcul : sinus")
        embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/550/PNG/512/business-color_calculator_icon-icons.com_53466.png')
        embed.add_field(name="Entré",value="```python\n"+"math.atan("+str(number)+")"+"```")
        embed.add_field(name="Sortie",value="```python\n"+str(squared_value)+"```")
        embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
        resultText = await client.send_message(channel, embed=embed)
        await client.add_reaction(resultText, "✔")
    else:
        embed = discord.Embed(title="essayez : ars sin {NOMBRE} {NOMBRE}", color=0xf85a5f)
        embed.set_author(name='Erreur')
        embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
        embed.set_footer(text="Il manque quelque chose..")
        reponseText = await client.send_message(channel, embed=embed)
        await client.add_reaction(reponseText, "✖")

@client.command(aliases=['celciustofanhrenheit','celtofan'],pass_context=True)
async def celtofar(ctx, number = -6537634684):
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    if number != -6537634684:
        squared_value = (number*9/5)+32
        embed = discord.Embed(title="Math calcul : Celsius en Fanhrenheit")
        embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/550/PNG/512/business-color_calculator_icon-icons.com_53466.png')
        embed.add_field(name="Entré",value="```python\n"+"("+str(number)+"-32)*5/9"+"```")
        embed.add_field(name="Sortie",value="```python\n"+str(squared_value)+"°F"+"```")
        embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
        resultText = await client.send_message(channel, embed=embed)
        await client.add_reaction(resultText, "✔")
    else:
        embed = discord.Embed(title="essayez : ars cube {NOMBRE}", color=0xf85a5f)
        embed.set_author(name='Erreur')
        embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
        embed.set_footer(text="Il manque quelque chose..")
        reponseText = await client.send_message(channel, embed=embed)
        await client.add_reaction(reponseText, "✖")

@client.command(aliases=['fanhrenheittocelcius','fantocel'],pass_context=True)
async def fartocel(ctx, number = -6537634684):
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    if number != -6537634684:
        squared_value = (number-32)*(5/9)
        embed = discord.Embed(title="Math calcul : Fanhrenheit en Celsius")
        embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/550/PNG/512/business-color_calculator_icon-icons.com_53466.png')
        embed.add_field(name="Entré",value="```python\n"+"("+str(number)+"-32)*5/9"+"```")
        embed.add_field(name="Sortie",value="```python\n"+str(squared_value)+"°C"+"```")
        embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
        resultText = await client.send_message(channel, embed=embed)
        await client.add_reaction(resultText, "✔")
    else:
        embed = discord.Embed(title="essayez : ars cube {NOMBRE}", color=0xf85a5f)
        embed.set_author(name='Erreur')
        embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
        embed.set_footer(text="Il manque quelque chose..")
        reponseText = await client.send_message(channel, embed=embed)
        await client.add_reaction(reponseText, "✖")

@client.command(pass_context=True)
async def bitcoin(ctx):
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        embed = discord.Embed(title="Prix d'un bitcoin", color=discord.Colour.dark_gold())
        embed.set_thumbnail(url='http://pngimg.com/uploads/bitcoin/bitcoin_PNG48.png')
        embed.add_field(name="Un bitcoin se vend",value=str(response['bpi']['USD']['rate'])+"$")
        embed.set_footer(text="Requête de : "+str(ctx.message.author)+" à "+str(time.strftime('%H:%M:%S')), icon_url=ctx.message.author.avatar_url)
        reponseText = await client.send_message(channel, embed=embed)
        await client.add_reaction(reponseText, "💰")

@client.command(pass_context=True)
async def test(ctx):
    channel = ctx.message.channel
    await client.send_typing(channel)
    await asyncio.sleep(1)
    embed = discord.Embed(title="ars {COMMAND} {VALEUR}", color=0xf85a5f)
    embed.set_author(name='Erreur')
    embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
    embed.set_footer(text="Il manque quelque chose..")
    reponseText = await client.send_message(channel, embed=embed)
    await client.add_reaction(reponseText, "✖")

@client.command(aliases=['say'])
async def echo(*args):
    output= ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

### NSFW COMMANDS
@client.command(name='xxx', aliases=['porn', 'sex', 'x', 'nsfw'], pass_context=True)
async def xxx(ctx, arg='zero'):
    getchannel = ctx.message.channel
    channelnsfwWarT = client.get_channel("475016603176534026")
    channelnsfwGMOD = client.get_channel("594888657547034634")
    channelnsfwDeep = client.get_channel("585786244966121513")
    channelnsfwMCGE = client.get_channel("584726450750619649")
    channelnsfwtest = client.get_channel("595057140922581003")
    channelnsfwAria = client.get_channel("599563416524423178")
    channelnfswLove = client.get_channel("599883583074730001")
    if getchannel == channelnsfwWarT or getchannel == channelnsfwGMOD or getchannel == channelnsfwDeep or getchannel == channelnfswLove or getchannel == channelnsfwMCGE or getchannel == channelnsfwtest or getchannel == channelnsfwAria:
        if arg == 'help' or arg == 'categorie' or arg == '?' or arg == 'aide':
            embed = discord.Embed(title="NSFW • Liste des commandes", color=0xed9ce7)
            embed.add_field(name='Utilisation :', value="ars porn `[CATEGORIE]`   **ou**\nars nsfw `[CATEGORIE]`   **ou**\nars sex `[CATEGORIE]`   **ou**\nars xxx `[CATEGORIE]`   **ou**\nars x `[CATEGORIE]`", inline=False)
            embed.add_field(name='Liste des catégories : (15)', value="(en *italique* son les categories alias)\n`anal` *ass* *sodomie*\n`biffle` *biflette*\n`bdsm` *bondage*\n`boobs` *seins*\n`ciseaux` *scissors* *scissor* *ciseau*\n`dick` *bite* *teub*\n`facial` *cumshot*\n`fist` *poing*\n`gay`\n`hentai` *anime*\n`nude` *snap* *snapchat*\n`poils` *poil* *fur* *hairiness* *pilosity*\n`pussy` *vagin* *vagina* *minou* *chatte*\n`squirt`\n`69`", inline=False)
            embed.set_footer(text="NSFW")
            reponseText = await client.send_message(getchannel, embed=embed)
        elif arg == 'zero':
            embed = discord.Embed(title="Il manque quelque chose NSFW • Liste des commandes", color=0xed9ce7)
            embed.add_field(name='Utilisation :', value="ars porn `[CATEGORIE]`   **ou**\nars nsfw `[CATEGORIE]`   **ou**\nars sex `[CATEGORIE]`   **ou**\nars xxx `[CATEGORIE]`   **ou**\nars x `[CATEGORIE]`", inline=False)
            embed.add_field(name='Liste des catégories : (15)', value="(en *italique* son les categories alias)\n`anal` *ass* *sodomie*\n`biffle` *biflette*\n`bdsm` *bondage*\n`boobs` *seins*\n`ciseaux` *scissors* *scissor* *ciseau*\n`dick` *bite* *teub*\n`facial` *cumshot*\n`fist` *poing*\n`gay`\n`hentai` *anime*\n`nude` *snap* *snapchat*\n`poils` *poil* *fur* *hairiness* *pilosity*\n`pussy` *vagin* *vagina* *minou* *chatte*\n`squirt`\n`69`", inline=False)
            embed.set_footer(text="NSFW")
            reponseText = await client.send_message(getchannel, embed=embed)
        elif arg == 'hentai' or arg == 'anime':
            possible_responses = [
                "https://images.sex.com/images/pinporn/2019/02/24/300/20740023.gif",
                "https://images.sex.com/images/pinporn/2017/03/26/300/17542758.gif",
                "https://images.sex.com/images/pinporn/2018/03/11/300/19229180.gif",
                "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/gif-sexe-hentai.gif",
                "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/gifs-hentai.gif",
                "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/sexe-debout-gif-hentai.gif",
                "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/hentai-gif.gif",
                "http://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-1.gif",
                "http://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-10.gif",
                "https://thumbs.gfycat.com/EcstaticPiercingHarborporpoise-size_restricted.gif",
                "http://hentai.bestsexphotos.eu/wp-content/uploads/2017/01/tumblr_ofkrfhY8dG1u2uu04o1_500.gif",
                "http://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-24.gif",
                "https://images.sex.com/images/pinporn/2017/06/29/300/17978814.gif",
                "https://images.sex.com/images/pinporn/2016/10/31/300/16821339.gif",
                "https://cdn.steemitimages.com/DQmNeRXJox1EV7HyrFbs2ZWyzA1MeWGtdSh4dDPJ1EERs2i/tumblr_pb2q6iPred1trjbc8o1_1280.gif",
                "http://hentai.bestsexphotos.eu/wp-content/uploads/2017/04/tumblr_ogjr4lgzyQ1vkefi9o1_500.gif",
                "https://steemitimages.com/0x0/https://cdn.steemitimages.com/DQmZ6BCxV9VTXQQ9fzq2sWNJpD1ksfzthHyXvvGDt8NDFPm/002.gif",
                "http://33.media.tumblr.com/2de6e699767d231e0853f5b28ddf05fc/tumblr_nc2jfmefoQ1tjgwy0o1_500.gif",
                "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/hentai.gif",
                "http://candy.adult/upload/media/entries/2019-01/22/15073-0-235dd0f1aade1b55aa16d85b8fa71356.gif"
            ]
            embed = discord.Embed(title="NSFW • hentai", color=0xed9ce7)
            embed.set_image(url=random.choice(possible_responses))
            embed.set_footer(text="NSFW")
            reponseText = await client.send_message(getchannel, embed=embed)
            await client.add_reaction(reponseText, "😏")
        elif arg == 'facial' or arg == 'cumshot':
            possible_responses = [
                "https://images.sex.com/images/pinporn/2018/06/10/300/19585338.gif",
                "https://images.sex.com/images/pinporn/2018/07/08/300/19697093.gif",
                "https://images.sex.com/images/pinporn/2016/12/20/300/17085626.gif",
                "https://images.sex.com/images/pinporn/2018/05/26/300/19527065.gif",
                "http://www.porngif.org/wp-content/uploads/2015/03/Asa-Akira-Facial.gif",
                "https://images.sex.com/images/pinporn/2016/11/04/300/16845972.gif",
                "http://gifgoo.com/media/galleries/5/a/5/7/0/5a570744a44bc/5a57076055261.gif",
                "http://porngif.org/wp-content/uploads/2013/12/Emma-Mae-Facial.gif",
                "https://images.sex.com/images/pinporn/2016/02/24/300/15078545.gif",
                "http://gifgoo.com/media/galleries/5/8/6/e/8/586e8f7ae1bbf/586e8f9fe73b8.gif",
                "http://x.imagefapusercontent.com/u/Barry54/6039943/1890560909/Juelz-Ventura-Messy-Facial.gif",
                "https://images.sex.com/images/pinporn/2018/12/23/300/20407582.gif",
                "https://www.rencontresanslendemain.net/wp-content/uploads/2018/09/image-cumshot.gif",
                "http://4.bp.blogspot.com/-pBLLG2Bf6vI/UNeDi16fbnI/AAAAAAAABP0/KOBW-9dacJ8/s1600/1355890436773.gif",
                "http://biteenfeu.b.i.pic.centerblog.net/b8c42116.gif",
                "https://images.sex.com/images/pinporn/2018/01/15/300/18951931.gif",
                "https://www.rencontresanslendemain.net/wp-content/uploads/2018/01/gif-ejac-faciale.gif",
                "https://images.sex.com/images/pinporn/2015/11/23/300/14378209.gif",
                "http://x.imagefapusercontent.com/u/Zonibaron/3469916/673878534/17.gif",
                "https://img03.rl0.ru/5792dd5cb1b3713cf495ce6f709e748a/c682x440/x.imagefapusercontent.com/u/VladTepez/6059469/1784604371/d.gif",
                "https://www.coquinetv.com/admin/uploads/articles/891101494465102.gif"
            ]
            embed = discord.Embed(title="NSFW • cumshot", color=0xed9ce7)
            embed.set_image(url=random.choice(possible_responses))
            embed.set_footer(text="NSFW")
            reponseText = await client.send_message(getchannel, embed=embed)
            await client.add_reaction(reponseText, "😏")
        elif arg == '69':
            possible_responses = [
                "https://images.sex.com/images/pinporn/2018/11/22/300/20251036.gif",
                "https://images.sex.com/images/pinporn/2016/05/10/300/15666865.gif",
                "https://www.rencontresanslendemain.net/wp-content/uploads/2018/09/gif-69-classique.gif",
                "https://images.sex.com/images/pinporn/2015/08/17/300/13561404.gif",
                "https://www.rencontresanslendemain.net/wp-content/uploads/2018/09/69-gif.gif",
                "https://images.sex.com/images/pinporn/2015/08/17/300/13561338.gif",
                "https://images.sex.com/images/pinporn/2016/01/23/300/14844099.gif",
                "http://commentseduire.net/wp-content/uploads/2014/12/gif-porno-69.gif",
                "https://www.rencontresanslendemain.net/wp-content/uploads/2018/09/animation-69.gif",
                "https://images.sex.com/images/pinporn/2016/04/21/300/15521200.gif",
                "https://buzzporn.net/wp-content/uploads/2018/02/Position-69-10.gif",
                "https://images.sex.com/images/pinporn/2014/05/22/300/6125560.gif",
                "https://www.niceandquite.com/wp-content/uploads/2015/09/ArtisticIgnorantBantamrooster.gif",
                "https://www.rencontresanslendemain.net/wp-content/uploads/2018/09/69-vertical.gif",
                "https://buzzporn.net/wp-content/uploads/2018/02/Position-69-11.gif",
                "https://www.rencontresanslendemain.net/wp-content/uploads/2018/09/image-animee-position-69.gif",
                "https://images.sex.com/images/pinporn/2018/07/09/300/19700470.gif",
                "https://www.pstargif.com/wp-content/uploads/2018/06/connie-carter-wowgirls-69-oral-sex.gif",
                "https://cdn5-images.motherlessmedia.com/images/A72BE9D.gif",
                "https://images.sex.com/images/pinporn/2015/09/28/300/13895444.gif",
                "https://images.sex.com/images/pinporn/2018/07/23/300/19753589.gif",
                "https://www.niceandquite.com/wp-content/uploads/2015/08/PertinentPeskyBelugawhale.gif",
                "https://images.sex.com/images/pinporn/2015/08/17/300/13561433.gif",
                "https://www.rencontresanslendemain.net/wp-content/uploads/2018/09/gif-sexe-69.gif",
                "http://www.freeporngifs.com/uploads/interesting_69_gif_49878.gif",
                "http://bestsexgif.com/wp-content/uploads/2015/02/69-blowjob-pussy-lick.gif",
                "http://sexwhatelse.s.e.pic.centerblog.net/$75b69rdggfgf.gif",
                "https://buzzporn.net/wp-content/uploads/2018/02/Position-69-01.gif",
                "http://teen-sex-photos.eu/wp-content/uploads/2014/11/tumblr_ndtixo0BOO1u012tyo1_500.gif",
                "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/gifs-69.gif"
            ]
            embed = discord.Embed(title="NSFW • 69", color=0xed9ce7)
            embed.set_image(url=random.choice(possible_responses))
            embed.set_footer(text="NSFW")
            reponseText = await client.send_message(getchannel, embed=embed)
            await client.add_reaction(reponseText, "😏")
        elif arg == 'poil' or arg == 'poils' or arg == 'fur' or arg == 'hairiness' or arg == 'pilosité' or arg == 'pilosity':
            possible_responses = [
                "https://www.grosnews.com/pictures/images_series_sexy/032016/filles-conservent-poils-pubiens-1.gif",
                "http://www.ict-peces.eu/image/865187.gif",
                "https://www.coquinetv.com/admin/uploads/articles/10601483591442.gif",
                "http://31.media.tumblr.com/2e5fe103237d0d76cec17e480241dc15/tumblr_mtwoh6LQxl1r3r865o1_500.gif",
                "https://www.chattepoiluegratuit.fr/wp-content/uploads/2015/09/plan-a-3-anal.gif",
                "https://www.coquinetv.com/admin/uploads/articles/552811522975462.gif",
                "https://images.sex.com/images/pinporn/2016/04/07/300/15413682.gif",
                "https://www.chattepoiluegratuit.fr/wp-content/uploads/2016/03/blonde-nympho-masse-chatte.gif",
                "https://www.grosnews.com/pictures/images_series_sexy/112016/photos-vintage-chatte-poilue-femme-baise-1.gif",
                "https://images.sex.com/images/pinporn/2016/07/22/300/16198955.gif",
                "https://cl.phncdn.com/gif/1649972.gif",
                "http://24.media.tumblr.com/e2d60488fd26d2ba6636944e08546ba8/tumblr_mtwoh6LQxl1r3r865o5_500.gif",
                "https://www.grosnews.com/pictures/images_series_sexy/032016/foufoune-poilue-1.gif",
                "https://www.chattepoiluegratuit.fr/wp-content/uploads/2016/04/masturbation-chatte-crepue-indienne.gif",
                "https://www.chattepoiluegratuit.fr/wp-content/uploads/2015/05/nympho-branlee-par-james-deen.gif",
                "https://diaryfrenchpua.com/wp-content/uploads/2018/09/gifs-cenes-porno.gif",
                "https://images.sex.com/images/pinporn/2018/12/07/300/20318644.gif",
                "http://gif.pornomass.com/download/367-le-porno-myanmar-gif.gif",
                "https://www.grosnews.com/pictures/images_series_sexy/072018/filles-noires-poilues-1.gif",
                "https://www.coquinetv.com/admin/uploads/articles/832991459991478.gif",
                "https://images.sex.com/images/pinporn/2018/12/21/300/20395370.gif",
                "https://www.chattepoiluegratuit.fr/wp-content/uploads/2015/05/cunnilngus-grosses-levres.gif",
                "https://www.madxfrance.com/wp-content/uploads/2014/07/chatte-poilu-d%C3%A9forestation.gif",
                "http://www.chaudasie.com/wp-content/uploads/tokyoite-nympho-poilue-sexe.gif",
                "http://www.chattepoiluegratuit.fr/wp-content/uploads/2016/12/videopoilues.gif",
                "http://www.2folie.com/wp-content/uploads/2018/02/1517854392_fa9b20capture_20111114_1_2.gif",
                "http://gifgoo.com/media/galleries/5/a/9/e/e/5a9eebb7dfd85/5a9eec65e3968.gif",
                "https://thumb-p2.xhcdn.com/a/YUoFGL4q1O1GoYPu5TJWNA/000/186/727/622_1000.gif",
                "https://4.bp.blogspot.com/-dNzUzYv8eC8/V0bJf-HsK0I/AAAAAAAAAUs/NhWFmzVqguo1vOuRVTFzoGTBkSiwuBGowCLcB/s1600/Keisha+Grey1.gif",
                "http://78.media.tumblr.com/310969810907acb503a7e98b8e87b704/tumblr_njrryelnN51sl7ykwo2_400.gif",
                "http://www.chattepoiluegratuit.fr/wp-content/uploads/2016/04/masturbation-chatte-crepue-indienne-2.gif"
            ]
            embed = discord.Embed(title="NSFW • poils", color=0xed9ce7)
            embed.set_image(url=random.choice(possible_responses))
            embed.set_footer(text="NSFW")
            reponseText = await client.send_message(getchannel, embed=embed)
            await client.add_reaction(reponseText, "😏")
        elif arg == 'boobs' or arg == 'seins':
            possible_responses = [
                "http://gfpics.com/wp-content/uploads/WatchMyTits4-1.gif",
                "http://gfpics.com/wp-content/uploads/1-76.gif",
                "http://www.funoct.eu/image/all-fours-swinging-boobs.gif",
                "https://media-blog.porn.com/wp-content/uploads/2015/11/PornDotCom-Giff-Boobs-001.gif",
                "http://gfpics.com/wp-content/uploads/4-66.gif",
                "https://cl.phncdn.com/gif/12811771.gif",
                "http://choualbox.com/Img/137501910848.gif",
                "https://images.sex.com/images/pinporn/2016/04/25/620/15548727.gif",
                "http://www.reuni.eu/image/124620.gif",
                "https://img07.rl0.ru/5201e8d428fa6ba3ec670b83b8e51768/c350x350/x.imagefapusercontent.com/u/matsuchebafubu/4115262/470891935/1270993542022.gif",
                "http://users.atw.hu/porngif/tmp/szexgif631642103.gif",
                "http://choualbox.com/Img/20110628111019W.gif",
                "http://gfpics.com/wp-content/uploads/1-68.gif",
                "http://www.porngif.org/wp-content/uploads/2014/08/Dillion-Harper-Bouncing-Tits.gif",
                "http://choualbox.com/Img/20120627210936P.gif",
                "http://www.motherless.me/wp-content/uploads/2014/09/big-dancing-boobs.gif",
                "http://sexwhatelse.s.e.pic.centerblog.net/$32nlieQllNkfkRS3.gif",
                "http://sexwhatelse.s.e.pic.centerblog.net/$1nlm4Cl61ubligro1_500.gif",
                "http://sexwhatelse.s.e.pic.centerblog.net/$2nle8yYbE1qzvcx0o2_500.gif",
                "http://sexwhatelse.s.e.pic.centerblog.net/$3nlao21qega1vo1_400.gif",
                "http://sexwhatelse.s.e.pic.centerblog.net/$4nl_catalina-taylor-4.gif",
                "http://sexwhatelse.s.e.pic.centerblog.net/$5nlyjqcqh1rjfb4to1_250.gif",
                "http://sexwhatelse.s.e.pic.centerblog.net/$7nl0znvud871svnfi3o1_500.gif",
                "http://sexwhatelse.s.e.pic.centerblog.net/$8n5sf45g4.gif",
                "http://sexwhatelse.s.e.pic.centerblog.net/$9nl$$$$$$$$$$$$$$$$$$$$$$$$$.gif",
                "http://porn.uw.hu/foto/xxxl_boobs_gif.gif",
                "http://commentseduire.net/wp-content/uploads/2017/06/big-boobs-on-desk.gif",
                "http://vintage-calc.info/img/455162.gif",
                "http://imawesa.info/pictures/naked-porn-boobs-gif-2.gif",
                "http://tse4.mm.bing.net/th?id=OGC.36fceab3a1d152cebfc8fb2b71e84a79&pid=1.7&rurl=http://68.media.tumblr.com/15006426c2d04361dbd4e212b9df2905/tumblr_o4cizbXw7o1vn16uxo1_400.gif&ehk=WiIw8fp0LWfeU5wuQh46JQ",
                "https://1.bp.blogspot.com/-XshSL_zlq1g/VvANewsFLVI/AAAAAAAABTY/Gdw69mkuIocDl8cFcphBVxFFd-OQapoiQ/s1600/y22CIev.jpg",
                "http://www.hugetitsgif.com/wp-content/uploads/2017/02/tumblr_ok1eainTYY1vvegmgo1_400.gif",
                "http://commentseduire.net/wp-content/uploads/2017/06/blonde-with-big-boobs.gif",
                "http://vintage-calc.info/img/nude-teens-showing-boobs-gif-2.gif",
                "http://tse1.mm.bing.net/th?id=OGC.2655d923fc53ca056b89f8a7d8e7ffa9&pid=1.7&rurl=http://68.media.tumblr.com/d8e8f63ef6869effc77c7e1991aa7b27/tumblr_omgzpyK4cg1vhoyheo1_400.gif&ehk=hbL5bJ2OBvaNQWZhfKWiAw",
                "http://gfpics.com/wp-content/uploads/WatchMyTits_31.gif",
                "https://media.tits-guru.com/images/57b1c307-a7df-4fbb-b46a-a7f0dbb56556.gif",
                "https://media.tits-guru.com/images/e0c40752-e39f-41d7-907b-d46dd734b23a.gif",
                "https://media.tits-guru.com/images/efc0eef1-d282-4d02-82ab-c15aa01f3296.gif",
                "https://media.tits-guru.com/images/cd95b3ab-34a3-40d3-94e4-4f97c7c8de71.gif",
                "http://tse3.mm.bing.net/th?id=OGC.2231c957bbe232befdb3e00be0f04c53&pid=1.7&rurl=http://2.bp.blogspot.com/-CSF_T2zwRzA/UNnBd5szaGI/AAAAAAAAFfM/gpKWo1WGXHI/s1600/teen-show-tits.gif&ehk=7m7XGPITcdEq5Samec6cLA",
                "https://images.sex.com/images/pinporn/2018/11/06/300/20183547.gif",
                "http://www.ict-peces.eu/image/773868.gif",
                "http://choualbox.com/Img/20120713175640C.gif",
                "http://sokol-tabor.info/pictures/541818.gif"
            ]
            embed = discord.Embed(title="NSFW • boobs", color=0xed9ce7)
            embed.set_image(url=random.choice(possible_responses))
            embed.set_footer(text="NSFW")
            reponseText = await client.send_message(getchannel, embed=embed)
            await client.add_reaction(reponseText, "😏")
        elif arg == 'ciseaux' or arg == 'scissor' or arg == 'scissors' or arg == 'ciseau':
            possible_responses = [
                "https://images.sex.com/images/pinporn/2018/02/05/300/19058064.gif",
                "http://tse4.mm.bing.net/th?id=OGC.b332e7e983012d22a09b98b3c4ab925d&pid=1.7&rurl=https://www.xpin.fr/wp-content/uploads/2017/10/Deux-gros-clitos-en-gros-plan-qui-se-frotte-chatte-contre-chatte.gif&ehk=Esc380ZwlBIITvsTKW29DQ",
                "https://images.sex.com/images/pinporn/2015/12/07/300/14480561.gif",
                "https://static-ca-cdn.eporner.com/photos/595716.gif",
                "http://choualbox.com/Img/138555908989.gif",
                "http://www.reuni.eu/image/nude-hot-naked-lesbians-gif-scissors-2.gif",
                "https://dl.phncdn.com/gif/16291982.gif",
                "https://images.sex.com/images/pinporn/2017/07/14/620/18050644.gif",
                "http://tse4.mm.bing.net/th?id=OGC.b772f83a90a4a2658773563adadd45b4&pid=1.7&rurl=http://33.media.tumblr.com/258c0e0c0ed13a33101a176d0d09c119/tumblr_mzd8x6fSrj1revz5to1_500.gif&ehk=Nx998/ZzfgsSWzul8jGuSw",
                "https://cdn5-images.motherlessmedia.com/images/CCF7129.gif?fs\u003dopencloud",
                "https://static-ca-cdn.eporner.com/photos/591292.gif",
                "https://images.sex.com/images/pinporn/2014/05/07/300/5899465.gif",
                "http://i.imgur.com/8EN8aCO.gif",
                "http://xxxpicss.com/xxx/lesbian-scissor-orgasm-wild-hardcore-erotica-lesbian-scissoring-gif.gif",
                "http://24.media.tumblr.com/37c91bdb48c50e6778f09f0d8e39ad91/tumblr_n22rlwXmyd1romx5eo4_400.gif",
                "http://38.media.tumblr.com/tumblr_m3bbf4MRbe1rt1ilfo1_500.gif",
                "http://tse1.mm.bing.net/th?id=OGC.23772f08b76eb4792a61cb0fe9808db5&pid=1.7&rurl=https%3A%2F%2Flistslut.com%2Fwp-content%2Fuploads%2F2016%2F05%2Fscissoring-gif-8.gif&ehk=IJogI0y6FmdVQX1dsb1nPg",
                "https://static-ca-cdn.eporner.com/photos/270866.gif",
                "http://tse3.mm.bing.net/th?id=OGC.a1e9f1a8eaa002b8c66606d46a2fad30&pid=1.7&rurl=http%3A%2F%2F38.media.tumblr.com%2Fed1b2ca36baf004b4b9b6436ee2ba6df%2Ftumblr_ni4x3hpwdv1u0gmezo3_500.gif&ehk=M1ePiifTSd7qOTMDo9vqdQ",
                "https://gifs.iloopit.net/resources/5de35f6c-06dd-4013-8728-aefa1920f779/converted.gif",
                "http://fb05.manworldmediacdn.com/data/images/straight/006/010/073/Abella-Danger-Staci-Carr-Lesbian-Scissoring-WE-LIVE-TOGETHER-GIF_web.gif?1435690375",
                "http://tse4.mm.bing.net/th?id=OGC.3dc85ba90f1c2a4cc1391b85102587b2&pid=1.7&rurl=https://images.sex.com/images/pinporn/2015/05/17/620/11966045.gif&ehk=AzF7/s9uHj2zV/908qV5Sg",
                "https://gifs.iloopit.net/resources/2fe10578-bed2-49af-8c5a-e9e343efb566/converted.gif",
                "http://tse3.mm.bing.net/th?id=OGC.06ec26f742d42ff927bfbd46fbb7d7ce&pid=1.7&rurl=http://24.media.tumblr.com/tumblr_m4zi4dSfJc1ruca7ao1_500.gif&ehk=JDOV3zF1JTulbAwJaZgRBg",
                "https://tse4.mm.bing.net/th?id=OGC.5c132483087ddf409a96ab41ca7ff776&pid=1.7&rurl=http%3A%2F%2F24.media.tumblr.com%2F5137a88580700f21231c07d8b2f29f25%2Ftumblr_ms7d557Q5k1s59ueeo1_500.gif&ehk=zAVS3S0IwnV8jaP%2FR4jO6w",
                "https://cdn4.images.motherlessmedia.com/images/20A1C5B.gif?fs//u003dopencloud",
                "https://tse1.mm.bing.net/th?id=OGC.c79aacba79f4adb7dd92a5727d5874cf&pid=1.7&rurl=http%3A%2F%2Fx.imagefapusercontent.com%2Fu%2FC3LESTE%2F4063107%2F1221800214%2Ftrib72.gif&ehk=M2CYKLC8OyRAJFRiRBeYPA",
                "https://gifs.iloopit.net/resources/7ee5d977-437a-4c70-95a4-f1cd554b0c6f/converted.gif",
                "http://www.juicygif.com/albums/userpics/2014y/06/16/18/1/7324-skin-diamon-scissoring-with-yasmine-de-leon.gif",
                "https://tse4.mm.bing.net/th?id=OGC.b628e89b86bd5fdb2ffd0dfb8a9a5b50&pid=1.7&rurl=http%3A%2F%2F31.media.tumblr.com%2F0412cb3d9f95f33b26e8e528706a8184%2Ftumblr_n39ve8caMa1rbieovo1_400.gif&ehk=IeMhvMgFJI%2Bu2tmlkDtbsQ"
            ]
            embed = discord.Embed(title="NSFW • scissor", color=0xed9ce7)
            embed.set_image(url=random.choice(possible_responses))
            embed.set_footer(text="NSFW")
            reponseText = await client.send_message(getchannel, embed=embed)
            await client.add_reaction(reponseText, "😏")
        elif arg == 'squirt':
            possible_responses = [
                "http://www.porngif.org/wp-content/uploads/2015/03/Asa-Akira-Squirting.gif",
                "https://dl.phncdn.com/gif/17593401.gif",
                "https://images.sex.com/images/pinporn/2016/03/10/300/15191674.gif",
                "https://cl.phncdn.com/gif/12842001.gif",
                "https://gifcandy.net/wp-content/uploads/2016/04/gifcandy-squirt-100.gif",
                "http://tse1.mm.bing.net/th?id=OGC.9ac13d819f2346957f15546e296ba97d&pid=1.7&rurl=http://i.smutty.com/media_smutty_2/m/y/f/a/b/myfapcam-tcg2a-e7b295.gif&ehk=lEAO0Mg8P/Dyin8bVh71hQ",
                "http://www.masterstudyprograms.eu/image/608541.gif",
                "https://images.sex.com/images/pinporn/2018/03/17/300/19254565.gif",
                "http://commentseduire.net/wp-content/uploads/2017/01/squirt-gif-5.gif",
                "http://tse4.mm.bing.net/th?id=OGC.e8ab2bfd5050b92b9b15da1bfce5fd96&pid=1.7&rurl=https%3A%2F%2Fporngifsforadults.com%2Fwp-content%2Fuploads%2F2017%2F12%2Fsex-gifs-squirt-2.gif&ehk=OayvYLG7qvpDZ9lc9vIC8g",
                "https://images.sex.com/images/pinporn/2017/06/24/620/17955154.gif",
                "https://tse1.mm.bing.net/th?id=OGC.dd7bf8ef9df74f1b4e7378820bddf828&pid=1.7&rurl=http%3A%2F%2Fporngiphy.com%2Fwp-content%2Fuploads%2F2015%2F12%2Fsquirting-from-gif-it-to-me-now.gif&ehk=C2copAanFkHOSwO5O9whXg",
                "http://38.media.tumblr.com/e8a3800d621c86cafcf36eba4d92c0ba/tumblr_naldnznEUT1txwtk5o1_500.gif",
                "https://static-ca-cdn.eporner.com/photos/166697.gif",
                "http://www.reuni.eu/image/4b1dfc3ed8ac1b449e43088e9089c68a.gif",
                "http://tse1.mm.bing.net/th?id=OGC.ae73f9b3c224893692ed79a69eca74bd&pid=1.7&rurl=http://gifssex.com/images/photos/medium/7dbf8918ae767606cdf1eaab4ee7f626.gif&ehk=Z9Z52HgECSGbTJw7MMi9bw",
                "https://tse3.mm.bing.net/th?id=OGC.82dcbc6cd80593334e9c3df38a0de1ab&pid=1.7&rurl=http%3A%2F%2Fwww.171gifs.com%2Fwp-content%2Fuploads%2F2016%2F02%2FLuna-Star-Big-Boob-Squirtdown-06-squirt-gif.gif&ehk=0jVZ5zcL1Zk9OICkVjzreQ",
                "https://i.imgur.com/diEN42D.gif",
                "https://img02.rl0.ru/23252872b020eafb78d6dd710f6c6a63/c1360x768/tubezzz.net/wp-content/uploads/2017/09/15135530-8966-tubezzz.net.gif",
                "https://mgsu.info/images/e58c4d9fad1928c5f943928788d578dc.gif",
                "http://squirtingpussy.xxx/images/thumb/996.gif",
                "http://users.atw.hu/porngif/tmp/squirt-porn-gif1525898947.gif",
                "http://68.media.tumblr.com/51f15e362fd463e99ebe74699ae7caf4/tumblr_mu0r3eTATY1s5ssa6o1_500.gif",
                "https://68.media.tumblr.com/9803d01d32d78b74628a2208022dcde1/tumblr_numz0m4YFb1ryino5o4_500.gif",
                "http://tse3.mm.bing.net/th?id=OGC.accc23dd76c2f77252222aa1d660d479&pid=1.7&rurl=http://24.media.tumblr.com/0c48162d53fdb36a05c31c7aca3e7245/tumblr_mw9dj0L73Z1s0oxwvo6_500.gif&ehk=aEF7z8RUOFaUVj1wG28VAw",
                "https://fotosbor.com/files/2018/10/IMGGIF1539269522cXvPjV/1539269522Iot5JK.gif",
                "http://68.media.tumblr.com/889721697d2dc93ce128d5f933c0ca1f/tumblr_oid810m5H01vfnenco1_500.gif",
                "http://xxxpicss.com/xxx/watch-me-squirt-tumblr.gif",
                "https://tse1.mm.bing.net/th?id=OGC.dfb691e0027876f3f445c5478bb6919b&pid=1.7&rurl=http%3A%2F%2Fjuicygif.com%2Falbums%2Fuserpics%2F2016y%2F06%2F05%2F12%2F1%2F4758-ombfun-vibe-toys-hot-squirting-masturbation-orgasm.gif&ehk=3KM40fKqVoU%2BHMGSu9lhqA",
                "http://tse2.mm.bing.net/th?id=OGC.511c97ae59d3afa99d4370863c19abd2&pid=1.7&rurl=http%3A%2F%2Fa.im9.eu%2Fanal-anal-makes-her-squirt.gif&ehk=5x0OTJCv6HxIJv%2BemFarYQ",
                "https://78.media.tumblr.com/65533250af39c4769704051c7f597454/tumblr_mlpmlq7low1rif4doo1_250.gif",
                "http://imgur.com/xHKWxid.gif",
                "https://78.media.tumblr.com/e499b51219f167f87055727507f0b27b/tumblr_mes5mut7Qw1r2sy0fo1_500.gif",
                "http://imgur.com/so6VUGo.gif",
                "https://78.media.tumblr.com/685a6e0fbc585734a65ce829a1affc44/tumblr_mgkwxttcPC1rapu2oo1_250.gif"
                ]
            embed = discord.Embed(title="NSFW • squirt", color=0xed9ce7)
            embed.set_image(url=random.choice(possible_responses))
            embed.set_footer(text="NSFW")
            reponseText = await client.send_message(getchannel, embed=embed)
            await client.add_reaction(reponseText, "😏")
        elif arg == 'anal' or arg =='sodomie' or arg == 'ass':
            possible_responses = [
                "https://images.sex.com/images/pinporn/2017/04/14/300/17625520.gif",
                "https://images.sex.com/images/pinporn/2018/09/29/300/20023883.gif",
                "https://images.sex.com/images/pinporn/2016/03/20/300/15269112.gif",
                "https://images.sex.com/images/pinporn/2018/10/03/300/20038498.gif",
                "https://images.sex.com/images/pinporn/2017/02/11/300/17346212.gif",
                "https://images.sex.com/images/pinporn/2019/02/22/300/20727240.gif",
                "https://static-ca-cdn.eporner.com/photos/208131.gif",
                "https://images.sex.com/images/pinporn/2018/10/03/300/20038487.gif",
                "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/gifs-sodomie.gif",
                "http://porngif.org/wp-content/uploads/2013/10/Anal234.gif",
                "https://images.sex.com/images/pinporn/2018/10/03/300/20038475.gif",
                "https://static-ca-cdn.eporner.com/photos/162387.gif",
                "http://cdn4.images.motherlessmedia.com/images/91F6BDF.gif?fs\u003dopencloud",
                "https://images.sex.com/images/pinporn/2018/09/21/300/19986134.gif",
                "http://porngif.org/wp-content/uploads/2014/01/1264.gif",
                "http://biteenfeu.b.i.pic.centerblog.net/anal-paradise-franceska-jaimes-2015-porn-gif.gif",
                "https://images.sex.com/images/pinporn/2017/05/19/300/17787139.gif",
                "http://www.pornosexgif.org/wp-content/uploads/2015/12/anal-720p-gif.gif",
                "https://mediav-img.porn.com/secure/837cd8c639481c02f3de175e11ad6f5d/sc/4/4362/4362279/source/002.gif",
                "https://i1.wp.com/morefunforyou.com/wp-content/uploads/2015/04/Dollie-Darko-Anal-Porn-Gifs.gif",
                "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/sodomie-gifs.gif",
                "https://dl.phncdn.com/gif/2075651.gif",
                "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/animation-sexe-anal.gif",
                "http://www.daporngifs.com/gif/riley-jenner-in-anal-doggystyle.gif",
                "http://gif.pornomass.com/download/165-gif-porn-anal-brutale.gif",
                "https://images.sex.com/images/pinporn/2018/06/18/300/19616422.gif",
                "http://www.porngif.org/wp-content/uploads/2014/08/Casey-Calvert-Anal-Sex.gif",
                "http://www.pornosexgif.org/wp-content/uploads/2015/12/kalite-anal-gif.gif",
                "https://i.imgur.com/w5HQfsu.gif",
                "https://images.sex.com/images/pinporn/2018/09/09/300/19938693.gif",
                "http://www.reuni.eu/image/700534.jpg"
                ]
            embed = discord.Embed(title="NSFW • anal", color=0xed9ce7)
            embed.set_image(url=random.choice(possible_responses))
            embed.set_footer(text="NSFW")
            reponseText = await client.send_message(getchannel, embed=embed)
            await client.add_reaction(reponseText, "😏")
        elif arg == 'vagin' or arg =='vagina' or arg == 'pussy' or arg == 'chatte' or arg == 'minou':
            possible_responses = [
                "https://images.sex.com/images/pinporn/2018/04/16/300/19376107.gif",
                "https://images.sex.com/images/pinporn/2018/04/10/300/19352078.gif",
                "https://images.sex.com/images/pinporn/2018/05/26/300/19527002.gif",
                "https://images.sex.com/images/pinporn/2018/05/22/300/19512120.gif",
                "https://images.sex.com/images/pinporn/2019/01/05/300/20477127.gif",
                "https://ebiza.info/images/3040781218_gif-porn-pussy.gif",
                "https://images.sex.com/images/pinporn/2017/05/22/300/17803958.gif",
                "http://www.coaching-et-formation-coaching.eu/image/xxx-dick-in-pussy-gifs.gif",
                "https://images.sex.com/images/pinporn/2019/02/16/300/20701186.gif",
                "https://images.sex.com/images/pinporn/2017/01/31/620/17297665.gif",
                "http://xxxlibz.com/wp-content/uploads/2017/11/07210043-9150-xxxlibz.com.gif",
                "http://tse1.mm.bing.net/th?id=OGC.e136ac5d57a2978a58d57a1a922e9453&pid=1.7&rurl=https://images.sex.com/images/pinporn/2016/10/26/620/16797519.gif&ehk=NpHZuMQOzBE65bPgtm/J/w",
                "https://images.sex.com/images/pinporn/2016/06/29/620/16032205.gif",
                "http://porngif.top/gif/kundicky/0109.gif",
                "http://24.media.tumblr.com/bbc0942fa517426a0d61c76febd61939/tumblr_miyi25VnCe1s1b6voo1_500.gif",
                "http://www.akceleratorbiznesu.eu/image/343541.gif",
                "http://porngif.top/gif/kundicky/0085.gif",
                "https://images.sex.com/images/pinporn/2018/08/12/300/19832623.gif",
                "https://dl.phncdn.com/gif/1870121.gif",
                "https://dl.phncdn.com/gif/454591.gif",
                "https://24.media.tumblr.com/tumblr_m0auzx2ZRY1qg6v7vo1_250.gif",
                "http://38.media.tumblr.com/be8a36c725da1a56a7f838fb791ecf9d/tumblr_ncouriNslX1sfkfqio3_500.gif",
                "http://tse4.mm.bing.net/th?id=OGC.98279951565a8b9a96e4279afde47b59&pid=1.7&rurl=http://www.juicygif.com/albums/userpics/2017y/08/26/22/1/8054-the-hottest-pussy-fuck-pov-sex-gifs.gif&ehk=1GfvGYLOUJENzqSgeq4dnQ",
                "http://tse2.mm.bing.net/th?id=OGC.596af79942643abedd11c5e58f58bfa9&pid=1.7&rurl=http://www.gifsfor.com/wp-content/uploads/2012/12/Gifs-for-Tumblr-1526.gif&ehk=Vqu5WYuurG9aewWJpeZl1g"
                ]
            embed = discord.Embed(title="NSFW • pussy", color=0xed9ce7)
            embed.set_image(url=random.choice(possible_responses))
            embed.set_footer(text="NSFW")
            reponseText = await client.send_message(getchannel, embed=embed)
            await client.add_reaction(reponseText, "😏")
        elif arg == 'dick' or arg =='bite' or arg == 'teub' or arg == 'penis':
            possible_responses = [
                "https://images.sex.com/images/pinporn/2018/11/10/300/20197765.gif",
                "http://1.bp.blogspot.com/-ldIIlN6J1H8/UJqSp3yg2EI/AAAAAAAAf_k/qhOP6cE8gnk/s640/tumblr_lwb8rf31tt1qkpqjoo1_500.gif",
                "http://x.imagefapusercontent.com/u/FurryBoy/4137084/1283416800/Wanker100.gif",
                "http://3.bp.blogspot.com/-slZj3dhR2gE/UZ97O-ri-II/AAAAAAAAe_E/zt2EVfdwNnE/s1600/tumblr_mjieb7DZUz1rbpu60o1_500.gif",
                "http://25.media.tumblr.com/tumblr_m3kvjcai5P1qkpqjoo1_400.gif",
                "https://cl.phncdn.com/gif/1482001.gif",
                "http://www.welovegoodsex.com/wp-content/uploads/2014/10/tumblr_nd6eu9cyA41twlj05o1_500.gif",
                "http://www.coaching-et-formation-coaching.eu/image/jacking-off-masturbation-porn.gif",
                "http://www.cheap-bg-properties.eu/image/158572.gif",
                "https://milliondicks.com/pics/t/s-47868.gif",
                "http://gaybf.com/wp-content/uploads/5-90.gif",
                "http://101hotguys.com/wp-content/uploads/2019/01/show_me_how_you_masturbate_06.gif",
                "http://www.reuni.eu/image/772836.gif",
                "http://www.mnimi.eu/image/764160.gif",
                "http://gaybf.com/wp-content/uploads/5-50.gif",
                "https://img1.vod.com/image2/spotlight/ghm-ethan5.gif",
                "http://4.bp.blogspot.com/-JVR-hitzBJU/UUceiUR6z5I/AAAAAAAAQ40/32HwI0UL31E/s640/gif12.gif",
                "http://101hotguys.com/wp-content/uploads/2019/02/WATCHING_PORN_01.gif",
                "http://www.tanie-auta.eu/image/924591.gif",
                "https://66.media.tumblr.com/71c8e6f1e4b429d81a4ba1f712709f6b/tumblr_na5wwhxu9A1s7twfho2_500.gif",
                "http://recit-trad.eu/wp-content/pics/circumcised-penis-masturbation.gif"
                ]
            embed = discord.Embed(title="NSFW • penis", color=0xed9ce7)
            embed.set_image(url=random.choice(possible_responses))
            embed.set_footer(text="NSFW")
            reponseText = await client.send_message(getchannel, embed=embed)
            await client.add_reaction(reponseText, "😏")
        elif arg == 'nude' or arg =='snap' or arg == 'snapchat':
            possible_responses = [
                "http://www.seemygf.com/wp-content/uploads/2016/07/Snapchat-Porn-Nude-Amateur-Teen-Naked-06.jpg",
                "https://snapchat-nude.com/uploads/posts/2016-11/medium/1480453888_4b5055f7718b4d6bbb6b611b614eec3c.jpg",
                "https://www.gfpics.com/ex-gf-porn-videos/snapchat/snapchat-naked-girl-pics.jpg",
                "http://gfpics.com/wp-content/uploads/sexting-selfie-naked-self-shot-amateur-ex-gf-porn-snapchat-leaked-pics_03.jpg",
                "https://www.amateurscrush.com/wp-content/uploads/2018/08/37-photo-snapchat-nudes-eviebaby-selfshot.jpg",
                "https://pbs.twimg.com/profile_images/466884169508089856/Ye84Zy3H.jpeg",
                "https://cdn.ghostnsfw.com/i/snapchat-megan-rain-littlesexbuddha-74b0.png",
                "http://www.gfnudephotos.com/wp-content/uploads/2017/11/Snapchat-Amazing-Naked-Tits-And-Nude-Ass-of-Cute-Teen-Girl-Leaked-XXX-Selfies-GFnudephotos.com-107.jpg",
                "https://www.gfnudephotos.com/wp-content/uploads/2017/11/Snapchat-Amazing-Naked-Tits-And-Nude-Ass-of-Cute-Teen-Girl-Leaked-XXX-Selfies-GFnudephotos.com-179-576x1024.jpg",
                "https://pbs.twimg.com/media/DDROoqaXoAEoxlW.jpg",
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCpjc4yER4o6LKKspAFcOBmKl80MxbKORuGO-qaBMMpfX8vvKa",
                "https://histoirepremium.fr/wp-content/uploads/2018/12/snapshat-fille-nue-6-1.jpg",
                "http://www.centreequestreboissyfresnoy.fr/wp-content/uploads/2019/01/snapchat-boobs-slut-nude-milf-horny-xxx-taylor-jay-taylor-jay-great-boobs-a1f5.png",
                "http://aadharhelp.info/wp-content/pics/nude-snapchat-selfies-4.jpg",
                "https://images.sex.com/images/pinporn/2018/06/29/300/19658678.jpg",
                "https://pbs.twimg.com/media/BPaJ7BtCMAMTkkD.jpg",
                "http://www.amateurscrush.com/wp-content/uploads/2018/03/leaked-beautiful-teen-selfies-snapchat-naked-tits.jpg",
                "https://i.redd.it/xqc3toexg0z11.jpg",
                "https://snapnude.fr/wp-content/uploads/2019/02/snapchat-sex-et-coquin-avec-fille-sexy-250x444.jpg",
                "https://pbs.twimg.com/media/CH4nqMHWgAAeHwz.jpg:large",
                "https://pbs.twimg.com/media/DZZN6keWsAAwKCJ.jpg",
                "http://www.sexy-feet.fr/wp-content/uploads/2019/01/belle-salope-francaise-du-13-partage-snapchat-576x1024-2.png",
                "http://i0.wp.com/www.seemygf.com/wp-content/uploads/2015/04/SeeMyGF-Selfie-Sexting-Amteur-ExGF-Porn-Teen-Leaked-Kik-Snapchat-Selfshot-Naked-Nude-Girls-61.jpg",
                "https://www.monteelancebranlette.fr/wp-content/uploads/2019/02/847_1000-1.jpg",
                "https://qpornx.com/xxx/snapchat-nudes-girls-pussy.jpg",
                "https://www.snapcoquin.fr/wp-content/uploads/2019/02/Snapsex-de-Virginie-en-train-de-pisser-577x1024.jpg",
                "http://adultxxxarea.com/all_img/xfgem4xi2mkrxbyz32xoz3jd4g8saist60k5rddtstkyw80t05.jpg",
                "http://nudebabes.realnakedgirls.net/wp-content/uploads/2018/03/rngnakedwhitebabe-152167826248lpc.png",
                "https://www.ava-moore.com/wp-content/uploads/2017/06/IMG_6600.jpg",
                "https://www.therackup.com/wp-content/uploads/2016/03/Sexy-College-Girl-on-Snapchat-1.jpg",
                "http://nudeselfie.net/img/2016/11/manoke-576x1024.jpg",
                "http://pornopics.co/photos/images/pic-3-cuckold-snapchats-1061247.jpg",
                "https://img.snapperparty.com/wp-content/themes/snapperparty/pictures/aussiegirlxox/aussiegirlxox_1487069448514.jpg",
                "http://compucasecorp.com/421/cc3fe2fab642ba245d48895b8e79720c.jpg",
                "https://snapchat-nude.com/uploads/posts/2016-11/medium/1480453888_4b5055f7718b4d6bbb6b611b614eec3c.jpg",
                "https://images.sex.com/images/pinporn/2018/09/12/300/19951041.gif",
                "https://images.sex.com/images/pinporn/2018/05/16/300/19488516.gif",
                "https://images.sex.com/images/pinporn/2018/09/06/300/19927187.gif"
                ]
            embed = discord.Embed(title="NSFW • snapchat", color=0xed9ce7)
            embed.set_image(url=random.choice(possible_responses))
            embed.set_footer(text="NSFW")
            reponseText = await client.send_message(getchannel, embed=embed)
            await client.add_reaction(reponseText, "😏")
        elif arg == 'bdsm' or arg =='bondage':
            possible_responses = [
                "https://images.sex.com/images/pinporn/2015/04/27/300/11655571.gif",
                "https://images.sex.com/images/pinporn/2018/12/28/300/20432171.gif",
                "https://images.sex.com/images/pinporn/2014/01/21/300/4771147.gif",
                "https://images.sex.com/images/pinporn/2017/01/03/300/17158559.gif",
                "http://commentseduire.net/wp-content/uploads/2014/12/photo-sexy-gif-porno-28.gif",
                "https://images.sex.com/images/pinporn/2017/12/19/300/18816950.gif",
                "http://users.atw.hu/porngif/tmp/szexgif773134949.gif",
                "https://images.sex.com/images/pinporn/2015/09/02/300/13681542.gif",
                "http://porn.uw.hu/foto/bdsm_porn_gif.gif",
                "http://gif.pornomass.com/download/208-gif-porno-bdsm.gif",
                "https://cdn5-images.motherlessmedia.com/images/BF6AE7C.gif",
                "https://dl.phncdn.com/gif/1161301.gif",
                "https://dl.phncdn.com/gif/16724721.gif",
                "https://cl.phncdn.com/gif/5101851.gif",
                "https://dl.phncdn.com/gif/10349742.gif",
                "https://dl.phncdn.com/gif/13452782.gif",
                "https://dl.phncdn.com/gif/10538242.gif",
                "https://dl.phncdn.com/gif/8616351.gif",
                "https://gifcandy.net/wp-content/uploads/2016/04/gifcandy-bdsm-141.gif",
                "https://images.sex.com/images/pinporn/2018/05/11/300/19468973.gif",
                "http://gif.pornomass.com/download/224-video-porno-bdsm.gif",
                "http://www.welovegoodsex.com/wp-content/uploads/2013/10/tumblr_mv10piUOUn1sa8kf7o1_400.gif",
                "https://i-gifv.porn.com/sc/5/5091/5091579/source/thumbnails/001.gif",
                "http://gif.pornomass.com/download/246-gif-sexy-bdsm.gif",
                "https://images.sex.com/images/pinporn/2014/03/19/620/5348929.gif?site=sex&user=redhotlaura",
                "https://images.sex.com/images/pinporn/2016/02/07/300/14945265.gif",
                "http://gifadult.com/wp-content/uploads/2019/02/gif-adult-porn-sex-20578666.gif",
                "http://24.media.tumblr.com/tumblr_md98f3Ilil1ryq8t2o1_500.gif",
                "https://images.sex.com/images/pinporn/2014/05/28/620/6203662.gif",
                "https://images.sex.com/images/pinporn/2018/01/14/300/18943284.gif",
                "https://images.sex.com/images/pinporn/2016/07/09/620/16102402.gif",
                "https://i-gifv.porn.com/sc/5/5135/5135749/source/thumbnails/001.gif",
                "https://static-ca-cdn.eporner.com/photos/182475.gif",
                "https://78.media.tumblr.com/b7f2514d9463e4dc06bf04f0c0434305/tumblr_nk2vac9zPC1ra9vkuo1_500.gif",
                "http://www.tudelicias.net/wp-content/uploads/2014/03/photo-BDSM-GIF-45002124.gif"
                ]
            embed = discord.Embed(title="NSFW • BDSM", color=0xed9ce7)
            embed.set_image(url=random.choice(possible_responses))
            embed.set_footer(text="NSFW")
            reponseText = await client.send_message(getchannel, embed=embed)
            await client.add_reaction(reponseText, "😏")
        elif arg == 'fist' or arg == 'poing':
            possible_responses = [
                "https://images.sex.com/images/pinporn/2016/07/04/300/16064751.gif",
                "https://dl.phncdn.com/gif/8095231.gif",
                "http://images5.sex.com/images/pinporn/2012/11/24/620/945858.gif?site=sex&user=skoscar77",
                "http://coupleamateursbellespoitrines.c.o.pic.centerblog.net/tumblr_nhkc54ND1b1tjb0dno1_400.gif",
                "http://stars69.s.t.pic.centerblog.net/11668374.gif",
                "http://i1.wp.com/24.media.tumblr.com/tumblr_m7y46tpef71rx6xyzo1_400.gif",
                "http://www.sexgifs.net/images/fisting/1740026857.gif",
                "https://images.sex.com/images/pinporn/2017/02/25/300/17408142.gif",
                "https://cdn.efukt.com/2017/04/0248a43f570cdfcc01565337c4c547ae.gif",
                "https://static-ca-cdn.eporner.com/photos/166691.gif",
                "https://gifs.iloopit.net/resources/ffcf35f4-ead2-447f-86a9-ecf14f41dace/converted.gif",
                "https://candy.porn/upload/media/entries/2018-08/28/14676-0-931c31709a1687da9fea2a0cbcf41cee.gif",
                "https://images.sex.com/images/pinporn/2016/12/12/300/17041299.gif",
                "http://67.media.tumblr.com/193496d4efcdb25af6ff02752106aef7/tumblr_ngsnvxD0DM1u66ehho1_500.gif",
                "http://ist3-1.filesor.com/pimpandhost.com/1/_/_/_/1/3/r/4/g/3r4g7/navidad-CarlosPrietoCBA9.gif",
                "https://gifs.iloopit.net/resources/cc388414-2396-4f62-9c4a-87dbd71b11ae/converted.gif",
                "https://images.sex.com/images/pinporn/2019/01/19/300/20552039.gif",
                "https://candy.porn/upload/media/entries/2018-08/28/14676-6-931c31709a1687da9fea2a0cbcf41cee.gif",
                "http://www.juicygif.com/albums/userpics/2015y/04/14/2/1/1094-anal-fist.gif",
                "https://candy.porn/upload/media/entries/2018-08/28/14676-3-931c31709a1687da9fea2a0cbcf41cee.gif",
                "http://tse3.mm.bing.net/th?id=OGC.41e41b410f339feb3c2184cb636d991c&pid=1.7&rurl=http://38.media.tumblr.com/8807d093e93ef5b30afad36c374e598c/tumblr_ngscpvAn3B1u66ehho1_400.gif&ehk=u4zyaD9VrRKrPqDjGx0wow",
                "http://sokol-tabor.info/pictures/d4814ea5036e20d81e61443ab18efb03.jpg",
                "http://juicygif.com/albums/userpics/2015y/09/03/1/1/3845-great-anal-fisting-action-with-two-girls-xhamster-4529-janvier56-01-gif.gif",
                "https://cdn5-images.motherlessmedia.com/images/B9DF897.gif",
                "http://thedeliciousness.net/_images/bf9821a3b6dbd00aa4236c98089f630b/1330%20-%20female%20fingering%20fisting%20gif%20tagme.gif"
                ]
            embed = discord.Embed(title="NSFW • fist", color=0xed9ce7)
            embed.set_image(url=random.choice(possible_responses))
            embed.set_footer(text="NSFW")
            reponseText = await client.send_message(getchannel, embed=embed)
            await client.add_reaction(reponseText, "😏")
        elif arg == 'gay':
            possible_responses = [
                "https://images.sex.com/images/pinporn/2018/09/17/300/19967673.gif",
                "https://images.sex.com/images/pinporn/2013/08/26/300/3521021.gif",
                "https://18gayteen.com/wp-content/uploads/2018/10/suck.gif",
                "http://boypost.com/wp-content/uploads/2016/01/anal-gay-sex-2_thumb.gif",
                "https://images.sex.com/images/pinporn/2018/06/28/300/19654842.gif",
                "https://www.gayteenlove.com/wp-content/uploads/2018/11/Joey_Mills_and_Justin_Owen_03.gif",
                "https://dl.phncdn.com/gif/7054801.gif",
                "http://101hotguys.com/wp-content/uploads/2018/11/horseman_04.gif",
                "https://dl.phncdn.com/gif/1469161.gif",
                "https://allfreegaycams.com/wp-content/uploads/gif/762.gif",
                "http://101hotguys.com/wp-content/uploads/2019/04/Kamasutra_gay_Blowjob_05.gif",
                "https://img-hw.xvideos.com/videos/profiles/galleries/3c/ce/c9/mariano_arg/gal1595157/pic_4_big.gif",
                "https://images.sex.com/images/pinporn/2015/10/25/300/14136687.gif",
                "http://www.reuni.eu/image/1c7054ca451ddcf8b0d5b63a273fa12b.gif",
                "https://18gayteen.com/wp-content/uploads/2018/12/cumming_twinks_04.gif",
                "http://101hotguys.com/wp-content/uploads/2018/03/ride_that_pony_09.gif",
                "http://porn-twinks.com/gif/11.gif",
                "https://78.media.tumblr.com/90c0508916e1aa6e033e56a8e7fa16f4/tumblr_mzg1tlQmZM1rntnuzo1_500.gif",
                "https://milliondicks.com/pics/t/s-215575.gif",
                "https://18gayteen.com/wp-content/uploads/2018/12/perfect_twinks_03.gif",
                "http://boypost.com/wp-content/uploads/2015/11/gay-fuck-gifs-2.gif",
                "http://www.queermenow.net/blog/wp-content/uploads/2015/12/Angel-Cruz-Hands-Free-Cumshot-Gay-Porn.gif",
                "https://www.gayteenlove.com/wp-content/uploads/2018/11/twink_cum_09.gif",
                "http://gaybf.com/wp-content/uploads/1-15.gif",
                "http://xxxpicss.com/xxx/twink-teen-gay-porn-gifs.gif",
                "https://31.media.tumblr.com/0d8172c174dc396a56384ddb7193e613/tumblr_mltrogaMgr1s70wu3o1_400.gif",
                "http://25.media.tumblr.com/tumblr_md76s6SOmY1rdxa6to1_500.gif",
                "https://www.gayteenlove.com/wp-content/uploads/2018/11/Joey_Mills_and_Justin_Owen_04.gif",
                "http://porn-twinks.com/gif/18.gif",
                "http://www.reuni.eu/image/936291.gif",
                "https://1.bp.blogspot.com/-s7YUewbfWi4/WdBAtM0go9I/AAAAAAAAPpM/N-5eR8Yqux86JYzl2XsoHNZVa8j5oLRYgCLcBGAs/s1600/40tumblr_nxclsnHB3o1tkgd2to1_500.gif"
                "https://allfreegaycams.com/wp-content/uploads/gif/347.gif"
                ]
            embed = discord.Embed(title="NSFW • gay", color=0xed9ce7)
            embed.set_image(url=random.choice(possible_responses))
            embed.set_footer(text="NSFW")
            reponseText = await client.send_message(getchannel, embed=embed)
            await client.add_reaction(reponseText, "😏")
        elif arg == 'biffle' or arg == 'bifle' or arg == 'bifflette':
            possible_responses = [
                "http://www.biffle.fr/wp-content/uploads/2014/09/35.gif",
                "http://www.biffle.fr/wp-content/uploads/2014/09/29.gif",
                "http://25.media.tumblr.com/e4f8018c9e4de17c0cf4035b5aefcddd/tumblr_mzzvczwZbR1rmjat4o1_400.gif",
                "http://www.biffle.fr/wp-content/uploads/2014/09/34.gif",
                "https://www.coquinetv.com/admin/uploads/articles/552611507860699.gif",
                "http://www.biffle.fr/wp-content/uploads/2014/09/47.gif",
                "http://www.biffle.fr/wp-content/uploads/2014/09/3.gif",
                "http://www.biffle.fr/wp-content/uploads/2014/09/48.gif",
                "https://buzzporn.net/wp-content/uploads/2013/10/biffle.gif",
                "http://www.biffle.fr/wp-content/uploads/2014/09/49.gif",
                "http://choualbox.com/Img/20120517230150C.gif",
                "https://images.sex.com/images/pinporn/2019/02/01/300/20622515.gif",
                "http://images-fanta.i.m.pic.centerblog.net/3aea9a4e.gif",
                "http://www.biffle.fr/wp-content/uploads/2014/09/44.gif",
                "http://choualbox.com/Img/20130311011842Q.gif",
                "https://www.top-x-porn.com/photos/galleries/Porno/Bifle/gif/jeune_brune_bifle_biflette_pov_visage.gif",
                "http://www.biffle.fr/wp-content/uploads/2014/09/55.gif",
                "https://www.top-x-porn.com/photos/galleries/Porno/Bifle/gif/biflette_grosse_bite_jeune_rousse.gif",
                "http://lenaty.fr/actu-sexy/wp-content/uploads/2014/08/bifle.gif",
                "https://www.top-x-porn.com/photos/galleries/Porno/Bifle/gif/jeune_blonde_bifle_avec_grosse_bite_de_blanc.gif",
                "http://www.biffle.fr/wp-content/uploads/2014/09/51.gif",
                "http://choualbox.com/Img/20130416125456F.gif",
                "http://images-fanta.i.m.pic.centerblog.net/2afa47fc.gif",
                "https://www.top-x-porn.com/photos/galleries/Porno/Bifle/gif/belle_bifle_jeune_pornstar_brune.gif",
                "https://www.top-x-porn.com/photos/galleries/Porno/Bifle/gif/biflette_pov_jeune_pornstar_brunette.gif",
                "https://www.top-x-porn.com/photos/galleries/Porno/Bifle/gif/bifle_interracial_pov_grosse_bite_black_pornstar_brune.gif",
                "http://images-fanta.i.m.pic.centerblog.net/bf01fa24.gif",
                "http://www.biffle.fr/wp-content/uploads/2014/09/12.gif",
                "https://www.top-x-porn.com/photos/galleries/Porno/Bifle/gif/jeune_ebony_biflette_grosse_bite.gif",
                "http://www.biffle.fr/wp-content/uploads/2014/09/52.gif",
                "http://biteenfeu.b.i.pic.centerblog.net/17993892.gif",
                "http://biteenfeu.b.i.pic.centerblog.net/FA_Massive_1.gif",
                "http://www.biffle.fr/wp-content/uploads/2014/09/38.gif",
                "http://images-fanta.i.m.pic.centerblog.net/2d7dd447.gif",
                "http://www.biffle.fr/wp-content/uploads/2014/09/30.gif",
                "https://www.top-x-porn.com/photos/galleries/Porno/Bifle/gif/une_bifle_en_ejaculant.gif",
                "https://thumb-p1.xhcdn.com/a/EFg2sH-VXUPXKvUwMkRSVQ/000/185/368/361_1000.gif",
                "http://biteenfeu.b.i.pic.centerblog.net/tumblr_odkm6zBFWM1ux33qko1_500.gif",
                "http://www.biffle.fr/wp-content/uploads/2014/09/25.gif",
                "https://www.xpin.fr/wp-content/uploads/2017/06/Lyc%C3%A9enne-sexy-se-fait-bifler-le-visage-plein-de-sperme-300x253.gif"
                ]
            embed = discord.Embed(title="NSFW • biffle", color=0xed9ce7)
            embed.set_image(url=random.choice(possible_responses))
            embed.set_footer(text="NSFW")
            reponseText = await client.send_message(getchannel, embed=embed)
            await client.add_reaction(reponseText, "😏")
        else:
            embed = discord.Embed(title="Mauvaise commande NSFW • Liste des commandes", color=0xed9ce7)
            embed.add_field(name='Liste des catégories : (15)', value="(en *italique* son les categories alias)\n`anal` *ass* *sodomie*\n`biffle` *biflette*\n`bdsm` *bondage*\n`boobs` *seins*\n`ciseaux` *scissors* *scissor* *ciseau*\n`dick` *bite* *teub*\n`facial` *cumshot*\n`fist` *poing*\n`gay`\n`hentai` *anime*\n`nude` *snap* *snapchat*\n`poils` *poil* *fur* *hairiness* *pilosity*\n`pussy` *vagin* *vagina* *minou* *chatte*\n`squirt`\n`69`", inline=False)
            embed.set_footer(text="NSFW")
            reponseText = await client.send_message(getchannel, embed=embed)
    else:
        await client.send_typing(getchannel)
        await asyncio.sleep(1)
        embed = discord.Embed(title="Tu ne peux pas utiliser cette commande ici !", color=0xf85a5f)
        embed.set_image(url='https://wi-images.condecdn.net/image/Dkja0z33Xve/crop/1020/f/18plus.jpg')
        embed.set_footer(text="Rend toi dans le salon NSFW")
        reponseText = await client.send_message(getchannel, embed=embed)
        await client.add_reaction(reponseText, "🔞")

@cube.error
async def cube_error(ctx, error):
    channel = ctx.message.channel
    embed = discord.Embed(title="essayez : ars cube {NOMBRE}", color=0xf85a5f)
    embed.set_author(name='Erreur')
    embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
    embed.set_footer(text="Il manque quelque chose..")
    reponseText = await client.send_message(channel, embed=embed)
    await client.add_reaction(reponseText, "✖")

@carre.error
async def carre_error(ctx, error):
    channel = ctx.message.channel
    embed = discord.Embed(title="essayez : ars carre {NOMBRE}", color=0xf85a5f)
    embed.set_author(name='Erreur')
    embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
    embed.set_footer(text="Il manque quelque chose..")
    reponseText = await client.send_message(channel, embed=embed)
    await client.add_reaction(reponseText, "✖")

@plus.error
async def plus_error(ctx, error):
    channel = ctx.message.channel
    embed = discord.Embed(title="essayez : ars plus {NOMBRE} {NOMBRE}", color=0xf85a5f)
    embed.set_author(name='Erreur')
    embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
    embed.set_footer(text="Il manque quelque chose..")
    reponseText = await client.send_message(channel, embed=embed)
    await client.add_reaction(reponseText, "✖")

@moins.error
async def moins_error(ctx, error):
    channel = ctx.message.channel
    embed = discord.Embed(title="essayez : ars moins {NOMBRE} {NOMBRE}", color=0xf85a5f)
    embed.set_author(name='Erreur')
    embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
    embed.set_footer(text="Il manque quelque chose..")
    reponseText = await client.send_message(channel, embed=embed)
    await client.add_reaction(reponseText, "✖")

@echo.error
async def echo_error(ctx, error):
    channel = ctx.message.channel
    embed = discord.Embed(title="essayez : ars echo {TEXT}", color=0xf85a5f)
    embed.set_author(name='Erreur')
    embed.set_image(url='https://www.elegantthemes.com/blog/wp-content/uploads/2016/03/500-internal-server-error-featured-image-1.png')
    embed.set_footer(text="Il manque quelque chose..")
    reponseText = await client.send_message(channel, embed=embed)
    await client.add_reaction(reponseText, "✖")

async def my_background_task():
    client.change_presence(game=discord.Game(name=next(status)))
    await asyncio.sleep(600)

client.run(TOKEN)