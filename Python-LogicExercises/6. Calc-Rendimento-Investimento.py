def calcular_ir(valor_resgate, dias_investidos, tipo_investimento):
    if tipo_investimento == 1:  # CDB
        if dias_investidos <= 180:
            aliquota_ir = 22.5
        elif 181 <= dias_investidos <= 360:
            aliquota_ir = 20
        elif 361 <= dias_investidos <= 720:
            aliquota_ir = 17.5
        else:
            aliquota_ir = 15
    else:
        return 0  # Para LCI e LCA, o IR é isento

    ir = valor_resgate * (aliquota_ir / 100)
    return ir

def main():
    print("Tipos de investimento:")
    print("1. CDB")
    print("2. LCI")
    print("3. LCA")

    tipo_investimento = int(input("Digite o tipo de investimento (1, 2 ou 3): "))
    if tipo_investimento not in [1, 2, 3]:
        print("Tipo de investimento inválido.")
        return
    valor_resgate = float(input("Digite o valor a ser resgatado: "))

    print("\nTabela de dias:")
    print("Até 180 dias")
    print("De 181 a 360 dias")
    print("De 361 a 720 dias")
    print("Acima de 720 dias\n")

    dias_investidos = int(input("Digite o número de dias que o valor permaneceu investido: "))

    ir = calcular_ir(valor_resgate, dias_investidos, tipo_investimento)
    print(f"\nImposto de Renda a ser pago: R$ {ir:.2f}")

if __name__ == "__main__":
    main()
