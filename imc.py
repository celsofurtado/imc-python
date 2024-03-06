# módulo imc
import estado_imc as calcular

peso = 0
altura = 0.0
nome = ""

nome = input("Qual o nome do paciente? ")

erro = True

while erro:
    try:
        peso = int(input("Qual o peso do paciente? "))
        erro = False
    except:
        print("Valor do peso está incorreto!")


erro = True
while erro:
    try:
        altura = float(input("Qual a altura do paciente? "))
        erro = False
    except:
        print("Valor da altura está incorreto!")

calcular.calcular_imc(peso, altura)


