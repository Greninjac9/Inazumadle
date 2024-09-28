### IMPORTS ###
import flet as ft
from characters import CharacterRef, Characters
import random

def main(page: ft.Page):
    page.title = "INAZUMADLE"
    page.bgcolor = ft.colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(
        image=ft.DecorationImage(src=r"assets\images\WEB\InazumadleBG.png", fit = ft.ImageFit.COVER)
    )
    page.window.resizable = False
    page.window.width = 830
    page.window.height = 1000

    #VARIABLES
    PJ = random.choice(Characters)
    lv = ft.ListView()

    #################
    ### FUNCIONES ###
    #################

    ### FUNCIONES SEARCHBAR ###
    def handle_tap(e):
        Searchbar.open_view()
    def handle_click(e):
        text = e.control.data
        Searchbar.close_view(text)
    def handle_change(e):
        list_to_show = [personaje for personaje in CharacterRef if e.data.lower() in personaje.lower()]
        lv.controls.clear()
        for i in list_to_show:
            lv.controls.append(ft.ListTile(title=ft.Text(f"{i}"), on_click=handle_click, data=i))
        Searchbar.update()

    ### FUNCION PRINCIPAL ###
    def Comprobar(e):
        COLORS = []
        
        for i in CharacterRef:
            # COMPRUEBA QUE EL PERSONAJE ELEGIDO ESTÁ ENTRE LOS PERSONAJES DISPONIBLES
            # CAPITALIZAMOS PARA EVITAR PROBLEMAS KEY SENSITIVE
            if (Searchbar.value).capitalize() == i.capitalize():
                Char = Characters[CharacterRef.index(i)]
                # COMPRUEBA SI LOS ELEMENTOS COINCIDEN CON EL PERSONAJE POR ADIVINAR
                for k in range(7):
                    Elementos = ["Nombre", "Curso", "Elemento", "Posición", "Género", "Invocador", "EQUIPO"]
                    # CAMBIA EL COLOR DEPENDIENDO DE SI ES IGUAL O NO
                    if Char[Elementos[k]] == PJ[Elementos[k]]:
                        COLORS.append(ft.colors.GREEN)
                    elif (Char[Elementos[k]]).split("_")[0] == (PJ[Elementos[k]]).split("_")[0]:
                        COLORS.append(ft.colors.AMBER)
                    else:
                        COLORS.append(ft.colors.RED)
        
        Searchbar.close_view()

        # FILA QUE CONTIENE TODOS LOS ELEMENTOS:
        Row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=25,
            controls=[
                ft.Container(
                    content=ft.Image(
                        src=(r"assets\images\SPRITES\\" + Char["Nombre"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(5, COLORS[0]),
                    height = 70,
                    width = 70,
                    bgcolor=COLORS[0],
                    border_radius = 10,
                ),
                ft.Container(
                    content=ft.Image(
                        src = (r"assets\images\MISCELANEO\\" + Char["Curso"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(10, COLORS[1]),
                    height = 70,
                    width = 70,
                    bgcolor=COLORS[1],
                    border_radius = 10,
                ),
                ft.Container(
                    content=ft.Image(
                        src=(r"assets\images\MISCELANEO\\" + Char["Elemento"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(15, COLORS[2]),
                    height = 70,
                    width = 70,
                    bgcolor=COLORS[2],
                    border_radius = 10
                ),
                ft.Container(
                    content=ft.Image(
                        src=(r"assets\images\MISCELANEO\\" + Char["Posición"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(10, COLORS[3]),
                    height = 70,
                    width = 70,
                    bgcolor=COLORS[3],
                    border_radius = 10
                ),
                ft.Container(
                    content=ft.Image(
                        src=(r"assets\images\MISCELANEO\\" + Char["Género"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(15, COLORS[4]),
                    height = 70,
                    width = 70,
                    bgcolor=COLORS[4],
                    border_radius = 10
                ),
                ft.Container(
                    content=ft.Image(
                        src=(r"assets\images\MISCELANEO\\" + Char["Invocador"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(15, COLORS[5]),
                    height = 70,
                    width = 70,
                    bgcolor=COLORS[5],
                    border_radius = 10
                ),
                ft.Container(
                    content=ft.Image(
                        src=(r"assets\images\EQUIPOS\\" + Char["EQUIPO"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(3, COLORS[6]), height = 70, width = 70, bgcolor=COLORS[6],
                    border_radius = 10
                ),
            ]
        )

        page.add(Row) 
        page.update()

    #################
    ### SEARCHBAR ###
    #################

    Searchbar = ft.SearchBar(
        view_elevation=4,
        controls = [
            lv,
        ],
        on_submit = Comprobar,
        on_tap = handle_tap,
        on_change=handle_change,
    )

    # AÑADIR LOGO DE INAZUMADLE + SEARCHBAR AL INICIO
    page.add(
        ft.Container(
                    foreground_decoration = ft.Image(
                        src=(r"assets\InazumadleBG"),
                        fit = ft.ImageFit.COVER,),
                ),
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls = [
            ft.Column(
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls = [ft.Image(src = r"assets\images\WEB\Inazumadle.png", width = 600, height = 300), Searchbar],)
        ],
    ),
    )
    page.update()

ft.app(main)
