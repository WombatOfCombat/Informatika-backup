#Maturita Informatika 
    #podprogramy
#podprogramy sú programy, ktoré vo svojom kóde dáva zmysel využívať viacero krát
#napr ak chcete nakresliť niekde snehuliaka a potom ho presunúť, nemusíte snehuliaka kreslit od znova iba musíte aktivovat podprogram, ktorý ho vykreslí podľa parametru koordinacií
#============================================================================================================================================================================================================================#
#definovať vlastné podprogramy s parametrami
def podprogram(parameter1,parameter2=0): #definujem podprogram s dvoma parametrami
#parameter1 je non-default toto znamená, že musí byť zadaní pri spustení podprogramu inač podprogram nebude fungovať
#parameter2 je default ciže v prípade v ktorom nieje zadefinovaný je jeho hodnota automaticky nastavená na hocijakú hodnotu, ktorou je zadefinovaný pri definícií podprogramu
#!!!POZOR default program v definícií musí vždy nasledovať všetky non-default programy inač kód nebude fungovať!!!
    return parameter1+parameter2 #podprogram vracia sucet parametrov pomocou navratnej hodnoty, navratna hodnota môže byť hocijaký typ údaja
print(podprogram(1,5))#1+5=6
print(podprogram(1))#1+0=0
#============================================================================================================================================================================================================================#
#dané podprogramy (knižnice)
import tkinter #s týmto príkazom som do programu vložil všetky funkcie, ktoré sa nachádzajú v knižnici tkinter a teraz ich môžem používať pomocou príkazu tkinter.
c=tkinter.Canvas(bg='black',width=100,height=100)
c.create_oval(0,0,100,100,fill='white') #tuto nemusím písať tkinter. lebo c už je zadefinované ako príkaz tkinteru Canvas, ktorého jednotlivé vlastnosti mením už pomocou normálneho pythonu
c.pack()
c.mainloop()
#podľa téz by ste ešte okrem tkinter mali vedieť funkcie podprogramov random a niektoré funkcie podprogramu math všetky sú nájditelné na webe a vysvetliť ich tu by bolo neefektívne