def soma_imposto(taxa_Imposto, Custo):
    return (1 + taxa_Imposto/100)*Custo
taxa_imposto = float(input("Insira a taxa de imposto: "))
custo = float(input("Insira o custo do produto: "))
print('Valor com imposto:', soma_imposto(taxa_imposto,custo))