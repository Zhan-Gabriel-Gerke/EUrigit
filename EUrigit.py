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
for country in Countries:
    country=input("sisesta riik: ")
    if country in Capitals:
        print('Riigi pealinn ' + country + ': ' + Capitals[country])
    else:
        print('Nimega riiki andmebaasis pole' + country)
        print("Kas soovite riigi lisada? kui jah, sisesta 1")
        if==1:
            a=input("Sisesta riik")
            b=input("Sisesta pealinn")
            dictionary['a'] = 'b'
        else:
            print("viga")