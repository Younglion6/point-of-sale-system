from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout

class SignInWindow(BoxLayout):
    pass


class SignInApp(App):
    def build(self):
        return SignInWindow()
    
if __name__ == "__main__":
    sa = SignInApp()
    sa.run()