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
chybovou hlášku a souběžně s tím program ukončí. Rovněž jsou zde umístěny i podmínky, které 
zajišťují vykreslení či vypsání dalších funkcí, v závislosti právě na zvoleném kartografickém 
zobrazení.


