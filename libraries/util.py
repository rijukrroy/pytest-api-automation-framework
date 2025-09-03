import openpyxl
import json

def read_excel_data(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):  # skip header
        data.append(row)
    return data

def read_json_data(file_path):
    with open(file_path, "r") as f:
        json_data = json.load(f)
    print(type(json_data))
    # Convert to list of tuples for parametrize
    user_data = [(item["name"], item["email"], item["gender"], item["status"]) for item in json_data]
    return user_data
