
def add_two_numbers(a,b):
    return a + b


def area_of_a_circle(r):
    return 3.1416 * r**2
    

def add_all_nums(aas):
    for i in aas:
        aas = aas + 1
        print(aas)


def from_celsius_to_fahrenheit(celsius):
    return(celsius * 9 / 5) + 32


def check_season(mes):
    if mes in ["march", "april", "may"]:
        return("Spring")
    
    elif mes in ["june", "july", "august"]:
        return("Summer")

    elif mes in ["septiembre", "october", "november"]:
        return("Autumn")

    elif mes in ["december", "january", "february"]:
        return("Winter")



def calculate_slope(x1, x2):
    return x2 + x1


def solve_quadratic_eqn(x1,x2,x3):
    solve = x2 * x2 -4 * x1 * x3 / 2 * x1
    return solve


def print_list(lss):
    lss = []
    for i in lss:
        print(i)


def reverse_list(lia):
    return lia[::-1]

