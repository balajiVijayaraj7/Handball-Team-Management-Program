class Team:
    # Initialising the team ID
    team_no = 0

    # Initialising the attributes
    def __init__(self, date, name, team_type, fee_paid, fee):
        Team.team_no = Team.team_no + 1
        self.__team_id = Team.team_no
        self.__date = date
        self.__name = name
        self.__team_type = team_type
        self.__fee_paid = fee_paid
        self.__fee = fee
        self.__cancel_date = None

    # setting the name attribute
    def set_name(self, name):
        self.__name = name

    def set_team_id(self, team_id):
        self.__team_id = team_id

    # setting the type
    def set_team_type(self, team_type):
        self.__team_type = team_type

    # setting the type
    def set_fee_paid(self, fee_paid):
        self.__fee_paid = fee_paid

    # setting fee
    def set_fee(self, fee):
        self.__fee = fee

    def set_cancel_date(self, cancel_date):
        self.__cancel_date = cancel_date

    # returning name
    def get_name(self):
        return self.__name

    # returning type
    def get_team_type(self):
        return self.__team_type

    # returning feePaid
    def get_fee_paid(self):
        return self.__fee_paid

    # returning fee
    def get_fee(self):
        return self.__fee

    # returning id
    def get_team_id(self):
        return self.__team_id

    # returning date
    def get_date(self):
        return self.__date

    def get_cancel_date(self):
        return self.__cancel_date

    def get_team_no(self):
        Team.team_no += 1
        return Team.team_no

    def __str__(self):
        def __str__(self):
            display = "{:<15} {:<10}\n".format("Team ID:", self.__id)
            display += "{:<15} {:<10}\n".format("Name:", self.__name)
            display += "{:<15} {:<10}\n".format("Register date:", self.__date)
            display += "{:<15} {:<10}\n".format("Type:", self.__type)
            display += "{:<15} {}\n".format("Fee Paid:", self.__fee_paid)
            display += "{:<15} {:<10}\n".format("Fee Amount:", self.__fee_amount)
            if self.__cancel_date:
                display += "Participation cancel date: {}\n".format(self.__cancel_date.strftime('%Y-%m-%d'))
            return display

