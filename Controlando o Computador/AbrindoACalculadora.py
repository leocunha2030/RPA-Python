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
#Digita calculadora na barra de pesquisa
posicaoMouse.typewrite("calc")

tempoEspera.sleep(1)
#Clica em calculadora
posicaoMouse.click(x=-1770, y=306)

tempoEspera.sleep(1)
