from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, NumericProperty
from kivy.lang import Builder
import pandas as pd
from plotnine import ggplot, aes, geom_point, labs, theme_minimal

class AntennaControl(BoxLayout):
    configured_vertical = NumericProperty(0)
    configured_horizontal = NumericProperty(0)
    current_vertical = NumericProperty(0)
    current_horizontal = NumericProperty(0)
    status_message = StringProperty("")
    check_message = StringProperty("")

    def send_alignment(self, vertical, horizontal):
        try:
            self.current_vertical = float(vertical)
            self.current_horizontal = float(horizontal)
            self.status_message = "Values Sent to Antenna!"
        except ValueError:
            self.status_message = "Invalid Input! Please enter numeric values."

    def reset_to_configured(self):
        self.current_vertical = self.configured_vertical
        self.current_horizontal = self.configured_horizontal
        self.status_message = "Antenna reset to configured values."

    def check_position(self):
        if (
            self.current_vertical == self.configured_vertical
            and self.current_horizontal == self.configured_horizontal
        ):
            self.check_message = "Antenna is in the correct position!"
        else:
            self.check_message = "Antenna is NOT in the correct position."

    def generate_plot(self):
        try:
            data = pd.DataFrame({
                "Type": ["Configured", "Current"],
                "Vertical": [self.configured_vertical, self.current_vertical],
                "Horizontal": [self.configured_horizontal, self.current_horizontal]
            })
            plot = (
                ggplot(data, aes(x="Horizontal", y="Vertical", color="Type"))
                + geom_point(size=5)
                + labs(title="Antenna Positions", x="Horizontal", y="Vertical")
                + theme_minimal()
            )
            plot.save("/tmp/antenna_plot.png", width=6, height=4, dpi=100)
            self.status_message = "Plot Generated: /tmp/antenna_plot.png"
        except Exception as e:
            self.status_message = f"Error generating plot: {e}"

class ConfigScreen(BoxLayout):
    def confirm_settings(self, vertical, horizontal):
        try:
            app = App.get_running_app()
            main_screen = app.root.get_screen("main").ids.antenna_control
            main_screen.configured_vertical = float(vertical)
            main_screen.configured_horizontal = float(horizontal)
            app.root.current = "main"
        except ValueError:
            self.ids.status_label.text = "Invalid input! Please enter numeric values."

Builder.load_file("app.kv")

class AntennaApp(App):
    def build(self):
        sm = ScreenManager()

        # Add the main screen
        main_screen = Screen(name="main")
        main_screen.add_widget(AntennaControl())
        sm.add_widget(main_screen)

        # Add the configuration screen
        config_screen = Screen(name="config")
        config_screen.add_widget(ConfigScreen())
        sm.add_widget(config_screen)

        return sm

if __name__ == "__main__":
    AntennaApp().run()
