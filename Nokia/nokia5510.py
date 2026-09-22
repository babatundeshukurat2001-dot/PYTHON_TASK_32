

def main():

    while True:
        print("\n==============================")
        print("          NOKIA MENU")
        print("==============================")

        print("1. Phone book")
        print("2. Messages")
        print("3. Chat")
        print("4. Call register")
        print("5. Tones")
        print("6. Settings")
        print("7. Call divert")
        print("8. Music")
        print("9. Games")
        print("10. Calculator")
        print("11. Reminders")
        print("12. Clock")
        print("13. Profiles")
        print("14. WAP Services")
        print("15. SIM Services")
        print("0. Exit")

        choice = int(input("\nEnter main menu: "))

        match choice:
            case 1:
                phone_book()

            case 2:
                messages()

            case 3:
                print("Chat")

            case 4:
                call_register()

            case 5:
                tones()

            case 6:
                settings()

            case 7:
                print("Call divert")

            case 8:
                music()

            case 9:
                print("Games")

            case 10:
                print("Calculator")

            case 11:
                print("Reminders")

            case 12:
                clock()

            case 13:
                print("Profiles")

            case 14:
                print("WAP Services")

            case 15:
                print("SIM Services")

            case 0:
                print("Goodbye!")
                break

            case _:
                print("Invalid option. Please try again.")




def phone_book():

    while True:
        print("\n---------- PHONE BOOK ----------")
        print("1. Search")
        print("2. Service Nos.")
        print("3. Add name")
        print("4. Erase")
        print("5. Edit")
        print("6. Assign tone")
        print("7. Send b card")
        print("8. Options")
        print("9. Speed dials")
        print("10. Voice tags")
        print("0. Back")

        choice = int(input("Enter: "))

        match choice:
            case 1:
                print("Search")

            case 2:
                print("Service Nos.")

            case 3:
                print("Add name")

            case 4:
                print("Erase")

            case 5:
                print("Edit")

            case 6:
                print("Assign tone")

            case 7:
                print("Send b card")

            case 8:
                phone_book_options()

            case 9:
                print("Speed dials")

            case 10:
                print("Voice tags")

            case 0:
                print("Returning to main menu...")
                break

            case _:
                print("Invalid option.")


def phone_book_options():

    while True:
        print("\n---------- OPTIONS ----------")
        print("1. Type of view")
        print("2. Memory status")
        print("0. Back")

        choice = int(input("Enter: "))

        match choice:
            case 1:
                print("Type of view")

            case 2:
                print("Memory status")

            case 0:
                print("Returning...")
                break

            case _:
                print("Invalid option.")


def messages():

    while True:
        print("\n---------- MESSAGES ----------")
        print("1. Write messages")
        print("2. Inbox")
        print("3. Outbox")
        print("4. Picture messages")
        print("5. Templates")
        print("6. Smileys")
        print("7. Message settings")
        print("8. Info service")
        print("9. Voice mailbox number")
        print("10. Service command editor")
        print("0. Back")

        choice = int(input("Enter: "))

        match choice:
            case 1:
                print("Write messages")

            case 2:
                print("Inbox")

            case 3:
                print("Outbox")

            case 4:
                print("Picture messages")

            case 5:
                print("Templates")

            case 6:
                print("Smileys")

            case 7:
                message_settings()

            case 8:
                print("Info service")

            case 9:
                print("Voice mailbox number")

            case 10:
                print("Service command editor")

            case 0:
                print("Returning to main menu...")
                break

            case _:
                print("Invalid option.")


def message_settings():

    while True:
        print("\n------ MESSAGE SETTINGS ------")
        print("1. Set 1")
        print("2. Common")
        print("0. Back")

        choice = int(input("Enter: "))

        match choice:
            case 1:
                print("\n1. Message centre number")
                print("2. Messages sent as")
                print("3. Message validity")

            case 2:
                print("\n1. Delivery reports")
                print("2. Reply via same centre")
                print("3. Character support")

            case 0:
                print("Returning...")
                break

            case _:
                print("Invalid option.")


def call_register():

    while True:
        print("\n------- CALL REGISTER -------")
        print("1. Missed calls")
        print("2. Received calls")
        print("3. Dialled numbers")
        print("4. Erase recent call lists")
        print("5. Show call duration")
        print("6. Show call costs")
        print("7. Call cost settings")
        print("8. Prepaid credit")
        print("0. Back")

        choice = int(input("Enter: "))

        match choice:
            case 1:
                print("Missed calls")

            case 2:
                print("Received calls")

            case 3:
                print("Dialled numbers")

            case 4:
                print("Erase recent call lists")

            case 5:
                call_duration()

            case 6:
                call_costs()

            case 7:
                call_cost_settings()

            case 8:
                print("Prepaid credit")

            case 0:
                print("Returning to main menu...")
                break

            case _:
                print("Invalid option.")


def call_duration():

    while True:
        print("\n------ CALL DURATION ------")
        print("1. Last call duration")
        print("2. All calls duration")
        print("3. Received calls duration")
        print("4. Dialled calls duration")
        print("5. Clear timers")
        print("0. Back")

        choice = int(input("Enter: "))

        match choice:
            case 1:
                print("Last call duration")

            case 2:
                print("All calls duration")

            case 3:
                print("Received calls duration")

            case 4:
                print("Dialled calls duration")

            case 5:
                print("Clear timers")

            case 0:
                print("Returning...")
                break

            case _:
                print("Invalid option.")


def call_costs():

    while True:
        print("\n--------- CALL COSTS ---------")
        print("1. Last call cost")
        print("2. All calls' cost")
        print("3. Clear counters")
        print("0. Back")

        choice = int(input("Enter: "))

        match choice:
            case 1:
                print("Last call cost")

            case 2:
                print("All calls' cost")

            case 3:
                print("Clear counters")

            case 0:
                print("Returning...")
                break

            case _:
                print("Invalid option.")


def call_cost_settings():

    while True:
        print("\n------ CALL COST SETTINGS ------")
        print("1. Call cost settings")
        print("2. Show cost limit")
        print("0. Back")

        choice = int(input("Enter: "))

        match choice:
            case 1:
                print("Call cost settings")

            case 2:
                print("Show cost limit")

            case 0:
                print("Returning...")
                break

            case _:
                print("Invalid option.")


def tones():

    print("\n---------- TONES ----------")

    print("1. Ringing tone")
    print("2. Ringing volume")
    print("3. Incoming call alert")
    print("4. Composer")
    print("5. Message alert tone")
    print("6. Keypad tones")
    print("7. Warning and game tones")
    print("8. Vibrating alert")
    print("9. Screen saver")


def settings():

    while True:
        print("\n---------- SETTINGS ----------")
        print("1. Call settings")
        print("2. Phone settings")
        print("3. Security settings")
        print("4. Restore factory settings")
        print("0. Back")

        choice = int(input("Enter: "))

        match choice:
            case 1:
                call_settings()

            case 2:
                phone_settings()

            case 3:
                security_settings()

            case 4:
                print("Restore factory settings")

            case 0:
                print("Returning...")
                break

            case _:
                print("Invalid option.")


def call_settings():

    print("\n------ CALL SETTINGS ------")
    print("1. Automatic redial")
    print("2. Speed dialling")
    print("3. Call waiting options")
    print("4. Own number sending")
    print("5. Phone line in use")
    print("6. Automatic answer")


def phone_settings():

    print("\n------ PHONE SETTINGS ------")
    print("1. Language")
    print("2. Cell info display")
    print("3. Welcome note")
    print("4. Network selection")
    print("5. Lights")
    print("6. Confirm SIM service actions")


def security_settings():

    print("\n------ SECURITY SETTINGS ------")
    print("1. PIN code request")
    print("2. Call barring service")
    print("3. Fixed dialling")
    print("4. Closed user group")
    print("5. Phone security")
    print("6. Change access codes")


def music():

    while True:
        print("\n---------- MUSIC ----------")
        print("1. Music player")
        print("2. Radio")
        print("3. Recorder")
        print("4. Track list")
        print("0. Back")

        choice = int(input("Enter: "))

        match choice:
            case 1:
                print("Music player")

            case 2:
                print("Radio")

            case 3:
                print("Recorder")

            case 4:
                print("Track list")

            case 0:
                print("Returning...")
                break

            case _:
                print("Invalid option.")


def clock():

    while True:
        print("\n---------- CLOCK ----------")
        print("1. Alarm clock")
        print("2. Clock settings")
        print("3. Date setting")
        print("4. Stopwatch")
        print("5. Countdown timer")
        print("6. Auto update of date and time")
        print("0. Back")

        choice = int(input("Enter: "))

        match choice:
            case 1:
                print("Alarm clock")

            case 2:
                print("Clock settings")

            case 3:
                print("Date setting")

            case 4:
                print("Stopwatch")

            case 5:
                print("Countdown timer")

            case 6:
                print("Auto update of date and time")

            case 0:
                print("Returning...")
                break

            case _:
                print("Invalid option.")


# ==========================================
# MAIN MENU
# ==========================================
#
#def main():
#
#    while True:
#        print("\n==============================")
#        print("          NOKIA MENU")
#        print("==============================")
#
#        print("1. Phone book")
#        print("2. Messages")
#        print("3. Chat")
#        print("4. Call register")
#        print("5. Tones")
#        print("6. Settings")
#        print("7. Call divert")
#        print("8. Music")
#        print("9. Games")
#        print("10. Calculator")
#        print("11. Reminders")
#        print("12. Clock")
#        print("13. Profiles")
#        print("14. WAP Services")
#        print("15. SIM Services")
#        print("0. Exit")
#
#        choice = int(input("\nEnter main menu: "))
#
#        match choice:
#            case 1:
#                phone_book()
#
#            case 2:
#                messages()
#
#            case 3:
#                print("Chat")
#
#            case 4:
#                call_register()
#
#            case 5:
#                tones()
#
#            case 6:
#                settings()
#
#            case 7:
#                print("Call divert")
#
#            case 8:
#                music()
#
#            case 9:
#                print("Games")
#
#            case 10:
#                print("Calculator")
#
#            case 11:
#                print("Reminders")
#
#            case 12:
#                clock()
#
#            case 13:
#                print("Profiles")
#
#            case 14:
#                print("WAP Services")
#
#            case 15:
#                print("SIM Services")
#
#            case 0:
#                print("Goodbye!")
#                break
#
#            case _:
#                print("Invalid option. Please try again.")
#
#
# ==========================================
# RUN PROGRAM
# ==========================================
#
#
#
