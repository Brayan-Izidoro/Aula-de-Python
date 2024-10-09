# Passo 1: Entrar no sistema da empresa: "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# no terminal: pip install pyautogui
import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.click -> clicar com o mouse
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> aperta um atalho de teclado (Ctrl, C)

pyautogui.PAUSE = 0.6

# clicar a tecla win
# digitar "chrome"
# clicar no campo do navegador para digitar o site
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Passo 2: Fazer login
#entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#quero dar uma pausa de 3 seg
time.sleep(2)
pyautogui.click(x=711, y=512)
pyautogui.write("brayanizidoro@hotmail.com")
pyautogui.press("tab")
pyautogui.write("123456789")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(2)

# Passo 3: Importar a base de dados
# pip install pandas
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastar 1 produto
# texto = string = str()
linha = 0
# para cada linha da minha tabela
for linha in tabela.index:
    # selecionar o 1º  campo
    pyautogui.click(x=670, y=364)

    # Precisa dos seguintes dados: 

    # Código do Produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # Marca do Produto
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # Tipo do Produto
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # Categoria do Produto
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # Preço Unitário do Produto
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    # Custo do Produto
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # OBS
    # nan = Not a Number = vazio
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    #clicar para cadastrar
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# Passo 5: Repetir o processo de cadastro até acabar os produtos
