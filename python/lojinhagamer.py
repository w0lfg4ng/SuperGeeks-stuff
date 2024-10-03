saldo = 5000

def mostrarSaldo():
  print("Saldo da loja é de: ", saldo)



#Fazer mais defs aqui

    
def venderProduto():
  global saldo
  print("quanto custa esse produto")
  preçoDoProduto = int(input())
  saldo == preçoDoProduto + saldo
  #eu nao sei defs vou me mataaaaaaar aaaaaaa
  #Terminar essa def
    
    
def menuPrincipal():
  while True:
    
    print("Olá Sr. Gerente, o que gostaria de fazer?")
    print("[1] - Cadastrar um novo produto no estoque")
    print("[2] - Listar produtos do estoque")
    print("[3] - Vender um produto")
    print("[4] - Ver o saldo da loja")
    print("[0] - Encerrar o programa")
    opc = int(input())
    if(opc == 1):
      print("1")
      print("Oi, qual o produto que você quer registrar?")
      registrarProduto = input()
      print("Quanto ele custou?")
      preçoProduto = int(input())
      print("Quantas unidades você vai querer?")
      unidadesProduto = input()
      preçoTotalProduto = unidadesProduto * preçoProduto 
      if preçoTotalProduto > saldo:
        print("Oh! Que pena, você não pode registrar isso, pois são muito caros para seu pequeno saldinho")
      elif preçoTotalProduto >= saldo:
        print("OK! Parabéns, você registrou um produto =D")
        saldo - preçoTotalProduto
    elif(opc == 2):
      print("2")
      
      
    elif(opc == 3):
      print("3")
      
    elif(opc == 4):
      print("4")
      
    elif(opc == 0):
      print("Bye bye")
      break
    else:
      print("Opção inválida")
  
  
menuPrincipal()
