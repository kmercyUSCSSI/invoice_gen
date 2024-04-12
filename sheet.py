# Module Name: sheet.py
# Purpose: Processing of google sheets using gspread, requires setup with OAuth
# credentials from Google Sheets API, and Google Drive API. Functions grab
# data in worksheet and provide list of services to populate in the word docx invoice
# Developer: Keivn Mercy
# _________________________________________________________________


import gspread


# Function Name: get_sh_records
# Function Purpose: return values in Google Sheet for input into invoice
# Function Parameters: none
# Function Return: list of the spreadsheet
def get_sh_records(url, wkst_name, o_auth_in, o_auth_authorized):
    # Authenticating into google spreadsheets
    gc = gspread.oauth(
        credentials_filename=o_auth_in, authorized_user_filename=o_auth_authorized
    )

    # Open the spreadsheet via url
    spreadsheet = gc.open_by_url(url)

    # Get the worksheet
    worksheet = spreadsheet.worksheet(wkst_name)

    # Get the records
    records = worksheet.get_all_values()

    print(records)

    # Return the records
    return records


# Function Name: return_services
# Purpose: Serializes the input table retrieved into format required for mailmerge
# in docx
# Parameters: url, wkst_name
# Return: serialized list of services
def return_services(url, wkst_name, o_auth_in, o_auth_authorized):
    # Get the full record list using sheets API
    records = get_sh_records(url, wkst_name, o_auth_in, o_auth_authorized)

    # Get rid of the header row
    services_only_arr = records[1:]
    services_dict = []

    # Iterate over rows and create serialization for services in mailmerge
    for record in services_only_arr:
        # Required json format
        item = {
            "Service": record[0],
            "Hours": record[1],
            "Rate": record[2],
            "SubTotal": record[3],
        }
        services_dict.append(item)
    # Return the dictionary
    return services_dict


# Function Name: get_total
# Purpose: Subs the services sub_total and returns total due
# Parameters: url, wkst_name
# Return: total due
def get_total(url, wkst_name, o_auth_in, o_auth_authorized):
    # Get the full record list using sheets API
    records = get_sh_records(url, wkst_name, o_auth_in, o_auth_authorized)

    # Get rid of the header row
    services_only_arr = records[1:]
    total = 0.0

    # Iterate over rows and += on subtotal to retrieve total due
    for record in services_only_arr:
        total += float(record[3])

    # Return the total
    print(total)
    return str(total)
