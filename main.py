import sqlite3
import csv

error=0
tabela=1

#pravimo tabele
def napravi_tabele():
    conn = sqlite3.connect("baza.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS  kontakti (
        ime TEXT,
        prezime TEXT,
        pol TEXT,
        pozivni_br TEXT,
        broj INT,
        fix_mob TEXT,
        tip TEXT,
        email TEXT,
        adresa TEXT,
        beleska TEXT
        )
        """
        )
    c.execute("""CREATE TABLE IF NOT EXISTS kontaktiCSV (
        ime TEXT,
        prezime TEXT,
        pol TEXT,
        pozivni_br TEXT,
        broj INT,
        fix_mob TEXT,
        tip TEXT,
        email TEXT,
        adresa TEXT,
        beleska TEXT
        )
        """)
    conn.commit()
    conn.close()

#upisujemo u tabele
def upis(ime="",prezime="",pol="",pozivni_br="",broj="",fix_mob="",tip="",email="",adresa="",beleska="",):
    global error
    conn = sqlite3.connect("baza.db")
    c = conn.cursor()
    if tabela==1:
        c.execute(f"SELECT * FROM kontakti WHERE ime = '{ime}' AND broj = '{broj}'")
        rezultat = c.fetchall()
        if len(rezultat)!=0: error=1
        if len(rezultat)==0 and ime !="" and broj !="" :
           try: c.execute("INSERT INTO kontakti VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(ime,prezime,pol,pozivni_br,int(broj),fix_mob,tip,email,adresa,beleska))
           except ValueError:error=2
    else:
        c.execute(f"SELECT * FROM kontaktiCSV WHERE ime = '{ime}' AND broj = '{broj}'")
        rezultat = c.fetchall()
        if len(rezultat)!=0: error=1
        if len(rezultat)==0 and ime !="" and broj !="":
            try: c.execute("INSERT INTO kontaktiCSV VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(ime,prezime,pol,pozivni_br,int(broj),fix_mob,tip,email,adresa,beleska))
            except ValueError:error=2
    conn.commit()
    conn.close()

#prikazujemo sve zapise iz tabela
def prikazi_sve():
    conn=sqlite3.connect("baza.db")
    c = conn.cursor()
    if tabela==1:
        c.execute("VACUUM")
        c.execute("SELECT rowid, * FROM kontakti")
    else:
        c.execute("VACUUM")
        c.execute("SELECT rowid, * FROM kontaktiCSV")
    rezultat = c.fetchall()
    conn.commit()
    conn.close()
    return rezultat

#brišemo zapis iz tabela
def obrisi(id):
    conn=sqlite3.connect("baza.db")
    c = conn.cursor()
    if tabela==1:
        c.execute(f"DELETE FROM kontakti WHERE rowid = {id}")
    else:
        c.execute(f"DELETE FROM kontaktiCSV WHERE rowid = {id}")
    conn.commit()
    conn.close()

#brišemo sve zapise iz tabela
def obrisi_sve():
    conn=sqlite3.connect("baza.db")
    c = conn.cursor()
    if tabela==1:
        c.execute("DELETE FROM kontakti")
    else:
        c.execute("DELETE FROM kontaktiCSV")
    conn.commit()
    conn.close()

#vršimo eksportovanje u csv fajl
def uCSV():
    conn=sqlite3.connect("baza.db")
    c = conn.cursor()
    if tabela==1:
        data=c.execute("SELECT rowid, * FROM kontakti")
    else:
        data=c.execute("SELECT rowid, * FROM kontaktiCSV")
    with open('export.csv', 'w', newline='', encoding='utf-8') as f:
        upisivanje=csv.writer(f)
        upisivanje.writerow(['Kontakt_ID','Ime','Prezime','Pol','Pozivni br.','Br.Telefona','Fiksni/Mobilni','Tip Kontakta','Email','Adresa','Beleska'])
        upisivanje.writerows(data)
    conn.commit()
    conn.close()

#importujemo csv fajl u tabelu 2
def izCSV():
    conn=sqlite3.connect("baza.db")
    c = conn.cursor()
    c.execute("DELETE FROM kontaktiCSV")
    with open('import.csv','r') as f:
        dr=csv.DictReader(f)
        to_db=[(i['ime'],i['prezime'],i['pol'],i['pozivni_br'],i['broj'],i['fix_mob'],i['tip'],i['email'],i['adresa'],i['beleska']) for i in dr]
    c.executemany("INSERT INTO kontaktiCSV VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",to_db)
    conn.commit()
    conn.close()

#ažuriramo zapis u tabelama
def azuriraj(id, ime,prezime,pol,pozivni_br,broj,fix_mob,tip,email,adresa,beleska):
    conn=sqlite3.connect("baza.db")
    c = conn.cursor()
    if tabela==1:
        if ime != "":
            c.execute(f"UPDATE kontakti SET ime = '{ime}' WHERE rowid = {id}")
        if prezime != "":
            c.execute(f"UPDATE kontakti SET prezime = '{prezime}' WHERE rowid = {id}")
        if broj != "":
            c.execute(f"UPDATE kontakti SET broj = '{broj}' WHERE rowid = {id}")
        if pol!= "":
            c.execute(f"UPDATE kontakti SET pol = '{pol}' WHERE rowid = {id}")
        if pozivni_br != "":
            c.execute(f"UPDATE kontakti SET pozivni_br = '{pozivni_br}' WHERE rowid = {id}")
        if fix_mob != "":
            c.execute(f"UPDATE kontakti SET fix_mob = '{fix_mob}' WHERE rowid = {id}")
        if tip != "":
            c.execute(f"UPDATE kontakti SET tip = '{tip}' WHERE rowid = {id}")
        if email != "":
            c.execute(f"UPDATE kontakti SET email = '{email}' WHERE rowid = {id}")
        if adresa != "":
            c.execute(f"UPDATE kontakti SET adresa = '{adresa}' WHERE rowid = {id}")
        if beleska != "":
            c.execute(f"UPDATE kontakti SET beleska = '{beleska}' WHERE rowid = {id}")
    else:
        if ime != "":
            c.execute(f"UPDATE kontaktiCSV SET ime = '{ime}' WHERE rowid = {id}")
        if prezime != "":
            c.execute(f"UPDATE kontaktiCSV SET prezime = '{prezime}' WHERE rowid = {id}")
        if broj != "":
            c.execute(f"UPDATE kontaktiCSV SET broj = '{broj}' WHERE rowid = {id}")
        if pol!= "":
            c.execute(f"UPDATE kontaktiCSV SET pol = '{pol}' WHERE rowid = {id}")
        if pozivni_br != "":
            c.execute(f"UPDATE kontaktiCSV SET pozivni_br = '{pozivni_br}' WHERE rowid = {id}")
        if fix_mob != "":
            c.execute(f"UPDATE kontaktiCSV SET fix_mob = '{fix_mob}' WHERE rowid = {id}")
        if tip != "":
            c.execute(f"UPDATE kontaktiCSV SET tip = '{tip}' WHERE rowid = {id}")
        if email != "":
            c.execute(f"UPDATE kontaktiCSV SET email = '{email}' WHERE rowid = {id}")
        if adresa != "":
            c.execute(f"UPDATE kontaktiCSV SET adresa = '{adresa}' WHERE rowid = {id}")
        if beleska != "":
            c.execute(f"UPDATE kontaktiCSV SET beleska = '{beleska}' WHERE rowid = {id}")
    conn.commit()
    conn.close()

#vršimo pretragu tabela
def pretraga(rec):
    conn=sqlite3.connect("baza.db")
    c = conn.cursor()
    if tabela==1:
        c.execute(f"""SELECT rowid, * FROM kontakti WHERE ime='{rec}' or prezime='{rec}' or broj='{rec}' or pol='{rec}'
        or pozivni_br='{rec}' or fix_mob='{rec}' or tip='{rec}' or email ='{rec}' or adresa='{rec}' or beleska='{rec}'  """)
    else:
        c.execute(f"""SELECT rowid, * FROM kontaktiCSV WHERE ime='{rec}' or prezime='{rec}' or broj='{rec}' or pol='{rec}'
        or pozivni_br='{rec}' or fix_mob='{rec}' or tip='{rec}' or email ='{rec}' or adresa='{rec}' or beleska='{rec}'  """)
    rezultat = c.fetchall()
    conn.commit()
    conn.close()
    return rezultat

napravi_tabele()


