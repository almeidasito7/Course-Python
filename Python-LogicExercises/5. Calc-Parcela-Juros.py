def calcular_parcela(valor_divida, taxa_juros, parcelas):
    valor_juros = valor_divida * taxa_juros / 100
    valor_total = valor_divida + valor_juros
    valor_parcela = valor_total / parcelas
    return valor_juros, valor_parcela

def main():
    valor_divida = float(input("Digite o valor da dívida: "))

    print("\nTabela de Parcelamento:")
    
    
    # Definindo as quantidades de parcelas e as taxas de juros
    quantidades_parcelas = [1, 3, 6, 9, 12]
    taxas_juros = [0, 10, 15, 20, 25]
    
    for parcelas, taxa_juros in zip(quantidades_parcelas, taxas_juros):
        valor_juros, valor_parcela = calcular_parcela(valor_divida, taxa_juros, parcelas)
        print(f"Total:R$ {valor_divida:.2f}  Juros:R$ {valor_juros:.2f}   Número de Parcelas:{parcelas}x   Valor da Parcela:R$ {valor_parcela:.2f}")
if __name__ == "__main__":
    main()

