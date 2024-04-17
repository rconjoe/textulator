from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Button, Digits
from textual.reactive import reactive


class CalculatorApp(App[None]):
    CSS_PATH = "main.css"

    number_displayed = reactive("0")

    def compose(self) -> ComposeResult:
        yield Digits("1234", id="display")
        with Grid():
            yield Button("AC", classes="top-button")
            yield Button("+/-", classes="top-button")
            yield Button("%", classes="top-button")
            yield Button.warning("/")
            yield Button("7", id="number-7", classes="number-button")
            yield Button("8", id="number-8", classes="number-button")
            yield Button("9", id="number-9", classes="number-button")
            yield Button.warning("*")
            yield Button("4", id="number-4", classes="number-button")
            yield Button("5", id="number-5", classes="number-button")
            yield Button("6", id="number-6", classes="number-button")
            yield Button.warning("-")
            yield Button("1", id="number-1", classes="number-button")
            yield Button("2", id="number-2", classes="number-button")
            yield Button("3", id="number-3", classes="number-button")
            yield Button.warning("+")
            yield Button("0", id="number-0", classes="number-button")
            yield Button(".")
            yield Button.warning("=")


if __name__ == "__main__":
    CalculatorApp().run()
