# Module Name: notes.py
# Purpose: Processing of YAML input files for validation of schema
# And reading of git-log file into string object for use in Invoice class
# Developer: Keivn Mercy
# _________________________________________________________________


from schema import Schema, Optional, SchemaError
import yaml


# Function Name: read_git_text_output
# Purpose: Read git commit file and start processing it for Invoice Class
# Parameters: in_f
def read_git_text_output(in_f):
    with open(in_f, "r") as file:
        commits = file.read()
        return commits


# Function Name: validate_yaml
# Purpose: validate schema of yaml file
# Parameters: in_yaml
# Return: dictionary of required parameters
def validate_yaml(in_yaml):
    config_schema = Schema(
        {
            "gspread_oauth_creds": str,
            "gspread_oauth_authorized": str,
            "gspread_url": str,
            "gspread_wksht": str,
            "provider_name": str,
            "provider_address": str,
            "provider_phone": str,
            "provider_email": str,
            "client_name": str,
            Optional("client_address"): str,
            Optional("client_phone"): str,
            Optional("client_email"): str,
            "invoice_template": str,
            "invoice_out": str,
            "invoice_num": str,
            Optional("git_log_outfile"): str,
        }
    )

    with open(in_yaml, "r") as file:
        configuration = yaml.safe_load(file)
        print(configuration)

        try:
            config_schema.validate(configuration)
            print("Configuration is valid.")
            return configuration
        except SchemaError as se:
            raise se
