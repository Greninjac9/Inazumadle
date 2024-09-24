import flet as ft
from characters import CharacterRef

def main(page: ft.Page):
    page.title = "INAZUMADLE"
    t = ft.Text()

    #################
    ### FUNCIONES ###
    #################

    def dropdown_change(e):
        for i in CharacterRef:
            if anchor.value == i:
                
        
        Row = ft.Row(
            spacing=25,
            controls=[
                ft.Container(
                    content=ft.Image(
                    src=f"assets\ARION_SHERWIND.png",
                    ),
                    height = 70,
                    width = 70,
                    bgcolor=ft.colors.RED,
                    border_radius = 10
                ),
                ft.Container(
                    content=ft.Text("1"),
                    height = 70,
                    width = 70,
                    bgcolor=ft.colors.RED,
                    border_radius = 10
                ),
            ]
        )
        t.value = f"Dropdown changed to {anchor.value}"
        anchor.close_view()
        page.add(Row)
        page.update()
    
    def handle_tap(e):
        anchor.open_view()
    def handle_click(e):
        text = e.control.data
        anchor.close_view(text)

    ### SEARCHBAR ###
    anchor = ft.SearchBar(
        autofocus=True,
        view_elevation=10,
        controls = [
            ft.ListTile(
                title = ft.Text(i),
                on_click = handle_click,
                data = i
                    )
            for i in CharacterRef
        ],
        on_submit = dropdown_change,
        on_tap = handle_tap
    )


    page.add(anchor,t)
ft.app(main)