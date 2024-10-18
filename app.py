### IMPORTS ###
import flet as ft
from characters import CharacterRef, Characters, Table
import random
import time
import sys
import os

def restart_program():
    time.sleep(2)
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def main(page: ft.Page):
    def get_resource_path(relative_path):
        try:
            # PyInstaller almacena archivos de datos en una carpeta temporal
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    # PROPIEDADES DE LA PÁGINA
    page.title = "INAZUMADLE"
    page.bgcolor = ft.colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(
        image=ft.DecorationImage(src=get_resource_path("assets\\images\\WEB\\InazumadleBG.png"), fit = ft.ImageFit.COVER)
    )
    page.window.resizable = False
    page.window.width = 900
    page.window.height = 1080

    #VARIABLES
    PJ = random.choice(Characters) #Personaje a adivinar
    print("PJ: ", PJ["Nombre"])
    lv = ft.ListView()
    Tries = 6

    #################
    ### FUNCIONES ###
    #################
    
    ### FUNCIONES SEARCHBAR ###
    def handle_click(e):
        ft.Audio(
            src=get_resource_path("assets\\audio\\sfx\\OK.mp3"), autoplay=True)
        Searchbar.close_view("")
        ft.Audio(
            src=get_resource_path("assets\\audio\\sfx\\WINDOW_CLOSE.wav"), autoplay=True)
        time.sleep(0.15)
        Comprobar(e.control.data)
    def handle_change(e):
        Searchbar.open_view()
        list_to_show = [personaje for personaje in CharacterRef if e.data.lower() in personaje.lower()]
        lv.controls.clear()
        for i in list_to_show:
            lv.controls.append(ft.ListTile(title=ft.Text(f"{i}"), on_click=handle_click, data=i))
        Searchbar.update()

    ### FUNCION PRINCIPAL ###
    def Comprobar(e):
        nonlocal Tries
        Tries -= 1
        STATE = ""
        COLORS = []

        for i in CharacterRef:
            # COMPRUEBA QUE EL PERSONAJE ELEGIDO ESTÁ ENTRE LOS PERSONAJES DISPONIBLES
            # CAPITALIZAMOS PARA EVITAR PROBLEMAS KEY SENSITIVE
            if (Searchbar.value).capitalize() == i.capitalize() or e.capitalize() == i.capitalize():
                Char = Characters[CharacterRef.index(i)]
                # COMPRUEBA SI LOS ELEMENTOS COINCIDEN CON EL PERSONAJE POR ADIVINAR
                for k in range(9):
                    Elementos = ["Nombre", "Curso", "Elemento", "Posición", "Género", 
                                 "Invocador", "Nacionalidad", "Debut", "EQUIPO"]
                    # CAMBIA EL COLOR DEPENDIENDO DE SI ES IGUAL O NO
                    if Char[Elementos[k]] == PJ[Elementos[k]]:
                        COLORS.append(ft.colors.GREEN)
                    elif (Char[Elementos[k]]).split("_")[0] == (PJ[Elementos[k]]).split("_")[0]:
                        COLORS.append(ft.colors.AMBER)
                    else:
                        COLORS.append(ft.colors.RED)
                for k in COLORS:
                    STATE = "VICTORY"
                    if k == ft.colors.RED or k == ft.colors.AMBER:
                        STATE = ""
                        break
        
        Searchbar.close_view()

        # FILA QUE CONTIENE TODOS LOS ELEMENTOS:
        Row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing = 15,
            controls=[
                ft.Container(
                    content=ft.Image(
                        src=get_resource_path("assets\\images\\SPRITES\\" + Char["Nombre"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(5, COLORS[0]),
                    height = 80,
                    width = 80,
                    bgcolor=COLORS[0],
                    border_radius = 10,
                    margin = ft.margin.symmetric(8)
                ),
                ft.Container(
                    content=ft.Image(
                        src = get_resource_path("assets\\images\\MISCELANEO\\" + Char["Curso"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(10, COLORS[1]),
                    height = 80,
                    width = 80,
                    bgcolor=COLORS[1],
                    border_radius = 10,
                    margin = ft.margin.symmetric(8)
                ),
                ft.Container(
                    content=ft.Image(
                        src=get_resource_path("assets\\images\\MISCELANEO\\" + Char["Elemento"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(15, COLORS[2]),
                    height = 80,
                    width = 80,
                    bgcolor=COLORS[2],
                    border_radius = 10,
                    margin = ft.margin.symmetric(8)
                ),
                ft.Container(
                    content=ft.Image(
                        src=get_resource_path("assets\\images\\MISCELANEO\\" + Char["Posición"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(10, COLORS[3]),
                    height = 80,
                    width = 80,
                    bgcolor=COLORS[3],
                    border_radius = 10,
                    margin = ft.margin.symmetric(8)
                ),
                ft.Container(
                    content=ft.Image(
                        src=get_resource_path("assets\\images\\MISCELANEO\\" + Char["Género"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(15, COLORS[4]),
                    height = 80,
                    width = 80,
                    bgcolor=COLORS[4],
                    border_radius = 10,
                    margin = ft.margin.symmetric(8)
                ),
                ft.Container(
                    content=ft.Image(
                        src=get_resource_path("assets\\images\\MISCELANEO\\" + Char["Invocador"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(15, COLORS[5]),
                    height = 80,
                    width = 80,
                    bgcolor=COLORS[5],
                    border_radius = 10,
                    margin = ft.margin.symmetric(8)
                ),
                ft.Container(
                    content=ft.Image(
                        src=get_resource_path("assets\\images\\MISCELANEO\\" + Char["Nacionalidad"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(15, COLORS[6]),
                    height = 80,
                    width = 80,
                    bgcolor=COLORS[6],
                    border_radius = 10,
                    margin = ft.margin.symmetric(8)
                ),
                ft.Container(
                    content=ft.Image(
                        src=get_resource_path("assets\\images\\MISCELANEO\\" + Char["Debut"] + ".png"),
                        fit = ft.ImageFit.FILL,),
                    border = ft.border.all(10, COLORS[7]),
                    height = 80,
                    width = 80,
                    bgcolor=COLORS[7],
                    border_radius = 10,
                    margin = ft.margin.symmetric(8)
                ),
                ft.Container(
                    content=ft.Image(
                        src=get_resource_path("assets\\images\\EQUIPOS\\" + Char["EQUIPO"] + ".png"),
                        fit = ft.ImageFit.FILL,),
                    border = ft.border.all(5, COLORS[8]),
                    height = 80,
                    width = 80,
                    bgcolor=COLORS[8],
                    border_radius = 10,
                    margin = ft.margin.symmetric(8)
                ),
            ],
        )

        page.add(Row)
        ft.Audio(
            src=get_resource_path("assets\\audio\\sfx\\NEXT_MESSAGE.wav", autoplay=True))
        page.update()

        time.sleep(0.5)

        if STATE == "" and Tries == 0:
            STATE = "DEFEAT"
        if STATE == "VICTORY" or STATE == "DEFEAT":
            dlg_modal = ft.AlertDialog(
                modal = True,
                content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls = [
                ft.Audio(
                    src=get_resource_path("assets\\audio\\sfx\\" + STATE + ".mp3", autoplay=True),),
                ft.Container(
                        content=ft.Image(
                            src=get_resource_path("assets\\images\\SPRITES\\" + PJ["Nombre"] + ".png"),
                            fit = ft.ImageFit.FIT_WIDTH),
                        border = ft.border.all(5, COLORS[0]),
                        height = 140,
                        width = 140,
                        bgcolor=COLORS[0],
                        border_radius = 10,
                    ),
                ft.Text(CharacterRef[Characters.index(PJ)], size=30, weight=ft.FontWeight.BOLD),
                ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing = 15,
            controls=[
                ft.Container(
                    content=ft.Image(
                        src = get_resource_path("assets\\images\\MISCELANEO\\" + PJ["Curso"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(10, COLORS[0]),
                    height = 70,
                    width = 70,
                    bgcolor=COLORS[0],
                    border_radius = 10,
                    margin = ft.margin.symmetric(10)
                ),
                ft.Container(
                    content=ft.Image(
                        src=get_resource_path("assets\\images\\MISCELANEO\\" + PJ["Elemento"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(15, COLORS[0]),
                    height = 70,
                    width = 70,
                    bgcolor=COLORS[0],
                    border_radius = 10,
                    margin = ft.margin.symmetric(10)
                ),
                ft.Container(
                    content=ft.Image(
                        src=get_resource_path("assets\\images\\MISCELANEO\\" + PJ["Posición"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(10, COLORS[0]),
                    height = 70,
                    width = 70,
                    bgcolor=COLORS[0],
                    border_radius = 10,
                    margin = ft.margin.symmetric(10)
                ),
                ft.Container(
                    content=ft.Image(
                        src=get_resource_path("assets\\images\\MISCELANEO\\" + PJ["Género"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(15, COLORS[0]),
                    height = 70,
                    width = 70,
                    bgcolor=COLORS[0],
                    border_radius = 10,
                    margin = ft.margin.symmetric(10)
                ),
                ft.Container(
                    content=ft.Image(
                        src=get_resource_path("assets\\\images\MISCELANEO\\" + PJ["Invocador"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(15, COLORS[0]),
                    height = 70,
                    width = 70,
                    bgcolor=COLORS[0],
                    border_radius = 10,
                    margin = ft.margin.symmetric(10)
                ),
                ft.Container(
                    content=ft.Image(
                        src=get_resource_path("assets\\images\\MISCELANEO\\" + PJ["Nacionalidad"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(15, COLORS[0]), height = 70, width = 70, bgcolor=COLORS[0],
                    border_radius = 10,
                    margin = ft.margin.symmetric(10)
                ),
                ft.Container(
                    content=ft.Image(
                        src=get_resource_path("assets\\images\\MISCELANEO\\" + PJ["Debut"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(10, COLORS[0]), height = 70, width = 70, bgcolor=COLORS[0],
                    border_radius = 10,
                    margin = ft.margin.symmetric(10)
                ),
                ft.Container(
                    content=ft.Image(
                        src=get_resource_path("assets\\images\\EQUIPOS\\" + PJ["EQUIPO"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(5, COLORS[0]), height = 70, width = 70, bgcolor=COLORS[0],
                    border_radius = 10,
                    margin = ft.margin.symmetric(10)
                ),
            ],
        ),],),)
            page.open(dlg_modal)
    

    #################
    ### SEARCHBAR ###
    #################

    Searchbar = ft.SearchBar(
        view_elevation=4,
        controls = [lv,],
        on_change=handle_change,
    )

    # AÑADIR LOGO DE INAZUMADLE + SEARCHBAR AL INICIO
    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls = [
            ft.Column(
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls = [ft.Image(src = get_resource_path("assets\\images\\WEB\\Inazumadle.png"), width = 600, height = 200), Searchbar,
                        Table],)
        ],
    ),
    )
    page.update()

ft.app(main)
