import UserInterface as UI


# Main function
def main():
    ui = UI.UserInterface()

    # initializing the variable for users choice
    choice = 0

    # Menu selection for users
    while choice != ui.EXIT:
        choice = ui.menu()
        if choice == ui.ADD:
            ui.add_team()
        elif choice == ui.INDIVIDUAL_TEAM:
            ui.display_individual_team()
        elif choice == ui.TEAM_TYPE:
            ui.display_type()
        elif choice == ui.ALL_TEAM:
            ui.display_all_Team()
        elif choice == ui.UPDATE:
            ui.update_details()
        elif choice == ui.DELETE:
            ui.delete()
        elif choice == ui.NO_OF_TEAMS_AND_PERCENTAGE:
            ui.display_teamCount_percent()
        elif choice == ui.WRITE_FILE:
            ui.write_file()
        elif choice == ui.READ_FILE:
            ui.read_file()
        elif choice == ui.CANCEL_PARTICIPATION:
            ui.cancel_participation()
        elif choice == ui.EXIT:
            print('Exit')
            print()


# call the main function
main()