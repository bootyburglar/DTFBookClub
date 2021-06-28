import sys

japan_year = {
    2019: "令和元年",
    1989: "平成元年",
    1926: "昭和元年",
    1912: "大正元年",
    1868: "明治元年",
}


def to_japan_year(input_year: int):
    for year, name in japan_year.items():
        if input_year >= year:
            year_count = input_year - year
            if year_count:
                return name.replace('元', str(input_year - year))
            return name
    else:
        return 'not support year'


def run():
    ret = to_japan_year(int(sys.argv[1]))
    print(ret)


if __name__ == '__main__':
    run()
