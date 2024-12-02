import numpy as np


with open("input", "r") as file:
    lines = file.readlines()

safe_reports_count = 0

for line in lines:
    report = list(map(int, line.split()))
    print(report)
    diff_report = []
    is_safe = True

    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        diff_abs = np.abs(diff)

        diff_report.append(diff)

    max_diff = max(np.abs(diff_report))
    min_diff = min(diff_report)
    safe_cond_1 = True
    if max_diff > 3 or min_diff == 0:
        safe_cond_1 = False

    is_all_positive = all(d > 0 for d in diff_report)
    is_all_negative = all(d < 0 for d in diff_report)
    safe_cond_2 = is_all_positive or is_all_negative
    print("Safe cond 1: ", safe_cond_1)
    print("Safe cond 2: ", safe_cond_2)
    is_safe = safe_cond_1 and safe_cond_2
    if is_safe:
        safe_reports_count += 1
    print()

print("Safe reports count: ", safe_reports_count)
