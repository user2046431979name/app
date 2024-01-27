from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.config import Config

class Calculator(App):
    def update_label(self):
        self.lbl.text = str(self.formula)
    def add_number(self,instance):
        try:
            if self.formula[0] == "0":
              self.formula = ""
            self.formula += str(instance.text)
            self.update_label()
        except IndexError:
            self.formula += "0"
    def delete_number(self,instance):
        self.formula = self.formula[:-1]
        self.update_label()

    def result(self,instance):
        try:
           self.formula = str(eval(self.formula))
           self.update_label()
        except SyntaxError:
            self.lbl.text = "так нельзя"
            self.formula = "0"
        except ZeroDivisionError:
            self.lbl.text = "любое число"
            self.formula = "0"
        except TypeError:
            self.lbl.text = "нормально вводи"
            self.formula = "0"
    def delete_numbers(self, instance):
        self.formula = "0"
        self.update_label()

    def build(self):
        self.formula = "0"
        bl = BoxLayout(orientation = "vertical")
        gl = GridLayout(cols = 4, size_hint = (1, .6), padding=50)
        self.lbl = Label(text="0", font_size=40,size_hint=(1, .4),halign="right")
        bl.add_widget(self.lbl)

        gl.add_widget(Button(text="<", on_press=self.delete_number))
        gl.add_widget(Button(text="C", on_press=self.delete_numbers))
        gl.add_widget(Button(text="(", on_press=self.add_number))
        gl.add_widget(Button(text=")", on_press=self.add_number))


        gl.add_widget(Button(text="7",on_press=self.add_number))
        gl.add_widget(Button(text="8",on_press=self.add_number))
        gl.add_widget(Button(text="9",on_press=self.add_number))
        gl.add_widget(Button(text="*",on_press=self.add_number))

        gl.add_widget(Button(text="4",on_press=self.add_number))
        gl.add_widget(Button(text="5",on_press=self.add_number))
        gl.add_widget(Button(text="6",on_press=self.add_number))
        gl.add_widget(Button(text="-",on_press=self.add_number))

        gl.add_widget(Button(text="1",on_press=self.add_number))
        gl.add_widget(Button(text="2",on_press=self.add_number))
        gl.add_widget(Button(text="3",on_press=self.add_number))
        gl.add_widget(Button(text="+",on_press=self.add_number))



        gl.add_widget(Button(text="/",on_press=self.add_number))
        gl.add_widget(Button(text="0",on_press=self.add_number))
        gl.add_widget(Button(text=".",on_press=self.add_number))
        gl.add_widget(Button(text="=",on_press=self.result))


        bl.add_widget(gl)
        return bl



if __name__ == '__main__':
    Calculator().run()
