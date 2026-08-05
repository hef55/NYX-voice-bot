import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ضع هنا معرف (ID) الروم الصوتي الخاص بك
VOICE_CHANNEL_ID = 123456789012345678  

@bot.event
async def on_ready():
    print(f'تم تشغيل البوت بنجاح: {bot.user}')
    channel = bot.get_channel(VOICE_CHANNEL_ID)
    if channel and isinstance(channel, discord.VoiceChannel):
        try:
            await channel.connect()
            print(f"البوت دخل الروم الصوتي: {channel.name}")
        except Exception as e:
            print(f"خطأ أثناء دخول الروم: {e}")

# جلب التوكن بشكل آمن من البيئة المحيطة
bot.run(os.environ.get('TOKEN'))
