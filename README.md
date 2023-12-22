# Generátor textu (“Český Lorem Ipsum”)

Tento projekt obsahuje jednoduchý generátor textu, který vytváří text na základě slabik. Kód používá bigramy (páry sousedních slabik) pro generování textu.

## Jak to funguje

Kód nejprve rozdělí vstupní text na slabiky. Jako text jsem vybral úryvek z povinné četby ‘Petr a Lucie’. Poté vytvoří bigramy (páry sousedních slabik) a list pro uchování následníků každé slabiky. Při generování textu vybírá následující slabiku na základě aktuální slabiky pomocí bigramů. Pro práci s textem jsem použil knihovnu NLTK, kterou jsem našel v souvislosti s prací s textem.

## Poznámky
Původně jsem chtěl generátor vytvořit na základě pravděpodobnosti výskytu slabik v českém jazyce a následnými podmínkami na ošetření navazování a opakování slabik, avšak k tomuto řešení jsem na internetu nenašel potřebná data. 
Pokud změníme “text”, bude se lišit i výstup kódu.
