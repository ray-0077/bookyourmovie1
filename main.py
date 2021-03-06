from movie import Movie
global row
global seats
print("Enter the number of rows: ")
row = int(input())
print("Enter the number of seats in each row: ")
seats = int(input())
while True:
    print("\n*** ------ Welcome------ ***")
    catalog = input(
        "1. Show Seats\n2. Buy Ticket\n3. View Statistics\n4. Show Booked Tickets Customer Info\n0. Exit\n\n")

    obj = Movie()

    if catalog == "1":
        obj.show_seats(row, seats)

    elif catalog == "2":
        obj.buy_ticket(row,seats)

    elif catalog == "3":
        obj.show_statistics(row, seats)

    elif catalog == "4":
        obj.show_booked_ticket()

    elif catalog == "0":
        break