from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Button


class CalculatorApp(App[None]):
    def compose(self) -> ComposeResult:
        with Grid():
            yield Button("AC")
            yield Button("+/-")
            yield Button("%")
            yield Button.warning("/")
            yield Button("7")
            yield Button("8")
            yield Button("9")
            yield Button.warning("*")
            yield Button("4")
            yield Button("5")
            yield Button("6")
            yield Button.warning("-")
            yield Button("1")
            yield Button("2")
            yield Button("3")
            yield Button.warning("+")
            yield Button("0")
            yield Button(".")
            yield Button.warning("=")


if __name__ == "__main__":
    CalculatorApp().run()
