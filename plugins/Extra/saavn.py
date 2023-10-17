from pyrogram import Client,filters, enums
import requests,os,wget
# from info import CHAT_GROUP, REQST_CHANNEL, SUPPORT_CHAT_ID, ADMINS

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
from info import LOG_CHANNEL
BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('💖🇮🇳✨ Made By ✨🇮🇳💖', url='https://t.me/TeamSugoiX')]])
A = """{} with user id:- {} used /saavn command."""
B = """{} with user id:- {} used /vsaavn command."""

# API = "https://apibu.herokuapp.com/api/y-images?query="

START_MESSAGE = """
𝐇𝐞𝐥𝐥𝐨 <a href='tg://settings'>𝐓𝐡𝐚𝐧𝐤 𝐘𝐨𝐮⚡️</a>

𝐅𝐨𝐫 𝐄𝐱𝐚𝐦𝐩𝐥𝐞 :-
/ssong 𝐀𝐥𝐨𝐧𝐞✔️ =-= 𝐬𝐚𝐚𝐯𝐧 𝐦𝐩𝟑 𝐬𝐨𝐧𝐠
/svideo 𝐀𝐥𝐨𝐧𝐞✔️ =-= 𝐬𝐚𝐚𝐯𝐧 𝐦𝐩𝟒 𝐬𝐨𝐧𝐠
/ysong 𝐀𝐥𝐨𝐧𝐞✔️ =-= 𝐲𝐨𝐮𝐭𝐮𝐛𝐞 𝐦𝐩𝟑 𝐬𝐨𝐧𝐠
/yvideo 𝐀𝐥𝐨𝐧𝐞✔️ =-= 𝐲𝐨𝐮𝐭𝐮𝐛𝐞 𝐦𝐩𝟒 𝐬𝐨𝐧𝐠

/𝐬𝐚𝐚𝐯𝐧 𝐀𝐥𝐨𝐧𝐞 𝐄𝐧𝐠𝐥𝐢𝐬𝐡 ❌️
/𝐯𝐦𝐩𝟒 𝐀𝐥𝐨𝐧𝐞 𝐔𝐧𝐝𝐨❌️
/𝐲𝐬𝐨𝐧𝐠 𝐀𝐥𝐨𝐧𝐞 𝐒𝐨𝐧𝐠❌️
/𝐲𝐯𝐢𝐝𝐞𝐨 𝐀𝐥𝐨𝐧𝐞 𝐍𝐞𝐰❌️
"""

@Client.on_message(filters.command('svideo') & filters.text)
async def video(client, message): 
    try:
       args = message.text.split(None, 1)[1]
    except:
        return await message.reply("/svideo requires an argument.")
    if args.startswith(" "):
        await message.reply("/svideo requires an argument.")
        return ""
    pak = await message.reply('Downloading...')
    try:
        r = requests.get(f"https://saavn.me/search/songs?query={args}&page=1&limit=1").json()
    except Exception as e:
        await pak.edit(str(e))
        return
    r = requests.get(f"https://saavn.me/search/songs?query={args}&page=2&limit=2").json()
    sname = r['data']['results'][0]['name']
    slink = r['data']['results'][0]['downloadUrl'][4]['link']
    ssingers = r['data']['results'][0]['primaryArtists']
#   album_id = r.json()[0]["albumid"]
    img = r['data']['results'][0]['image'][2]['link']
    thumbnail = wget.download(img)
    file = wget.download(slink)
    ffile = file.replace("mp3", "mp4")
    os.rename(file, ffile)
    buttons = [[
        InlineKeyboardButton("JOIN MOVIES", url="https://t.me/Team_Netflix")
    ]]                           
    await message.reply_video(
    video=ffile, caption=f"[{sname}]({r['data']['results'][0]['url']}) - from @Team_Netflix ",thumb=thumbnail,
    reply_markup=InlineKeyboardMarkup(buttons)
)
    await message.reply_text(text="download mp3 song @Team_Netflix")
    os.remove(ffile)
    os.remove(thumbnail)
    await pak.delete()

    await client.send_message(LOG_CHANNEL, B.format(message.from_user.mention, message.from_user.id)) 
    


#    await client.send_message(LOG_CHANNEL, A.format(message.from_user.mention, message.from_user.id)) 
        

@Client.on_message(filters.command('ssong') & filters.text)
async def song(client, message):
    try:
       args = message.text.split(None, 1)[1]
    except:
        return await message.reply("/ssong requires an argument.")
    if args.startswith(" "):
        await message.reply("/ssong requires an argument.")
        return ""
    pak = await message.reply('Downloading...')
    try:
        r = requests.get(f"https://saavn.me/search/songs?query={args}&page=1&limit=1").json()
    except Exception as e:
        await pak.edit(str(e))
        return
    sname = r['data']['results'][0]['name']
    slink = r['data']['results'][0]['downloadUrl'][4]['link']
    ssingers = r['data']['results'][0]['primaryArtists']
  #  album_id = r.json()[0]["albumid"]
    img = r['data']['results'][0]['image'][2]['link']
    thumbnail = wget.download(img)
    file = wget.download(slink)
    ffile = file.replace("mp4", "mp3")
    os.rename(file, ffile)
    await pak.edit('Uploading...')
    await message.reply_audio(audio=ffile, title=sname, performer=ssingers,caption=f"[{sname}]({r['data']['results'][0]['url']}) - from saavn ",thumb=thumbnail)
    os.remove(ffile)
    os.remove(thumbnail)
    await pak.delete()
    await client.send_message(LOG_CHANNEL, A.format(message.from_user.mention, message.from_user.id)) 
    

@Client.on_message(filters.command("song") & filters.group) 
async def r_message(client, message):
    mention = message.from_user.mention
    buttons = [[
        InlineKeyboardButton('𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩', url=f'https://t.me/WeebZoneX')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(START_MESSAGE.format(message.from_user.mention, message.chat.title),
    protect_content=True,
    reply_markup=reply_markup, 
    parse_mode=enums.ParseMode.HTML
  )
