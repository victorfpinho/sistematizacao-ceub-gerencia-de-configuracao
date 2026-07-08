def converter_dolar_para_real(valor_dolar, taxa_cambio):
    if valor_dolar < 0 or taxa_cambio <= 0:
        raise ValueError("Os valores devem ser maiores que zero.")
    return round(valor_dolar * taxa_cambio, 2)

if __name__ == "__main__":
    print("--- Conversor de Moeda Simples ---")
    try:
        # Captura as entradas como texto puro (string)
        entrada_dolar = input("Digite o valor em USD: $")
        entrada_taxa = input("Digite a taxa de câmbio (Ex: 5.50 ou 5,50) ou pressione Enter para usar 5.50: ")
        
        # Se o usuário apenas apertar Enter na taxa, define o padrão de 5.50
        if not entrada_taxa.strip():
            entrada_taxa = "5.50"

        # Trata a vírgula substituindo por ponto antes de converter para float
        dolar = float(entrada_dolar.replace(",", "."))
        taxa = float(entrada_taxa.replace(",", "."))
        
        # Executa a função de conversão
        real = converter_dolar_para_real(dolar, taxa)
        
        print(f"\nResultado: ${dolar:.2f} com a taxa de R${taxa:.2f} equivale a: R${real:.2f}")
        
    except ValueError as e:
        # Captura tanto o erro da nossa função quanto erros de digitação de letras
        if "ValueError" in str(e) or "maiores que zero" in str(e):
            print(f"\nErro de negócio: {e}")
        else:
            print(f"\nErro de entrada: Certifique-se de digitar apenas números válidos.")
