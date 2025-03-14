import json

current_letter = 'A'
cont_hint = 0

def init_bot():
    try:
        print('Bot is initialized')
        open_current_word()
    except Exception as e:
        print(f'Error: {e}')
        reset_bot()

def reset_bot():
    print('Bot is reset')

def next_word():
    if current_letter == 'Z':
        current_letter = 'A'
    else:
        current_letter = chr(ord(current_letter) + 1)
    
    # Abrir y cargar el contenido del fichero JSON
    # Elegir el JSON correspondiente a la letra actual palabras_agrupadas.json
    # Elejir una palabra aleatoria del JSON de letras
    # Guardar la palabra en un fichero JSON palabra_actual.json

def get_hint():
    print('Hint: world')

def open_current_word():
    # Abrir y cargar el contenido del fichero JSON
    with open('palabra_actual.json', 'r', encoding='utf-8') as file:
        current_word = json.load(file)  # Convierte el JSON en un diccionario de Python

    print(f"{current_word['titulo']} ** {current_word['letra']} **: \n {current_word['definicion']}")

    userInput = ''
    while userInput != current_word['respuesta']:
        userInput = input('Try to guess: ')
        if userInput == '.next':
            next_word()
        elif userInput == '.hint':
            get_hint()
        elif userInput == '.reset':
            reset_bot()
        elif userInput == '.resolve':
            print(f'{current_word['respuesta']}')
        elif userInput == '.status':
            print(f'Running...')
        elif userInput.lower() == current_word['respuesta'].lower():
            print('Correct! 👍')
            next_word()



if __name__ == '__main__':
    init_bot()