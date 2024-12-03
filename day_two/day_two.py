def get_reports_from_file(filepath):
    with open(filepath) as file:
        lines = file.readlines()
        reports_as_string =  [line.replace("\n", "").split(" ") for line in lines]
        reports = []
        for ras in reports_as_string:
            reports.append(list(map(int, ras)))
        return reports

def levels_are_increasing(actual_level, next_level):
    return actual_level - next_level < 0

def levels_difference_in_specs(actual_level, next_level):
    difference_range = range(1,4)
    return abs(actual_level - next_level) in difference_range

def report_is_safe(report):
    increasing = levels_are_increasing(report[0], report[1])
    safe = True
    for i in range(len(report) - 1):
        if levels_are_increasing(report[i], report[i + 1]) != increasing or not levels_difference_in_specs(report[i], report[i + 1]):
            safe = False
            return safe
    return safe

if __name__ == "__main__":
    reports = get_reports_from_file("/home/fl/PycharmProjects/AOC2024/day_two/sample.txt")
    for report in reports:
        print(report_is_safe(report))
