from telethon.sync import TelegramClient


api_id = 1293277
api_hash = "13c33b0243b9c6f21e5b435763738924"

with TelegramClient("session_name", api_id, api_hash) as client:
    participants = client.get_participants("chat_or_channel_name")
    for participant in participants:
        print(participant.username)

with TelegramClient("session_name", api_id, api_hash) as client:
    client.send_message("username_or_chat", "Hello! This is a test message.")
