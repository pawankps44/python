from flask.views import MethodView
from wtforms import Form,StringField,SubmitField
from Flatmate_Bill import flat
from flask import jsonify

#render template for accessing other files,store other files in Templates folder while using flask for connecting multiple files.
from flask import Flask,render_template,request

#Flask class is the central class that connects all the webpages,Where __name__ is syntax.
app = Flask(__name__)

#each classes define each webpage here.
class home_page(MethodView):

    def get(self):
        return render_template('index.html')
        print("flatmatebill")

class BillFormPage(MethodView):

    def get(self):
        bill_form = Billform()
        # billForm is the variable used for forms in html,where bill_form is the object instance of Billform class where forms are defined
        return render_template('Bill_form_page.html',billForm = bill_form)

class Results(MethodView):

    def post(self):
        # request.form is access data entering in the forms.
        billform = Billform(request.form)
        bill1 = flat.Flat_Bill(float(billform.bill.data),billform.period.data)
        f1 = flat.Flatmates(billform.Name1.data,float(billform.days_in_the_house1.data))
        f2 = flat.Flatmates(billform.Name2.data,float(billform.days_in_the_house2.data))
        amount = bill1.flatmate_bill(f1,f2)
        # return amount
        # return f"{billform.Name1.data} pays {amount[0]} and {billform.Name2.data} pays {amount[1]}"
        # amount = bill1.flatmate_bill(f1,f2)
        return render_template("results.html",name1 = billform.Name1.data,Bill1 = bill1.flatmate_bill(f1,f2),name2 = billform.Name2.data,Bill2 = bill1.flatmate_bill(f2,f1))


# declaring this class for defining forms
# default value is added in forms
class Billform(Form):
    bill = StringField("BILL:",default=2000)
    period = StringField("Period:",default = "feb 2024")

    Name1 = StringField("Name1:",default = "Pawan")
    days_in_the_house1 = StringField("days_in_the_house1:",default=20)
    Name2 = StringField("Name2:",default="Messi")
    days_in_the_house2 = StringField("days_in_the_house2:",default=12)

    Submit = SubmitField('Submit')

#adding url to the classes
app.add_url_rule('/',view_func=home_page.as_view('home_page'))
app.add_url_rule('/bill',view_func=BillFormPage.as_view('BillFormPage'))
app.add_url_rule('/results',view_func=Results.as_view('results'))


#finally you have to run the object instance app,(debug = true enables you to not run app code every time for seeing changes in the application you have made).
app.run(debug = True)