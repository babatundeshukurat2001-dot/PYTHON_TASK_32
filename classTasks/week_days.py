#number_of_the_week = int(input("Enter nunber of the week: "))
#
#match number_of_the_week:
#
#    case 1:
#        print("Monday")
#
#    case 2:
#        print("Tuesday")
#
#    case 3:
#        print("Wednesday")
#
#    case 4:
#        print("Thursday")
#
#    case 5:
#        print("Friday")
#
#    case 6:
#        print("Saturday")
#
#    case 7:
#        print("Sunday")

number_of_the_week = int(input("Enter number of the week: "))


get_day = lambda n: {

    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}.get(n, "Invalid number")

print(get_day(number_of_the_week))
