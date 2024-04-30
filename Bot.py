import datetime
import discord
from discord.ext import commands
import random
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("The bot is now online to booli ya all, sorry. ")  # Corrected grammar and added emoji

@bot.command()
async def hello(ctx):
    username = ctx.message.author.mention
    # Delete the triggering command message (ctx.message)
    
    await ctx.message.delete()
    await ctx.send(f"Hello there! I'm a custom bot made by Spig. {username}")  # Improved formatting

@bot.command()
@commands.has_role("Admin")
async def ban(ctx, member: discord.Member, *, reason=None):  # Set reason as optional
    if reason is None:
        reason = f"This user was banned by {ctx.message.author.name}."
    await member.ban(reason=reason)
    # Delete the triggering command message (ctx.message)
    
    await ctx.message.delete()
    await ctx.send(f"**{member.name}** has been banned.")  # Confirmation message

@bot.command()
@commands.has_role("Admin")
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason is None:
        reason = f"This user was kicked by {ctx.message.author.name}."
    await member.kick(reason=reason)
        # Delete the triggering command message (ctx.message)
    
    await ctx.message.delete()
    await ctx.send(f"**{member.name}** has been kicked.")  # Confirmation message

@bot.command()
async def mute(ctx, member: discord.Member, timelimit: str):
    time_unit = timelimit.lower().strip()[-1:]  # Extract time unit (s, m, h)
    if time_unit not in ("s", "m", "h"):  # Validate time unit
        await ctx.send("Invalid time unit. Use 's' for seconds, 'm' for minutes, or 'h' for hours.")
        return

    try:
        time_value = int(timelimit.strip(time_unit))  # Extract numerical value
    except ValueError:
        await ctx.send("Invalid time limit. Please enter a valid number.")
        return

    # Calculate timeout based on time unit and Discord's limit
    max_timeout = 241900  # 28 days in seconds (Discord's limit)
    timeout = min(time_value * (60 if time_unit == "m" else (3600 if time_unit == "h" else 1)), max_timeout)

    await member.edit(timed_out_until=discord.utils.utcnow() + datetime.timedelta(seconds=timeout))
    # Delete the triggering command message (ctx.message)
    
    await ctx.message.delete()
    await ctx.send(f"**{member.name}** skill issue you bitchass nigga go fuck your ownself with that castrated imaginary dick of yours you fucking nigga and enjoy stroking you dickless ego for {timelimit}.")  # Confirmation message

@bot.command()
@commands.has_role("Admin")
async def unmute(ctx, member: discord.Member):
  try:
    # Attempt to remove timed_out_until attribute to unmute
    await member.edit(timed_out_until=None)
    await ctx.send(f"**{member.name}** has been unmuted.")
  except discord.HTTPException as e:
    # Handle potential errors (e.g., user not muted)
    await ctx.send(f"An error occurred trying to unmute {member.name}. Maybe they are not muted already?")

# Delete the triggering command message (ctx.message)
    
  await ctx.message.delete()

@bot.command()
@commands.has_role("Admin")  # Adjust this to your desired permission role
async def warn(ctx, member: discord.Member, *, reason=None):
  """Warns a user and sends them a DM with the reason."""
  if reason is None:
    reason = "No reason provided."

  # Send DM to warned user
  try:
    await member.send(f"You have been warned on {ctx.guild.name} for: {reason}")
  except discord.HTTPException as e:
    # Handle potential errors (e.g., unable to DM)
    await ctx.send(f"Failed to send DM to {member.name}. Maybe their DMs are closed?")
# Delete the triggering command message (ctx.message)
    
  await ctx.message.delete()
  # Send confirmation message in channel
  await ctx.send(f"**{member.name}** has been warned for: {reason}")

@bot.command(name="gayrate")
async def gayrate(ctx, member: discord.Member=None):
  """Returns a random 'gay rate' for a user (for fun, not to be taken seriously)."""
  if member is None:
    member = ctx.author  # Default to the user who invoked the command

  # Generate random number between 0 and 100
  gay_rate = random.randint(0, 100)
# Delete the triggering command message (ctx.message)
    
  await ctx.message.delete()
  # Respond with a funny message
  await ctx.send(f"️‍ {member.name}'s Gay Rate: **{gay_rate}%** ️‍ (you gay ass faggot go breed ur sorry ass)")

import random
import asyncio  # Import for potential asynchronous operations
import requests  # Import for making HTTP requests

@bot.command()
async def insult(ctx):
    """Returns a random insult for comedic purposes (avoiding repeats)."""

    # Define a fallback insult for cases where external source is unavailable
    fallback_insult = "Looks like the insult generator is taking a nap."

    # Responsible Scraping Example (replace with your preferred method)
    # This example demonstrates basic scraping principles, but keep in mind:
    #  - Always respect robots.txt and website terms of service.
    #  - Consider alternative approaches like APIs if available.
    async def get_insult_from_website():
        url = "http://www.robietherobot.com/insult-generator.htm"  # Replace with your chosen URL
        headers = {
            "User-Agent": "Discord Insult Bot (your_username#your_discriminator)"  # Identify your bot
        }
        try:
            async with requests.get(url, headers=headers) as response:
                if response.status_code == 200:
                    # Parse the HTML to extract the insult (replace with your parsing logic)
                    # This is a simplified example, you might need more complex parsing
                    soup = BeautifulSoup(response.content, 'html.parser')
                    insult_element = soup.find('div', class_='insult')  # Adjust selectors as needed
                    if insult_element:
                        return insult_element.text.strip()
                    else:
                        return fallback_insult  # Fallback if insult element not found
                else:
                    return fallback_insult  # Fallback on error
        except Exception as e:
            print(f"Error retrieving insult from website: {e}")
            return fallback_insult

    # Try to get insult from website or use fallback
    try:
        insult = await get_insult_from_website()
    except Exception as e:  # Catch potential errors from scraping or other sources
        print(f"Error retrieving insult: {e}")
        insult = fallback_insult

    # Implement logic to track used insults (using a set)
    used_insults = set()
    while True:
        if insult not in used_insults:  # Check if insult has been used
            break
        used_insults.add(insult)  # Add used insult to the set
        # If using an external source, you might need to fetch a new insult here

    # Send the insult message
    await ctx.send(f"{insult}")

# ... other necessary imports

intents = discord.Intents.default()  # Use default intents (recommended)

client = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='announce') # Consider a more descriptive name like "!announce"
async def announce_command(ctx, *, message):  # Use *message to capture everything after the command
    # Check if user has Administrator permission (optional)
    if not ctx.author.guild_permissions.administrator:  # Uncomment this line if you want permission check
        await ctx.send("You don't have permission to use this command.")
        return

    # Construct the announcement message with ping
    announcement = f"@everyone {message}"
# Delete the triggering command message (ctx.message)
    await ctx.message.delete()
    await ctx.send(announcement)

@bot.command(name='helpmenu')
async def helpmenu_command(ctx, *,message):
    await ctx.message.delete()
    await ctx.send("current commands the bot can run are hello, Mute, Unmute, Ban, Unban, gayrate, Insult, Announce,")

@bot.command(name='phoenix')
async def phoenix(ctx):
   await ctx.message.delete()
   await ctx.send(f"phoenix is the biggest WOS (a roblox game) based Gang known in Asia, some of the things that best describes the gang is activeness, robux gaws, most rare in game items etc gaws, one of the oldest yet strongest gang, frequent tournaments with big prizes")
   
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


frozen_users = {}

@bot.command(name='nickfreeze')
@commands.has_permissions(administrator=True)
async def nickfreeze(ctx, member: discord.Member, *, nick):
    """Freeze a user's nickname"""
    frozen_users[member.id] = nick
    await member.edit(nick=nick)
    ctx.send(f"Nickname of {member.mention} has been frozen to {nick}.")

@tasks.loop(seconds=2)
async def check_nicknames():
    """Check if frozen nicknames have been changed"""
    for guild in bot.guilds:
        for member_id, nick in frozen_users.items():
            member = guild.get_member(member_id)
            if member and member.nick != nick:
                await member.edit(nick=nick)

@bot.event
async def on_ready():
    """Start the task when the bot is ready"""
    check_nicknames.start()

    
# Ensure your bot token is replaced with a valid one (removed for security
bot.run()
