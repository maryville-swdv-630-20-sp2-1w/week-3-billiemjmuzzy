from LeaveManagement import LeaveManagement, PaidTimeOff, FlexTime, WorkFromHome
from helpers import print_header


class main():
    """
    Testing LeaveManagement.py
    """

    def leave_management():
        print_header("Leave Management")
        test_leave = LeaveManagement(1121, ("Billie", "Muzzy"), 10)
        # output = label + 1121, Billie Muzzy, 10
        print(test_leave)

    def paid_time_off():
        print_header("Paid Time Off")
        test_pto = PaidTimeOff(1234, ("Atlas", "Muzzy"), 23, 0, 0)
        test_pto.add_hours(10)
        test_pto.subtract_hours(5)
        test_pto.add_hours(1)
        test_pto.subtract_hours(2)
        # output = label + 1234, Atlas Muzzy, 27
        print(test_pto)

    def flex_time():
        print_header("Flex Time")
        test_flex = FlexTime(4321, ("Gizmo", "Muzzy"), 0, 0)
        test_flex.add_flex(43)
        # output = label + 4321, Gizmo Muzzy, 3
        print(test_flex)

    def work_from_home():
        print_header("Work From Home")
        test_wfh = WorkFromHome(1111, ("Mystery", "Person"), 16, 0)
        test_wfh.deduct_wfh(8)
        test_wfh.deduct_wfh(8)
        # output = label + 1111, Myster Person, 0, 16
        print(test_wfh)

    leave_management()
    paid_time_off()
    flex_time()
    work_from_home()


main()
