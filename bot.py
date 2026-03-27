import asyncio
from telethon import TelegramClient, events

# ============= YOUR CREDENTIALS =============
api_id = 34744950
api_hash = '84c70ffa1be13540ac8f3116360f9024'
phone = '+923194790108'  # ⚠️ Apna phone number with country code daalein

# ============= SOURCE & DESTINATION =============
source_group = '@mrchandiootpgroup'
destination_group = '@SMS_RECIVED'

# ============= SCRIPT =============
print("🤖 Starting Telegram Forwarder...")
print(f"📡 Source: {source_group}")
print(f"📤 Destination: {destination_group}")

client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(chats=source_group))
async def forward_messages(event):
    try:
        if not event.out:
            message_text = event.message.text or "📎 Media"
            await client.send_message(destination_group, message_text)
            print(f"✅ Forwarded: {message_text[:50]}...")
    except Exception as e:
        print(f"❌ Error: {e}")

async def main():
    await client.start(phone=phone)
    me = await client.get_me()
    print(f"✅ Logged in as: {me.first_name} (@{me.username})")
    print("🚀 Bot is running! Waiting for messages...\n")
    await client.run_until_disconnected()

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("\n🛑 Bot stopped")
    finally:
        loop.close()
