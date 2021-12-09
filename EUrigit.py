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
print("Kas soovite riigi pealinnaga tutvuda? 1 Kas soovite testida oma teadmisi Euroopa riikide kohta? 2")
if=="1"
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
elif=="2":
    for x in range(10):
        print(chose(Countries))

            else:
                print("viga")
else:
    print("Viga")
