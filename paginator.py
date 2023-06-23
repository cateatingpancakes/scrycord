import discord


class Paginator(discord.ui.View):
    def __init__(self, pages: list[discord.Embed]):
        super().__init__()
        self.page = 0
        self.pages = pages

    
    @discord.ui.button(label="Previous", style=discord.ButtonStyle.secondary, row=0)
    async def previous_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.page > 0:
            self.page -= 1
            await interaction.response.edit_message(embed=self.pages[self.page])
        else:
            await interaction.response.edit_message(embed=self.pages[0])

    
    @discord.ui.button(label="Next", style=discord.ButtonStyle.secondary, row=0)
    async def next_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.page < len(self.pages) - 1:
            self.page += 1
            await interaction.response.edit_message(embed=self.pages[self.page])
        else:
            await interaction.response.edit_message(embed=self.pages[0])
