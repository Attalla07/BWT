def bwt(testo) :
    test += "$" #per aggungere il $ alla fine

#per fare le rotazioni
    print("Rotazioni: ")
    rotazioni=[]
    for i in range(len(testo)):
        rotazione= testo[i:]+testo[:i]
        rotazioni.append(rotazione)
        print(rotazione)

    print()

#per ordinarlo in ordine alfabetico
    print("In ordine alfabetico: ")
    rotazioni.sort()
    for r in rotazioni:
        print(r)

    print()

#per prendere l'ultima lettera di ogni riga della partte prima
    print("Risultato: ")
    risultato=""
    for r in rotazioni:
        risultato += +r[-1]
        print(risultato)

    return risultato


    
