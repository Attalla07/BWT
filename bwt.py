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

    

