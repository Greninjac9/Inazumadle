### IMPORTS ###
import flet as ft
from characters import CharacterRef, Characters
import random

def main(page: ft.Page):
    page.title = "INAZUMADLE"
    page.theme_mode = ft.ThemeMode.DARK

    #VARIABLES
    PJ = random.choice(Characters)
    Victory = False
    Defeat = False
    Tries = 6

    #################
    ### FUNCIONES ###
    #################

    ### FUNCIONES SEARCHBAR ###
    def handle_tap(e):
        Searchbar.open_view()
    def handle_click(e):
        text = e.control.data
        Searchbar.close_view(text)

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
                    elif (Char[Elementos[k]]).split(_)[0] == (PJ[Elementos[k]]).split(_)[0]:
                        COLORS.append(ft.colors.AMBER)
                    else:
                        COLORS.append(ft.colors.RED)
                # DETERMINA SI SE HA GANADO O PERDIDO:
                Tries -= 1
                if Char == PJ:
                    Victory = True
                elif Tries = 0:
                    Defeat = True
                break
        
        Searchbar.close_view()

        # FILA QUE CONTIENE TODOS LOS ELEMENTOS:
        Row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=25,
            controls=[
                ft.Container(
                    content=ft.Image(
                    src=("assets\images\\" + Char["Nombre"] + ".png"),
                    ),
                    height = 70,
                    width = 70,
                    bgcolor=COLORS[0],
                    border_radius = 10
                ),
                ft.Container(
                    content=ft.Image(
                    src = ("assets\images\\" + Char["Curso"] + ".png"),
                    height=700,
                    width = 700,
                    ),
                    height = 70,
                    width = 70,
                    bgcolor=COLORS[1],
                    border_radius = 10
                ),
                ft.Container(
                    content=ft.Image(
                    src=("assets\images\\" + Char["Elemento"] + ".png"),
                    ),
                    height = 70,
                    width = 70,
                    bgcolor=COLORS[2],
                    border_radius = 10
                ),
                ft.Container(
                    content=ft.Image(
                    src=("assets\images\\" + Char["Posición"] + ".png"),
                    fit = ft.ImageFit.FIT_WIDTH,
                    ),
                    border = ft.border.all(10, COLORS[3]),
                    margin = 50,
                    height = 70,
                    width = 70,
                    bgcolor=COLORS[3],
                    border_radius = 10
                ),
                ft.Container(
                    content=ft.Image(
                    src=("assets\images\\" + Char["Género"] + ".png"),
                    ),
                    height = 70,
                    width = 70,
                    bgcolor=COLORS[4],
                    border_radius = 10
                ),
                ft.Container(
                    content=ft.Image(
                    src=("assets\images\\" + Char["Invocador"] + ".png"),
                    ),
                    height = 70,
                    width = 70,
                    bgcolor=COLORS[5],
                    border_radius = 10
                ),
                ft.Container(
                    content=ft.Image(
                    src=("assets\images\\" + Char["EQUIPO"] + ".png"),
                    ),
                    height = 70,
                    width = 70,
                    bgcolor=COLORS[6],
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
        view_elevation=10,
        controls = [
            ft.ListTile(
                title = ft.Text(i), on_click = handle_click,
                data = i
                    )
            for i in CharacterRef
        ],
        on_submit = Comprobar,
        on_tap = handle_tap
    )

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls = [Searchbar],
    )
    )
    page.update()

ft.app(main)
