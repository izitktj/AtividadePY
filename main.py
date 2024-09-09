# Função que recebe um número inteiro e retorna em qual faixa etária você se encaixa
def VoceEh(idade):
    # Verifica se a idade é válida (entre 0 e 100)
    if idade < 0 or idade >= 100:
        return 'Valor não encontrado!'

    # Se a idade for válida e menor que 11 retorna "Você é uma criança"
    if idade <= 10:
        return 'Você é uma criança'
    
    # Se a idade for válida e entre 10 e 20, retorna "Você é adolescente"
    elif idade < 20:
        return 'Você é adolescente'

    # Se a idade for válida e entre 20 e 30, retorna "Você é jovem"
    elif idade < 30:
        return 'Você é jovem'
    
    # Se a idade for válida e entre 20 e 100, retorna "Você é adulto"
    elif idade <= 100:
        return 'Você é um adulto'

    # Se for um valor invalido não verificado antes retorna "Valor não encontrado!"
    else:
        return 'Valor não encontrado!'

# Recebe um input do úsuario e converte para inteiro
idade = int(input('Digite sua idade: '))

# Manda o input recebido anteriormente para a função "VoceEh(int)" e printa o resultado
print(VoceEh(idade))