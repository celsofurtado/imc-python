# Módulo estado_imc

def definir_estado_imc(imc):
    estado = ""
    if imc < 18.5:
        estado = "Abaixo do Peso"
    elif imc >= 18.5 and imc < 25.0:
        estado = "Peso Ideal!"
    elif imc >= 25.0 and imc < 30.0:
        estado = "Levemente acima do peso"
    elif imc >= 30.0 and imc < 35.0:
        estado = "Obesidade Grau I"
    elif imc >= 35.0 and imc < 40.0:
        estado = "Obesidade Grau II"
    else:
        estado = "Obesidade Grau III"

    print(f"O IMC do paciente é: {imc:.1f} - {estado}.")

def calcular_imc(peso, altura):
    imc = peso / altura**2
    definir_estado_imc(imc)
