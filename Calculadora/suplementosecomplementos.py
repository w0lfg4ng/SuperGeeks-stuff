print("digite S para saber um suplemento ou C para um complemento de um ângulo")
X = input()
if(X == "S"):
  print("digite um numero de 1 - 180")
  N = int(input())
  if(N<=180):
    print("resultado:")
    print(180 - N)
  else:
    print("reinicie o programa, você inseriu um numero maior que 180!")
elif(X == "C"):
  print("digite um numero de 1 - 90")
  Y = int(input())
  if(Y <= 90):
    print("resultado:")
    print(90 - Y)
  else:
    print("reinicie o programa, você inseriu um numero maior que 90, sendo que digitou D")
else:
  print("desculpa, não entendi")
