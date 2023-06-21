import discord

from discord.commands import Option
from paginator import Paginator
from scryfall import call

bot = discord.Bot()


@bot.slash_command(name="ping", description="Returns the bot's latency.")
async def ping(ctx):
    await ctx.respond(f"Pong! The latency is `{round(bot.latency, 3)}` milliseconds.")


@bot.slash_command(name="search", description="Do a Scryfall search.")
async def search(ctx, query: Option(str, "The query, as you would write it on the website.", required=True)):
    cards = call(query)

    if cards is None:
        await ctx.respond("Your query failed due to the Scryfall rate limit, or returned no cards.")
    else:
        embeds = []
        for current, card in enumerate(cards["data"]):
            total = len(cards["data"])

            embed = discord.Embed(
                title=card["name"],
                description=f"Showing result `{current + 1}` of `{total}`.",
            )

            if "card_faces" in card:
                card = card["card_faces"][0]

            embed.set_image(url=card["image_uris"]["png"])
            embeds.append(embed)

        await ctx.respond(embed=embeds[0], view=Paginator(embeds))


with open("token", encoding="utf-8") as file:
    token = file.read()
    bot.run(token)
