#Maturita Informatika 
    #znaky a textové reťazce
#============================================================================================================================================================================================================================#
#je znak písmeno alebo cifra?
def je_pismeno(znak):
    if 'a'<=znak<='z' or 'A'<=znak<='Z': #spozoruje ascii poradové číslo znaku leží medzi ascii poradovými číslicami písmen a a z alebo A a Z (veľké písmená majú iné poradové číslo)
        return True #vráti odpoveď pravda => znak je písmeno
    else: #ak sa podmienka že znak je písmeno nesplní
        return False  #vráti odpoveď nepravda => znak nie je písmeno a ak sú na výber iba písmená a čísla znak je číslo
znaky=['a','4','z','C','7'] #zadefinoval som list znakov
print('je znak pismeno alebo cifra')
for z in znaky:
    if je_pismeno(z): #prejde z cez funkciu je_pismeno co vrati True ak z je pismeno a False ak z nieje pismeno, == True netreba písať lebo True==True je jednoducho True
        print(z,'je pismeno')
    else:
        print(z,'je cislo')

#krátka alternatíva (na maturite nepoužívať)
print('vysledok kratkej alternativy')
for z in znaky:
    print(z,'je cislo' if z.isnumeric() else 'je pismeno') #prejde znak z cez vbudovanú funkciu pythonu .isnumeric(), ktorá zistí či sa string z vie premeniť na integer bez toho aby spôsobil error a ak sa dá tak je z cislo
#============================================================================================================================================================================================================================#
#výskit znaku v reťazci a indexovanie
    #vyskit znaku
retazec='informatika' #zadefinoval som retazec informatika
def pocet_pismen(hladany_retazec,hladany_znak): #funkcia pocet_pismen potrebuje vediet ktore pismeno hladame a v ktorom retazci
    pocet=0 #zaciatocny pocet je 0
    for z in hladany_retazec: #pre kazdy znak v retazci
        if  z == hladany_znak: #pozriem ci znak je znak ktory pocitam
            pocet+=1 #ak ano zvysim pocet o 1
    return pocet #vratim pocet hladaneho pismena
print('pismeno i sa vyskituje v retazci',pocet_pismen(retazec,'i'),'krat')
print('pismeno o sa vyskituje v retazci',pocet_pismen(retazec,'o'),'krat')
print('pismeno a sa vyskituje v retazci',pocet_pismen(retazec,'a'),'krat')
if 'i' in retazec: #pozrie ci sa i nachadza v retazci ale nie kolko krat
    print('i sa nachadza v retazci')
    #indexovanie
posledny_znak=retazec[-1]#pouzivam indexovanie zo zadu nato aby som nasiel posledny znak bez ohladu na dlzku retazca
posledny_znak=retazec[len(retazec)-1]#alternativa pouzitelna na maturite ktora pouziva dlzku retazca !!! pozor kedze sa indexuje od nuli musime odratat 1 !!!
prvy_znak=retazec[0]#prvy znak retazca je indexovany 0 hocijako dlhy je retazec
print('prvy znak retazca',retazec,'je',prvy_znak,'a posledny je',posledny_znak)
#============================================================================================================================================================================================================================#
#nahradit alebo odstranit znak alebo podretazec v textovom retazci
print(retazec.replace('i','x')) #nahradi kazdy znak i znakom x v retazci
print(retazec.replace('for','oop')) #nahradi kazdy podretazec for podretazcom oop
retazec1='py'
retazec2='thon'
#============================================================================================================================================================================================================================#
#zostavit retazec z podretazcov podla kriteria
podretazce=['a','4','b','C','e','F','p','1','7','c']
cisla=[]
pismena=[]
for i in podretazce:
    if je_pismeno(i): #pouzivam funkciu z prveho zadania
        pismena+=[i] #triedim cisla a pismena
    else:
        cisla+=[i]
vysledok=''
index_pismena=0
index_cisla=0
for i in range(len(cisla)*2): #pre kazde cislo dva krat
    if i%2==0: #pre kazde parne indexovane cislo
        vysledok+=cisla[index_cisla] #pridaj do vysledku cislo
        index_cisla+=1 #zvecsim cislo nato aby sa dalsie cislo vybralo po porade nasledujuce predosle
    else: #pre kazde neparne indexovane cislo
        vysledok+=pismena[index_pismena]  #pridaj do vysledku pismeno
        index_pismena+=1
print(vysledok)
#============================================================================================================================================================================================================================#
#formatovanie vystupu
vek=12
meno='Peter'
bydlisko='Bratislava'
PSC=82109
print('{} ma {} rokov, byva v {} a jeho PSC je {}'.format(meno,vek,bydlisko,PSC)) #.format umoznuje nahradit {} zatvorky v texte premennou