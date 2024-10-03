module Combate
  def foiAtacado(atacante)
    case atacante.arma
    when "Pistolinha"
      self.tomouDano(5)
    when "Caderninho"
      self.tomouDano(10)
    when "mordida"
      self.tomouDano(15)
    end
  end
end



module Inventario
  attr_accessor :pocao, :arma, :dinheiro

  def inventario(pocao, arma, dinheiro)
    @pocao = pocao
    @arma = arma 
    @dinheiro = dinheiro
  end
end


class Oc
  attr_accessor :nome, :vida, :des
  include Inventario
  include Combate
  def initialize(nome, vida, des)
    @nome = nome
    @vida = vida
    @des = des
    
  end

  def tomouDano(quantidade)
    self.vida-= quantidade

  if (self.vida <= 0)
    puts "#{self.nome} foi dessa pra melhor"
  else
    puts "#{self.nome} tem #{self.vida} de vida restando"
   end
  end
end

class Dragao < Oc
  attr_accessor :sopro, :voo
  def initialize(nome, vida, des, sopro, voo)
    super(nome, vida, des)
    @sopro = sopro
    @voo = voo

  end
end
connor = Oc.new("connor", 20, 20)
connor.pocao = 5
connor.arma = "Pistolinha"


evan = Oc.new("Evan", 20, 20)
evan.arma = "Caderninho"
roberto = Dragao.new("Roberto", 500, 20, "Veneno", 100)
roberto.arma = "mordida"
puts "#{connor.nome} #{evan.nome} apareceu"

puts "#{roberto.nome} é um dragão"

connor.tomouDano(10)
evan.tomouDano(10)

connor.foiAtacado(roberto)
