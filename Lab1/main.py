from datetime import datetime
from decimal import Decimal

from file_writer import file_menu
from task_runner import run_until_completed

SYSTEM = "system.conf"


def format_places(num, places=12):
    return f"{num:.{places}f}".rstrip('0').rstrip('.')

def input_decimal(msg, command=None, min_=None, max_=None):
    while True:
        try:
            num = input(msg)

            if command and num.lower() == command.lower():
                return None
            dec = Decimal(num)

            if min_ is not None and dec <= min_:
                print("Value is too small. Write value greater than", min_)
                continue

            if max_ is not None and dec >= max_:
                print("Value is too big. Write value lesser than", max_)
                continue

            return dec
        except:
            print("Invalid value. Write decimal number like 0.0000")

def main():
    results = []

    while True:
        x = input_decimal("Enter the function argument(-inf, inf) or `end` to quit: ", command="end")
        if x is None:
            file_menu(SYSTEM, results)
            return
        eps = input_decimal("Enter the precision of the calculation(0, 1): ", min_=0, max_=1)

        y, n = run_until_completed(x, eps)

        x = format_places(x)
        eps = format_places(eps)
        if y is not None and eps is not None:
            y = format_places(y)
            n = f"{n}"
            print(f"f({x}, {eps}) = {y}")
            print(f"N({x}, {eps}) = {n}")
        else:
            y = "-"
            n = "-"

        results.append({
            "Date (DD.MM.YYYY)": datetime.now().strftime("%d.%m.%Y"),
            "Argument x": x,
            "Precision e": eps,
            "Function result": y,
            "The series number N": n
        })

if __name__ == "__main__":
    main()