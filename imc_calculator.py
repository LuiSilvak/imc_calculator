def calcular_imc(peso, altura):
    """Calcula o índice de Massa Corporal (IMC)."""
    return peso / (altura ** 2)


def classificar_imc(imc):
    """Classifica o IMC com base nos critérios da OMS."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau 2"
    else: 
        return "Obesidade Grau 3"
    

def main():
    print("=== Calculadora de IMC ===")
    try:
        peso = float(input("Digite seu peso (em kg): "))
        altura = float(input("Digite sua altura (em metros): "))

        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)

        print(f"\nSeu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
    except ValueError:
        print("Por favor, insira valores válidos para peso e altura.")


if __name__ == "__main__":
    main()