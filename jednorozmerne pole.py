#Maturita Informatika 
    #jednorozmerné pole
#============================================================================================================================================================================================================================#
#generovanie obsahu pola
pole=[] #zadefinujem premennú ako prázdne pole
pole=list() #rovnako ale pomocou funkcie
#nasledujúci prvok je súčtom predchádzajúcich dvoch
pole=[1,1] #prvé dva prvky musím zadefinovať
for i in range(2,10): #číslo 10 určuje finálny počet prvkov pola
    pole.append(pole[i-1]+pole[i-2]) #pridávam súčet prvkov pola, ktoré sú 1 a 2 indexy za prvkom, ktorý generujem
print('pole 2 predchadzajuce',pole)
    #vynulovanie
pole=[0]*len(pole)#premení všetky prvky pola na nulu
for i in range(len(pole)):#premení všetky prvky pola na nulu
    pole[i]=0
print('pole vynujovane',pole)
#============================================================================================================================================================================================================================#
#používať pole na uchovávanie zložitejších údajov
import random #pre generovanie údajov
pole=[]
for i in range(20):
    pole.append([random.randint(0,100),random.randint(0,100)]) #do pola vkladam súradnice bodov čo sú jednorozmerné polia => pole je dvojrozmerné
print('pole bodov',pole)
print('dlzka pola bodov',len(pole)) #pozor dĺžka pola je počet súradníc nie počet čísiel čiže 20
#============================================================================================================================================================================================================================#
#hladať prvky s vlastnosťami
pole=[random.randint(0,100) for _ in range(20)] #generujem pole jedním riadkom lebo som lenivý na maturite používajte len keď to viete vysvetliť
print('pole nahodnych cisiel',pole)
    #najmenší
najmensi=pole[0] #na prvé porovnanie používam prvý prvok pola aby som napred neodhadoval hodnotu, ktorá by mohla byť menšia ako najmenšia hodnota pola
for cislo in pole: #pre každé číslo v poli
    if najmensi>cislo:#skontrolujem či je číslo menšie ako číslo, ktoré predpokladám za najmenšie
        najmensi=cislo#ak je menšie začnem predpokladať, že toto nové číslo je najmenšie
print('najmensi prvok',najmensi)
    #najväčší
najvacsi=pole[0]
for cislo in pole: #pre každé číslo v poli
    if najvacsi< cislo:#skontrolujem či je číslo väčšie ako číslo, ktoré predpokladám za najväčšie
        najvacsi=cislo#ak je väčšie začnem predpokladať, že toto nové číslo je najväčšie
print('najvacsi prvok',najvacsi)
    #druhý najmenší
while najmensi in pole: #zatial čo sa v poli nachádza aspoň jeden prvok rovný najmenšiemu prvku
    pole.remove(najmensi) #odstráň najmenší prvok (opakujem lebo sa v poli môže nachádzať viacero krát)
najmensi=pole[0] #opakujem nájdenie najmenšieho prvku z modifikovaným listom
for cislo in pole: #pre každé číslo v poli
    if najmensi>cislo:#skontrolujem či je číslo menšie ako číslo, ktoré predpokladám za najmenšie
        najmensi=cislo#ak je menšie začnem predpokladať, že toto nové číslo je najmenšie
print('druhe najmensie',najmensi)
#============================================================================================================================================================================================================================#
#zistiť či pole obsahuje prvky z danými vlastnosťami
    #číslo 0
pole=[random.randint(0,3) for _ in range(10)]
print('pole nahodnych cisiel od 0 po 3',pole)
if 0 in pole: #niesom si istý či toto nieje príliž jednoduché pre maturitnú komisiu ale ak je 0 v liste
    print('0 sa nachadza v poli') #vypíš, že 0 je v liste
else:
    print('0 sa nenachadza v poli')
#============================================================================================================================================================================================================================#
#dlhšia alternatíva bez použitia if x in y:
je_0=False
for prvok in pole:
    if prvok==0:
        je_0=True
        break
if je_0:
    print('0 sa nachadza v poli')
else:
    print('0 sa nenachadza v poli')
    #prvý výskyt medzeri
pole=[random.choice(['p','y','t','h','o','n',' ']) for _ in range(40)]
print(pole)
for i in range(len(pole)):
    if pole[i]==' ':
        print(f'prva medzera je na {i+1}. mieste')
        break
#============================================================================================================================================================================================================================#
#zisťovať či pole spĺňa kritérium
pole1=[random.choice(['a','b','c','d','e','pramparam','0'])]*20
pole2=[random.choice(['a','b','c','d','e','pramparam','0']) for _ in range(20)]
print('pole1:',pole1)
print('pole2:',pole2)
    #všetky prvky sú rovnaké
for i,pole in enumerate([pole1,pole2]): #pre kazde z poli 1 a 2
    konstantne=True #zadefinujem premennu konstantne ako pravda
    for prvok in pole: #pre kazdy prvok pola
        if prvok!=pole[0]: #ak je prvok nerovny prvemu prvku
            konstantne=False #konstantne je nepravda
            break #koncim kontrolu lebo som uz nasiel ze nie vsetky prvky su rovnake
    if konstantne: #vypisujem ci su vsetky prvky rovnake alebo nie
        print(f'pole{i+1} ma vsetky prvky rovnake')
    else:
        print(f'pole{i+1} nema vsetky prvky rovnake')
    #pole je zoradene
        #vzostupne
pole=[random.randint(0,100) for _ in range(100)] #nematuritne zadefinujem pole zo 100 prvkami od 0 po 100
pole.sort() #nematuritne triedim pole od najmensieho po najvecsi prvok
#pole.append(2)
print(pole)
vzostupne=True #zadefinujem kontrolnu premennu
for i in range(1,len(pole)-1): #pre všetky prvky pola okrem prvého (prvý nemáme s čím porovnať)
    if pole[i+1]<pole[i]: # ak je terajší prvok menší ako minulí (začínam prvkami 1 a 0) pre zostupne usporiadanie prehodte znak < na > pozor nie ako negacia vyrokovej logiky >= lebo v oboch pripadoch zoradenia sa dalsi prvok moze aj rovnat
        vzostupne=False #prehoď kontrolnú premennú na False
        break #ukoncim kontrolu
if vzostupne: #vypisem vysledok
    print('pole je vzostupne')
else:
    print('pole nie je vzostupne')
#============================================================================================================================================================================================================================#
#modifikovať prvky pola
    #zobrať prvok bez zmeny poradia [1,2,3] => [1,3]
pole=[1,1,2,3,3]
print('pred',pole)
pole.remove(2) #odstráni prvý prvok rovný parametru z listu
print('po',pole)
    #pridať prvok bez zmeny poradia
def pridat(dane_pole,chceny_index,vsunuta_hodnota): #definujem funkciu pridat z parametrami pola, chceneho indexu a vsunutej hodnoty
    return dane_pole[:chceny_index]+[vsunuta_hodnota]+dane_pole[chceny_index:] #funkcia vytvori pole ktore siaha od zaciatku daneho pola po index, vsunie nove cislo a pokracuje od indexu dalej
pole=pridat(pole,1,2)
print('pole zo zaradenou dvojkou na druhom indexe',pole)
#============================================================================================================================================================================================================================#
#manipulovanie z viacerimi poliami
    #kopirovanie casti pola/pola
        #celeho pola
pole=[1,2,3]
print('pole',pole)
pole_kopia=pole[:] #musim nove pole definovat ako podmnozinu inac python bere obe premenne za jednu
        #casti
pole_kopia=pole[0:2] #podla indexu
print('cast pola',pole_kopia)
    #obratenie pola
pole_obratene=pole[::-1] #nech pole ide od zaciatku po koniec ale v krokoch od zadu o -1
print('pole obratene',pole_obratene)
    #zlucovanie postupnosti
postupnost1=range(2,100,4)
postupnost2=range(400,600,8)
postupnost_zlucenie=[]
for i in range(len(postupnost1)): #maturnitna verzia
    postupnost_zlucenie.append(postupnost1[i]+postupnost2[i])
postupnost_zlucenie=[postupnost1[i]+postupnost2[i] for i in range(len(postupnost1))] #nematuritna verzia
print(postupnost_zlucenie)
#============================================================================================================================================================================================================================#
#zobrazovat pole vykreslenim a vypisanim
import tkinter
c=tkinter.Canvas(bg='black',width=1000,height=700)
pole=[random.randint(300,500) for _ in range(int(1000/20))]
print('nahodne cisla',pole)
    #spojnicovy diagram
spojnicove_body=[] #definujem prazdne pole pre suradnice bodov
for i in range(len(pole)): #pre kazde cislo v poli ktore sa snazim grafovo znazornit
    spojnicove_body.append([i*20,700-pole[i]]) #oddialim sa v xovej osi o 20 a v y osi 700-hodnota lebo idem zo spodu kde je y najvecsie
print('body spojnicoveho diagramu',spojnicove_body)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #stlcovy graf aby bolo vidno obe davam ho pred spojnicovi
for i in range(len(spojnicove_body)):
    c.create_rectangle(i*20+20,700,spojnicove_body[i][0],spojnicove_body[i][1],fill='grey') #nizsie aby bolo vidno obe
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        #vykreslenie spojnicoveho diagramu
c.create_line(spojnicove_body,fill='white') #vytvorim spojnicovy diagram pomocou funkcie create_line
#============================================================================================================================================================================================================================#
    #vypisanie prvkov pola
for i,prvok in enumerate(pole):
    print(f'{i+1}. prvok je {prvok}')
c.pack()
c.mainloop()
