import main
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

lst = ['']
prekidac=1

#pravimo glavni prozor
glavni_prozor = Tk()
glavni_prozor.geometry("1755x840")
glavni_prozor.title("Imenik")
defaultbg = glavni_prozor.cget('bg')

#pravimo temu
tema = ttk.Style()
tema.configure('Noc.TFrame', background='#2c2c2c', foreground="white")
tema.configure('Dan.TFrame', background='white', foreground="black",)
tema.map('Dan.TFrame', background=[('selected', '#257AFD')])
tema.map('Noc.TFrame', background=[('selected', '#257AFD')])


#delimo glavni prozor
frejm1 = Frame(glavni_prozor)
frejm1.place(x=65, y=50)
frejm2 = Frame(glavni_prozor)
frejm2.place(x=1670, y=50,height=525.5)

#pravimo treeview i scroll
pregled = ttk.Treeview(frejm1, height=25, style='Dan.TFrame',show='headings')
pregled.pack()
skrol= Scrollbar(frejm2, orient="vertical", command=pregled.yview)
pregled.configure(yscrollcommand=skrol.set)
skrol.pack(side="right" ,fill="y")

# definišemo kolone i headere
kolone=pregled["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11")
for kol in kolone:
    pregled.heading(kol,command=lambda k=kol: sortiraj(k,0))

pregled.column("1", width= 70, anchor='center',stretch=False)
pregled.column("2", width= 150, anchor='center',stretch=False)
pregled.column("3", width= 200, anchor='center',stretch=False)
pregled.column("4", width= 30, anchor='center',stretch=False)
pregled.column("5", width= 70, anchor='center',stretch=False)
pregled.column("6", width= 150, anchor='center',stretch=False)
pregled.column("7", width= 70, anchor='center',stretch=False)
pregled.column("8", width= 100, anchor='center',stretch=False)
pregled.column("9", width= 230, anchor='center',stretch=False)
pregled.column("10", width= 300, anchor='center',stretch=False)
pregled.column("11", width= 230, anchor='center',stretch=True)

pregled.heading("1", text="Korisnik ID")
pregled.heading("2", text="Ime")
pregled.heading("3", text="Prezime")
pregled.heading("4", text="Pol")
pregled.heading("5", text="Pozivni Br.")
pregled.heading("6", text="Broj")
pregled.heading("7", text="Fiks / Mob")
pregled.heading("8", text="Tip Kontakta")
pregled.heading("9", text="Email")
pregled.heading("10", text="Adresa Korisnika")
pregled.heading("11", text="Kratka Beleska")

pregled.bind("<<TreeviewSelect>>",lambda event:selekcija())

def upis(ime,prezime,pol,pozivni_br,broj,fix_mob,tip,email,adresa,beleska):
    main.error=0
    if ime_textbox.get() == '' or broj_textbox.get() == '' : messagebox.showerror("Greska prilikom unosa", "Morate uneti IME i BROJ")
    if pol=="Zenski":pol="♀"
    if pol=="Muski":pol="♂"
    if pozivni_br=="Srbija (+381)":pozivni_br="+381"
    if pozivni_br=="Crna Gora (+382)":pozivni_br="+382"
    if pozivni_br=="Hrvatska (+385)":pozivni_br="+385"
    if pozivni_br=="Slovenija (+386)":pozivni_br="+386"
    main.upis(ime,prezime,pol,pozivni_br,broj,fix_mob,tip,email,adresa,beleska)
    if main.error==1:messagebox.showinfo("Postojeci korisnik", "Korisnik sa istim IMENOM i BROJEM vec postoji")
    if main.error==2:messagebox.showerror("Los format podataka", "Broj mora sadrzati samo cifre")
    ocisti(1)
    prikazi()

#funkcija ažuriranja podataka
def azuriraj(id,ime,prezime,pol,pozivni_br,broj,fix_mob,tip,email,adresa,beleska):
    if id_combobox.get()=='':
        messagebox.showerror("Greska prilikom unosa", "Morate izabrati ID ili selektovati red")
    if pol=="Zenski":pol="♀"
    if pol=="Muski":pol="♂"
    if pozivni_br=="Srbija (+381)":pozivni_br="+381"
    if pozivni_br=="Crna Gora (+382)":pozivni_br="+382"
    if pozivni_br=="Hrvatska (+385)":pozivni_br="+385"
    if pozivni_br=="Slovenija (+386)":pozivni_br="+386"
    main.azuriraj(id,ime,prezime,pol,pozivni_br,broj,fix_mob,tip,email,adresa,beleska)
    ocisti(1)
    prikazi()
    messagebox.showinfo("Uspeh!", "Uspesno azuriran korisnik")


#funkcija brisanja podataka
def obrisi(id):
    if id_combobox.get()=='':
        messagebox.showerror("Greska prilikom unosa", "Morate izabrati ID ili selektovati red")
    main.obrisi(id)
    prikazi()
    ocisti(1)
    messagebox.showinfo("Uspeh!", "Uspesno obrisan korisnik")

#funkcija brisanja svih podataka
def obrisi_sve():
    main.obrisi_sve()
    prikazi()
    ocisti(1)
    messagebox.showinfo("Uspeh!", "Uspesno obrisani svi korisnici")

#funkcija upisivanja u csv fajl
def ucsv():
    main.uCSV()
    messagebox.showinfo("Uspeh!", "Uspesno eksportovani svi korisnici u export.csv")

#funkcija čitanja csv fajla
def izcsv():
    try:
        main.tabela=2
        main.izCSV()
        prikazi()
        messagebox.showinfo("Uspeh!", "Uspesno importovani svi korisnici iz import.csv")
    except FileNotFoundError:
        messagebox.showinfo("Greska", "Fajl import.csv nije pronadjen")
    except Exception:
        messagebox.showinfo("Greska", "Fajl import.csv nije dobro formatiran")

#funkcija menjanja moda(izgleda) naseg programa
def Dark_mod():
        global prekidac
        if prekidac==1:
            Darkmod_Dugme.configure(image=slika4,background="lightpink")
            glavni_prozor.configure(bg="#454141")
            pregled.column("11", width= 230)
            pregled.configure(style='Noc.TFrame')
            id_label.configure(bg="#454141")
            ime_label.configure(fg="white",bg="#454141")
            prezime_label.configure(fg="white",bg="#454141")
            broj_label.configure(fg="white",bg="#454141")
            pol_label.configure(fg="white",bg="#454141")
            email_label.configure(fg="white",bg="#454141")
            adresa_label.configure(fg="white",bg="#454141")
            drzava_label.configure(fg="white",bg="#454141")
            beleska_label.configure(fg="white",bg="#454141")
            tip_label.configure(fg="white",bg="#454141")
            fiksmob_label.configure(fg="white",bg="#454141")
            ocisti_Dugme.configure(background="#454141")
            sakrij_Dugme.configure(background="#454141")
            zakljucaj_Dugme.configure(background="#454141")
            osvezi_Dugme.configure(background="#454141")
            pretrazi_Dugme.configure(background="#454141",image=slika9)
            prekidac=0
        else:
            Darkmod_Dugme.configure(image=slika3,background="yellow")
            glavni_prozor.configure(bg=defaultbg)
            pregled.column("11", width= 230)
            pregled.configure(style='Dan.TFrame')
            id_label.configure(bg=defaultbg)
            ime_label.configure(fg="black",bg=defaultbg)
            prezime_label.configure(fg="black",bg=defaultbg)
            broj_label.configure(fg="black",bg=defaultbg)
            pol_label.configure(fg="black",bg=defaultbg)
            email_label.configure(fg="black",bg=defaultbg)
            adresa_label.configure(fg="black",bg=defaultbg)
            drzava_label.configure(fg="black",bg=defaultbg)
            beleska_label.configure(fg="black",bg=defaultbg)
            tip_label.configure(fg="black",bg=defaultbg)
            fiksmob_label.configure(fg="black",bg=defaultbg)
            ocisti_Dugme.configure(background=defaultbg)
            sakrij_Dugme.configure(background=defaultbg)
            zakljucaj_Dugme.configure(background=defaultbg)
            osvezi_Dugme.configure(background=defaultbg)
            pretrazi_Dugme.configure(background=defaultbg,image=slika8)
            prekidac=1

#funkcija sakrivanja treeviewa i scrolla
def sakrij():
    if pregled.winfo_manager():
        pregled.pack_forget()
        skrol.pack_forget()

    else:
       pregled.pack()
       skrol.pack(side="right" ,fill="y")

#funkcija zakljucavanja osnovnih dugmića
def zakljucaj():
    if  napravi_Dugme['state']!='disabled':
        zakljucaj_Dugme.configure(image=slika6)
        napravi_Dugme['state']='disabled'
        obirsi_Dugme['state']='disabled'
        obrisiSve_Dugme['state']='disabled'
        azuriraj_Dugme['state']='disabled'
    else:
        zakljucaj_Dugme.configure(image=slika5)
        napravi_Dugme['state']='normal'
        obirsi_Dugme['state']='normal'
        obrisiSve_Dugme['state']='normal'
        azuriraj_Dugme['state']='normal'

#funkcija čisćenja svih text/comboboxeva
def ocisti(a):
    id_combobox.set('')
    ime_textbox.delete("0","end")
    broj_textbox.delete("0","end")
    email_textbox.delete("0","end")
    adresa_textbox.delete("0","end")
    prezime_textbox.delete("0","end")
    beleska_textbox.delete("0","end")
    pol_combobox.set('')
    drzava_combobox.set('')
    tip_combobox.set('')
    fiksmob_combobox.set('')
    if a==1:
        pregled.selection_set()
        ocisti_Dugme.focus()

#funkcija pretrage tabele/treeviewa
def pretrazi(rec):
    global pregled
    pregled.delete(*pregled.get_children())
    for i in main.pretraga(rec):
        pregled.insert("", 'end', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))

#funkcija sortiranja odredjenje kolone treeviewa
def sortiraj(kol,redosled):
    data = [(pregled.set(child, kol), child) for child in pregled.get_children()]
    if (kol=="1"):
        data=sorted(data, key=lambda x: (int(x[0])), reverse=redosled)
    else:
        data.sort(reverse=redosled)
    for i, iid in enumerate(data):
        pregled.move(iid[1], '', i)
    pregled.heading(kol, command=lambda kol=kol: sortiraj(kol, not redosled))


#selekcija reda
def selekcija():
    if len(pregled.selection()) > 0:
        id_combobox.set(pregled.item(pregled.focus())["values"][0])
        fokus(0)

#omogucavanje raznih funkcionalnosti prilikom selektovanja ID-a / reda
def fokus(a):
    children=pregled.get_children()
    if(id_combobox.get()!=''):
        id=int(id_combobox.get())
        pregled.focus_set()
        if children:
            pregled.focus(children[id-1])
            selektovan=pregled.focus()
        if children and a==1:
            pregled.selection_set(children[id-1])
        ocisti(0)
        if(pregled.item(selektovan)["values"][3]=="♂" or pregled.item(selektovan)["values"][3]=="M"):pol="Muski"
        if(pregled.item(selektovan)["values"][3]=="♀"or pregled.item(selektovan)["values"][3]=="Z"):pol="Zenski"
        if(pregled.item(selektovan)["values"][3]==""):pol=""
        if(pregled.item(selektovan)["values"][4]==""):drzava=""
        if(pregled.item(selektovan)["values"][4]==381):drzava="Srbija (+381)"
        if(pregled.item(selektovan)["values"][4]==382):drzava="Crna Gora (+382)"
        if(pregled.item(selektovan)["values"][4]==385):drzava="Hrvatska (+385)"
        if(pregled.item(selektovan)["values"][4]==386):drzava="Slovenija (+386)"
        id_combobox.set(pregled.item(selektovan)["values"][0])
        ime_textbox.insert(0,pregled.item(selektovan)["values"][1])
        prezime_textbox.insert(0,pregled.item(selektovan)["values"][2])
        pol_combobox.set(pol)
        drzava_combobox.set(drzava)
        broj_textbox.insert(0,pregled.item(selektovan)["values"][5])
        fiksmob_combobox.set(pregled.item(selektovan)["values"][6])
        tip_combobox.set(pregled.item(selektovan)["values"][7])
        email_textbox.insert(0,pregled.item(selektovan)["values"][8])
        adresa_textbox.insert(0,pregled.item(selektovan)["values"][9])
        beleska_textbox.insert(0,pregled.item(selektovan)["values"][10])
    else:
        ocisti(1)


#funkcija prikaza/učitavanja podataka u treeview
def prikazi():
    global pregled
    global lst
    lst=['']
    pregled.delete(*pregled.get_children())
    for i in main.prikazi_sve():
            pregled.insert("", 'end', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
            lst.append(i[0])
    id_combobox.configure(values=lst)

#funkcija pravljenja prozora za dugme "Uputstvo"
def otvoriUputstvo():
    Uputstvo = Toplevel(glavni_prozor,bg="lightblue")
    Uputstvo.title("Uputstvo")
    Uputstvo.geometry("1400x800")
    tekst="\n"+"KOMANDNI DUGMIĆI: "
    tekst2="\n"+"""Dugme Kreiraj: Kreira novi kontakt, minimalno zahteva ime i broj. Kontakt ne sme imati isto ime i broj kao već registrovani korisnik.
Dugme Ažuriraj: Ažurira postojeći kontakt pomoću birača ID-a korisnika ili selektovanog reda, može ažurirati bilo koje polje uključujući više polja odjednom.
Dugme Obrisi: Briše željeni kontakt iz baze podataka pomoću birača Korisnik ID-a ili selektovanog reda.
Dugme Obrisi Sve: Briše sve kontakte iz baze podataka.
    """
    tekst3="\n\n\n\n\n"+"CSV DUGMIĆI: "
    tekst4="\n"+"""⭳ CSV: Dugme eksportuje citavu listu u csv formatu u export.csv fajl koji se nalazi u folderu programa
⭱ CSV: Dugme importuje listu formata tipa csv iz fajla import.csv koji se nalazi u folderu programa
    """
    tekst5="\n\n\n\n\n"+"OSTALI DUGMIĆI: "
    tekst6="\n"+"""Incognito: Sakriva treeview tabelu i sve podatke u njoj, otkriva je ponovnim klikom.
Dugme za zaključavanje: Zaključava svu komandna dugmad i sprečava njihovu upotrebu, otključava ih ponovnim klikom.
Dugme za pretragu: Vrši pretragu u celoj listi i prikazuje rezultate za željenu reč iz polja za tekst (razlikuje velika i mala slova), enter postiže isti rezultat.
Dugme za noćni režim: Nalazi se na desnoj strani (sunce/mesec), menja temu ili izgled programa između dva režima „dan“ (podrazumevano) i „noć“.
Dugme Uputstvo: Prikazuje kratak vodič za svako dugme u programu.
Dugme Opis: Prikazuje osnovne detalje o programu, njegov kratak opis kao i opis svih njegovih funkcija.
Dugme za smeće: Briše sav tekst iz text/combobox-eva iz prethodnih unosa.
Dugme Osveži: Osvežava listu, korisno kada koristimo pretragu i kada želimo da se vratimo na prvobitnu listu.
    """
    Label(Uputstvo,text=tekst,fg="red",bg="lightblue",font=('Times New Roman',15,'bold')).pack()
    Label(Uputstvo,text=tekst2,justify="left",bg="lightblue",font=('Times New Roman',12)).pack()
    Label(Uputstvo,text=tekst3,bg="lightblue",fg="green",font=('Times New Roman',15,'bold')).pack()
    Label(Uputstvo,text=tekst4,bg="lightblue",justify="left",font=('Times New Roman',12)).pack()
    Label(Uputstvo,text=tekst5,bg="lightblue",fg="purple",font=('Times New Roman',15,'bold')).pack()
    Label(Uputstvo,text=tekst6,bg="lightblue",justify="left",font=('Times New Roman',12)).pack()

#funkcija pravljenja prozora za dugme "Opis"
def otvoriOpis():
    Opis = Toplevel(glavni_prozor,bg="beige")
    Opis.title("Opis")
    Opis.geometry("1400x850")
    tekst="\nKRATKI OPIS: "
    tekst2="\n"+"""Program ispunjava svrhu običnog imenika sa nekoliko različitih funkcija. Čita, kreira, ažurira i briše kontakte kao osnovne radnje,
ali takođe ima mogućnost pretraživanja, sortiranja, zaključavanja osnovnih funkcija, promene teme, skrivanja i osvežavanja.
Pored toga, omogućava izvoz ili uvoz css datoteka u/iz liste/baze podataka.
    """
    tekst3="\n\n\n\n\n"+"OPIS SVIH FUNKCIJA: "
    tekst4="\n"+"""Funkcija prikaži: prikazuje ili "čita" sve podatke iz odredjenje databaze imenika i prikazuje ih u treeview tabeli. Ova funkcija se manualno može pozvati klikom na dugme "osveži".
Funkcija upis: Pravi/dodaje novi zapis u tabelu kontakti(CSV) sa atributima uzetim iz text/comboboxeva i poziva funkciju prikaži koja dodaje unos na treeview prikaz.
Funkcija ažuriraj: Updatetuje jedan zapis iz tabele kontakata odredjen izabranim ID-om iz comboboxa "Korisnik ID" ili selektovanim redom iz treeview-a i podacima u svim combo/textboxevima,takodje poziva funckiju prikazi.
Funkcija obriši: Briše dati zapis iz tabele odredjen izabranim ID-om iz comboboxa "Korisnik ID" ili selektovanim redom is treeview-a i poziva funckiju prikaži.
Funckija obriši sve: Jednostavno Briše sve zapise iz tabele kontakata.
Funckija ucsv: Uzima sve podatke iz tabele i upisuje ih u preodredjeni format csv fajla u fajl export.csv
Funckija izcsv: Čita csv fajl "import.csv" sa preodredjenim formatom i upisuje ga u novu tabelu "kontaktiCSV" koja je onda prikazana u treeviewu,i sve operacije se mogu vršiti na njoj kao i na normalnoj tabeli kontakti.
Funkcija pretrage: Traži unesenu reč u datom textboxu kroz celu tabelu i sva njena polja i prikazuje rezultat, pretraga se može vršiti klikom na lupa dugme ili pritiskom na enter.
Funkcija sortiraj: Sortira celu treeview kolonu abecednim redom pritiskom na njen header, ako je kolona "Korisnik ID" vrši se numeričko sortiranje.
Funkcija dark mod: Menja temu prozora za treeview, menja razne atribute razlicitih objekata kao što su pozadina, boja teksta i slika(ikonica).
Funkcija sakrij: Sakriva treeview i skrol, i ponovo ih prikazuje.
Funkcija zaključaj: Isključuje opciju korišćenja odredjenih komandnih dugmića i ponovo ih "osposobljava".
Funkcija ocisti: Čisti sve unose iz text/comboboxeva radi jednostavnijeg ponovnog unosa.
Funkcije otvori opis/uputstvo: Otvaraju nove prozore klikom na odredjene dugmiće, novi prozori prikazuju tekst uputsvta ili opisa programa.
"""
    tekst5="\n\n\n\n\n"+"Osnovni podaci o projektu: "+" "*39
    tekst6="\n"+"""Ime projekta: Kontakt Imenik
Programski jezici: sqlite & python
Autor: Milan Vuković | I011-57
Škola: MEF Fakultet
Predmet: Praktikum primenjenog programiranja - II godina
Predavač: Doc. dr. Dejan Viduka, asistent Luka Ilić
Datum: Jul. 2022
    """
    Label(Opis,text=tekst,fg="red",bg="beige",font=('Times New Roman',15,'bold')).pack()
    Label(Opis,text=tekst2,justify="left",bg="beige",font=('Times New Roman',12)).pack()
    Label(Opis,text=tekst3,bg="beige",fg="green",font=('Times New Roman',15,'bold')).pack()
    Label(Opis,text=tekst4,bg="beige",justify="left",font=('Times New Roman',12)).pack()
    Label(Opis,text=tekst5,bg="beige",fg="purple",font=('Times New Roman',12)).pack(anchor='e')
    Label(Opis,text=tekst6,bg="beige",justify="left",font=('Times New Roman',10,'italic')).pack(anchor='e')


#pravimo elemente programa labele i text/comboboxeve
pretraga_textbox = Entry(glavni_prozor, width=86)
pretraga_textbox.place(x=65,y=15)
pretraga_textbox.bind("<Return>", lambda pretraga: pretrazi(pretraga_textbox.get()))


id_label = Label(glavni_prozor, text="Korisnik ID: ", foreground="red")
id_label.place(x=733,y=592)
id_combobox = ttk.Combobox(glavni_prozor,width=5,state='readonly')
id_combobox.option_add('*TCombobox*Listbox.Justify', 'center')
id_combobox.place(x=803,y=592)
id_combobox.bind("<<ComboboxSelected>>",lambda event:fokus(1))


ime_label = Label(glavni_prozor, text="Ime: ")
ime_label.place(x=30,y=637)
ime_textbox = Entry(glavni_prozor, width=15)
ime_textbox.place(x=65,y=637)

prezime_label = Label(glavni_prozor, text="Prezime: ")
prezime_label.place(x=190,y=637)
prezime_textbox = Entry(glavni_prozor, width=20)
prezime_textbox.place(x=245,y=637)

broj_label = Label(glavni_prozor, text="Broj: ")
broj_label.place(x=405,y=637)
broj_textbox = Entry(glavni_prozor, width=15)
broj_textbox.place(x=440,y=637)

adresa_label = Label(glavni_prozor, text="Adresa: ")
adresa_label.place(x=565,y=637)
adresa_textbox = Entry(glavni_prozor, width=40)
adresa_textbox.place(x=615,y=637)

email_label = Label(glavni_prozor, text="Email: ")
email_label.place(x=885,y=637)
email_textbox = Entry(glavni_prozor, width=35)
email_textbox.place(x=930,y=637)

pol_label = Label(glavni_prozor, text="Pol: ")
pol_label.place(x=30,y=683)
pol_combobox = ttk.Combobox(glavni_prozor,width=10)
pol_combobox['values'] = ('','Muski', 'Zenski')
pol_combobox['state'] = 'readonly'
pol_combobox.place(x=65,y=683)

drzava_label = Label(glavni_prozor, text="Drzava: ")
drzava_label.place(x=190,y=683)
drzava_combobox = ttk.Combobox(glavni_prozor,width=15,state='readonly')
drzava_combobox['values'] = ('','Srbija (+381)', 'Crna Gora (+382)','Hrvatska (+385)', 'Slovenija (+386)')
drzava_combobox.place(x=245,y=683)

fiksmob_label = Label(glavni_prozor, text="Fiksni/Mobilni: ")
fiksmob_label.place(x=398,y=683)
fiksmob_combobox = ttk.Combobox(glavni_prozor,width=10,state='readonly')
fiksmob_combobox['values'] = ('','Fiksni', 'Mobilni')
fiksmob_combobox.place(x=495,y=683)

tip_label = Label(glavni_prozor, text="Tip: ")
tip_label.place(x=610,y=683)
tip_combobox = ttk.Combobox(glavni_prozor,width=10,state='readonly')
tip_combobox['values'] = ('','Poslovni', 'Porodicni', 'Prijateljski', 'Ostali')
tip_combobox.place(x=646,y=683)

beleska_label = Label(glavni_prozor, text="Kratka Beleska: ")
beleska_label.place(x=762,y=683)
beleska_textbox = Entry(glavni_prozor, width=40)
beleska_textbox.place(x=860,y=683)


#dodajemo slike koje koriste neki dugmići
slika1 = PhotoImage(file="slike/slika1.png")
slika2 = PhotoImage(file="slike/slika2.png")
slika3 = PhotoImage(file="slike/slika3.png")
slika4 = PhotoImage(file="slike/slika4.png")
slika5 = PhotoImage(file="slike/slika5.png")
slika6 = PhotoImage(file="slike/slika6.png")
slika7 = PhotoImage(file="slike/slika7.png")
slika8 = PhotoImage(file="slike/slika8.png")
slika9 = PhotoImage(file="slike/slika9.png")

#pravimo dugmiće
napravi_Dugme = Button(text="NAPRAVI", bg="lightgreen", font=('Myriad',11,'bold'),  width=10, command=lambda:upis(ime_textbox.get(),prezime_textbox.get(),
pol_combobox.get(),drzava_combobox.get(),broj_textbox.get(),fiksmob_combobox.get(),tip_combobox.get(),email_textbox.get(),adresa_textbox.get(),beleska_textbox.get()))
napravi_Dugme.place(x=400,y=740)

azuriraj_Dugme = Button(text="AZURIRAJ", bg="lightblue", font=('Myriad',11,'bold'), width=10, command=lambda:azuriraj(id_combobox.get(),ime_textbox.get(),
prezime_textbox.get(),pol_combobox.get(),drzava_combobox.get(),broj_textbox.get(),fiksmob_combobox.get(),tip_combobox.get(),email_textbox.get(),adresa_textbox.get(),
beleska_textbox.get()))
azuriraj_Dugme.place(x=540,y=740)

obirsi_Dugme = Button(text="OBRISI", bg="#ff726f",font=('Myriad',11,'bold'), width=10, command=lambda:obrisi(id_combobox.get()))
obirsi_Dugme.place(x=680,y=740)

obrisiSve_Dugme = Button(text="OBRISI SVE", bg="red", font=('Myriad',11,'bold'), width=10, command=obrisi_sve)
obrisiSve_Dugme.place(x=1570, y=760)

uputstvo_Dugme = Button(glavni_prozor,border=1,relief="ridge", height=2, width=15, text ="UPUTSTVO",bg="lightblue" ,font=('Helvetica',11,'bold'), command=otvoriUputstvo)
uputstvo_Dugme.place(x=1545,y=613)
opis_Dugme = Button(glavni_prozor, border=1,relief="ridge", height=2, width=15, text ="O PROGRAMU",bg="beige" ,font=('Helvetica',11,'bold'), command = otvoriOpis)
opis_Dugme.place(x=1545,y=677)

pretrazi_Dugme = Button(border=0,image=slika8, width=20, height=17, command=lambda:pretrazi(pretraga_textbox.get()))
pretrazi_Dugme.place(x=598, y=14)

ocisti_Dugme = Button(border=0, width=32 , height=28 ,image=slika7,command=lambda:ocisti(1))
ocisti_Dugme.place(x=1117,y=677)

osvezi_Dugme = Button(border=0, width=32 , height=28 ,image=slika1,command=prikazi)
osvezi_Dugme.place(x=1155, y=630)

sakrij_Dugme = Button(border=0, width=32, height=32,image=slika2,command=sakrij)
sakrij_Dugme.place(x=15, y=10)

zakljucaj_Dugme=Button(border=0,width=32,image=slika5,command=zakljucaj)
zakljucaj_Dugme.place(x=15, y=60)

Darkmod_Dugme= Button(width=32, height=32,image=slika3,bg="yellow", command=Dark_mod)
Darkmod_Dugme.place(x=1703, y=50)

uCsv_Dugme=Button(text=" ⭳ CSV ",background="Green", font=('Myriad',11,'bold'), width=10, command=ucsv)
uCsv_Dugme.place(x=1300, y=630)

izCsv_Dugme=Button(text=" ⭱ CSV ",background="Green", font=('Myriad',11,'bold'), width=10, command=izcsv)
izCsv_Dugme.place(x=1300, y=677)

prikazi()
mainloop()
