# refer tailwindcss.com for styling the webpage
import justpy as jp

# this below one is a decorator to connect webpage with the server
@jp.SetRoute('/')

def home():
    # webpage is a class of justpy webframework,we are instantiating that class below,wp is obj instance
    # we use QuasarPage here which is another interface as webpageyui-=
    wp = jp.QuasarPage(tailwind=True)

    # to change the background colour on the page
    Divv = jp.Div(a=wp,classes='bg-gray-200 h-screen')

    # arrangement using Div and Grid
    div1 = jp.Div(a=Divv,classes = 'grid grid-cols-3 p-2 gap-4')

    # 'a=wp' is nothing but adding the div to that webpage argument(wp)
    in1 = jp.Input(a=div1,placeholder='please enter first value',classes='form-input')
    in2 = jp.Input(a=div1,placeholder='please enter second value',classes='form-input')
    op = jp.Div(a=div1,text='Result goes here',classes='text-gray-500')
    jp.Div(a=div1,text='just another div')
    jp.Div(a=div1,text='just another div')

    div2 = jp.Div(a=Divv, classes='grid grid-cols-3 p-2 gap-4')
    jp.Button(a=div2,text='calculate',classes = 'border border-yellow-500 m-2 py-1 px-2 rounded hover:bg-red-700 hover:text-white',click = calc,in_1=in1,in_2=in2,output = op)
    jp.Div(a=div2,text = 'i am a cool interactive div!',classes= 'text-red-500',mouseenter = mouse_enter,mouseleave = mouse_leave)

    #function should return webpage instance
    return wp

# widget contains button component and msg contains attributes of the button
def calc(widget,msg):
    # widget.output.text = float(widget.in_1.value) + float(widget.in_2.value)
    print(widget.output.text)

def mouse_enter(widget,msg):
    widget.text = 'mouse have entered'

def mouse_leave(widget,msg):
    widget.text = 'mouse left'
# to connect the webpage with the server(we can either us this or decorator based on our flexibilty
# jp.Route("/",home)

# to start the server to get the wepage using justpy
jp.justpy()