from maclaurin import MaclaurinSeries


def main():
    res = MaclaurinSeries.evaluate("0.1", "0.000000000001")
    print(res)


if __name__ == "__main__":
    main()