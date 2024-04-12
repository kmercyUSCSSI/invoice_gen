# invoice_gen
Automated Invoice Generation using Google Sheets, git-log, and Microsft Word to create a
stylized invoice. Stylized invoice fills in details regarding client information,
provider information, dates, services rendered, total due, and notes as a list of
commits from git-log using an input Microsoft Word docx with merge-fields enabled and
a .yaml file specifying the configurations of the matching attributes in Microsoft Word.
This project is useful for general software engineers looking for a quick way to
automate invoices for their clients. Or without git-log notes, for general consultants.

## Pre-requisites:
- Goolge Sheets Worksheet, including list of services, hours, rates, and subtotals.
Follow general row schema (include header followed by rows of data) e.g.:

["Service", "Hours", "Rate", "SubTotal"]

["Software Services", "10", "20", "200"]

etc.

Project requires a google sheet name, and its url
- Setup access to Google Sheets API, Google Drive API and receive credentials
for OAuth for your account (See here:https://docs.gspread.org/en/v6.0.0/oauth2.html and
follow instructions for "For End Users: Using OAuth Client ID").

Project requires a json document of your credentials from Google Developer and a json
file to store authorized user credentials: e.g. you and your access token.

This setup is required to interacte directly with Google Sheets in Python
- git repo with commits that you want to append as "notes".

See test docs/generate_commits_example.sh for useage.

Basically format git-log to your liking and save the output to a file location
you have access to (easier to use in linux, I used in git bash terminal)

It is OPTIONAL to produce git-log and add this output to "Notes" part of invoice
- Microsoft word -> for editing the template to your liking and viewing the output
- Install Anaconda and setup python env for project.

(https://docs.anaconda.com/free/anaconda/install/).

Project was tested/built on Windows using Anaconda.

## General Use
Install anaconda and run (replace <env> with your desired environment name):

```
conda create --name <env> --file /docs/conda_requirments.txt
```

Activate new conda env:
```
conda activate <env>
```

Run the program:
```
python main.py yaml_config.yaml
```

### Note: edit yaml_config.yaml to match your parameters
Schema Below:
REQUIRED gspread_oauth_creds: /path/to/my/gspread/oauth/credentials.json

REQUIRED gspread_oauth_authorized: /path/to/my/gspread/oauth/authorized_credentials.json

REQUIRED gspread_url: https://docs.google.com/spreadsheets/myfile

REQUIRED gspread_wksht: MyWorkSheetName

OPTIONAL git_log_outfile: /path/to/my/git-log/output.txt

REQUIRED client_name: Client Business Name

OPTIONAL client_address: 123 Business Place, NYC, NY 99999

OPTIONAL client_email: buiness@gmail.com

OPTIONAL client_phone: 111 111 1111

REQUIRED provider_name: My LLC

REQUIRED provider_address: 123 My Address St, NYC, NY 99999

REQUIRED provider_phone: 111 111 1111

REQUIRED provider_email: mybusiness@gmail.com

REQUIRED invoice_template: /path/to/invoice.docx

REQUIRED invoice_out: /path/to/my/output/invoice.docx

REQUIRED invoice_num: INV-001

git-log outfile for writing to notes is optional along with Client Address, Email, and Phone

Provider information if required, along with Google Sheets OAuth credentials, sheetname,
and url.

Required input of word .docx template file (exmple included in /docs/invoice.docx) with
mailmerge fields. Program will use your config, GoogleSheet values, git-log values
to "merge" with template fields in template .docx

Required outfile path of .docx -> Place in location of your liking

Required Invoice #: Any string will do

Assuming the input template is valid (like example in /docs/invoice.docx) and config
contains correct information for accessing Google Sheets, with correct formatting of
GoogleSheet, and optional git-log output file -- program will merge configurations
into a new output .docx file.
