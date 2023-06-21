import discord

class Paginator(discord.ui.View):
    def __init__(self, pages: list[discord.Embed]):
        super().__init__()
        self.page = 0
        self.pages = pages

    @discord.ui.button(label="Previous", row=0, style=discord.ButtonStyle.secondary)
    async def prev_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.page > 0:
            self.page -= 1
            await interaction.response.edit_message(f"Showing result {self.page} of {self.pages}", embed=self.pages[self.page])
        else:
            pass

    @discord.ui.button(label="Next", row=0, style=discord.ButtonStyle.secondary)
    async def next_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.page < len(self.pages) - 1:
            self.page += 1
            await interaction.response.edit_message(f"Showing result {self.page} of {self.pages}", embed=self.pages[self.page])
        else:
            pass