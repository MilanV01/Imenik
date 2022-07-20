# Imenik
Jednostavni imenik napisan u pythonu sa dosta funkcija...


# Opis Funkcija


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


# Lista Zadataka

* Prevesti program i dodati dugme za prevod
* Dodati trenutno vreme u program
* Dodati opciju za omiljeni kontakt u vidu zvezdice
* Dodati login ekran

