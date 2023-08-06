# Passo a passo do projeto de automação;

# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pandas as pd
import pyautogui as py
import time

# pyautogui.PAUSE -> delay entre as exec
py.PAUSE = 0.7

# abrir o navegador(chrome)
py.press("win")
py.write("chrome")
py.press("enter")

# entrar no link
py.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
py.press("enter")
time.sleep(2)

# selecionar o campo de email
py.click(x=715, y=400)

# Passo 2: Fazer o login
py.write("brbruno082003@gmail.com")
py.press("tab")
py.write("osasco")
py.click(x=684, y=553)

# Passo 3: Importar a base de produtos para cadastrar
tabela = pd.read_csv("produtos.csv")
time.sleep(3)

# Passo 4: Cadastrar um produto e repetir o processo
for linha in tabela.index:
# clicar no campo de código
    py.click(x=683, y=282)
# pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
# preencher o campo
    py.write(str(codigo))
    py.press("tab")
    py.write(str(tabela.loc[linha, "marca"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "tipo"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "categoria"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "preco_unitario"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "custo"]))
    py.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        py.write(str(tabela.loc[linha, "obs"]))
    py.press("tab")
    py.press("enter")

# dar scroll para subir a tela
    py.scroll(5000)

