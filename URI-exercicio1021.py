notas = [
    100, 
    50,    
    20,      
    10,
    5,
    2]
    
moedas = [
    1.00,
    0.50,
    0.25,
    0.10,
    0.05,
    0.01]

def calculate_min_notes_coins(money):
    print("NOTAS:")
    for nota in notas:
        notas_qtd = 0
        if money >= nota:
            notas_qtd = int(money // nota)
            money = round(money - notas_qtd*nota, 2)
        print("%d nota(s) de R$ %.2f" % (notas_qtd, nota))

    #Estou fazendo isso, transformando as moedas em "notas" (numeros inteiros) , para evitar problemas com o ponto flutuante.
    money = int(round(money*100))
    print("MOEDAS:")
    for moeda in moedas:
        #Estou fazendo isso, transformando as moedas em "notas" (numeros inteiros) , para evitar problemas com o ponto flutuante.
        moeda = int(moeda*100)
        moedas_qtd = 0
        if money >= moeda:
            moedas_qtd = int(money // moeda)
            money = round(money - moedas_qtd*moeda, 2)
        print("%d moeda(s) de R$ %.2f" % (moedas_qtd, moeda/100)) 

money = float(input()) 
calculate_min_notes_coins(round(money,2))