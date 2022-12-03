def extrair_operandos(pilha):
    # Pega dois operandos da pilha, removendo-os (pop), e retorna eles ao x e y
    return pilha.pop(), pilha.pop()


def adicao(pilha):
    x, y = extrair_operandos(pilha)
    # Ao retornar será feito o cálculo e adicionaremos (append) o novo número ao topo da pilha
    pilha.append(x + y)


def subtracao(pilha):
    x, y = extrair_operandos(pilha)
    pilha.append(y - x)


def multiplicacao(pilha):
    x, y = extrair_operandos(pilha)
    pilha.append(x * y)


def divisao(pilha):
    x, y = extrair_operandos(pilha)
    pilha.append(y / x)


def potencia(pilha):
    x, y = extrair_operandos(pilha)
    pilha.append(y ** x)
