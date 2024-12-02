import numpy as np


with open("input", "r") as file:
    lines = file.readlines()

safe_reports_count = 0


def is_report_safe(report):
    diff_report = []
    is_safe = True

    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        diff_report.append(diff)

    max_diff = max(np.abs(diff_report))
    min_diff = min(diff_report)

    safe_cond_1 = True
    if max_diff > 3 or min_diff == 0:
        safe_cond_1 = False

    is_all_positive = all(d > 0 for d in diff_report)
    is_all_negative = all(d < 0 for d in diff_report)
    safe_cond_2 = is_all_positive or is_all_negative

    # print("Safe cond 1: ", safe_cond_1)
    # print("Safe cond 2: ", safe_cond_2)
    is_safe = safe_cond_1 and safe_cond_2

    return is_safe


for line in lines:
    report = list(map(int, line.split()))
    print(report)
    is_safe = is_report_safe(report)

    if not is_safe:
        for i in range(len(report)):
            new_report = report.copy()
            new_report.pop(i)
            is_safe = is_report_safe(new_report)
            if is_safe:
                break

    print("Is safe: ", is_safe)
    if is_safe:
        safe_reports_count += 1
    print()

print("Safe reports count: ", safe_reports_count)
