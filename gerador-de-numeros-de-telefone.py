import random

def gerador_telefonico():
    digitos = ['9']
    telefone = []
    for i in range(0,8):
        digitos += str(random.randint(0, 9))    
    
    digitos.insert(5, '-')
    telefone = ''.join(digitos)
    
    return telefone

def verificador_operadoras(digitos):
    ddd_operadora = digitos[1] + digitos[2]
    

    operadora_vivo = [67,71,72,95,96,97,98,99]
    operadora_claro = [68,73,74,75,76,91,92,93,94]
    operadora_tim = [69,79,80,81,82,83]
    operadora_oi = [84,85,86,87,88,89]
    for numero in operadora_vivo:
        if int(ddd_operadora) == numero:
            operadora = 'é da operadora Vivo'
            break
        
    else:
        for numero in operadora_claro:
            if int(ddd_operadora) == numero:
                operadora = 'é da operadora Claro'
                break

        else:
            for numero in operadora_tim:
                    if int(ddd_operadora) == numero:
                        operadora = 'é da operadora Tim'
                        break
            else:
                for numero in operadora_oi:
                    if int(ddd_operadora) == numero:
                        operadora = 'é da operadora Oi'

                else:
                    operadora = 'esse número não tem operadora, logo ele não existe'
                    
    return ddd_operadora , operadora

telefone = gerador_telefonico()
ddd, operadora_frase = verificador_operadoras(telefone)
print(f'O número de telefone: {telefone}\nDe DDD: {ddd}, {operadora_frase}')