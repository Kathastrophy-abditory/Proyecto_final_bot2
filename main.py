import discord
from discord.ext import commands
import random
import os
import requests 
from noticias import una_noticia_solar

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def en_linea(ctx):
    print(f'Tu bot {bot.user} esta en linea')

@bot.command("hola")
async def hola(ctx):
    await ctx.send("Hola! Soy El gato informador de noticias sobre energías renovables. Estoy aqui para informar sobre el cambio climatico y las energías limpias, escribe !comandos para ver lo que puedo hacer!")
    await ctx.send(file=discord.File(r"C:\Users\katea\OneDrive\Escritorio\Python Pro\Proyecto_final_bot\images\dancing.gif"))

@bot.command("comandos")
async def comandos(ctx):
    await ctx.send("Estos son los comandos que puedes usar:\n!noticias_solar - Noticias sobre energía solar\n!definicion - Definición de cambio climático")
    await ctx.send(file=discord.File(r"C:\Users\katea\OneDrive\Escritorio\Python Pro\Proyecto_final_bot\images\typing.gif"))

@bot.command("definicion")
async def definicion(ctx):
    await ctx.send("El cambio climático es una alteración significativa y duradera de los patrones climáticos de la Tierra, principalmente un aumento de la temperatura promedio global, causado en gran medida por actividades humanas desde el siglo XIX, como la quema de combustibles fósiles (carbón, petróleo, gas) y la deforestación. ")
    await ctx.send(file=discord.File(r"C:\Users\katea\OneDrive\Escritorio\Python Pro\Proyecto_final_bot\images\cambioclimatico.jpg"))

@bot.command("noticias_solar")
async def noticias_solar(ctx):
    noticia = una_noticia_solar()
    titulo = noticia["titulos_noticias"]
    enlace = noticia["enlaces"]
    fecha = noticia["fecha_publicacion"]
    await ctx.send("Aquí tienes una noticia reciente sobre energía solar!")
    await ctx.send(f"**Título:** {titulo}\n**Enlace:** {enlace}\n**Fecha de publicación:** {fecha}")

@bot.command("noticias_eolica")
async def noticias_eolica(ctx):
    noticia = una_noticia_eolica()
    titulo = noticia["titulos_noticias"]
    enlace = noticia["enlaces"]
    fecha = noticia["fecha_publicacion"]
    await ctx.send("Aquí tienes una noticia reciente sobre energía eólica!")
    await ctx.send(f"**Título:** {titulo}\n**Enlace:** {enlace}\n**Fecha de publicación:** {fecha}")

token = ""

bot.run(token)