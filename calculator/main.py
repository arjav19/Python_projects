from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class CalculatorLayout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # Output Display Label
        self.output_label = Label(size_hint_y=0.75, font_size=50)
        self.output_label.bind(height=self.resize_label_text)
        self.add_widget(self.output_label)

        # Button Symbols Grid Configuration
        button_symbols = (
            "1",
            "2",
            "3",
            "+",
            "4",
            "5",
            "6",
            "-",
            "7",
            "8",
            "9",
            ".",
            "0",
            "*",
            "/",
            "=",
        )

        button_grid = GridLayout(cols=4, size_hint_y=2)

        # Add and bind buttons cleanly in a single loop
        for symbol in button_symbols:
            btn = Button(text=symbol)
            if symbol == "=":
                btn.bind(on_press=self.evaluate_result)
            else:
                btn.bind(on_press=self.print_button_text)
            button_grid.add_widget(btn)

        self.add_widget(button_grid)

        # Clear Button
        clear_button = Button(text="Clear", size_hint_y=None, height=100)
        clear_button.bind(on_press=self.clear_label)
        self.add_widget(clear_button)

    def print_button_text(self, instance):
        # Reset if display currently shows an error state
        if self.output_label.text == "Error":
            self.output_label.text = ""
        self.output_label.text += instance.text

    def evaluate_result(self, instance):
        if not self.output_label.text or self.output_label.text == "Error":
            return

        try:
            result = eval(self.output_label.text)
            # Display whole floating numbers as integers (e.g. 4.0 -> 4)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.output_label.text = str(result)
        except Exception:
            self.output_label.text = "Error"

    def clear_label(self, instance):
        self.output_label.text = ""

    def resize_label_text(self, label, new_height):
        label.font_size = 0.5 * label.height


class myApp(App):

    def build(self):
        return CalculatorLayout()


if __name__ == "__main__":
    myApp().run()
