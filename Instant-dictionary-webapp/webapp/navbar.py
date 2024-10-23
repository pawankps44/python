import justpy as jp
class nav_bar(jp.QLayout):
    def __init__(self,view="hHh lpR fFf", **kwargs):
        # super refers to QLayout which in inherited
        super().__init__(view=view,**kwargs)
        wp = jp.QuasarPage(tailwind=True)
        header = jp.QHeader(a=self, classes="bg-primary text-white")
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=self, show_if_above=True, v_model="leftDrawerOpen", side="left", bordered=True)
        a_classes = 'text-xl text-blue-500 hover:bg-red-700'
        list = jp.QList(a=drawer)
        jp.A(a=list, text='Home', href='/', classes=a_classes)
        jp.Br(a=list)
        jp.A(a=list, text='dict', href='/dict', classes=a_classes)
        jp.Br(a=list)
        jp.A(a=list, text='about', href='/about', classes=a_classes)
        jp.Br(a=list)

        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon='menu', click=self.move_Drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text='instant dictionary')


    @staticmethod
    def move_Drawer(widget,msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True