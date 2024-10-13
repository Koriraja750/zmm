#!/usr/bin/env python3
try:
    from pyrogram import Client
except Exception:
    print("\nInstall Pyrogram and try again: pip3 install pyrogram --break-system-packages")
    exit(1)

print("Get your app creds from https://my.telegram.org/apps and enter them below.")
API_KEY = int(input("22787559"))
API_HASH = input("e771139d8f3d4ae57f663ad049bbb710")
PHONE_NO = input("+48884789769")

with Client(
    name="ZEE",
    in_memory=True,
    api_id=API_KEY,
    api_hash=API_HASH,
    phone_number=PHONE_NO,
    app_version="@Z_Mirror Session",
    device_model="@Z_Mirror Bot",
    system_version="@Z_Mirror Server",
) as app:
    app.send_message("me",
                     "**Pyrogram Session String**:\n\n"
                     f"||{app.export_session_string()}||\n\n"
                     "**Do not share this anywhere!**\n\n"
                     "**Generated by @Z_Mirror**"
                     )
    print(
        "Your Pyrogram session string has been sent to "
        "Saved Messages of your Telegram account!"
    )