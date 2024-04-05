
import discord
import os
import asyncio
import datetime
import pytz
import requests
from discord.ext import commands
import sqlite3
from key_generator.key_generator import generate


connection = sqlite3.connect("database.sqlite")
print(connection.total_changes)
cursor = connection.cursor()







client = commands.Bot(
    command_prefix='$',
    intents=discord.Intents.all()

    










client.run(os.enviorn("TOKEN"))
connection.close()