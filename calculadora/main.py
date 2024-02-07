import operacoes as op

while True:

    try:
    
     n1 = int(input('Informe o primeiro número: '))
     break

    except:
       
     print("Valor inválido para efetuar qualquer operação!")


while True:

    try:
    
     n2 = int(input('Informe o segundo número: '))
     break

    except:
       
     print("Valor inválido para efetuar qualquer operação!")

while True:

  sinal = input('Selecione o sinal correspondente operação a ser executada: \n + Soma \n - Subtração \n * Multiplicão \n / Divisão \n')


  match sinal:
    
    case '+':

      print(f'{n1} + {n2} = {op.soma(n1,n2)}')
      break
    case '-':

      print(f'{n1} - {n2} = {op.sub(n1,n2)}')
      break
    case '*':

      print(f'{n1} * {n2} = {op.mult(n1,n2)}')
      break
    case '/':

      print(f'{n1} / {n2} = {op.div(n1,n2)}')
      break
    case __:

      print('Operação não válida!')