print(' ')

print('Hi! Welcome to my first python tools project.')
print('''
1. Spammer
2.
3.
''')

select = int(input('Select a tool: '))

if select == 1:
    print('Spammer selected')
    import pyautogui
    import time

    mensagem = input('Insert message: ')
    quantidade = int(input('Number of messages: '))

    print('5')
    time.sleep(1)
    print('4')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    
    for i in range(quantidade):
        pyautogui.typewrite(f"{mensagem}")
        pyautogui.press("enter")
        time.sleep(0)

    print('Mensagens enviadas com sucesso!')
else:
    print('Erro, opção inválida!')

print(' ')
