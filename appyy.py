import pyautogui
from time import sleep
from mouseinfo import mouseInfo


###fazendo login
#usuario
pyautogui.click(709, 450, duration=2)
pyautogui.write('paulo')
#senha
pyautogui.click(713, 477, duration=1)
pyautogui.write('123456')
#botao entrar
pyautogui.click(624, 508, duration=2)
###extrair cada produto
#abrindo arquivo
with open('produtos.txt', 'r') as file:
    for linha in file:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        #digitando produto
        pyautogui.click(431, 439, duration=2)
        pyautogui.write(produto)
        #digitando quantidade
        pyautogui.click(444,466,duration=1)
        pyautogui.write(quantidade)
        #digitando preco
        pyautogui.click(445,487,duration=1)
        pyautogui.write(preco)
        #registrando
        pyautogui.click(352,646,duration=1)
        sleep(1)