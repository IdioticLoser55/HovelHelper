import discord

# opens a file as readonly to obtain the token.
token = open("token.txt", "r").read()

# Stars the discord client
client = discord.Client()


# function to find out external IP.
async def whatsMyIP(message):
    # need this to do what its actually supposed to do.
    await message.channel.send(f"```Hello```")


COMMANDS = {
    "ip": whatsMyIP
}


@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/. Basically makes the following function as if it has been declared inside of the function event.
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.

@client.event
async def on_message(message):  # event that happens per any message.
    if(message.content[0] == "?"):
        # Need to check or have some try catch for empty ones.
        # Also the ones that don't have a match.
        await COMMANDS[message.content[1:len(message.content)]](message)

    # each message has a bunch of attributes. Here are a few.
    # check out more by print(dir(message)) for example.
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")




client.run(token)  # recall my token was saved!
