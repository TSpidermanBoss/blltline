from pyrogram import Client, Filters
from pyrogram.errors import FloodWait
import time
app = Client("del",728044,"a41ddadc9696482aff94a4b37221574a")
s = -1001262096355
d = -1001378725482
@app.on_deleted_messages(Filters.chat(s))
def main(client, messages):
 for v in messages:
  file = open("sure.txt" , "r")
  lines = file.readlines()
  file.close()
  for line in lines:
   x = line.split()
   id = str(v.message_id )
   if id in x:
    try:
     client.delete_messages(d,int(x[x.index(id)+1]))
    except FloodWait as e:
     time.sleep(e.x)
app.run()
