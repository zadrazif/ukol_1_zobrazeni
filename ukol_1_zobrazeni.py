import turtle, math
from turtle import setpos, right, left, penup, pendown, circle, speed, fd, exitonclick

#Funkce, která vytváří zeměpisnou síť v Postelově zobrazení (azimutální zobrazení)
def postel(polomer_Zeme, meritko, km_na_px):
    radius1 = polomer_Zeme*math.radians(10)/km_na_px
    radius2 = radius1
    speed(10)
    penup()
    right(90)
    fd(radius1)
    left(90)
    pendown()
    for i in range (18):
        circle(radius1)
        radius1 += radius2
        penup()
        right(90)
        fd(radius2)
        left(90)
        pendown()
    penup()
    setpos(0,0)
    pendown()
    for j in range (36):
        fd(polomer_Zeme*math.radians(180)/km_na_px)
        penup()
        setpos(0,0)
        pendown()
        left(10)

#Funkce, která vytváří zeměpisnou síť v Marinově zobrazení (válcové zobrazení)
def marin(polomer_Zeme, meritko, km_na_px):
    x0 = -math.radians(180)*polomer_Zeme/km_na_px
    y0 = math.radians(90)*polomer_Zeme/km_na_px
    xy_roz = polomer_Zeme*math.radians(10)/km_na_px
    speed(100)
    penup()
    setpos(x0,y0)
    pendown()
    for i in range (19):
        fd(polomer_Zeme*math.radians(360)/km_na_px)
        y0 -= xy_roz
        penup()
        setpos(x0,y0)
        pendown()
    right(90)
    y0 = math.radians(90)*polomer_Zeme/km_na_px
    penup()
    setpos(x0,y0)
    pendown()

    for j in range (37): 
        fd(polomer_Zeme*math.radians(180)/km_na_px)
        x0 += xy_roz
        penup()
        setpos(x0,y0)
        pendown()

#Funkce, která vytváří zeměpisnou síť v Lambertově kuželovém zobrazení (kuželové zobrazení)
def lambert(polomer_Zeme, meritko, km_na_px):
    delta = 10
    radius1 = 2*polomer_Zeme*math.sin(math.radians(delta)/2)/math.cos(math.radians(30))/km_na_px
    speed(100)
    left(45)
    for i in range(37):
        fd(2*polomer_Zeme*math.sin(math.radians(180)/2)/math.cos(math.radians(30))/km_na_px)
        penup()
        setpos(0,0)
        pendown()
        right(7.5)
    left(7.5)

    for j in range(18):
        fd(radius1)
        left(90)
        circle(radius1,270)
        penup()
        setpos(0,0)
        pendown()
        delta +=10
        radius1 = (2*polomer_Zeme*math.sin(math.radians(delta)/2))/(math.cos(math.radians(30))*km_na_px)

#Funkce, která vypočitá souřadnice zvoleného bodu na mapě v Postelově zobrazení
def souradnice_bodu_v_mm_postel(sirka, delka, polomer_Zeme, meritko, km_na_px):
    if delka >= 0:
        if delka <= 90:
            uhel = 270 + delka
        if delka > 90 and delka <= 180:
            uhel = delka - 90
    elif delka < 0:
        if delka >= -90:
            uhel = delka + 270
        if delka < -90 and delka >= -180:
            uhel = delka + 270

    if sirka >= -90: 
        if sirka <= 90:
            r = ((polomer_Zeme*math.radians(90-sirka)/km_na_px)*0.3)
    print("Zvolené souřadnice se v mapě od středu nachází pod úhlem", uhel, "° a ve vzdálenosti", r, "mm")

#Funkce, která vypočítá souřadnice zvoleného bodu na mapě v Lambertově zobrazení
def souradnice_bodu_v_mm_lambert(sirka, delka, polomer_Zeme, meritko, km_na_px):
    if delka >= 0:
        if delka <= 120:
            uhel = delka * 0.75 + 270
        elif delka > 120 and delka <= 180:
            uhel = delka * 0.75 - 90
    elif delka < 0:
        if delka >= -90:
            uhel = delka * 0.75 + 270
        elif delka < -90 and delka >= -180:
            uhel = delka * 0.75 + 270
    else:
        exit("Byla zadána neplatná zeměpisná délka")


#Funkce, která umožňuje zadávání vstupních hodnot vybraných zobrazení
def vyber_zobrazeni():
    print("""Vyber si jedno z těchto zobrazení a vepiš jeho zkratku: 
    Po (Postelovo)
    Ma (Marinovo)
    Lk (Lambertovo kuželové)""")
    
    projection = input("Zadej zkratku vybraného mapového zobrazení:")
    
    selected_projections = ["Po", "Ma", "Lk"]
    if projection not in selected_projections:
        exit("Byla vybrána neplatná zkratka. Ukončuji program.")

    meritko = float(input("Zadej celočíselné měřítko mapy: 1:")) 
    
    if meritko < 0 or meritko % 1 != 0:
        exit("Zadali jste příliš malé nebo neceločíselné číslo. Ukončuji program.") 
    
    polomer_Zeme = int(float(input("Zadej poloměr Země:")))
    
    if polomer_Zeme < 0:
        exit("Zadali jste příliš malé číslo. Ukončuji program.")
    if polomer_Zeme == 0:
        polomer_Zeme = 6371.11
    
    km_na_px = 3/10000000 * meritko
    
    sirka = int(float(input("Zadej zeměpisnou šířku ve stupních:")))
    
    delka = int(float(input("Zadej zeměpisnou délku ve stupních:")))
    
    if projection == "Po":
        souradnice_bodu_v_mm_postel(sirka, delka, polomer_Zeme, meritko, km_na_px)
        postel(polomer_Zeme, meritko, km_na_px)
    elif projection == "Ma":
        marin(polomer_Zeme, meritko, km_na_px)
    elif projection == "Lk":
        souradnice_bodu_v_mm_lambert(sirka, delka, polomer_Zeme, meritko, km_na_px)
        lambert(polomer_Zeme, meritko, km_na_px)
    exitonclick()
vyber_zobrazeni()