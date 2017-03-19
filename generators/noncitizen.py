import csv


def get_noncitizen_data_parse_into_lists(NonCitizenPrisonersAndPrisonersAge17AndUnderBySex2015):
    """
    Method that will read from the CSV file titled NonCitizenPrisonersAndPrisonersAge17AndUnderBySex2015
    and parse CSV data into lists by line
    Author: Dani Adkins
    """
    with open(NonCitizenPrisonersAndPrisonersAge17AndUnderBySex2015, "r", encoding="latin-1") as noncitizen_data:
        for noncitizen_data in csv.reader(noncitizen_data):
            yield noncitizen_data

if __name__ == '__main__':
    filename = "../excel_files/NonCitizenPrisonersAndPrisonersAge17AndUnderBySex2015.csv"
    iter_data = iter(get_noncitizen_data_parse_into_lists(filename))
    next(iter_data)

    for row in iter_data:

        state = row[1]
        total_noncitizen_prisoners = row[3]
        #will need a for to add total state and federal together for allover total
        print(state, total_noncitizen_prisoners)

