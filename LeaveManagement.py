class LeaveManagement:
    """
    Generic superclass to implement the
    Leave Management System functionality.

    Main methods:
        display_id: returns employee id
        display_name: returns employee name
        display_hours: returns total leave hours available
    """

    def __init__(self, id, name, hours):
        """
        Initializer
        @params
            id: employee id
            name: employee's full name
            hours: hours of leave available
        """
        self.employee_id = id
        self.name = name
        self.total_hours = hours

    def display_id(self):
        """
        Method to return employee id
        """
        # TODO allow ids to start with 0
        return self.employee_id

    def display_name(self):
        """
        Method to return employee full name
        """
        # TODO think about including middle name
        # TODO handle order of first and last name
        return f"{self.name[0]} {self.name[1]}"

    def display_hours(self):
        """
        Method to return hours
        """
        return self.total_hours

    def __str__(self):
        """
        Method to return details of leave
        """
        return f'Employee ID: {self.employee_id}\nEmployee Name: {self.name[0]} {self.name[1]}\nAvailable: {self.total_hours}\n'


class PaidTimeOff(LeaveManagement):
    """
    Child class of LeaveManagement

    Main Methods:
        add_hours:  returns accrued hours and total hours available
        display_accrued: returns accrued hours
        subtract_hours: returns hours taken and total hours available
        display_taken: returns PTO taken
    """

    def __init__(self, id, name, hours, accrued, taken):
        super().__init__(id, name, hours)
        """
        Initializer for Paid Time Off
        Inherits params from LeaveManagement class
        @params:
            accrued:  hours accumulated
            taken: hours taken
        """
        self.accrued = accrued
        self.taken = taken

    def add_hours(self, accrued):
        """
        Method to increment hours available
        to request
        Returns hours accrued and hours available
        """
        self.accrued += accrued
        self.total_hours += accrued
        return self.accrued, self.total_hours

    def display_accrued(self):
        """
        Method to return accrued hours
        """
        return self.accrued

    def subtract_hours(self, taken):
        """
        Method to decrement hours available
        to request from.
        Returns hours taken and hours available
        """
        self.taken += taken
        self.total_hours -= taken
        return self.taken, self.total_hours

    def display_taken(self):
        """
        Method to return hours taken
        """
        return self.taken

    def __str__(self):
        """
        Method to return details of leave
        """
        return f'Employee ID: {self.employee_id}\nEmployee Name: {self.name[0]} {self.name[1]}\nAvailable: {self.total_hours}\nAccrued: {self.accrued}\nTaken: {self.taken}\n'


class FlexTime(LeaveManagement):

    def __init__(self, id, name, hours, hours_worked):
        super().__init__(id, name, hours)
        """
        Initializer for Flex Time
        Inherits params from LeaveManagement class
        @params:
            hours_worked: number of hours worked in work week
        """
        self.hours_worked = hours_worked

    def add_flex(self, hours_worked):
        # TODO allow multiple weeks to accumulate
        """
        Method to increment flex hours
        Returns hours worked and hours available
        """
        self.hours_worked += hours_worked
        if self.hours_worked > 40:
            self.total_hours = self.hours_worked - 40
            return self.hours_worked, self.total_hours
        else:
            self.total_hours = 0
            return self.total_hours

    def display_hours_worked(self):
        """
        Method to return hours worked
        """
        return self.hours_worked


class WorkFromHome(LeaveManagement):
    def __init__(self, id, name, hours, deduct):
        super().__init__(id, name, hours)
        """
        Initializer for WorkFromHome
        Inherits params from LeaveManagement class
        @params:
            deduct: total hours deducted
        """
        self.deduct = deduct

    def deduct_wfh(self, deduct):
        """
        Method to deduct hours
        Returns hours available, hours deducted
        """
        self.deduct += deduct
        self.total_hours -= deduct
        return self.total_hours, self.deduct

    def __str__(self):
        """
        Method to return details of leave
        """
        return f'Employee ID: {self.employee_id}\nEmployee Name: {self.name[0]} {self.name[1]}\nAvailable: {self.total_hours}\nTotal Deducted: {self.deduct}\n'
