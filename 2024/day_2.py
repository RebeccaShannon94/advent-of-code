import pandas as pd

input_file = "data/input_day_2.csv"
data = pd.read_csv(input_file, header=None)

def check_sorted(report: list):
    """check values in list is all ascending or all descending"""
    return (
        True
        if report == sorted(report, reverse=True) or report == sorted(report)
        else False
    )

def check_all_dif_in_list(report: list):
    """check difference between all adjacent values between 1 and 3"""
    count = 0
    for i, j in zip(report[:-1], report[1:]):
        count = (
            count + 1
            if abs(int(i) - int(j)) > 0 and abs(int(i) - int(j)) < 4
            else count
        )
    return True if count == len(report) - 1 else False

def check_if_rm_level_makes_safe(report: list):
    """check if one value removed from list makes list meet check_sorted and check_all_dif_in_list conditions"""
    for i in list(range(0, len(report), 1)):
        test_report = report.copy()
        del test_report[i]
        if check_sorted(test_report) and check_all_dif_in_list(test_report):
            safe = True
            break
        else:
            safe = False
    return safe

lst_1 = data[0].tolist()

safe_count = 0
for report_number in list(range(0, len(lst_1))):
    report = list(map(int, lst_1[report_number].split(" ")))
    if check_sorted(report) and check_all_dif_in_list(report):
        safe_count += 1
print(f"safe reports: {safe_count}")

safe_count = 0
for report_number in list(range(0, len(lst_1))):
    report = list(map(int, lst_1[report_number].split(" ")))
    if check_sorted(report) and check_all_dif_in_list(report):
        safe_count += 1
    elif check_if_rm_level_makes_safe(report):
        safe_count += 1
print(f"safe reports (including removal): {safe_count}")
