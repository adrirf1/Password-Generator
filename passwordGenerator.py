import sys
import string
import secrets

letrasMin = string.ascii_lowercase
letrasMay = string.ascii_letters
numeros = string.digits
simbolos = string.punctuation


if len(sys.argv) > 1:
    #numeros,mayuscula,simbolos
    if "-n" in sys.argv and "-M" in sys.argv and "-S" in sys.argv:
        try:
            contrasena = ''.join(secrets.choice(letrasMay+numeros+simbolos) for i in range(int(sys.argv[1])))
            print(contrasena)
        except:
            print("Error. Uso: py passwordGenerator.py 7")
    #numeros,mayusculas
    elif "-n" in sys.argv and "-M" in sys.argv:
        try:
            contrasena = ''.join(secrets.choice(letrasMay+numeros) for i in range(int(sys.argv[1])))
            print(contrasena)
        except:
            print("Error. Uso: py passwordGenerator.py 7")
    #numeros,simbolos
    elif "-n" in sys.argv and "-S" in sys.argv:
        try:
            contrasena = ''.join(secrets.choice(letrasMin+numeros+simbolos) for i in range(int(sys.argv[1])))
            print(contrasena)
        except:
            print("Error. Uso: py passwordGenerator.py 7")
    #mayusculas,simbolos
    elif "-M" in sys.argv and "-S" in sys.argv:
        try:
            contrasena = ''.join(secrets.choice(letrasMay+simbolos) for i in range(int(sys.argv[1])))
            print(contrasena)
        except:
            print("Error. Uso: py passwordGenerator.py 7")
    #mayusuclas
    elif "-M" in sys.argv:
        try:
            contrasena = ''.join(secrets.choice(letrasMay) for i in range(int(sys.argv[1])))
            print(contrasena)
        except:
            print("Error. Uso: py passwordGenerator.py 7")
    #numeros
    elif "-n" in sys.argv:
        try:
            contrasena = ''.join(secrets.choice(letrasMin+numeros) for i in range(int(sys.argv[1])))
            print(contrasena)
        except:
            print("Error. Uso: py passwordGenerator.py 7")
    #simbolos
    elif "-S" in sys.argv:
        try:
            contrasena = ''.join(secrets.choice(letrasMin+simbolos) for i in range(int(sys.argv[1])))
            print(contrasena)
        except:
            print("Error. Uso: py passwordGenerator.py 7")
    #minusculas
    else:
        contrasena = ''.join(secrets.choice(letrasMin) for i in range(int(sys.argv[1])))
        print(contrasena)
else:
    print("Escoge numero minimo para tu contrasena")
    print("Ejemplo de uso: ")
    print("py passwordGenerator.py 32")
    print("Eso te crea una contrasena aleatoria de 32 digitos en puras minusculas")
    print("Para mayusculas: -M")
    print("Para numeros: -n")
    print("Para simbolos: -S")