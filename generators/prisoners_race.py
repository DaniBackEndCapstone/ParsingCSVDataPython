import csv


def get_prisoners_by_race_data_parse_into_lists(PrisonersUnderJurisdicitonOfStateOrFederalByRace2015):
    """
    Method that will read from the CSV file titled PrisonersUnderJurisdicitonOfStateOrFederalByRace2015
    and parse CSV data into lists by line
    Author: Dani Adkins
    """
    with open(PrisonersUnderJurisdicitonOfStateOrFederalByRace2015, "r", encoding="latin-1") as prisoners_race_data:
        for prisoners_race_data in csv.reader(prisoners_race_data):
            yield prisoners_race_data

if __name__ == '__main__':
    filename = "../excel_files/PrisonersUnderJurisdicitonOfStateOrFederalByRace2015.csv"
    iter_data = iter(get_prisoners_by_race_data_parse_into_lists(filename))
    next(iter_data)

    for row in iter_data:
        print(row)

# def get_specific_prisoners_race_data_for_DB():