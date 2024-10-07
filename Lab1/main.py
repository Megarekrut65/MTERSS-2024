import json
from datetime import datetime
from decimal import Decimal

from task_runner import run_until_completed

SYSTEM = "system.conf"

def format_places(num, places=12):
    return f"{num:.{places}f}".rstrip('0').rstrip('.')

def input_filename(msg):
    while True:
        answer = input(msg).strip()
        if len(answer) <=0 or len(answer) > 5:
            print("Length of filename must be between 1 and 5. Try other name")
            continue
        return answer + ".txt" if answer != "*" else None

def input_yes_no(msg):
    while True:
        answer = input(msg).strip().title()
        if answer == "Yes" or answer == "No":
            return answer

        print("Incorrect data. Write Yes or No")

def get_sys_info():
    try:
        sys_file = open(SYSTEM)
        obj = json.loads(sys_file.read())
        obj["files"] = obj.get("files", [])
        return obj
    except:
        return {"files":[]}

def save_sys_info(sys_info):
    file = open(SYSTEM, "w")
    file.write(json.dumps(sys_info, indent=2))
    file.close()

def get_actual_filename(sys_info):
    last_filename = sys_info.get("last")
    if not last_filename:
        return input_filename("The name of the new file (up to 5 letters of the Ukrainian and Latin alphabet and/or numbers)\n"
                       "or the symbol * in case of refusal to record and end the program: ")

    answer = input_yes_no(f"Write results to file <{last_filename}>? (Yes/No): ")
    if answer == "Yes":
        return last_filename
    # No

    files = sys_info["files"]
    count = len(files)
    if 0 < count < 5:
        return input_filename("The name of an existing file or a new file (up to 5 letters of the Ukrainian and Latin "
                       "alphabet and/or numbers)\nor the symbol * in case of refusal to record and end the program: ")

    answer = input_filename("The name of an existing file or the * symbol\nin case of aborting the write "
                   "and terminating the program: ")

    while answer and answer not in files:
        print(f"File <{answer}> not found")
        answer = input_filename("The name of an existing file or the * symbol\nin case of aborting the write "
                       "and terminating the program: ")

    return answer

WIDTH = {
    "Date (DD.MM.YYYY)":17,
    "Argument x":20,
    "Precision e":20,
    "Function result":21,
    "The series number N":21
}

SEP_LINE = "+"+"+".join(["-"*count for count in WIDTH.values()])+"+"
HEADER_LINE = "|" + "|".join([f"{key:^{value}}" for key, value in WIDTH.items()]) + "|"

def result_to_row(result):
    return "|" + "|".join([f"{value}".rjust(WIDTH[key]) for key, value in result.items()]) + "|"

def count_rows(filename):
    try:
        file = open(filename)
        count = 0
        for line in file:
            if line.startswith("|"):
                count+=1
        file.close()

        return count - 1
    except:
        return 0
def file_menu(results):
    answer = input_yes_no("Write the results to a file? (Yes/No): ")
    if answer == "No":
        print("Data is not written to the file")
        return

    sys_info = get_sys_info()
    filename = get_actual_filename(sys_info)
    if filename is None:
        print("Data is not written to the file")
        return

    sys_info["last"] = filename

    file = open(filename, "a")
    files = sys_info["files"]
    if filename not in files:
        files.append(filename)
        file.write(SEP_LINE + "\n")
        file.write(HEADER_LINE+"\n")
        file.write(SEP_LINE + "\n")

    for result in results:
        file.write(result_to_row(result) + "\n")
        file.write(SEP_LINE + "\n")
    file.close()

    save_sys_info(sys_info)

    count = count_rows(filename)
    print(f"Data is written to file <{filename}>.\nThe current number of rows is <{count}>")

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
            file_menu(results)
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