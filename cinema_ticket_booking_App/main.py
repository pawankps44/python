import sqlite3
from fpdf import FPDF
import string
import random

class User:
    def __init__(self,name):
        self.name = name

    def user_ticket(self,seat,card):
        if seat.seat_aval():
            if card.validate(seat.get_price()):
                print('card is valid')
                seat.seat_occupy()
                ticket = Ticket(self.name, seat.get_price(), seat.seat_number)
                ticket.to_pdf()
            else:
                print('there is a problem with your card')

        else:
            print('seat is not available')

class Seat:

    database = 'cinema.db'

    def __init__(self,seat_number):
        self.seat_number = seat_number

    def get_price(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""SELECT price From Seat WHERE seat_id = ? """, [self.seat_number])
        price = cursor.fetchall()[0][0]
        print('PRICE',price)
        return price

    def seat_aval(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""SELECT taken from Seat where seat_id = ? """,[self.seat_number])
        result = cursor.fetchall()[0][0]
        print(result)

        if result == 0:
            return True
        else:
            return False

    def seat_occupy(self):
        connection = sqlite3.connect(self.database)
        connection.execute("""UPDATE Seat SET taken = ? WHERE seat_id = ? """, [1,self.seat_number])
        connection.commit()
        connection.close()


class Card:
    database = 'banking.db'

    def __init__(self,card_type,card_number,ccv):
        self.card_type = card_type
        self.card_number = card_number
        self.ccv = ccv

    def validate(self,price):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""SELECT balance FROM Card WHERE number = ? and cvc = ? """, [self.card_number,self.ccv])
        result = cursor.fetchall()

        if result:
            balance = result[0][0]
            print('bal','price',type(balance),type(price))
            print('bal','price',balance,price)
            if balance >= float(price):

                connection = sqlite3.connect(self.database)
                connection.execute("""UPDATE Card SET balance = ? where number = ? and cvc = ?  """, [balance - price,self.card_number,self.ccv])
                connection.commit()
                connection.close()
                return True

class Ticket:
    def __init__(self,name,price,seat_num):
        self.name = name
        self.price = price
        self.seat_num = seat_num
        self.id = "".join([random.choice(string.ascii_letters) for i in range(8)])

    def to_pdf(self):
        pdf = FPDF('P',unit='pt',format='A4')
        pdf.add_page()

        pdf.set_font(family="Times", style="B", size=24)
        pdf.cell(w=0, h=80, txt="Your Digital Ticket", border=1, ln=1, align="C")

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=25, txt="Name: ", border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=0, h=25, txt=self.name, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=25, txt="Ticket ID", border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=0, h=25, txt=self.id, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=25, txt="Price", border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=0, h=25, txt=str(self.price), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=25, txt="Seat Number", border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=0, h=25, txt=str(self.seat_num), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.output('sample_ticket.pdf')
        print(self.id)


if __name__ == "__main__":

    user_name = input('Enter name:')
    seat_num = input('Enter seat number:')
    card_type = input('Enter card type:')
    card_number = input('Enter card number:')
    ccv = input('Enter ccv number:')

    User_obj = User(user_name)
    Seat_det = Seat(seat_num)
    Card_det = Card(card_type,card_number,ccv)

    User_obj.user_ticket(Seat_det,Card_det)

