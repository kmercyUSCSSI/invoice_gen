# Module Name: main.py
# Purpose: main driver for processing invoices: use as main.py C:/path_to_yaml
# Generates word docx invoice using word mailmerge function with properly formatted
# word doc, data stored in Google Sheets, and a list of git commits from
# git-log
# Developer: Keivn Mercy
# _________________________________________________________________


from sheet import return_services, get_total
from Invoice import Invoice
from notes import read_git_text_output, validate_yaml
from schema import SchemaError
import sys
import os


# Function: main
# Purpose: run main processing of YAML configuration file to generate invoice
# Parameters: arg -> YAML config file with correct schema (See notes.py for schema)
# Return: creates an output file with the data from google spreadsheet, git, and word
# template
def main(in_yaml):

    try:
        content = validate_yaml(in_yaml)

        in_git_txt = ""
        if "git_log_outfile" in content.keys():
            in_git_txt = read_git_text_output(content["git_log_outfile"])

        services = return_services(
            content["gspread_url"],
            content["gspread_wksht"],
            content["gspread_oauth_creds"],
            content["gspread_oauth_authorized"],
        )

        total_due = get_total(
            content["gspread_url"],
            content["gspread_wksht"],
            content["gspread_oauth_creds"],
            content["gspread_oauth_authorized"],
        )

        today_invoice = Invoice(
            client_name=content["client_name"],
            provider_name=content["provider_name"],
            provider_address=content["provider_address"],
            provider_email=content["provider_email"],
            provider_phone=content["provider_phone"],
            invoice_template=content["invoice_template"],
            invoice_num=content["invoice_num"],
            invoice_out=content["invoice_out"],
            notes=in_git_txt,
            services=services,
            total=total_due,
        )

        if "client_address" in content.keys():
            today_invoice.set_client_address(content["client_address"])

        if "client_phone" in content.keys():
            today_invoice.set_client_phone(content["client_phone"])

        if "client_email" in content.keys():
            today_invoice.set_client_email(content["client_email"])

        today_invoice.print_atts()

        today_invoice.fill_template()

    except SchemaError as se:
        raise RuntimeError("Failed to run program") from se


# Define entry point of package
# Useage: python main.py D:/data/invoice.yaml
# Fails without input yaml, and incorrect yaml will be rejected
# See notes.py for schema configuration
if __name__ == "__main__":

    args = sys.argv[1:]
    print(args)

    if len(args) > 0:
        if os.path.exists(args[0]):
            main(args[0])
        else:
            print("Not a correct config file")
            sys.exit()
    else:
        print("No file argument passed")
        sys.exit()
