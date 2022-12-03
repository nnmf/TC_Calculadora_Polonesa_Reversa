from calculadora import adicao, subtracao, multiplicacao, divisao, potencia


def main():
    # Aqui eu crio um 'dicionário' que mapeia os operadores para chamar as funções
    operadores = {'+': adicao,
                  '-': subtracao,
                  '*': multiplicacao,
                  '/': divisao,
                  '**': potencia
                  }

    # Inicializo uma pilha1 vazia e na outra pilha2 coloco o cálculo na notação poloneza
    pilha1, pilha2 = [], input('Insira a expressão na Notação Polonesa Reversa:\n>').strip().split()

    for operador in pilha2:
        if operador in operadores:
            # Aqui eu faço a opreção com os dois números no topo da pilha1 passando o operador encontrado na pilha 2
            operadores[operador](pilha1)
        else:
            # Ao encontrarmos um número na pilha2, colocamos ele(append) no topo da pilha 1
            pilha1.append(float(operador))
        print(">" + str(pilha1))

    # print(pilha2)
    # Aqui mostro o resultado
    print(">" + str(pilha1[0]))


if __name__ == "__main__":
    op = 1
    while op == 1:
        main()
        op = input('Digite 0 para sair ou qualquer outro número para continuar:\n>')
        op = int(op)
