lista_carros = ['gol','vectra','corsa','prisma','fox']
consumo_carros = [12.5,10,11.5,11,13]

def economia_carro(lista_carros,consumo_carros):
    
    indice_min = consumo_carros.index(min(consumo_carros))   
    nome_carro = lista_carros[indice_min] 
    
 
    return  nome_carro


def calcula_consumo(consumo_carros):
    
    rodagem = []
    for consumo in consumo_carros:
        
        consumo_total = 1000/consumo
        rodagem.append(round(consumo_total,2))
        
    
    
    return rodagem


def custo_consumo(consumo_carros):
    
    preco_gasolina = []
    for consumo in consumo_carros:
        preco = consumo * 2.25
        preco_gasolina.append(round(preco,2))    
        
    return preco_gasolina

def main():
    
    lista_consumo = calcula_consumo(consumo_carros)
    lista_preço = custo_consumo(lista_consumo)
    
    
    
    print('\nComparativo de Consumo de Combustível\n\n\n')
    for indice, nome_carro in enumerate(lista_carros):
        
        print(f'Veiculo {indice}')
        print(f'Nome: {nome_carro}')
        print(f'Km por litro: {consumo_carros[indice]}')
        
    print('\n\nrelatório final:')
    for indice, nome_carro in enumerate(lista_carros):
        
        print(f'{indice+1} - \t{nome_carro}\t- \t{consumo_carros[indice]} - \t{lista_consumo[indice]} litros - \tR${lista_preço[indice]}') 
    
    print(f'O menor consumo é o {economia_carro(lista_carros,consumo_carros)}')
    
    
main()



