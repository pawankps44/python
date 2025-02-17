class Flatmates:

    """
    This class gets names of flatmates and no of days stayed
    """

    def __init__(self,name,days_stayed):
        self.name = name
        self.days_stayed = days_stayed


class Flat_Bill:

    """
    this class gets total bill and time period of bill as input and returns each flatmate bill
    """

    def __init__(self,total_bill,time_period):
        self.total_bill = total_bill
        self.time_period = time_period

    # we are calculating both flatmates bill by calling this function by interchanging their positions,since the function only gives the flatmate1 argument bill value
    def flatmate_bill(self,Flatmate1,Flatmate2):
        weight = Flatmate1.days_stayed/(Flatmate1.days_stayed+Flatmate2.days_stayed)
        bill_1 = weight * int(self.total_bill)
        bill_2 = self.total_bill - bill_1
        # returing in list format because we are using flask
        # return [bill_1,bill_2]
        return bill_1


    """
    this class generate pdf with flatmate names,their bill,no of days stayed and the total bill for the
    time period
    """
