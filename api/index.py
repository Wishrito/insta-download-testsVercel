from os import path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse


class App(FastAPI):
    def __init__(self):
        super().__init__()  # Appelle le constructeur de FastAPI

        @self.get("/", response_class=HTMLResponse)
        def read_root():
            return self._render_page('home')

    def _render_page(self, page_name: str) -> str:
        try:
            # Utilisation d'un contexte de gestion pour ouvrir le fichier
            with open(path.join('data', 'src', 'pages', f'{page_name}.html'), 'r') as file:
                page = file.read()
            return page
        except FileNotFoundError:
            return "<h1>Page not found</h1>"


# Crée une instance de l'application
app = App()
