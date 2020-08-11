# critGenBot
A Python driven Discord bot that will announce or whisper the results of either a critical hit or critical miss.
critically, the .env file is missing, which contains the bot's token as well as channel ids

Hits and misses are rolled with the following syntax:
!hit
!HIT
!Hit
!HiT
!miss
!MISS
!Miss
!mISs

the roll will be direct messaged to the roller if the word "whisper" is used:
whisper !hit
!MISS WHISPER

The bot can be told to terminate with the following commands:
!goodbye
!bye
