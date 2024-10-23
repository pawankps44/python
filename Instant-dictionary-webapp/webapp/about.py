import justpy as jp
from webapp.navbar import nav_bar
from webapp import page


# the about class handles url part,where as serve class handles html and css part of the page
# we are using composition here(has-a relationship),where inheritance as is-a relationship
class About:
    path = '/about'

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        lay = nav_bar(a=wp)
        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container,classes='bg-gray-200 h-screen')
        jp.Div(a=div,text='this is the about page',classes= 'text-yellow-500')
        jp.Div(a=div,text = 'kljjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjkjhjjkhjjhjkhkjhkjdhkjbadskbasjdhjasd,masdiuyjqw em,dqbwjidajbdm,asbdbcjahdm qw',classes='text-violet-500')
        return wp

