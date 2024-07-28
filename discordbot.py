import discord
from discord.ext import commands
from interfaces import InterfazDiscord
from credenciales import *


class Bot:
    def __init__(self):
        self.api = InterfazDiscord()
        self.iniciar_servicios()
        self.run()

    def run(self):
        self.bot.run(TOKEN_DISCORD_BOT)

    def iniciar_servicios(self):
        '''@self.bot.command(aliases=['t','te'])
        async def test(ctx, *args):
            arguments = ', '.join(args)
            await ctx.send(f'{len(args)} arguments: {arguments}', file=discord.File('ruta/'))'''
        
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix='.', intents=intents)

        @self.bot.event
        async def on_ready():
            print(f'Iniciada sesion de {self.bot.user}')

        @self.bot.command(aliases=['dolar'])
        async def precio_dolar(ctx, *args):
            await ctx.send(content=(self.api.precio_del_dolar(ctx, *args))['mensaje'])

        @self.bot.command(aliases=['fortnite'])
        async def precio_pase_fortnite(ctx, *args):
            await ctx.send(content=(self.api.precio_del_pase_fortnite(ctx, *args))['mensaje'])

        @self.bot.command(aliases=['mc', 'mcserver', 'minecraft'])
        async def minecraft_server_status(ctx, *args):
            await ctx.send(content=(self.api.minecraft_server_status(ctx, *args))['mensaje'])

        @self.bot.command(aliases=['iniciarmc'])
        async def iniciar_minecraft_server(ctx, *args):
            await ctx.send(content=(self.api.iniciar_minecraft_server(ctx, *args))['mensaje'])

        @self.bot.command(aliases=['ashee', 'asheee', 'buenardo', 'polimardo', 'pesuti', 'buenardopolis'])
        async def mensajovich(ctx, *args):
            await ctx.send(content=(self.api.mensajovich(ctx, *args))['mensaje'])

        @self.bot.command(aliases=['files', 'files_server'])
        async def iniciar_files_server(ctx, *args):
            await ctx.send(content=(self.api.iniciar_files_server(ctx, *args))['mensaje'])

Bot()
