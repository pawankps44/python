import justpy as jp

# the about class handles url part,where as serve class handles html and css part of the page
# we are using composition here(has-a relationship),where inheritance as is-a relationship
class Doc:


    def serve(self):
        wp = jp.WebPage()

        div = jp.Div(a=wp,classes='bg-gray-200 h-screen')

        jp.Div(a=div,text='this is instant dictonary api',classes= 'text-yellow-500 text-4xl')
        jp.Div(a=div,text='get definition of words',classes= 'text-yellow-500 text-lg')
        jp.Hr(a=div)
        jp.Div(a=div,text='http://127.0.0.1:8000/api?w=moon')
        jp.Hr(a=div)
        jp.Div(a=div,text = '{"word": "moon", "definition": ["A natural satellite of a planet.", "A month, particularly a lunar month (approximately 28 days).", "To fuss over adoringly or with great affection.", "Deliberately show ones bare ass (usually to an audience, or at a place, where this is not expected or deemed appropriate).", "To be lost in phantasies or be carried away by some internal vision, having temorarily lost (part of) contact to reality."]}',classes='text-violet-500')
        return wp

