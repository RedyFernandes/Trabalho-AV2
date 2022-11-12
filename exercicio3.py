def converter_hora(hora):
    return (hora -12)

A = "am"
P = "pm"
def mostra_conver():
    hora = int(input("Digite a hora: "))
    minuto = int(input("Digite os minutos: "))

    if(hora <= 12):
        print(hora,minuto, A)

    if (hora > 24 or minuto > 59):
       print("Error")
    
    else:
       print(converter_hora(hora), minuto, P)

opcao = 1

while opcao:
    print("Deseja converter hora?")
    print("se sim, insira 1.  se não insira um numero negativo")

    opcao = int(input("Digite aqui: "))



    if (opcao == 1):
        mostra_conver()
    if (opcao < 0):
        break