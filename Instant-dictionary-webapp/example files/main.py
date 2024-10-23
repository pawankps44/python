# refer tailwindcss.com for styling the webpage
import justpy as jp

# this below one is a decorator to connect webpage with the server
@jp.SetRoute('/')

def home():
    # webpage is a class of justpy webframework,we are instantiating that class below
    wp = jp.WebPage()

    # 'a=wp' is nothing but adding that add the div to that webpage argument(wp)
    jp.Div(a=wp,text='hello world',classes='bg-yellow-500 text-blue-900 font-serif text-lg')
    jp.Div(a=wp,text='hello hi')

    #function should return webpage instance
    return wp

# to connect the webpage with the server(we can either us this or decorator based on our flexibilty
# jp.Route("/",home)

# to start the server to get the wepage using justpy
jp.justpy()