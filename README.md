# Ugnius_Jankauskas_EEf-24
Kursinio darbo ataskaita: Asmeninių išlaidų stebėjimo programa.

Įvadas:
   
1. a) Kas tai per programa?

Tai programa, sukurta  naudojant Python kalbą, skirta sekti asmenines pajamas ir išlaidas. Naudotojas gali įrašyti savo išlaidas ir pajamas, matyti visą istoriją, apskaičiuoti bendras išlaidas, pajamas, likusį balansą po išlaidų bei išsaugoti ar įkelti duomenis iš CSV failo. Programa supaprastina asmeninių finansų stebėjimą.

b) Kaip paleisti programą?
1. Pirmiausia, patikrinkite, ar kompiuteryje įdiegtas Python 3, jei ne – atsisiųskite.
2. Išsaugokite kodą faile, pavadintame ExpensesTracker.py.
3. Viršuje dešinėje pamatysite trikampiuką (Run Python File) VS CODE
4. Jei trikampiuko nematote, įveskite šią komandą į terminalą:
python  .\ExpensesTracker.py

c) Kaip naudotis programa?

Kai paleidžiama programa, pasirodo paprastas meniu su sunumeruotais pasirinkimais:
1. Pridėti išlaidas – įvedama data, aprašymas ir suma.
2. Pridėti pajamas – įvedamos pajamos.
3. Pašalinti įrašą – nurodamas įrašo numeris sąraše.
4. Peržiūrėti įrašus – parodomi visi iki šiol įvesti įrašai.
5. Bendros išlaidas – parodomos susumuotos išlaidos. 
6. Peržiūrėti balansą – parodomas likes balansas po išlaidų. 
7. Išsaugoti ir išeiti – duomenys išsisaugo ir uždaro programą.

Pagrindinė dalis / Analizė:

a) Kaip programa įgyvendina funkcinius reikalavimus:

Išlaidų pridėjimas-Kuriamas Expense objektas su data, aprašymu ir suma. Pridedamas per add_transaction().

Pajamų pridėjimas-Income klasė leidžia nenurodyti datos (naudojama šiandienos data).

Peržiūrėti įrašus-view_transactions() metodas rodo visus įrašus naudodamas get_summary().

Pašalinti įrašą-remove_transaction() metodas pašalina nurodytą įrašą pagal indeksą.

Suskaičiuoti sumas-total_expenses() ir total_income() susumuoja atitinkamus įrašus.

Apskaičiuoti balansą-balance() rodo skirtumą tarp pajamų ir išlaidų.

Išsaugoti į CSV-save_to_file() metodas išsaugo visus įrašus su antraštėmis į failą.

Įkelti iš CSV-load_from_file() skaito duomenis ir atkuria objektus programoje.

Singleton šablonas-ExpenseTracker klasė naudoja singleton šabloną, kad visur būtų viena instancija.

Rezultatai ir apibendrinimas:

a) Rezultatai (funkcinė išvestis):

Programa sėkmingai atlieka visus pagrindinius išlaidų sekimo veiksmus. Išbandžius programą paaiškėjo, kad duomenys teisingai išsaugomi ir įkeliami, skaičiavimai atliekami teisingai. Nors programa yra paprasta, buvo iššūkių užtikrinti duomenų įrašymo tikslumą, ypač įkeliant ir išsaugant duomenis I CSV failą.

b) Išvados:

Programa pilnai atitinka pagrindinius funkcinius tikslus. Jos struktūra aiški, kodas organizuotas ir lengvai išplečiamas. Visa svarbi informacija vartotojui pateikiama aiškiai ir suprantamai.

c) Ką būtų galima patobulinti ateityje:

- Kategorijų žymėjimas (pvz., Maistas, Būstas, Alga).
- Mėnesinės/metinės ataskaitos su diagrama ar suvestinė.
- Vartotojo paskyros su slaptažodžiais, kad būtų galima naudoti keliems vartotojams.






