import flet as ft
import time
import sys
import os

def restart_program():
    time.sleep(2)
    python = sys.executable
    os.execl(python, python, * sys.argv)

def get_resource_path(relative_path):
    try:
        # PyInstaller almacena archivos de datos en una carpeta temporal
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Table = ft.Row(
          alignment=ft.MainAxisAlignment.CENTER,
          spacing = 15,
          controls=[
              ft.Container(
                  content=ft.Text("Jugador", weight=ft.FontWeight.BOLD),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Curso", weight=ft.FontWeight.BOLD),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Elemento", weight=ft.FontWeight.BOLD),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Posición"),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Género", weight=ft.FontWeight.BOLD),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Invocador", weight=ft.FontWeight.BOLD),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Nación", weight=ft.FontWeight.BOLD),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Debut", weight=ft.FontWeight.BOLD),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Equipo", weight=ft.FontWeight.BOLD),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),])