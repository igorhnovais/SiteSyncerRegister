import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# abrir navegador 
pyautogui.press("win")
time.sleep(2)
pyautogui.click(x=654, y=68, clicks=1)
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)

# entrar no site
pyautogui.click(x=345, y=76, clicks=1)
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

# fazer login
pyautogui.click(x=587, y=386, clicks=1) #ver no arquivo auxiliar
pyautogui.write("qualqueremail@hotmail.com")
pyautogui.press("tab")
pyautogui.write("qualquersenha123")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1.5)

# importar base de dados
table = pandas.read_csv("produtos.csv")

# cadastrar um produto
#repetir o processo ate acabar a base de dados
for linha in table.index:

    pyautogui.click(x=640, y=279, clicks=1)

    code = table.loc[linha, "codigo"]
    pyautogui.write(code)
    pyautogui.press("tab")

    brand = table.loc[linha, "marca"]
    pyautogui.write(brand)
    pyautogui.press("tab")

    pyautogui.write(table.loc[linha, "tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(table.loc[linha, "categoria"])) #transformar em string
    pyautogui.press("tab")

    pyautogui.write(str(table.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")  

    pyautogui.write(str(table.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = table.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(2000)

