import csv


def get_gender_data_parse_into_lists(NumberPersonsCorrectionalFacilityBySexAndStatus):
    """
    Method that will read from the CSV file titled NumberPersonsCorrectionalFacilityBySexAndStatus
    and parse CSV data into lists by line
    Author: Dani Adkins
    """
    with open(NumberPersonsCorrectionalFacilityBySexAndStatus, "r", encoding="latin-1") as gender_data:
        for gender_data in csv.reader(gender_data):
            yield gender_data

if __name__ == '__main__':
    filename = "../excel_files/NumberPersonsCorrectionalFacilityBySexAndStatus.csv"
    iter_data = iter(get_gender_data_parse_into_lists(filename))
    next(iter_data)

    for row in iter_data:
        print(row)

# def get_specific_gender_data_for_DB():
