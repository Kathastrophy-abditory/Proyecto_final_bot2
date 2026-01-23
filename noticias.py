from bs4 import BeautifulSoup
import requests
import pandas as pd
import random

def noticias_energia_solar():
    dict_news_02 = {
        "titulos_noticias": [],
        "enlaces": [],
        "fecha_publicacion": []
    }

    # Guardamos en la variable 'url' la dirección del sitio web del que queremos sacar las noticias.
    url = "https://www.xataka.com/tag/energia-solar"

    # Usamos la librería 'requests' para enviar una solicitud a la página y obtener su contenido.
    response = requests.get(url)

    # Usamos BeautifulSoup para poder leer y analizar el código HTML de la página.
    # El segundo argumento "lxml" es el tipo de analizador (parser) que usaremos, es rápido y eficiente.
    bs = BeautifulSoup(response.text, "lxml")

    # Buscamos todos los artículos que están dentro de etiquetas <article> con clases específicas.
    # Estas clases ayudan a identificar las noticias más recientes.
    temp = bs.find_all('article', class_="recent-abstract abstract-article")

    # Recorremos cada artículo encontrado en la página.
    for post in temp:
        # Extraemos el enlace (URL) de la noticia. Está dentro de una etiqueta <a>, que a su vez está en un <h2>.
        dict_news_02["enlaces"].append(post.h2.a.get("href"))

        # Extraemos el título de la noticia (el texto que está dentro de la etiqueta <a>).
        dict_news_02["titulos_noticias"].append(post.h2.a.text)

        # Extraemos la fecha de publicación. Está dentro de una etiqueta <time> con un atributo 'datetime'.
        # Usamos [0:10] para quedarnos solo con la fecha (formato AAAA-MM-DD), sin la hora.
        dict_news_02["fecha_publicacion"].append(post.time.get("datetime")[0:10])

    # Convertimos el diccionario con los datos recolectados en un DataFrame usando la librería pandas.
    # Esto nos permite ver la información organizada como una tabla con columnas.
    df_news_02 = pd.DataFrame(dict_news_02, columns=["titulos_noticias", "enlaces", "fecha_publicacion"])

    # El DataFrame resultante.
    return df_news_02

def una_noticia_solar():
    df = noticias_energia_solar()
    
    if not df.empty:
        df_10 = df.head(10)
        indice_random = random.choice(df_10.index)
        return df_10.loc[indice_random]
    


def noticias_energia_eolica():
    dict_news_02 = {
        "titulos_noticias": [],
        "enlaces": [],
        "fecha_publicacion": []
    }

    # Guardamos en la variable 'url' la dirección del sitio web del que queremos sacar las noticias.
    url = "https://www.xataka.com/tag/energia-solar"

    # Usamos la librería 'requests' para enviar una solicitud a la página y obtener su contenido.
    response = requests.get(url)

    # Usamos BeautifulSoup para poder leer y analizar el código HTML de la página.
    # El segundo argumento "lxml" es el tipo de analizador (parser) que usaremos, es rápido y eficiente.
    bs = BeautifulSoup(response.text, "lxml")

    # Buscamos todos los artículos que están dentro de etiquetas <article> con clases específicas.
    # Estas clases ayudan a identificar las noticias más recientes.
    temp = bs.find_all('article', class_="recent-abstract abstract-article")

    # Recorremos cada artículo encontrado en la página.
    for post in temp:
        # Extraemos el enlace (URL) de la noticia. Está dentro de una etiqueta <a>, que a su vez está en un <h2>.
        dict_news_02["enlaces"].append(post.h2.a.get("href"))

        # Extraemos el título de la noticia (el texto que está dentro de la etiqueta <a>).
        dict_news_02["titulos_noticias"].append(post.h2.a.text)

        # Extraemos la fecha de publicación. Está dentro de una etiqueta <time> con un atributo 'datetime'.
        # Usamos [0:10] para quedarnos solo con la fecha (formato AAAA-MM-DD), sin la hora.
        dict_news_02["fecha_publicacion"].append(post.time.get("datetime")[0:10])

    # Convertimos el diccionario con los datos recolectados en un DataFrame usando la librería pandas.
    # Esto nos permite ver la información organizada como una tabla con columnas.
    df_news_03 = pd.DataFrame(dict_news_02, columns=["titulos_noticias", "enlaces", "fecha_publicacion"])

    # El DataFrame resultante.
    return df_news_03

def una_noticia_eolica():
    df = noticias_energia_eolica()
    
    if not df.empty:
        df_10 = df.head(10)
        indice_random = random.choice(df_10.index)
        return df_10.loc[indice_random]

