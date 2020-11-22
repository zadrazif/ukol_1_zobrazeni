# Dokumentace k úkolu 1
## Úvod
Tento soubor slouží jako uživatelská dokumentace, která uživateli programu popíše jeho strukturu, 
funkce a vysvětlí, jak s ním vhodně zacházet. Jedná se o pomůcku při počítání a kreslení 
kartografických zobrazení. Zdrojový kód byl vytvořen v rámci tvorby prvního úkolu na cvičení
z předmětu Úvod do programování.
## Základní stavba programu
Základem programu je funkce umístěná na řádku 131 až 171. Jedná se o funkci do níž uživatel
postupně vkládá jednotlivé vstupy (input), se kterými následně program pracuje. Těmito vstupy
jsou: zkratka vybraného zobrazení, zeměpisná šířka a délka (ve stupních), celočíslené měřítko 
a volitelný poloměr Země. Zároveň jsou inputy ošetřeny proti chybovým hláškám a to pomocí podmínek
(if, elif, else). Pokud je některá ze zadaných podmínek porušena, program vypíše předepsanou 
chybovou hlášku a souběžně s tím program ukončí. Rovněž jsou zde umístěny i podmínky, které 
zajišťují vykreslení či vypsání dalších funkcí, v závislosti právě na zvoleném kartografickém 
zobrazení a důležitá proměnná km_na_px, která zajišťuje převod kilometrů na pixely, s nimiž 
pak program operuje při kreslení.
## Převod souřadnic na milimetry v mapě
Jednou ze stěžejních funkcí definovaných v programu je schopnost převádět vložené hodnoty souřadnic
na milimetry, a to pro všechna tři volitelná zobrazení. Souřadnice bodů pro Postelovo a Lambertovo
kuželové zobrazení jsou vypsány v polární soustavě a pro Marinovo v soustavě kartézské. Uživatelem 
nastavené parametry jsou zde využity pro přepočet vstupních hodnot na hodnoty v mm, které prozrazují,
kam kreslit jednotlivé body v případě, že bychom se je rozhodli přenést např. na papír. Výstupem z 
funkce je print(), který výsledné hodnoty uživateli vytiskne. 
## Želví grafika
Velmi důležitou součástí zdrojového kódu jsou i funkce, které nám zajistí vykreslení zeměpisných
sítí v želví grafice pro jakékoli ze tří nabízených zobrazení. Aby se něco takového mohlo uskutečnit, 
je potřeba zavolat si do programu hned na začátku modul turtle a importovat z něj všechny potřebné
funkce. V tomto případě se jednalo o setpos (přesunutí na zadanou pozici), fd (forward; pohyb 
vpřed), right (pootočí "tužku" o zvolený počet stupňů doprava) , left (stejné chování jako u right 
ale doprava), exitonclick (po kliknutí na vykreslenou síť ukončí program), penup (zvednutí tužky), 
pendown (položení tužky), circle (vykreslí kruh o zadaném radiusu) a speed (určuje rychlost vykreslování
sítě.   


