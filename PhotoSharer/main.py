from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
import time
from file_upload import FileSharer
from kivy.core.clipboard import Clipboard
import webbrowser
print("koli")
Builder.load_file('frontend.kv')

class First_screen(Screen):
    def Start(self):
        self.ids.camera.play = True
        self.ids.button.text = 'Stop'
        # self.ids.camera.texture = self.ids.camera._camera.texture

    def Stop(self):
        self.ids.camera.play = False
        self.ids.button.text = 'Start'
        self.ids.camera.texture = None

    def Capture(self):
        filename = time.strftime('%Y%m%d-%H%M%S')
        self.file = f"files/{filename}.png"

        self.ids.camera.export_to_png(self.file)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.file

class ImageScreen(Screen):
    def capture_link(self):
        file_path = App.get_running_app().root.ids.first_screen.file
        filesharer = FileSharer(filepath = file_path)
        self.url = filesharer.share()
        self.ids.link.text = self.url

    def copy_url(self):
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = 'create a link first'

    def open_url(self):
        webbrowser.open(self.url)


class Rootwidget(ScreenManager):
    pass

class MainApp(App):
     def build(self):
         return Rootwidget()

MainApp().run()