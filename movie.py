import math
import re

class Movie:

    global customer
    global number
    number = []
    customer = []
    def show_seats(self, row, seats):
        global tickets_booked
        tickets_booked = 0
        print("Cinema:")
        for i in range(row + 1):
            for j in range(seats + 1):
                if i == 0:
                    if i == j == 0:
                        print(" ", end=" ")
                        continue
                    else:
                        print(j, end=" ")
                else:
                    if i == 1 and j == 0:
                        print("")
                    else:
                        count = 1
                        print(i, end=" ")
                        while (True):
                            if count <= seats:
                                seat_no = int(str(i) + str(count))
                                if seat_no in number:
                                    print("B", end=" ")
                                    tickets_booked += 1
                                else:
                                    print("S", end=" ")
                                count = count + 1
                            else:
                                print("")
                                break
                        break

    def buy_ticket(self, row, seats):
        global ticket_price
        global seat_status
        global seat_no
        s_row = int(input("Enter row number:"))
        s_col = int(input("Enter seat number:"))
        s_seat_no = int(str(s_row) + str(s_col))
        seat_no = int(str(row) + str(seats))
        seat_status = "Available"
        if s_seat_no in number:
            print("Seat already booked! Kindly see the arrangement and book another seat!\n")
            seat_status = "Booked"
        if seat_status == "Available":
            if s_row <= row and s_col <= seats:
                seat_no = int(str(s_row) + str(s_col))
                ticket_price = 0
                total_seats = row * seats
                if total_seats <= 60:
                    ticket_price = 10
                else:
                    division = row / 2
                    f_row = math.floor(division)
                    if s_row <= f_row:
                        ticket_price = 10
                    else:
                        ticket_price = 8
                print("Ticket price :", ticket_price)
                prompt = input("Do you want to book the ticket ? (yes/no):")
                ans = prompt.lower()
                if ans == "yes":
                    data = {}
                    name = input("Name: ")

                    while True:

                        gender = input("Gender(Male, Female or Transgender): ")
                        if gender.lower() not in ["male", "female", "transgender"]:
                            print("Invalid Gender")
                            continue
                        break

                    while True:

                        age = int(input("Age: "))
                        if age not in range(1, 101):
                            print("Invalid age ! Please enter age with intergers only")
                            continue
                        break

                    while True:

                        ph_no = (input("Phone Number: "))
                        x = re.match("[7-9][0-9]{9}", ph_no)
                        if not x:
                            print("Invalid Phone Number ! Please enter valid 10 digit number")
                            continue
                        break

                    data["name"] = name
                    data["gender"] = gender
                    data["age"] = age
                    data["ph_no"] = ph_no
                    data["seat_no"] = seat_no
                    data["row"] = row
                    data["ticket_price"] = ticket_price
                    customer.append(data)
                    if data["name"] in name:
                        number.append(seat_no)
                        print("Booked Successfully !!!!!!")
                        print("Thank you for booking.")
                    else:
                        print("Error")
                else:
                    print("Booking Cancelled.\n")
            else:
                print("Seat does not exist! Enter a valid seat number.")

    def show_statistics(self, row, seats):
        global total_income
        total_income = 0
        tickets_booked = len(number)
        print("Number of tickets purchased:", tickets_booked)

        total_seats = row * seats
        percentage_of_tickets_booked = (tickets_booked / total_seats) * 100
        print("Percentage of tickets booked:", str(round(percentage_of_tickets_booked, 2)) + "%")

        res = [key["ticket_price"] for key in customer]
        print("Current Income: ", str(sum(res)), "$")

        x = row * seats
        if x <= 60:
            total_income = 10 * seats * row
        else:
            x = row / 2
            division_row = math.floor(x)
            premium_tickets_price = 10 * seats * division_row
            normal_tickets_rows = row - division_row
            normal_tickets_price = 8 * seats * normal_tickets_rows
            total_income = premium_tickets_price + normal_tickets_price
        print("Total Possible Income:", "$" + str(total_income))


    def show_booked_ticket(self):
        ans = input("Do you want to see all customer information or about a particular seat of customer (all/seat number) ?\n")
        Ans = ans.lower()

        if Ans == "all":
            customer_number = 0
            for customers in customer:
                customer_number += 1
                print(str(customer_number) + ".)")
                print("Name:", customers["name"])
                print("Gender:", customers["gender"])
                print("Age:", customers["age"])
                print("Ticket Price:" + str(customers["ticket_price"]) + "$")
                print("Phone Number:", customers["ph_no"], "\n")

        elif Ans == "seat number":
            s_row = int(input("Enter row:"))
            s_col = int(input("Enter col:"))
            sno = int(str(s_row) + str(s_col))
            x = next((customer_info for customer_info in customer if customer_info["seat_no"] == sno))
            if sno == x["seat_no"]:
                print("Name:", x["name"])
                print("Gender:", x["gender"])
                print("Age:", x["age"])
                print("Ticket Price:", str(x["ticket_price"]) + "$")
                print("Phone Number:", x["ph_no"])
            else:
                print("No booking for this seat.\n")

        else:
            print("Invalid input!\n")
            