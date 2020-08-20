import os
import json

bucle = True
bucle2 = True

with open('data.txt') as json_file:
    data = json.load(json_file)

def login():
    os.system("cls")
    print("\tIniciar Sesión")
    print("Usuario:")
    user = input()
    print("Contraseña:")
    contra = input()

    if user in data["Banco"].keys():
        if data["Banco"][user]["pass"] == contra:

            print("Cuenta accedida")
            global bucle2
            while bucle2:

                os.system("cls")
                print("\tCuenta")
                print("Usuario: ", user)
                print("Dinero: ", data["Banco"][user]["money"])
                print("\nPresiona + para depositar y - para retirar y x para salir")
                val = input()
                if val == "+":
                    print("Ingrsa cantidad a depositar:")

                    try:
                        valu = int(input())
                        data["Banco"][user]["money"] += valu
                    except:
                        print("Error")

                elif val == "-":
                    print("Ingrsa cantidad a retirar:")

                    try:
                        valu = int(input())

                        if valu > data["Banco"][user]["money"]:
                            print("Dinero insuficiente")
                            os.system("pause")
                        else:
                            data["Banco"][user]["money"] -= valu
                            
                    except:
                        print("Error")

                elif val == "x":
                    print("Saliendo...")
                    bucle2 = False
                else:
                    print("Valor no valido")
            os.system("cls")
            with open('data.txt', 'w') as outfile:
                json.dump(data, outfile, indent=4)

        else:
            print("Contraseña incorrecta")
    else:
        print("Este Usuario no existe")

def signin():
    print("\tCrear Cuenta")
    print("Usuario:")
    newuser = input()
    print("Contraseña:")
    newpass = input()
    print("Confirmar contraseña:")
    conpass = input()
    if newpass == conpass:
        if newuser in data["Banco"].keys():
            print("Esta cuenta ya existe")
        else:
            print("Ingresa la cantidad de dinero inicial en tu cuenta:")
            data["Banco"][newuser] = {}
            data["Banco"][newuser]["pass"] = newpass
            try:
                valur = int(input())
                data["Banco"][newuser]["money"] = valur
                with open('data.txt', 'w') as outfile:
                    json.dump(data, outfile, indent=4)
            except:
                print("Error")
    else:
        print("Las contraseñas no coincidem")

while bucle:
    print("\tBanco")
    print("1.-Iniciar Sesión")
    print("2.-Crear Cuenta")
    cuenta = input()

    if cuenta == "1":
        login()
    elif cuenta == "2":
        os.system("cls")
        signin()
    else:
        print("Caracter no valido")
    
    
    print("Desea salir del programa [y/n]")
    res = input()
    if res == "y":
        bucle2 = False
        bucle = False
    elif res == "n":
        bucle2 = True
        bucle = True
    else:
        print("Valor no valido")
    os.system("cls")

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile, indent=4)