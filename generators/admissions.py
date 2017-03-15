import csv
# import json
# import sys, getopt

def get_admissions_data_parse_into_plain_text(AdmissionsAndReleasesOfPrisonersStateAndLocal20142015):
    """
    Method that will read CSV and parse CSV data into plain text with commas in between
    Author: Dani Adkins
    """
    # with open('../excel_files/AdmissionsAndReleasesOfPrisonersStateAndLocal20142015.csv', newline='') as admission_csv:
    #       admission_reader = csv.reader(admission_csv, delimiter=',')
    #       # rows = list(admission_reader)
    #       for row in admission_reader:
    #           print(', '.join(row))


# Read CSV and output into lists

def get_admissions_data_parse_into_lists(AdmissionsAndReleasesOfPrisonersStateAndLocal20142015):
    """
    Method that will read CSV and parse CSV data into lists by line
    Author: Dani Adkins
    """
    with open(AdmissionsAndReleasesOfPrisonersStateAndLocal20142015, "r", encoding="latin-1") as admission_data:
        for admission_data in csv.reader(admission_data):
            yield admission_data

if __name__ == '__main__':
    filename = "../excel_files/AdmissionsAndReleasesOfPrisonersStateAndLocal20142015.csv"
    iter_data = iter(get_admissions_data_parse_into_lists(filename))
    next(iter_data)

    for row in iter_data:
        print(row)




# def write_admissions_json(iter_data, AdmissionsAndReleasesOfPrisonersStateAndLocal20142015):
#   with open(AdmissionsAndReleasesOfPrisonersStateAndLocal20142015, "w") as admission_data_open:
#     if format == "pretty":
#       admission_data_open.write(json.dumps(data, separators=(","), encoding="utf-8",ensure_ascii=False))
#     else:
#       f.write(json.dumps(data))




