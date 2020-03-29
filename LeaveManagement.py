class LeaveManagement:
    """
    Generic superclass to implement the
    Leave Management System functionality.

    Main methods:
    """

    def __init__(self, id, name, hours):
        """
        Initializer
        @params
            name: full name of user
            hrs: number of hours available
        """
        self.employee_id = id
        self.name = name
        self.total_hours = hours

    def display_id(self):
        # TODO allow ids to start with 0
        return self.employee_id

    def display_name(self):
        """
        Method to return name
        """
        return f"{self.name[0]} {self.name[1]}"

    def display_hours(self):
        """
        Method to return hours
        """
        return self.total_hours

    def __str__(self):
        return f'Employee ID: {self.employee_id}\nEmployee Name: {self.name[0]} {self.name[1]}\nAvailable: {self.total_hours}\n'


class PaidTimeOff(LeaveManagement):
    def __init__(self, id, name, hours, accrued, taken):
        super().__init__(id, name, hours)
        self.accrued = accrued
        self.taken = taken

    def add_hours(self, accrued):
        """
        Method to increment hours available
        to request
        """
        self.accrued += accrued
        self.total_hours += accrued
        return self.accrued, self.total_hours

    def display_accrued(self):
        return self.accrued

    def subtract_hours(self, taken):
        """
        Method to decrement hours available
        to request from
        """
        self.taken += taken
        self.total_hours -= taken
        return self.taken, self.total_hours

    def display_taken(self):
        return self.taken

    def __str__(self):
        return f'Employee ID: {self.employee_id}\nEmployee Name: {self.name[0]} {self.name[1]}\nAvailable: {self.total_hours}\nAccrued: {self.accrued}\nTaken: {self.taken}\n'


class FlexTime(LeaveManagement):
    # TODO allow multiple weeks to accumulate
    def __init__(self, id, name, hours, hours_worked):
        super().__init__(id, name, hours)
        self.hours_worked = hours_worked

    def add_flex(self, hours_worked):
        self.hours_worked += hours_worked
        if self.hours_worked > 40:
            self.total_hours = self.hours_worked - 40
            return self.hours_worked, self.total_hours
        else:
            self.total_hours = 0
            return self.total_hours

    def display_hours_worked(self):
        return self.hours_worked


class WorkFromHome(LeaveManagement):
    def __init__(self, id, name, hours, deduct):
        super().__init__(id, name, hours)
        self.deduct = deduct

    def deduct_wfh(self, deduct):
        self.deduct += deduct
        self.total_hours -= deduct
        return self.total_hours, self.deduct

    def __str__(self):
        return f'Employee ID: {self.employee_id}\nEmployee Name: {self.name[0]} {self.name[1]}\nAvailable: {self.total_hours}\nTotal Deducted: {self.deduct}\n'
