import random
from datetime import datetime

def game1():
    health = 3
    rNum = random.randrange(0, 10)
    game = True
    while game:
        num = int(input('Di un número: '))
        if num == rNum: 
            print(f"Correcto! El número era {rNum}")
            menu()
        elif num < rNum: 
            print(f"Incorrecto! El número es más grande que {num}")
            health -= 1
        elif num > rNum: 
            print(f"Incorrecto! El número era el {rNum}")
            health -= 1

        if health == 0:
            print(f"Tienes {health} vidas! G A M E  O V E R!")
            menu()

def singleplayer(mats):
    bot = 0
    player = 0
    botHealth = 3
    playerHealth = 3

    skill = 0

    game = True

    difficulty = int(input("Escoje dificultad:\n1) FÁCIL\n2) NORMAL\n3) DIFÍCIL\n4) CHAD\n"))

    while game:
        match difficulty:
            case 1:
                skill = 0
            case 2:
                skill = 25
            case 3:
                skill = 50
            case 4:
                skill = 69
        print(f"1, 2, 3, piedra, papel, tijera, 1, 2, 3. ¡Ya!\n")

        player = int(input('Escoje entre:\n1) Piedra\n2) Papel\n3) Tijera\n'))

        isSkillTurn = skillTurn(skill)

        if isSkillTurn:
            match player:
                case 1:
                    bot = 2
                case 2:
                    bot = 3
                case 3:
                    bot = 1
                case _:
                    print("Número fuera de rango")
                    game1()
        else:
            bot = random.randint(1, len(mats))  # Elige entre 1 y 3
            

        print(f"Jugador = {player} ({mats[player - 1]})\nBot = {bot} ({mats[bot - 1]})")
        
        if player == 1 and bot == 2:
            playerHealth -= 1
        elif player == 2 and bot == 1:
            botHealth -= 1
        elif player == 1 and bot == 3:
            botHealth -= 1
        elif player == 3 and bot == 1:
            playerHealth -= 1
        elif player == 2 and bot == 3:
            playerHealth -= 1
        elif player == 3 and bot == 2:
            botHealth -= 1
        
        print(f"VIDAS:\nJugador = {playerHealth}\t\tBot = {botHealth}")

        if botHealth == 0:
            print(f"¡El jugador ha ganado! G A M E  O V E R!")
            menu()
        elif playerHealth == 0:
            now = datetime.now().strftime("%H:%M")
            botIA = ["EZ EZ EZ", "WHAT A SAVE!", "ZZZ", "L"]
            botMessage = botIA[random.randrange(0, len(botIA))]
            print(f"Te ha ganado el bot!\n({now}) Bot: {botMessage}")
            menu()

def twoPlayers(mats):
    player1 = 0
    player2 = 0
    player1Health = 3
    player2Health = 3

    game = True

    while game:
        print(f"1, 2, 3, piedra, papel, tijera, 1, 2, 3. ¡Ya!\n")

        player1 = int(input('Jugador 1, escoje entre:\n1) Piedra\n2) Papel\n3) Tijera\n'))
        player2 = int(input('Jugador 2, escoje entre:\n1) Piedra\n2) Papel\n3) Tijera\n'))

        print(f"Jugador1 = {player1} ({mats[player1 - 1]})\nJugador2 = {player2} ({mats[player2 - 1]})")
        
        if player1 == 1 and player2 == 2:
            player1Health -= 1
        elif player1 == 2 and player2 == 1:
            player2Health -= 1
        elif player1 == 1 and player2 == 3:
            player2Health -= 1
        elif player1 == 3 and player2 == 1:
            player1Health -= 1
        elif player1 == 2 and player2 == 3:
            player1Health -= 1
        elif player1 == 3 and player2 == 2:
            player2Health -= 1
        
        print(f"VIDAS:\nJugador 1 = {player1Health}\t\tJugador 2 = {player2Health}")

        if player1Health == 0:
            print(f"¡El Jugador 2 ha ganado! G A M E  O V E R!")
            menu()
        elif player2Health == 0:
            print(f"¡El Jugador 1 ha ganado! G A M E  O V E R!")
            menu()

def skillTurn(skill):
    turn = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
    return turn <= skill  # Retorna True si el turno está dentro de la habilidad del bot

def game2():
    mats = ['Piedra', 'Papel', 'Tijera']
    players = int(input("1) SINGLEPLAYER\n2) 2 PLAYERS\n"))
    match players:
        case 1:
            singleplayer(mats)
        case 2:
            twoPlayers(mats)

def game3():
    words = [
        "arbol", "sol", "luna", "avion", "carro", "escuela", "perro", "gato", "casa", "playa",
        "montana", "rio", "jardin", "libro", "lapiz", "mesa", "silla", "ventana", "puerta", "cielo",
        "estrella", "nube", "piedra", "camino", "puente", "ciudad", "pueblo", "bosque", "desierto", "fuego",
        "agua", "tierra", "viento", "huracan", "mar", "oceano", "isla", "volcan", "cueva", "rio",
        "barco", "tren", "bicicleta", "moto", "avion", "cohete", "astronauta", "satelite", "planeta", "galaxia",
        "universo", "cometa", "asteroide", "gravedad", "cuaderno", "boligrafo", "tijeras", "goma", "regla", "pincel",
        "papel", "cinta", "pegamento", "marcador", "reloj", "calendario", "mapa", "globo", "computadora", "raton",
        "teclado", "pantalla", "telefono", "camara", "lampara", "bateria", "auriculares", "paraguas", "botella", "vaso",
        "tenedor", "cuchillo", "cuchara", "plato", "sarten", "cacerola", "horno", "nevera", "microondas", "television",
        "radio", "altavoz", "ventilador", "espejo", "cuadro", "alfombra", "sofa", "cama", "armario", "estante"
    ]
    
    rNum = random.randint(0, len(words) - 1)
    word = words[rNum]
    health = len(word) + 5
    wordDisplay = []
    playerGuesses = []

    for letter in word:
        wordDisplay.append("*")
    
    print("Palabra oculta: " + "".join(wordDisplay))  # Se muestra la palabra oculta con asteriscos
    

    game = True
    
    while game:
        print(f"Tienes {health} vidas restantes.")
        opc = int(input("Escoja:\n1) Decir una letra\n2) Decir la palabra\n"))
        
        match opc:
            case 1:
                letter = input("Di una letra: ").lower()
                if letter in playerGuesses:
                    print(f"Ya adivinaste la letra {letter}. Prueba otra.")
                    continue
                playerGuesses.append(letter)

                if letter in word:
                    print(f"La letra {letter} forma parte de la palabra!")
                    for i, char in enumerate(word):
                        if char == letter:
                            wordDisplay[i] = letter
                else:
                    print(f"La letra {letter} no está en la palabra.")
                    health -= 1

                print("Palabra actual: " + "".join(wordDisplay))

                if "*" not in wordDisplay:
                    print(f"¡Felicidades! Has adivinado la palabra '{word}' correctamente.")
                    game = False
                    
            case 2:
                guess = input("Adivina la palabra: ").lower()
                if guess == word:
                    print(f"¡Correcto! La palabra era '{word}'.")
                    game = False
                else:
                    print("Incorrecto, sigue intentando.")
                    health -= 1

                if health == 0:
                    print(f"¡Se te han acabado las vidas! La palabra era '{word}'. G A M E  O V E R!")
                    game = False

    menu() 


def menu():
    opc = int(input("GAMEROOM\n-----------\n\n1) Adivina el número\n2) Piedra, papel, tijera!\n3) El ahorcado\n"))
    match opc:
        case 1:
            game1()
        case 2:
            game2()
        case 3:
            game3()

menu()
