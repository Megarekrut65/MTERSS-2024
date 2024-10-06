
from app.maclaurin import MaclaurinSeries

def file_menu(results):
    answer = input("Write the results to a file? (Yes/No): ")
    if answer.title() == "No":
        print("Data is not written to the file")
        return



def main():
    results = []

    while True:
        x = input("Enter the function argument(-inf, inf) or `end` to quit: ")
        if x.lower() == "end":
            filename = input("Enter the filename(optional): ")

        eps = input("Enter the precision of the calculation(0, 1): ")

        try:
            y, n = MaclaurinSeries.evaluate(x, eps)
            results.append((y, n))
            print(f"f({x}, {eps}) = {y}")
            print(f"N({x}, {eps}) = {n}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()