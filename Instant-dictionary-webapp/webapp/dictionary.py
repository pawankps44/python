import justpy as jp
import definition
from webapp.navbar import nav_bar

import requests


# the about class handles url part,where as serve class handles html and css part of the page
# we are using composition here(has-a relationship),where inheritance as is-a relationship
class Dict:
    print('dict class')
    path = '/dict'

    # changing self to cls as it should define class and not the request object sent by justpy,and giving req explicitly
    # class method makes the self(cls) refer to class
    @classmethod
    def serve(cls,req):
        wp = jp.QuasarPage(tailwind=True)
        lay = nav_bar(a=wp)
        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container,classes='bg-gray-200 h-screen')
        jp.Div(a=div,text='Instant Dictionary',classes= 'text-yellow-500 text-4xl m-2')
        jp.Div(a=div,text = 'type the word for which you want meaning below.',classes='text-violet-500 text-lg')
        input_div = jp.Div(a=div,classes = 'grid grid-cols-2')
        in_div = jp.Input(a=input_div,placeholder = 'enter the word',classes='m-2 border-2 border-gray-400 rounded focus:bg-white' 
                                                              'focus outline-none focus:border-yellow-500 px-2 py-2')

        output_div = jp.Div(a=div,classes = 'm-2 p-2 h-40 text-lg border-2 border-yellow-400 ')
        jp.Button(a=input_div, text='click here for meaning', classes='border-2 border-purple-500 text-gray-500',
                  click=cls.output, outputdiv = output_div,inputdiv = in_div)
        print(cls,req)
        return wp

    # static method is considered as independent function which dont need instance of class or class itslef as a parameter
    @staticmethod
    def output(widget,msg):
        # synonyms = definition.Definition(widget.inputdiv.value).get()
        # widget.outputdiv.text = " ".join(synonyms)

        req = requests.get(f"http://127.0.0.1:8000/api?w={widget.value}")
        syn = req.json()
        widget.outputdiv.text = " ".join(syn['definition'])


