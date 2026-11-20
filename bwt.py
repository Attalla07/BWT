def bwt(testo) :
    testo += "$" #per aggungere il $ alla fine

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

#per prendere l'ultima lettera di ogni riga
    print("Ultima lettera di ogni riga: ")
    risultato=""
    for r in rotazioni:
        risultato = risultato+r[-1]
        print(risultato)

    return risultato

#per riuscire ad eseguire questo file da solo
if __name__ == "__main__":
    parola= input("Scrivi una stringa: ")
    print("Risultato finale: ",bwt(parola))
    
