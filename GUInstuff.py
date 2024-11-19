import flet as ft
from genztranslator import GenZTranslator


def main(page):
    translator = GenZTranslator()
    page.scroll = "adaptive"
    page.title = "genZ translator"

    def send_button_clicked(e):
        msg = translator.translate_genz(text_input.value)
        text.value = msg
        text_input.value = ""
        page.update()

    text = ft.Text(color=ft.colors.RED, size= 20, selectable=True)
    text_input = ft.TextField(hint_text="Translate genZ")
    send_button = ft.ElevatedButton(text="Submit", on_click=send_button_clicked)
    page.add(text_input, send_button, text)

ft.app(main)