import csv


def get_state_private_jail_data_parse_into_lists(PrisonersUnderJurisdictionOfStateAndPrivatePrisons20142015):
    """
    Method that will read from the CSV file titled PrisonersUnderJurisdictionOfStateAndPrivatePrisons20142015
    and parse CSV data into lists by line
    Author: Dani Adkins
    """
    with open(PrisonersUnderJurisdictionOfStateAndPrivatePrisons20142015, "r", encoding="latin-1") as state_private_jail_data:
        for state_private_jail_data in csv.reader(state_private_jail_data):
            yield state_private_jail_data

if __name__ == '__main__':
    filename = "../excel_files/PrisonersUnderJurisdictionOfStateAndPrivatePrisons20142015.csv"
    iter_data = iter(get_state_private_jail_data_parse_into_lists(filename))
    next(iter_data)

    for row in iter_data:
        print(row)

# def get_specific_state_private_jail_for_DB():
