from random import*
Capitals=()
Capitals=dict()
Capitals['Belgia'] = 'Brüssel'
Capitals['Leedu'] = 'Vilnius'
Capitals['Bulgaaria'] = 'Sofia'
Capitals['Luksemburg'] = 'Luksemburg'
Capitals['Tsehhi Vabariik'] = 'Praha'
Capitals['Ungari'] = 'Budapest'
Capitals['Taani'] = 'Kopenhaagen'
Capitals['Malta'] = 'Valletta'
Capitals['Saksamaa'] = 'Berliin'
Capitals['Madalmaad'] = 'Amsterdam'
Capitals['Esti'] = 'Tallinn'
Capitals['Austria'] = 'Viin'
Capitals['Iirimaa'] = 'Dublin'
Capitals['Poola'] = 'Varssavi'
Capitals['Kreeka'] = 'Ateana'
Capitals['Portugal'] = 'Lissabon'
Capitals['Hispania'] = 'Madrid'
Capitals['Rumeenia'] = 'Bukarest'
Capitals['Prantsustmaa'] = 'Pariis'
Capitals['Sloveenia'] = 'Ljubljana'
Capitals['Horvaatia'] = 'Zagreb'
Capitals['Slovakkia'] = 'Bratislava'
Capitals['Itaalia'] = 'Rooma'
Capitals['Sooma'] = 'Helsingi'
Capitals['Küpros'] = 'Nikosia'
Capitals['Rootsi'] = 'Stockholm'
Capitals['Läti'] = 'Riga'
Countries = ['Belgia','Leedu','Bulgaaria','Luksemburg','Tsehhi Vabariik','Ungari','Taani','Malta','Saksamaa','Madalmaad','Esti','Austria','Iirimaa','Poola','Kreeka','Portugal','Hispania','Rumeenia','Prantsustmaa','Slovakkia','Itaalia','Sooma','Küpros','Rootsi','Läti',]
Pealinnes = ['Brüssel','Vilnius','Sofia','Luksemburg','Praha','Budapest','Kopenhaagen','Valletta','Berliin','Amsterdam','Tallinn','Viin','Dublin','Varssavi','Ateana','Lissabon','Madrid','Bukarest','Pariis','Ljubljana','Zagreb','Bratislava','Rooma','Helsingi','Nikosia','Stockholm','Riga']
g=input("Kas soovite riigi pealinnaga tutvuda? 1 Kas soovite testida oma teadmisi Euroopa riikide kohta? 2:(Если что писать надо с большой буквы что бы работало) ")
if g=="1":
    for country in Countries:
        country=input("sisesta riik: ")
        if country in Capitals:
            print('Riigi pealinn ' + country + ': ' + Capitals[country])
        else:
            print('Nimega riiki andmebaasis pole' + country)
            c=input("Kas soovite riigi lisada? kui jah, sisesta 1 võib-olla oli kirjaviga, kui selle parandad 2")
            if c=="1":
                a=input("Sisesta riik")
                b=input("Sisesta pealinn")
                Capitals.update({a: b})
            elif c=="2":
                g=input("Sisesta riik:")
                Capitals.pop(g)
                q=input("Sisesta riik")
                w=input("Sisesta pealinn")
                Capitals.update({q:w})
            else:
                print("viga")
elif g=="2":
    for x in range(10):
        Countries.sort()
        Countries.reverse()
        m=0
        for i in range(10):
            country=str(choice(Countries))
            print(country)
            st=input("Sisesta peallinn: ")
            if st==Capitals[country]:
                print("Hea")
                chet+=1
            else:
                print("Viga")
        if chet==0:
            print("0/10")
        elif chet==1:
            print("1/10")
        elif chet==2:
            print("2/10")
        elif chet==3:
            print("3/10")
        elif chet==4:
            print("4/10")
        elif chet==5:
            print("5/10")
        elif chet==6:
            print("6/10")
        elif chet==7:
            print("7/10")
        elif chet==8:
            print("8/10")
        elif chet==9:
            print("9/10")
        elif chet==10:
            print("10/10")  
else:
    print("Viga")