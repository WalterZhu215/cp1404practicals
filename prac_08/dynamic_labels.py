from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """ DynamicLabelsApp is a Kivy App to display a list of names as labels """

    def __init__(self, **kwargs):
        """ Initialize the app with a list of names """
        super().__init__(**kwargs)
        self.names = ["David", "Dimo", "Dylan", "Diana"]

    def build(self):
        """ Build the Kivy app from the kv file and add dynamic labels """
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')


        for name in self.names:
            label = Label(text=name, font_size=32)
            self.root.ids.main.add_widget(label)

        return self.root


if __name__ == '__main__':
    DynamicLabelsApp().run()