from LeaveManagement import LeaveManagement, PaidTimeOff


class main():

    def leave_management():
        test_leave = LeaveManagement(1121, ("Billie", "Muzzy"), 10)
        # output = label + 1121, Billie Muzzy, 10
        print(f"{test_leave}\n")

    def paid_time_off():
        test_pto = PaidTimeOff(1234, ("Atlas", "Muzzy"), 23, 0, 0)
        test_pto.add_hours(10)
        test_pto.subtract_hours(5)
        test_pto.add_hours(1)
        test_pto.subtract_hours(2)
        # output = label + 1234, Atlas Muzzy, 27
        print(test_pto)

    # leave_management()
    paid_time_off()


main()
