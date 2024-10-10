import json


def correct_name(filename:str):
    for sign in filename:
        if not sign.isdigit() and not sign.isalpha():
            return False

    return True

def input_filename(msg):
    while True:
        answer = input(msg).strip()
        if len(answer) <=0 or len(answer) > 5:
            print("Length of filename must be between 1 and 5. Try other name")
            continue
        if not correct_name(answer):
            print("The file name can only contain characters of the Ukrainian or Latin alphabet or numbers. Try other name")
            continue
        return answer + ".txt" if answer != "*" else None

def input_yes_no(msg):
    while True:
        answer = input(msg).strip().title()
        if answer == "Yes" or answer == "No":
            return answer

        print("Incorrect data. Write Yes or No")

def get_sys_info(sys_path):
    try:
        sys_file = open(sys_path)
        obj = json.loads(sys_file.read())
        obj["files"] = obj.get("files", [])
        return obj
    except:
        return {"files":[]}

def save_sys_info(sys_path, sys_info):
    file = open(sys_path, "w")
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
        print(f"File <{answer}> not found in existing. Try existing name")
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
def file_menu(sys_path, results):
    answer = input_yes_no("Write the results to a file? (Yes/No): ")
    if answer == "No":
        print("Data is not written to the file")
        return

    sys_info = get_sys_info(sys_path)
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

    save_sys_info(sys_path, sys_info)

    count = count_rows(filename)
    print(f"Data is written to file <{filename}>.\nThe current number of rows is <{count}>")

