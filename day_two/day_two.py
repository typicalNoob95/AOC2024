def get_reports_from_file(filepath):
    with open(filepath) as file:
        lines = file.readlines()
        return [line.replace("\n", "").split(" ") for line in lines]

def report_is_increasing(report):
    return report[1] - report[0] > 0

if __name__ == "__main__":
    reports = get_reports_from_file("/home/fl/PycharmProjects/AOC2024/day_two/sample.txt")
