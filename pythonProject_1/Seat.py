def seat(r, n):
    while n <= 0:
        print("Invalid Seat Number")
        return

    while r <= 0:
        print("Invalid Input")
        return

    while n == 1:
        print("Window Seat")
        return

    while n > 11*r:
        print("Invalid Seat Number")
        return

    if n % r == 0:
        print("Window Seat")
    else:
        print("Not Window Seat")

# Main Program
row_seat = int(input("Enter no.of seats in a row: "))
seat_no = int(input("Enter selected seat number: "))
seat(row_seat, seat_no)
