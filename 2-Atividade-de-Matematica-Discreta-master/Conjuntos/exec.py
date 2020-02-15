import conjunto
Conj = conjunto.Conjunto("A")


Conj.inserir('a')
Conj.inserir('b')
Conj.inserir('c')
Conj.inserir('A')
Conj.inserir('d')
Conj.inserir('D')


ConjB = conjunto.Conjunto("A")

Conj.inserir('a')
Conj.inserir('b')
Conj.inserir('c')
Conj.inserir('A')
Conj.inserir('d')
Conj.inserir('D')
ConjB.inserir(ConjB)


print('\n')
Conj.show()
print('\n')


