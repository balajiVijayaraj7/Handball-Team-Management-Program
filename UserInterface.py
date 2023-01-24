from datetime import datetime
import Team as t


class UserInterface:
    ADD = 1
    INDIVIDUAL_TEAM = 2
    ALL_TEAM = 3
    TEAM_TYPE = 4
    UPDATE = 5
    DELETE = 6
    NO_OF_TEAMS_AND_PERCENTAGE = 7
    WRITE_FILE = 8
    READ_FILE = 9
    CANCEL_PARTICIPATION = 10
    EXIT = 11

    def __init__(self):
        self.teamList = []

    def menu(self):

        # defining menu options
        print('==========================================================')
        print('Menu:')
        print('1: Add New team')
        print('2: Show Individual Team')
        print('3: Show All Team')
        print('4: Show Teams based on type')
        print('5: Update Team information')
        print('6: Delete Team information')
        print('7: No.of.Teams and percentage of fees paid by them')
        print('8: Writing the data in a file')
        print('9: Reading the data from a file')
        print('10: Cancel Participation')
        print('11: Exit')
        print('==========================================================')

        choice = 0
        while choice < 1 or choice > 11:
            try:
                choice = int(input('Enter a valid choice from 1 to 11 : '))
            except:
                print("Value is not a number between 1 to 11")
        return choice

    # The add function adds a new team into the list
    def add_team(self):

        name = input('Name of handball team: ')
        while name in ["", "|"]:
            print("Enter a team name")
            name = input('Name of handball team: ')
        team_Date = datetime.today().strftime('%Y-%m-%d')
        team_type = input('Type of the team(Boys or Girls): ')

        # Type checking for type in the team
        while team_type.lower() not in ["boys", "girls"]:
            print("Please enter type of team as Boys or Girls")
            team_type = input("Boys or Girls: ")

        fee_paid = input('Do they pay the fees?(Yes:No): ')

        # Fee paid validation
        while fee_paid.lower() not in ["yes", "no"]:
            print("Please enter Yes or No to indicate payment of fees")
            fee_paid = input("Yes or No: ")

        if fee_paid.lower() == "yes":
            paid = True
            fee = input('Fee amount paid by the team for the participation: ')
        else:
            paid = False
            fee = 0

        print()

        team = t.Team(team_Date, name, team_type, paid, fee)
        self.teamList.append(team)

        print("Successful entry")
        print()

        print("your Team id is", team.get_team_id())
        print()


    # Update the participation details
    def update_details(self):

        if len(self.teamList) == 0:
            print('There is no team entered.')
            print()
            return
        team_id = 0
        while team_id == 0:
            try:
                team_id = int(input('Enter the id to update : '))
            except:
                print("Enter a number")

        updated = False
        for i in self.teamList:
            if team_id == i.get_team_id():
                name = input('Name of handball team: ')
                while name in [""]:
                    print("Enter a team name")
                    name = input('Name of handball team: ')
                team_type = input('Type of the handball team(Boys or Girls): ')
                while team_type.lower() not in ("boys", "girls"):
                    print("Please enter type of handball team as Boys or Girls")
                    team_type = input("Girls/Boys: ")

                fee_paid = input('Fee paid by handball team? (yes/no): ')
                while fee_paid.lower() not in ("yes", "no"):
                    print("Please enter Yes or No to indicate fee_paid completion.")
                    fee_paid = input("Yes/No: ")

                if fee_paid.lower() == "yes":
                    paid = True
                    fee = input('Fee amount paid by the team : ')
                else:
                    paid = False
                    fee = 0

                i.set_name(name)
                i.set_team_type(team_type)
                i.set_fee_paid(paid)
                i.set_fee(fee)

                print()
                print("Details Updated.")
                updated = True
                return

        if not updated:
            print("Id not registered")
            print()

    # The delete function deletes an entry from the participation list
    def delete(self):
        if len(self.teamList) == 0:
            print("No team available to delete")
            print()
            return
        else:
            deleted = False
            team_id = 0
            while team_id == 0:
                try:
                    team_id = int(input('Enter the id to delete : '))
                except:
                    print("Enter a number")
            for i in range(len(self.teamList)):
                if self.teamList[i].get_team_id() == team_id:
                    self.teamList.pop(i)
                    deleted = True
                    print("The team has been deleted from the list")

                    if len(self.teamList) == 0:
                        print("Teams list is empty")
                        print()
                    else:
                        print("The remaining teams in the list are :")
                        self.display_all_Team()
                    break

            if not deleted:
                print("Id not registered")
                print()

                # This function will display the individual team list details

    def display_individual_team(self):
        if len(self.teamList) == 0:
            print("No team available to display")
            print()
        else:
            print()
            team_id = 0
            while team_id == 0:
                try:
                    team_id = int(input('Enter the id of the team : '))
                except:
                    print("Enter a number")
            found = False
            for i in self.teamList:
                if team_id == i.get_team_id():
                    found = True
                    print('------------------------------------')
                    print("Handball Team List")
                    print("ID :", str(i.get_team_id()))
                    print("Date :", i.get_date())
                    print("Name :", i.get_name())
                    print("Type :", i.get_team_type())
                    print("Fee paid :", i.get_fee_paid())
                    print("Fee Amount :", i.get_fee())
                    print('------------------------------------')
                    print()
                    return

            if not found:
                print("Id not registered")
                print()

    # This function will display team list based on gender
    def display_type(self):

        if len(self.teamList) == 0:
            print("No team available to display")
            print()
        else:
            brg = input('Enter the type of gender need to be chosen:').lower()
            print()
            found = False
            # Gender type validation
            while brg.lower() not in ["boys", "girls"]:
                print("Please enter type of handball team as Boys or Girls.")
                brg = input("Boys or Girls: ")

            # Loop will iterate over the list to find the selected gender type details
            for i in self.teamList:
                if brg.lower() == str(i.get_team_type()).lower():
                    found = True
                    print('------------------------------------')
                    print("Handball Team")
                    print("ID :", str(i.get_team_id()))
                    print("Date :", i.get_date())
                    print("Name :", i.get_name())
                    print("Type :", i.get_team_type())
                    print("Fee paid :", i.get_fee_paid())
                    print("Fee Amount :", i.get_fee())
                    print('------------------------------------')
                    print()

            if not found:
                print("No teams with type Boys or Girls")
                print()

    # This function will display details of all team in the participation list
    def display_all_Team(self):
        if len(self.teamList) == 0:
            print("No team available to display")
            print()
        else:
            print("Handball Team List")
            print("--------------------------------------")
            for i in self.teamList:
                print("ID :", str(i.get_team_id()))
                print("Date :", i.get_date())
                print("Name :", i.get_name())
                print("Type :", i.get_team_type())
                print("Fee paid :", i.get_fee_paid())
                print("Fee Amount :", i.get_fee())
                print("--------------------------------------")
            print()

    # Total team existing and percentage of all teams that has paid their fees
    def display_teamCount_percent(self):
        count_paid = 0
        if len(self.teamList) == 0:
            print("No team available in the list to calculate the percentage.")
            print()
        else:
            total_count = len(self.teamList)
            print("Number of teams : ", total_count)

            # percentage of all teams that has paid their fees calculation
            for i in self.teamList:
                if i.get_fee_paid():
                    count_paid += 1
            avg = (count_paid / total_count) * 100.0
            print("Percent of teams that paid the fee", format(avg, '.2f'), '%')
            print()

    # Participation cancellation by the team
    def cancel_participation(self):

        if len(self.teamList) == 0:
            print("No team available to display")
            print()
        else:
            team_id = 0
            while team_id == 0:
                try:
                    team_id = int(input('Enter the id to cancel participation : '))
                except:
                    print("Enter a number")
            id_found = [t for t in self.teamList if t.get_team_id() == team_id]
            if id_found:
                # The result is a list with 1 element
                id_found = id_found[0]
                # Check if the team has already cancelled the participation:
                if id_found.get_cancel_date():
                    print("\nThis Team has already cancelled the participation.")
                    print()
                else:
                    confirmation = str(
                        input("Confirm cancelling the participation for the team? (Y/N): ")).strip().upper()
                    if confirmation == "Y":
                        id_found.set_cancel_date(datetime.today())
                        for i in range(len(self.teamList)):
                            # update teams after cancellation
                            if self.teamList[i].get_team_id() == id_found.get_team_id():
                                self.teamList[i] = id_found
                                break
                        print("Participation Cancelled ")
                        print()
                    else:
                        print("No change has been made")
                        print()
            else:
                print("Id not found.")
                print()

    # Writing the contents to the team file
    def write_file(self):

        if len(self.teamList) == 0:
            print("No team available to save.")
        else:
            # Open a file for writing.
            team_file = open('team.txt', 'w')

            # Write the list to the file.
            team_file.write('Id|Date|Name|Type|Fee Paid|Fee|Participation Cancelled Date\n')

            for item in self.teamList:
                team_file.write(
                    str(item.get_team_id()) + '|' + item.get_date() + '|' + item.get_name() + '|' + item.get_team_type() + '|' + str(
                        item.get_fee_paid()) + '|' + str(item.get_fee()) + '|')
                if item.get_cancel_date() is None:
                    team_file.write(str(item.get_cancel_date()) + '\n')
                else:
                    team_file.write(item.get_cancel_date().strftime('%Y-%m-%d') + '\n')

            # Close the file.
            print("Your team details are Successfully stored in a file \n")
            team_file.close()

    # Reading the contents from team file
    def read_file(self):
        try:
            team_file = open('team.txt', 'r')
            file_content = team_file.read()
            # split into lines
            file_content = file_content.splitlines()

            # 1 line is header line
            if len(file_content) > 1:
                # remove header line
                file_content = file_content[1:]
                # If the file contains any data, clear the current list:
                self.teamList.clear()

                # split data based upon | delimiter
                for content in file_content:
                    data = content.split("|")

                    # read values
                    id = int(data[0])
                    team_date = data[1]
                    name = data[2]
                    team_type = data[3]
                    fee_paid = bool(data[4])
                    fee = float(data[5])

                    # construct Team object
                    team = t.Team(team_date, name, team_type, fee_paid, fee)
                    team.set_team_id(id)

                    # if cancel date is not none then add it to team object
                    if data[6] != 'None':
                        cancel_date = datetime.strptime(data[6], '%Y-%m-%d').date()
                        team.set_cancel_date(cancel_date)

                    self.teamList.append(team)

                print("Data Loaded to Team List")
                print()
            else:
                print("No data found")
        except:
            print("team.txt file not found to read data.")
            print()
