# bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
channel1ID = int(os.getenv('CHANNEL1'))
channel2ID = int(os.getenv('CHANNEL2'))
client = discord.Client()
greetings = ['Bite my shiny metal ass!',
             "I'm still alive, baby!",
             "Kill all humans!",
             "critGenBot does not condone the cool cool crime of robbery!"
             ]


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    channel1 = client.get_channel(channel1ID)
    channel2 = client.get_channel(channel2ID)
    await channel1.send(random.choice(greetings))
    await channel2.send(random.choice(greetings))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    hits = ["Ludicrous Maneuver. All allies with Passive Perception 12 get +2 on next roll.",
            "Late Timing. As an immediate action attack the same opponent at disadvantage.",
            "Wide Open. Target incapacitated 1 round. No 1's or 2's on damage die.",
            "Guarded Strike. +2AC for 1 round. No 1's or 2's on damage die.",
            "Savage Chop. Ignore damage resistance. No 1's or 2's on damage die.",
            "Retaliation. As an immediate action attack the same opponent. No1's or 2's on damage die.",
            "Ruthless Assault. Extra damage die.",
            "Defensive Strike. +4 AC for 1 round. Extra damage die.",
            "Traumatic Injury. Ignore damage resistance. Extra damage die.",
            "Victimized. Opponent provokes attacks of opportunity. Extra damage die.",
            "Calamitous Fall. DC 13 DEX save or prone. Extra damage die.",
            "Disoriented. DC 13 CON save or stunned for 1 round. Extra damage die.",
            "Dirt in Eye. DC 13 WIS save or blinded for 1 round. Extra damage die.",
            "Bleeder. 1d6 bleeding damage per round. Extra damage die.",
            "Rout. Attacker has melee advantage and the target has disadvantage for 1round. Extra damage die.",
            "The Gods Have Spoken. Roll twice and take the better result.",
            "Momentum. As an immediate action attack the same opponent. Extra damagedie.",
            "Great Hit. Ignore damage resistance. DoubleDamage.",
            "Inspirational Display. All allies receive advantage on next roll. DoubleDamage.",
            "Vertigo. Drop all items in hand. Knocked back 1d3 squares. DC 15DEX save or prone. Double Damage.",
            "Perplexed Reaction. Target incapacitated 1 round,provokes attacks of opportunity. Double Damage.",
            "...and Stay Down. Prone and stunned 1 round. DC 15 CON save or move halved until rest. Double Damage.",
            "Astute Counter. As an immediate action attack the same opponent with advantage. DoubleDamage.",
            "Impaled. 1d10 bleeding damage per round. Stunned 1 round. TripleDamage.",
            "Conspiracy. The next hit landed on the foe is an automatic critical hit. Blinded 1 round. Triple Damage.",
            "Demoralized. Prone. Stunned 2 rounds. TripleDamage.",
            "Knockout. DC 16 CON save or unconscious. Prone. Stunned 2 rounds. Triple Damage.",
            "Final Strike. DC 18 CON save or die. Prone 1d4 squares back. Stunned 3rounds. QuadrupleDamage.",
            ]
    misses = ["Seppuku.Knocked prone. Disarmed 1d3 squares away. Stunned 2 rounds. Critical hit on self.",
              "Total Failure. Knocked prone. Disarmed 1d3 squares away. Stunned 1 round.  Critical hit on self.",
              "Predictable Parry.Knocked prone. Disarmed. Stunned 1 round. Damage to ally (self).",
              "Bloody Mess.Bleeding 1d6 per round. Disarmed. Stunned 1 round. Damage to self.",
              "Gut Check.Damage to ally (self).  Incapacitated for 1 round.",
              "InYour Face.Damage to self. Incapacitated for 1 round.",
              "Tipping the Scales.Opponent has advantage and attacker has disadvantage for 1 round.",
              "Mighty Disarm.Disarmed 1d6 squares away. Disadvantage 1 round.",
              "Terrible Maneuver.Nearest opponent gets a free attack with advantage as an immediate action.",
              "The Bigger They Are...Knocked back 1d3 squares before falling prone. ",
              "Butterfingers.Disarmed. Disadvantage on next attack roll.",
              "Dropped Guard.Nearest opponent gets a free attack as an immediate action, if possible",
              "Vision Impairment.Blinded 1 round.",
              "Loss of Resolve.The next saving throw in combat automatically fails.",
              "Partial Blow. Half damage to self.",
              "Wide Open.Provoke attack of opportunity from closest melee opponent, if possible.",
              "Poor Karma.The next saving throw in combat is at disadvantage.",
              "Slow to Respond.No bonus action or reaction next round.",
              "Tough Recovery.Go last in initiative next round.",
              "Nothing unusual happens.",
              ]

    whisper_text = f'{client.user} whispered result to {message.author}'
    bye = "Cheese it!"

    if '!hit' in message.content.lower():
        response = random.choice(hits)
        if 'whisper' in message.content.lower():
            await message.author.send(response)
            await message.channel.send(whisper_text)
            print(f'{message.author} whispered a roll\n    ' + response)
        else:
            await message.channel.send(response)
            print(f'{message.author} made a roll\n    ' + response)
    elif '!miss' in message.content.lower():
        response = random.choice(hits)
        if 'whisper' in message.content.lower():
            await message.author.send(response)
            await message.channel.send(whisper_text)
            print(f'{message.author} whispered a roll\n    ' + response)
        else:
            await message.channel.send(response)
            print(f'{message.author} made a roll\n    ' + response)
    elif "!goodbye" or "!bye" in message.content.lower():
        await message.channel.send(bye)
        await client.close()
client.run(TOKEN)
