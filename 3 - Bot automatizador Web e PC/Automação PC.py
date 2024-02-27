import pyautogui
import time
    # Time.sleep para me dar tempo ( isso travou o código por 3 segundos), o pyautogui.position() me falou a relação do meu mouse em um plano cartesiano na minha tela me dando o x e o y.
time.sleep(3)
pyautogui.position()

    # Esse código me permite colocar um tempo de pause de execução das ações, por que o pyautogui faz tudo em milesimos de segundos.
pyautogui.PAUSE = 4

    # Abrir a ferramenta / sistema / programa
pyautogui.press('win')
pyautogui.write('login.xlsx')
pyautogui.press('enter')

     # Preencher o Loginlogin.xlsx
pyautogui.click(x=620, y=488)
pyautogui.write('Gostoso')

      # Preencher a senha
pyautogui.click(x=620, y=542)
pyautogui.write('6969')

       # Pressionar o botão de login
pyautogui.click(x=575, y=674)






