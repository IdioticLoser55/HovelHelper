import discord

#not sure if I need this.
#print(discord.__version__)  # check to make sure at least once you're on the right version!

# opens a file as readonly to obtain the token.
token = open("token.txt", "r").read()

# Stars the discord client
client = discord.Client()


@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/. Basically makes the following function as if it has been declared inside of the function event.
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.


@client.event
async def on_message(message):  # event that happens per any message.

    # each message has a bunch of attributes. Here are a few.
    # check out more by print(dir(message)) for example.
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")


client.run(token)  # recall my token was saved!
