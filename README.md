## GlasnostBot

A bot made for forwarding Oulun Tietoteekkarit ry Telegram announcements from OTiT Glasnost to their Discord server.

All shorter than 2000 character messages, including forwards, are supported and copied from Telegram to Discord. 
Forwarded messages include name of the original message sender:

Forward from individual user. `prefer_username` option exists for users that have one 

![Forward from user](images/forward_example.PNG)

Forward from a channel. Channel title is used by default.

![Forward from channel](images/forward_example2.PNG)

The telegram library used in this bot is also made by me and has its own repository 
[telegram.py](https://github.com/Visperi/telegram.py).

## TODO
Non-exhaustive list of features still needed for stable support:

- Support messages over length of 2000 characters
- Support replies to old forwarded messages by replying them directly
- Support attachments in messages
    - In edited messages support attachment deletion

## Licence

MIT Licence

Full licence: [LICENCE](LICENCE)
