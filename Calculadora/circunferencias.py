print("Bem vindo ao Sistema de Circunferências. Como você se chama?")

NomeDeUsuario = input()

print("Olá,", NomeDeUsuario, "! Provavelmente você é um amante da matemática, ou um estudante.")
print("Mas isso não importa no momento. Se você está aqui, quer dizer que precisa de ajuda com circunferências, certo?")
print("Com o que você precisa de ajuda?")
print("Digite A para saber o diâmetro de uma circunferência")
print("Digite B para saber o raio de uma circunferência")
print("Digite C para saber o perímetro de uma circunferência")
opcUsuario = input()
if (opcUsuario == "A" or opcUsuario == "a"):
  print("Conte-me o comprimento do raio, que eu faco o resto para você")
  CRaio = float(input())
  resultadoA = CRaio*2
  print(resultadoA)
elif(opcUsuario == "B" or opcUsuario == "b"):
  print("Conte-me o comprimento do diâmetro, que eu faco o resto")
  CDiametro = float(input())
  resultadoB = CDiametro/2
  print(resultadoB)
elif(opcUsuario == "C" or opcUsuario == "c"):
  print("Conte-me o diametro da circunferencia, que eu faco o resto")
  CDiametroC = float(input())
  resultadoC = CDiametroC*3.14159265359
  print(resultadoC)
else:
  print("por favor, recarregue a pagina e selecione uma opção válida")
