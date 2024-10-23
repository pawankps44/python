import webbrowser
import os

from fpdf import FPDF



class Pdf:
    def __init__(self,pdf_name):
        self.pdf_name = pdf_name

    def generate_pdf(self,flatmate1,flatmate2,bill):
        flatmate1_pay = str(round(bill.flatmate_bill(flatmate1, flatmate2),2))
        flatmate2_pay = str(round(bill.flatmate_bill(flatmate2, flatmate1),2))
        pdf = FPDF('p', 'pt', 'a4')

        # inserting page
        pdf.add_page()

        # Adding Photo
        pdf.image('FILES\house.png',w=30,h=30)

        pdf.set_font('Times', 'B', 20)



        # inserting values
        pdf.cell(0, 50, 'Flatmate Bill', 1, 1000, 'C')

        pdf.set_font('Times', 'B', 15)
        pdf.cell(100, 40, 'Period:', 1, align='C')
        pdf.cell(200, 40, bill.time_period, 1, align='C',ln=1)

        pdf.set_font('Times', size=13)
        pdf.cell(100, 40,flatmate1.name, 1, align='C')
        pdf.cell(200, 40, flatmate1_pay, 1, align='C',ln=1)
        pdf.cell(100, 40,flatmate2.name, 1, align='C')
        pdf.cell(200, 40, flatmate2_pay, 1, align='C')


        pdf.output(f"FILES/{self.pdf_name}")

        # changing directory since webrowser wont work with /(files/)
        os.chdir('FILES')
        webbrowser.open(self.pdf_name)
