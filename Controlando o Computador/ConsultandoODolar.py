import pyautogui as posicaoMouse
import pyautogui as tempoEspera

#Tempo de espera
tempoEspera.sleep(1)

#Movendo o mouse até o botão iniciar
posicaoMouse.moveTo(x=-1894, y=845)

tempoEspera.sleep(1)
#Coloca o mouse no iniciar
posicaoMouse.click(x=-1894, y=845)

tempoEspera.sleep(1)
#Digitando o nome do navegador
posicaoMouse.typewrite("Google Chrome")

tempoEspera.sleep(1)

#Pressiona o enter
posicaoMouse.press("enter")

tempoEspera.sleep(1)
#Digitando a palavra dolar
posicaoMouse.typewrite("Valor do dolar")

tempoEspera.sleep(1)

#Pressionando enter
posicaoMouse.press("enter")