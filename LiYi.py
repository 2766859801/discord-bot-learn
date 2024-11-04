import discord
import os
from dotenv import load_dotenv

load_dotenv()


class MyClient(discord.Client):
  async def on_ready(self):
    print(f'Logged in as {self.user} (ID: {self.user.id})')
    print('------')


  async def on_message(self,message):
    if message.author.id == self.user.id:
      return
    if message.content.startswith('你好'):
      await message.reply('Hello，User！',mention_author=True)


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(os.getenv('TOKEN'))
