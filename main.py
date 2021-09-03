def print_world(fname):
    print(fname + ", hello Bud!")


#print_world("Anton")


def how_many():
    klicivost = 80
    uhyne = 8
    rostliny_celkem = 14513
    baleni = 100
    kytek_uhyne = (((baleni/baleni)*klicivost)/100)*8
    print(kytek_uhyne)
    print(rostliny_celkem/((baleni/baleni)*klicivost-kytek_uhyne))


#how_many()


def what_is_the_name():
    username = input("What is your name? ")
    answer = input("Are you really named " + username)
    if answer in ['y', 'Y', 'yes', 'Yes', 'YES']:
        print("great")
    else:
        what_is_the_name()


#what_is_the_name()

def weather():
    dest = False
    vitr = False
    mlha = False
    prsi = input("Prsi? ")
    je_vitr = input("Je vitr? ")
    je_mlha = input("Je mlha? ")
    if je_vitr in ['y', 'Y', 'yes', 'Yes', 'YES']:
        vitr = True
    else:
        if je_vitr in ['n', 'N', 'no', 'No', 'NO']:
            vitr = False
    if je_mlha in ['y', 'Y', 'yes', 'Yes', 'YES']:
        je_mlha = True
    else:
        if je_mlha in ['n', 'N', 'no', 'No', 'NO']:
            je_mlha = False
    if prsi in ['y', 'Y', 'yes', 'Yes', 'YES']:
        prsi = True
    else:
        if prsi in ['n', 'N', 'no', 'No', 'NO']:
            prsi = False

    if(not prsi and not je_vitr and not je_mlha):
        print("Dobre pocasi, neni treba destnik")
    else:
        if(prsi or je_mlha and not prsi):
            print("Doporucil bych destnik")
        else:
            if(je_vitr and not prsi):
                print("Doporucil bych cepici")
                if(je_mlha):
                    print("Jeste reflexni obleceni")
#not completed

def narozeni():
    day = input("Zadej den ")
    mesic = input("Zadej mesic ")
    rok = input("Zadej rok ")
    print(day + ". " + mesic +  ". " + rok)

#narozeni()

def vojaci():
    for x in range(300):
        print(str(x+1) + ". voják u Thermopyl zdraví svého krále.")


#vojaci()

def mocnina():
    zaklad = input("Zadejte zaklad: ")
    mocnin = input("Zadejte mocninu ")
    zaklad_orig = zaklad
    for x in range(mocnin):
        zaklad = zaklad_orig*zaklad;
    print(zaklad)

#mocnina() not completed