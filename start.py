import telethon
from telethon import events
@midway.on(events.NewMessage(incoming=True,pattern="/start"))
async def start(started):
  await started.reply("Get LOst!")
