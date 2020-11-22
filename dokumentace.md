# Dokumentace k úkolu 1
### Úvod
Tento soubor slouží jako uživatelská dokumentace, která uživateli programu popíše jeho strukturu, 
funkce, principy a vysvětlí, jak s ním vhodně zacházet. Jedná se o užitečnou pomůcku při 
počítání a kreslení kartografických zobrazení. Zdrojový kód byl vytvořen v rámci tvorby 
prvního úkolu na cvičení z předmětu Úvod do programování.
### Základní stavba programu
Celý zdrojový kód sestává ze sedmi funkcí a tou hlavní je ta zcela na konci. Tato funkce je 
umístěna na řádku 131 až 171. Jedná se o funkci do níž uživatel postupně vkládá jednotlivé
vstupy (*input*), se kterými následně program pracuje. Těmito vstupy jsou: zkratka vybraného
zobrazení, zeměpisná šířka a délka (ve stupních), celočíslené měřítko a volitelný poloměr
Země. Některé tyto proměnné jsou ihned po vložení převedeny ze stringu do floatu či integeru, 
aby bylo možné je nadále využívat např. při výpočtu dalších proměnných. Některé inputy 
jsou zároveň ošetřeny proti nežádoucím hodnotám a to pomocí podmínek (*if, elif, else*). 
Pokud je některá ze zadaných podmínek porušena, program vypíše předepsanou chybovou hlášku
a souběžně s tím program ukončí (*exit()*). Rovněž jsou zde umístěny i podmínky, které zajišťují
vykreslení či vypsání dalších funkcí, v závislosti právě na zvoleném kartografickém zobrazení 
a důležitá proměnná *km_na_px*, která zajišťuje převod kilometrů na pixely, s nimiž pak program
operuje při kreslení. Pro lepší přehlednost a pochopení programu jsou všechny funkce opatřeny 
komentářem, který odhaluje způsob využití dané funkce a začíná vždy mřížkou (*#*). 
### Převod souřadnic na milimetry v mapě
Jednou ze stěžejních funkcí definovaných v programu je schopnost převádět vložené hodnoty souřadnic
na milimetry, a to pro všechna tři volitelná zobrazení (viz řádky 85 až 128). Souřadnice bodů pro
Postelovo a Lambertovo kuželové zobrazení jsou vypsány v polární soustavě a pro Marinovo v 
soustavě kartézské. Uživatelem nastavené parametry jsou zde využity pro přepočet vstupních hodnot
na hodnoty v mm, které prozrazují, kam kreslit jednotlivé body v případě, že bychom se je 
rozhodli přenést např. na papír. Výstupem z funkce je *print()*, který výsledné hodnoty uživateli
vytiskne. U všech tří zobrazení jsmem vycházel ze zobrazovacích rovnic, které nám byly poskytnuty
cvičícím a jejichž znění bylo potřeba znát i při tvorbě želví grafiky. Kvůli těmto vzorcům tak
musel být do kódu naimportován modul *math*, který umí například pomocí *radians.* umně převádět 
stupně na radiány.
### Želví grafika
Velmi důležitou součástí zdrojového kódu jsou totiž i funkce, které nám zajistí vykreslení zeměpisných
sítí v želví grafice pro jakékoli ze tří nabízených zobrazení. Aby se něco takového mohlo uskutečnit, 
je potřeba zavolat si do programu hned na začátku mimo *math* i modul *turtle* a importovat z něj 
všechny potřebné funkce. V tomto případě se jednalo o *setpos* (přesunutí na zadanou pozici), *fd* 
(*forward*; pohyb vpřed), *right* (pootočí "tužku" o zvolený počet stupňů doprava) , *left* (stejné chování
jako u right ale doprava), *exitonclick* (po kliknutí na vykreslenou síť ukončí program), *penup* (zvednutí
tužky), *pendown* (položení tužky), *circle* (vykreslí kruh o zadaném radiusu) a *speed* (určuje rychlost 
vykreslování sítě. Základem úspěchu vykreslení sítě je především *for cyklus* neboli funkce, která v počtu
nastavených opakování kreslí zadané údaje. V tomto případě byla nejvíce využita při tvorbě kružnic (funkce 
*circle*, resp. 3/4 kružnic (rovnoběžky) a poledníků a rovnoběžek v Marinově zobrazení. Při tvorbě kódu
je také velmi důležité dát si pozor na směr šipky, která kreslí linie. Například i přes použití *setpos*,
*pendown* či *penup*, zůstavá vektor natočení šipky stále stejný a je potřeba s ním otáčet tak, jak je potřeba.
K tomu nám pomáhají již zmíněné funkce *left* a *right*.
### Závěr
Pevně věřím, že program v sobě neobsahuje žádné hrubé chyby a v rámci možností splní požadované účely 
a ulehčí tak uživateli práci při tvorbě kartografických sítí. 


-----:
Filip Zadražil



