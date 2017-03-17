import csv


def get_correctional_totals_data_parse_into_lists(EstimatedNumberAndRateOfPersonsSupervisedByUSFacilities2015):
    """
    Method that will read from the CSV file titled EstimatedNumberAndRateOfPersonsSupervisedByUSFacilities2015
    and parse CSV data into lists by line
    Author: Dani Adkins
    """
    with open(EstimatedNumberAndRateOfPersonsSupervisedByUSFacilities2015, "r", encoding="latin-1") as correctional_totals_data:
        for correctional_totals_data in csv.reader(correctional_totals_data):
            yield correctional_totals_data

if __name__ == '__main__':
    filename = "../excel_files/EstimatedNumberAndRateOfPersonsSupervisedByUSFacilities2015.csv"
    iter_data = iter(get_correctional_totals_data_parse_into_lists(filename))
    next(iter_data)

    for row in iter_data:
        print(row)

# def get_specific_correctional_totals_data_for_DB():