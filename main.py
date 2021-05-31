import discord
import os
from replit import db


my_secret = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
  print('Jarvis is ready')

@client.event
async def on_message(msg):
  key = msg.content.split('$',1)[1]
  print(key)
  if msg.author == client.user:
    return
  if msg.content.startswith('$new'): #Only the author is allowed to add new keys
    if msg.author.id == 733579039637504030:  #Checking if the author is who he is claiming to be
      extract = msg.content.split("$new",1)[1]
      key = extract.split()
      db[key[0]] = key[1]
      await msg.channel.send('New Coin-Address pair added to the database')
    else:
      await msg.channel.send('Not allowed to add new coins!')

  if msg.content.startswith('$delete'): #Only the author is allowed to delete
    if msg.author.id == 733579039637504030: #Checking if the author is who he is claiming to be
      extract = msg.content.split('$delete ',1)[1]
      if extract in db.keys():
        del db[extract]
        await msg.channel.send("Key deleted!")
      else:
        await msg.channel.send("Key does not exist!")
    else:
      await msg.channel.send("Not allowed to Delete the key!")
  
  if msg.content.startswith('$list'):
    response = str(db.keys())
    await msg.channel.send('Here are the coins that Jarvis has stored with him: ' + response)

  if msg.content.startswith('$help'):
    response = 'Hi there! I am just a bot. Do not fall for my sweet words but fall for my sweet efforts. Please use the $help command to know what I can do. Use the $new command to add new coin-address pair. Use the $list command to check the list of coins I have. Use the %<coin name> to get the coin'
    await msg.channel.send(response)

  else:
    await msg.channel.send('Please send funds to the address: ' + db[key])

  
client.run(my_secret)

