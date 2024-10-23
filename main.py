### IMPORTS ###
import flet as ft
from characters import CharacterRef, Characters
from extra import Table
import random

def ChooseCharacter():
      PJ = random.choice(Characters) #Personaje a adivinar
      return PJ

def main(page: ft.Page):
    PJ = ""
    Voiceline = ""
    lv = ft.ListView()
    Tries = 6
    FirstOpen = True
    
    page.title = "INAZUMADLE"
    page.bgcolor = ft.colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(image=ft.DecorationImage(src=("assets\\images\\WEB\\InazumadleBG.png"), fit = ft.ImageFit.COVER))
    page.window.resizable = False
    page.window.width = 1000
    page.window.height = 1080

    def handle_click(e):
        nonlocal FirstOpen
        page.overlay.append(ft.Audio(src=("assets\\audio\\sfx\\OK.mp3"), autoplay=True))
        page.update()
        Searchbar.close_view("")
        Comprobar(e.control.data)
        FirstOpen = True
    def handle_change(e):
        nonlocal FirstOpen
        if FirstOpen:
            page.overlay.append(ft.Audio(src=("assets\\audio\\sfx\\WINDOW_OPEN.wav"), autoplay=True))
            page.update()
            FirstOpen = False
        page.overlay.append(ft.Audio(src=("assets\\audio\\sfx\\NEXT_MESSAGE.wav"), autoplay=True))
        page.update()
        Searchbar.open_view()
        list_to_show = [personaje for personaje in CharacterRef if e.data.lower() in personaje.lower()]
        lv.controls.clear()
        for i in list_to_show:
            lv.controls.append(ft.ListTile(title=ft.Text(f"{i}"), on_click=handle_click, data=i))
        Searchbar.update()

    def GetVoiceline():
        page.overlay.append(ft.Audio(src=("assets\\audio\\voicelines\\" + PJ["Nombre"] + ".mp3"), autoplay=True))
        page.update()

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
                for k in range(10):
                    Elementos = ["Nombre", "Curso", "Elemento", "Posición", "Género", 
                                 "Invocador", "Dorsal", "Nacionalidad", "Debut", "EQUIPO"]
                    # CAMBIA EL COLOR DEPENDIENDO DE SI ES IGUAL O NO
                    if Elementos[k] == "Dorsal":
                        if Char[Elementos[k]] == PJ[Elementos[k]]:
                            DorsalValue = ""
                            COLORS.append(ft.colors.GREEN)
                        elif Char[Elementos[k]] == "" or PJ[Elementos[k]] == "":
                            DorsalValue = ""
                            COLORS.append(ft.colors.RED)
                        elif int(Char[Elementos[k]]) < int(PJ[Elementos[k]]):
                            DorsalValue = "MAYOR"
                            if int(Char[Elementos[k]]) >= int(PJ[Elementos[k]]) - 3:
                                COLORS.append(ft.colors.AMBER)
                            else:
                                COLORS.append(ft.colors.RED)
                        else:
                            DorsalValue = "MENOR"
                            if int(Char[Elementos[k]]) <= int(PJ[Elementos[k]]) + 3:
                                COLORS.append(ft.colors.AMBER)
                            else:
                                COLORS.append(ft.colors.RED)
                    else:
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

        Row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing = 15,
            controls=[
                ft.Container(
                    content=ft.Image(
                        src=("assets\\images\\SPRITES\\" + Char["Nombre"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(5, COLORS[0]),
                    height = 80, width = 80,
                    bgcolor=COLORS[0], border_radius = 10,
                    margin = ft.margin.symmetric(4),
                ),
                ft.Container(
                    content=ft.Image(
                        src = ("assets\\images\\MISCELANEO\\" + Char["Curso"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(10, COLORS[1]),
                    height = 80, width = 80,
                    bgcolor=COLORS[1], border_radius = 10,
                    margin = ft.margin.symmetric(4)
                ),
                ft.Container(
                    content=ft.Image(
                        src=("assets\\images\\MISCELANEO\\" + Char["Elemento"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(15, COLORS[2]),
                    height = 80, width = 80,
                    bgcolor=COLORS[2], border_radius = 10,
                    margin = ft.margin.symmetric(4)
                ),
                ft.Container(
                    content=ft.Image(
                        src=("assets\\images\\MISCELANEO\\" + Char["Posición"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(10, COLORS[3]),
                    height = 80, width = 80,
                    bgcolor=COLORS[3], border_radius = 10,
                    margin = ft.margin.symmetric(4)
                ),
                ft.Container(
                    content=ft.Image(
                        src=("assets\\images\\MISCELANEO\\" + Char["Género"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(15, COLORS[4]),
                    height = 80, width = 80,
                    bgcolor=COLORS[4], border_radius = 10,
                    margin = ft.margin.symmetric(4)
                ),
                ft.Container(
                    content=ft.Image(
                        src=("assets\\images\\MISCELANEO\\" + Char["Invocador"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(15, COLORS[5]),
                    height = 80, width = 80,
                    bgcolor=COLORS[5], border_radius = 10,
                    margin = ft.margin.symmetric(4)
                ),
                ft.Container(
                    image=ft.DecorationImage(src=("assets\\images\\MISCELANEO\\" + DorsalValue + ".png"), opacity=0.4),
                    content=ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[ft.Text(Char["Dorsal"], size=50, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK)]),
                    height = 80, width = 80,
                    bgcolor=COLORS[6], border_radius = 10,
                    margin = ft.margin.symmetric(4)
                ),
                ft.Container(
                    content=ft.Image(
                        src=("assets\\images\\MISCELANEO\\" + Char["Nacionalidad"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(15, COLORS[7]),
                    height = 80, width = 80,
                    bgcolor=COLORS[7], border_radius = 10,
                    margin = ft.margin.symmetric(4)
                ),
                ft.Container(
                    content=ft.Image(
                        src=("assets\\images\\MISCELANEO\\" + Char["Debut"] + ".png"),
                        fit = ft.ImageFit.SCALE_DOWN,),
                    border = ft.border.all(10, COLORS[8]),
                    height = 80, width = 80,
                    bgcolor=COLORS[8], border_radius = 10,
                    margin = ft.margin.symmetric(4)
                ),
                ft.Container(
                    content=ft.Image(
                        src=("assets\\images\\EQUIPOS\\" + Char["EQUIPO"] + ".png"),
                        fit = ft.ImageFit.SCALE_DOWN,),
                    border = ft.border.all(5, COLORS[9]),
                    height = 80, width = 80,
                    bgcolor=COLORS[9], border_radius = 10,
                    margin = ft.margin.symmetric(4)
                ),
            ],
        )                    
        page.add(Row)
        page.update()

        if STATE == "" and Tries == 0:
            STATE = "DEFEAT"
        if STATE != "":
            dlg_modal = ft.AlertDialog(
                modal = True,
                content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls = [
                ft.Audio(src=("assets\\audio\\sfx\\" + STATE + ".mp3"), autoplay=True),
                ft.Container(
                        content=ft.Image(
                            src=("assets\\images\\SPRITES\\" + PJ["Nombre"] + ".png"),
                            fit = ft.ImageFit.FIT_WIDTH),
                        border = ft.border.all(5, COLORS[0]),
                        height = 140, width = 140,
                        bgcolor=COLORS[0], border_radius = 10,
                        on_click=GetVoiceline,
                    ),
                ft.Text(CharacterRef[Characters.index(PJ)], size=30, weight=ft.FontWeight.BOLD),
                ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing = 15,
            controls=[
                ft.Container(
                    content=ft.Image(
                        src = ("assets\\images\\MISCELANEO\\" + PJ["Curso"] + ".png"),
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
                        src=("assets\\images\\MISCELANEO\\" + PJ["Elemento"] + ".png"),
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
                        src=("assets\\images\\MISCELANEO\\" + PJ["Posición"] + ".png"),
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
                        src=("assets\\images\\MISCELANEO\\" + PJ["Género"] + ".png"),
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
                        src=("assets\\images\\MISCELANEO\\" + PJ["Invocador"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(15, COLORS[0]),
                    height = 70,
                    width = 70,
                    bgcolor=COLORS[0],
                    border_radius = 10,
                    margin = ft.margin.symmetric(10)
                ),
                ft.Container(
                    content=ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[ft.Text(Char["Dorsal"], size=50, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK)]),
                    border = ft.border.all(15, COLORS[0]), height = 70, width = 70, bgcolor=COLORS[0],
                    border_radius = 10,
                    margin = ft.margin.symmetric(10)
                ),
                ft.Container(
                    content=ft.Image(
                        src=("assets\\images\\MISCELANEO\\" + PJ["Nacionalidad"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(15, COLORS[0]), height = 70, width = 70, bgcolor=COLORS[0],
                    border_radius = 10,
                    margin = ft.margin.symmetric(10)
                ),
                ft.Container(
                    content=ft.Image(
                        src=("assets\\images\\MISCELANEO\\" + PJ["Debut"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(10, COLORS[0]), height = 70, width = 70, bgcolor=COLORS[0],
                    border_radius = 10,
                    margin = ft.margin.symmetric(10)
                ),
                ft.Container(
                    content=ft.Image(
                        src=("assets\\images\\EQUIPOS\\" + PJ["EQUIPO"] + ".png"),
                        fit = ft.ImageFit.FIT_WIDTH,),
                    border = ft.border.all(5, COLORS[0]), height = 70, width = 70, bgcolor=COLORS[0],
                    border_radius = 10,
                    margin = ft.margin.symmetric(10)
                ),
                ],
        ),],),)
            page.open(dlg_modal)

    Searchbar = ft.SearchBar(
        view_elevation=4,
        controls = [lv,],
        on_change=handle_change,
    )
    
    def PLAY(e):
            nonlocal PJ      
            nonlocal Voiceline
            page.overlay.append(ft.Audio(src=("assets\\audio\\sfx\\OK.mp3"), autoplay=True))
            page.update()
            page.controls.clear()
            PJ = ChooseCharacter()
            Voiceline = ("assets\\audio\\voicelines\\" + PJ["Nombre"] + ".mp3")
            page.add(ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls = [ft.Column(
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls = [ft.Image(src = ("assets\\images\\WEB\\Inazumadle.png"), width = 600, height = 200), Searchbar, Table],)
              ],),)
        
    page.add(
          ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[ft.Column(
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls = [ft.Image(src = ("assets\\images\\WEB\\Inazumadle.png"), width = 600, height = 200),ft.FilledButton(text="Jugar", on_click=PLAY)],
                  ),])
        )

ft.app(main)
