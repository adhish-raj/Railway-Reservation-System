# Railway Reservation System
print("Welcome to Railway Reservation System")
print("System Ready to Use")
total_seats = 50
bookings = {}
seat_counter = 1


def check_availability():
    available = total_seats - len(bookings)
    print(f"Available seats: {available}")


def book_ticket():
    global seat_counter

    if len(bookings) >= total_seats:
        print("Sorry, no seats available.")
        return

    name = input("Enter your name: ")
    age = input("Enter your age: ")

    booking_id = f"B{100 + len(bookings)}"
    seat_number = seat_counter

    bookings[booking_id] = {
        "name": name,
        "age": age,
        "seat": seat_number
    }

    seat_counter += 1

    print("Ticket booked successfully!")
    print(f"Booking ID: {booking_id}")
    print(f"Seat Number: {seat_number}")


def view_ticket():
    booking_id = input("Enter Booking ID: ")

    if booking_id in bookings:
        print("Ticket Details:")
        print(f"Name: {bookings[booking_id]['name']}")
        print(f"Age: {bookings[booking_id]['age']}")
        print(f"Seat: {bookings[booking_id]['seat']}")
    else:
        print("Invalid Booking ID.")


def cancel_ticket():
    global seat_counter

    booking_id = input("Enter Booking ID to cancel: ")

    if booking_id in bookings:
        del bookings[booking_id]
        print("Ticket cancelled successfully!")
    else:
        print("Invalid Booking ID.")


def menu():
    while True:
        print("\n--- Railway Reservation System ---")
        print("1. Check Availability")
        print("2. Book Ticket")
        print("3. View Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            check_availability()
        elif choice == '2':
            book_ticket()
        elif choice == '3':
            view_ticket()
        elif choice == '4':
            cancel_ticket()
        elif choice == '5':
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again.")


# Run the program
menu()
