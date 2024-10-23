import flet as ft

def PLAY(e):
          page.controls.clear()
          page.add(ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls = [ft.Column(
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls = [ft.Image(src = ("assets\\images\\WEB\\Inazumadle.png"), width = 600, height = 200), Searchbar, Table],)
          ],),)

Table = ft.Row(
          alignment=ft.MainAxisAlignment.CENTER,
          spacing = 15,
          controls=[
              ft.Container(
                  content=ft.Text("Jugador", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Curso", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Elemento", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Posición", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Género", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Invocador", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Nación", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Debut", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Equipo", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),])
