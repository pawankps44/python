import justpy as jp
from webapp.navbar import nav_bar





# the about class handles url part,where as serve class handles html and css part of the page
# we are using composition here(has-a relationship),where inheritance as is-a relationship
class Home:
    path = '/'

    @classmethod
    def serve(cls,req):
        wp = jp.QuasarPage(tailwind=True)
        lay = nav_bar(a=wp)
        container = jp.QPageContainer(a=lay)

        # layout = jp.QLayout(a=wp,view="hHh lpR fFf")
        # header = jp.QHeader(a=layout,classes="bg-primary text-white")
        # toolbar = jp.QToolbar(a=header)
        #
        #
        # drawer = jp.QDrawer(a=layout,show_if_above = True,v_model="leftDrawerOpen",side="left",bordered = True )
        # a_classes = 'text-xl text-blue-500 hover:bg-red-700'
        # list = jp.QList(a=drawer)
        # jp.A(a = list,text='Home',href = '/',classes = a_classes)
        # jp.Br(a=list)
        # jp.A(a= list,text='dict',href = '/dict',classes = a_classes)
        # jp.Br(a=list)
        # jp.A(a=list,text='about',href = '/about',classes = a_classes)
        # jp.Br(a=list)
        #
        # jp.QBtn(a=toolbar,dense = True,flat = True,round = True, icon = 'menu',click = cls.move_Drawer,drawer = drawer)
        # jp.QToolbarTitle(a=toolbar, text='instant dictionary')
        #
        # container = jp.QPageContainer(a=layout)

        div = jp.Div(a=container
                     ,classes='bg-gray-200 h-screen')
        jp.Div(a=div,text='this is the Home page',classes= 'text-yellow-500')
        jp.Div(a=div,text = 'kljjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjkjhjjkhjjhjkhkjhkjdhkjbadskbasjdhjasd,masdiuyjqw em,dqbwjidajbdm,asbdbcjahdm qw',classes='text-violet-500')
        return wp


# jp.Route(Home.path,Home.serve)
# jp.justpy()