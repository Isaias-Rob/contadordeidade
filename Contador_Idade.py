message = input('Qual seu nome?\n')
print('Olá, ', message)
while True:
  try:
    ano = int(input('Qual o ano do seu nascimento?\n'))
    if (ano < 1000):
      raise ValueError
  except ValueError as e:
    print('Apenas números de 4 digitos são permitidos')
  except:
    continue
  else:
    break
while True:
  try:
    atual = int(input('Em que ano estamos?\n'))
    if ((atual < 1000) or (atual < ano)):
      raise ValueError
  except ValueError as e:
    print('Apenas números de 4 digitos são permitidos/ o ano atual não pode ser menor que o ano de nascimento\n')
  except:
    continue
  else:
    break
while True:
  try:
    mes = int(input('Qual é o mês do seu nascimento?\n'))
    if(mes > 12 or mes < 1):
      raise ValueError
  except ValueError as e:
    print('Coloque o mês em números, e de 1 até 12\n')
  except:
    continue
  else:
    break
while True:
  try:
    mesat = int(input('Por fim, em que mês estamos?\n'))
    if(mesat > 12 or mesat < 1):
      raise ValueError
  except ValueError as e:
    print('Coloque o mês em números, e de 1 até 12\n')
  except:
    continue
  else:
    break
dia = int()
diat = int()
idade = atual - ano
if(mesat > mes):
  print('Você tem {} anos de idade'.format(idade))
elif(mesat == mes):
  while True:
    try:
      print('Bom, preciso saber o dia em que você nasceu\n')
      dia = int(input('Qual é o dia do seu nascimento?\n'))
      if(dia < 1 or dia > 31 or (dia > 28 and mes == 2) or (dia > 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11))):
        raise ValueError
    except ValueError as e:
      print('Você digitou um valor inválido ou se você nasceu no dia 29 de fevereiro, favor digitar 28')
    except:
      continue
    else:
      break
  while True:
    try:
      print('E agora, por favor, me diga o dia em que estamos\n')
      diat = int(input('Qual é o dia atual?\n'))
      if(diat < 1 or diat > 31) or (diat > 28 and mesat == 2) or (diat > 30 and (mesat == 4 or mesat == 6 or mesat == 9 or mesat == 11)):
        raise ValueError
    except ValueError as e:
      print('Você digitou um valor inválido, um dia que o mês escolhido não possui ou se hoje é dia 29 de fevereiro, favor digitar 28\n')
    except:
      continue
    else:
      break
  if(diat > dia):
    if(idade == 18):
      print('Você está no seu primeiro ano como maior de idade!\n')
    else:
      print('Você fez este mês {} anos de idade esse mês!\n'.format(idade))
  elif(diat == dia):
    print('Hoje é seu aniversário!, Parabéns pelos {} de idade!\n'.format(idade))
  else:
    print('Você fará {} anos de idade esse mês!\n'.format(idade))
else:
  print('Você fará {} anos de idade esse ano!\n'.format(idade))
