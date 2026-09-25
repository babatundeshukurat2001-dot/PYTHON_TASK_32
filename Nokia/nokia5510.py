
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

    choice = input("\nEnter main menu: ")
    choice = choice.strip()

    match choice:
        case "1":
            
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

                sub = input("Enter: ")

                match sub:
                    case "1":
                        print("Search")
                    case "2":
                        print("Service Nos.")
                    case "3":
                        print("Add name")
                    case "4":
                        print("Erase")
                    case "5":
                        print("Edit")
                    case "6":
                        print("Assign tone")
                    case "7":
                        print("Send b card")
                    case "8":
                        
                        while True:
                            print("\n---------- OPTIONS ----------")
                            print("1. Type of view")
                            print("2. Memory status")
                            print("0. Back")

                            sub2 = input("Enter: ")

                            match sub2:
                                case "1":
                                    print("Type of view")
                                case "2":
                                    print("Memory status")
                                case "0":
                                    print("Returning to Phone Book...")
                                    break
                                case _:
                                    print("Invalid option.")
                    case "9":
                        print("Speed dials")
                    case "10":
                        print("Voice tags")
                    case "0":
                        print("Returning to main menu...")
                        break
                    case _:
                        print("Invalid option.")

        case 2:
            
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

                sub = input("Enter: ")

                match sub:
                    case "1":
                        print("Write messages")
                    case "2":
                        print("Inbox")
                    case "3":
                        print("Outbox")
                    case "4":
                        print("Picture messages")
                    case "5":
                        print("Templates")
                    case "6":
                        print("Smileys")
                    case "7":
                        
                        while True:
                            print("\n---------- MESSAGE SETTINGS ----------")
                            print("1. Set 1")
                            print("2. Common")
                            print("0. Back")

                            sub2 = input("Enter: ")

                            match sub2:

                                case "1":
                                    print("\n1. Message centre number")
                                    print("2. Messages sent as")
                                    print("3. Message validity")

                                case "2":
                                    print("\n1. Delivery reports")
                                    print("2. Reply via same centre")
                                    print("3. Character support")

                                case "0":
                                    print("Returning to Messages...")
                                    break

                                case _:
                                    print("Invalid option.")
                    case "8":
                        print("Info service")
                    case "9":
                        print("Voice mailbox number")
                    case "10":
                        print("Service command editor")
                    case "0":
                        print("Returning to main menu...")
                        break
                    case _:
                        print("Invalid option.")

        case "3":
            print("\nChat")

        case "4":
            
            while True:
                print("\n---------- CALL REGISTER ----------")
                print("1. Missed calls")
                print("2. Received calls")
                print("3. Dialled numbers")
                print("4. Erase recent call lists")
                print("5. Show call duration")
                print("6. Show call costs")
                print("7. Call cost settings")
                print("8. Prepaid credit")
                print("0. Back")

                sub = input("Enter: ")

                match sub:
                    case "1":
                        print("Missed calls")
                    case "2":
                        print("Received calls")
                    case "3":
                        print("Dialled numbers")
                    case "4":
                        print("Erase recent call lists")
                    case "5":
                       
                        while True:
                            print("\n---------- CALL DURATION ----------")
                            print("1. Last call duration")
                            print("2. All calls duration")
                            print("3. Received calls duration")
                            print("4. Dialled calls duration")
                            print("5. Clear timers")
                            print("0. Back")

                            sub2 = input("Enter: ")

                            match sub2:
                                case "1":
                                    print("Last call duration")
                                case "2":
                                    print("All calls duration")
                                case "3":
                                    print("Received calls duration")
                                case "4":
                                    print("Dialled calls duration")
                                case "5":
                                    print("Clear timers")
                                case "0":
                                    print("Returning to Call Register...")
                                    break
                                case _:
                                    print("Invalid option.")
                    case "6":
                        
                        while True:
                            print("\n---------- CALL COSTS ----------")
                            print("1. Last call cost")
                            print("2. All calls' cost")
                            print("3. Clear counters")
                            print("0. Back")

                            sub2 = input("Enter: ")

                            match sub2:
                                case "1":
                                    print("Last call cost")
                                case "2":
                                    print("All calls' cost")
                                case "3":
                                    print("Clear counters")
                                case "0":
                                    print("Returning to Call Register...")
                                    break
                                case _:
                                    print("Invalid option.")
                    case "7":
                        
                        while True:
                            print("\n---------- CALL COST SETTINGS ----------")
                            print("1. Call cost settings")
                            print("2. Show cost limit")
                            print("0. Back")

                            sub2 = input("Enter: ")

                            match sub2:
                                case "1":
                                    print("Call cost settings")
                                case "2":
                                    print("Show cost limit")
                                case "0":
                                    print("Returning to Call Register...")
                                    break
                                case _:
                                    print("Invalid option.")
                    case "8":
                        print("Prepaid credit")
                    case "0":
                        print("Returning to main menu...")
                        break
                    case _:
                        print("Invalid option.")

        case "5":
           
            while True:
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
                print("0. Back")

                sub = input("Enter: ")

                match sub:
                    case "1":
                        print("Ringing tone")
                    case "2":
                        print("Ringing volume")
                    case "3":
                        print("Incoming call alert")
                    case "4":
                        print("Composer")
                    case "5":
                        print("Message alert tone")
                    case "6":
                        print("Keypad tones")
                    case "7":
                        print("Warning and game tones")
                    case "8":
                        print("Vibrating alert")
                    case "9":
                        print("Screen saver")
                    case "0":
                        print("Returning to main menu...")
                        break
                    case _:
                        print("Invalid option.")

        case "6":
           
            while True:
                print("\n---------- SETTINGS ----------")
                print("1. Call settings")
                print("2. Phone settings")
                print("3. Security settings")
                print("4. Restore factory settings")
                print("0. Back")

                sub = input("Enter: ")

                match sub:
                    case "1":
                        print("\n---------- CALL SETTINGS ----------")
                        print("1. Automatic redial")
                        print("2. Speed dialling")
                        print("3. Call waiting options")
                        print("4. Own number sending")
                        print("5. Phone line in use")
                        print("6. Automatic answer")

                    case "2":
                        print("\n---------- PHONE SETTINGS ----------")
                        print("1. Language")
                        print("2. Cell info display")
                        print("3. Welcome note")
                        print("4. Network selection")
                        print("5. Lights")
                        print("6. Confirm SIM service actions")

                    case "3":
                        print("\n---------- SECURITY SETTINGS ----------")
                        print("1. PIN code request")
                        print("2. Call barring service")
                        print("3. Fixed dialling")
                        print("4. Closed user group")
                        print("5. Phone security")
                        print("6. Change access codes")

                    case "4":
                        print("Restore factory settings")

                    case "0":
                        print("Returning to main menu...")
                        break

                    case _:
                        print("Invalid option.")

        case "7":
            print("\nCall divert")

        case "8":
           
            while True:
                print("\n---------- MUSIC ----------")
                print("1. Music player")
                print("2. Radio")
                print("3. Recorder")
                print("4. Track list")
                print("0. Back")

                sub = input("Enter: ")

                match sub:
                    case "1":
                        print("Music player")
                    case "2":
                        print("Radio")
                    case "3":
                        print("Recorder")
                    case "4":
                        print("Track list")
                    case "0":
                        print("Returning to main menu...")
                        break
                    case _:
                        print("Invalid option.")

        case "9":
            print("\nGames")

        case "10":
            print("\nCalculator")

        case "11":
            print("\nReminders")

        case "12":
            
            while True:
                print("\n---------- CLOCK ----------")
                print("1. Alarm clock")
                print("2. Clock settings")
                print("3. Date setting")
                print("4. Stopwatch")
                print("5. Countdown timer")
                print("6. Auto update of date and time")
                print("0. Back")

                sub = input("Enter: ")

                match sub:
                    case "1":
                        print("Alarm clock")
                    case "2":
                        print("Clock settings")
                    case "3":
                        print("Date setting")
                    case "4":
                        print("Stopwatch")
                    case "5":
                        print("Countdown timer")
                    case "6":
                        print("Auto update of date and time")
                    case "0":
                        print("Returning to main menu...")
                        break
                    case _:
                        print("Invalid option.")

        case "13":
           
            while True:
                print("\n---------- PROFILES ----------")
                print("1. General")
                print("2. Silent")
                print("3. Meeting")
                print("4. Outdoor")
                print("5. Pager")
                print("0. Back")

                sub = input("Enter: ")

                match sub:
                    case "1":
                        print("General profile")
                    case "2":
                        print("Silent profile")
                    case "3" :
                        print("Meeting profile")
                    case "4":
                        print("Outdoor profile")
                    case "5":
                        print("Pager profile")
                    case "0":
                        print("Returning to main menu...")
                        break
                    case _:
                        print("Invalid option.")

        case "14":
            
            while True:
                print("\n---------- WAP SERVICES ----------")
                print("1. Home")
                print("2. Bookmarks")
                print("3. Service inbox")
                print("4. Settings")
                print("0. Back")

                sub = input("Enter: ")

                match sub:
                    case "1":
                        print("Home")
                    case "2":
                        print("Bookmarks")
                    case "3":
                        print("Service inbox")
                    case "4":
                        print("WAP settings")
                    case "0":
                        print("Returning to main menu...")
                        break
                    case _:
                        print("Invalid option.")

        case "15":
            
            while True:
                print("\n---------- SIM SERVICES ----------")
                print("1. SIM menu")
                print("2. SIM information")
                print("3. SIM applications")
                print("0. Back")

                sub = input("Enter: ")

                match sub:
                    case "1":
                        print("SIM menu")
                    case "2":
                        print("SIM information")
                    case "3":
                        print("SIM applications")
                    case "0":
                        print("Returning to main menu...")
                        break
                    case _:
                        print("Invalid option.")

        case "0":
            print("\nGoodbye!")
            break

        case _:
            print("\nInvalid option. Please try again.")
