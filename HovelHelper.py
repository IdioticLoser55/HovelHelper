import discord
import subprocess

# opens a file as readonly to obtain the token.
token = open("/home/idiot/HovelHelper/token.txt", "r").read()

# Stars the discord client
client = discord.Client()


# function to find out external IP.
async def whatsMyIP(message):
    # grabs my ip.
    result = subprocess.run(['drill', '-Q', 'myip.opendns.com', '@resolver1.opendns.com'], capture_output=True, text=True).stdout
    # prints my ip.
    await message.channel.send(f"```{result[0:len(result) - 1]}```")


COMMANDS = {
    "ip": whatsMyIP
}


@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/. Basically makes the following function as if it has been declared inside of the function event.
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.

    # Sends a simple startup message.
    channel = client.get_guild(909496426390753280).get_channel(934415946410504242)
    if(channel != None):
        await channel.send(f"```Hello```")

@client.event
async def on_message(message):  # event that happens per any message.
    # prints message and details.
    print(f"{message.guild}: {message.channel}: {message.author}: {message.author.name}: {message.content}")

    if(message.content[0] == "?"):
        # Need to check or have some try catch for empty ones.
        # Also the ones that don't have a match.
        await COMMANDS[message.content[1:len(message.content)]](message)





client.run(token)  # recall my token was saved!
