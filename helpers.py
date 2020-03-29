# helper functions written by Billie Muzzy for formatting
def bar():
    """
    prints a bar 50 chars long
    made with the = symbol
    """
    print(f"{'='*50}")


def print_header(title):
    """
    prints a bar 50 chars long
    made with the = symbol
    also outputs title centered
    """
    bar()
    print("{0:^50}".format(title))
    bar()
