# Class Name: Invoice
# Class Vars: provider information, client information, total, notes, due date,
# today date, services
# Class for generating a word document invoice using input information. Class will
# be used to automate retrieval of spreadsheet and git information to populate the
# invoice
# Developer: Keivn Mercy
# _____________________________________________________________________________________


from mailmerge import MailMerge
from datetime import date, timedelta


# Class Invoice -- Creating Invoices using the template, and populating them
# with required information. Generation of Class, and export of document to word
class Invoice:
    # Set invoice template
    invoice_template = ""
    invoice_num = ""
    invoice_out = ""

    # Dates
    today = date.today()
    today = today.strftime("%b %d, %Y")
    due_date = date.today() + timedelta(days=30)
    due_date = due_date.strftime("%b %d, %Y")

    # Provider vars - Set to My information if not passed in
    provider_name = ""
    provider_address = ""
    provider_phone = ""
    provider_email = ""

    # Client vars - Set to blank if not passed in
    client_name = ""
    client_address = ""
    client_phone = ""
    client_email = ""

    # Other vars - set to black if not passed in
    total = ""
    notes = ""

    # Services
    services = []

    # Parameterized Constructor to set values if they are passed in
    def __init__(
        self,
        provider_name=None,
        provider_address=None,
        provider_phone=None,
        provider_email=None,
        client_name=None,
        client_address=None,
        client_phone=None,
        client_email=None,
        invoice_template=None,
        invoice_num=None,
        invoice_out=None,
        total=None,
        notes=None,
        services=None,
    ):
        if provider_name != None:
            self.provider_name = provider_name

        if provider_address != None:
            self.provider_address = provider_address

        if provider_phone != None:
            self.provider_phone = provider_phone

        if provider_email != None:
            self.provider_email = provider_email

        if client_name != None:
            self.client_name = client_name

        if client_address != None:
            self.client_address = client_address

        if client_phone != None:
            self.client_phone = client_phone

        if client_email != None:
            self.client_email = client_email

        if invoice_template != None:
            self.invoice_template = invoice_template

        if invoice_num != None:
            self.invoice_num = invoice_num

        if invoice_out != None:
            self.invoice_out = invoice_out

        if total != None:
            self.total = total

        if notes != None:
            self.notes = notes

        if services != None:
            self.services = services

    # Member Function: print_atts
    # Purpose: Print all member variable attributes
    def print_atts(self):
        # Provider info
        print("Provider Name:", self.provider_name)
        print("Provider Address:", self.provider_address)
        print("Provider Phone:", self.provider_phone)
        print("Provider Email:", self.provider_email)

        # Client info
        print("Client Name:", self.client_name)
        print("Client Address:", self.client_address)
        print("Client Phone:", self.client_phone)
        print("Client Email:", self.client_email)

        # File info
        print("Invoice template docx:", self.invoice_template)
        print("Invoice number:", self.invoice_num)
        print("Invoice outfile:", self.invoice_out)

        # Total and Dates
        print("Total Due:", self.total)
        print("Today:", self.today)
        print("Due Date:", self.due_date)

        # Notes
        print("Notes:", self.notes)

        # Services retrieved from Google Sheets
        print("Services:", self.services)

    # Member Function: set_invoice_template
    # Purpose: set the invoice infile template
    # Parameters: invoice templated file, word doc with mailmerge settings
    def set_invoice_template(self, in_template):
        self.invoice_template = in_template

    # Member Function: set_invoice_outfile
    # Purpose: set the outfile docx path
    # Parameters: output word file path
    def set_invoice_outfile(self, outf):
        self.invoice_out = outf

    # Member Function: set_invoice_num
    # Purpose: set the invoice num
    # Parameters: invoice num
    def set_invoice_num(self, num):
        self.invoice_num = num

    # Member Function: set_provider_name
    # Purpose: set the provider name
    # Parameters: provider name
    def set_provider_name(self, name):
        self.provider_name = name

    # Member Function: set_provider_address
    # Purpose: set the provider address
    # Parameters: provider address
    def set_provider_address(self, address):
        self.provider_address = address

    # Member Function: set_provider_phone
    # Purpose: set the provider phone
    # Parameters: provider phone
    def set_provider_phone(self, phone):
        self.provider_phone = phone

    # Member Function: set_provider_email
    # Purpose: set the provider email
    # Parameters: provider email
    def set_provider_phone(self, email):
        self.provider_email = email

    # Member Function: set_client_name
    # Purpose: set the client name
    # Parameters: client name
    def set_client_name(self, name):
        self.client_name = name

    # Member Function: set_client_address
    # Purpose: set the client address
    # Parameters: client address
    def set_client_address(self, address):
        self.client_address = address

    # Member Function: set_client_phone
    # Purpose: set the client phone
    # Parameters: client phone
    def set_client_phone(self, phone):
        self.client_phone = phone

    # Member Function: set_client_email
    # Purpose: set the client email
    # Parameters: client email
    def set_client_email(self, email):
        self.client_email = email

    # Member Function: fill_template
    # Purpose: Using populated class, fill in the Invoice template and export
    # the out document
    def fill_template(self):
        # Setting up MailMerge with the input template
        out_doc = MailMerge(self.invoice_template)

        # Performing merge using specified fields/data
        out_doc.merge(
            InvoiceNumber=self.invoice_num,
            InvoiceDate=self.today,
            ProviderName=self.provider_name,
            ProviderAddress=self.provider_address,
            ProviderPhone=self.provider_phone,
            ProviderEmail=self.provider_email,
            ClientName=self.client_name,
            ClientAddress=self.client_address,
            ClientPhone=self.client_phone,
            ClientEmail=self.client_email,
            Total=self.total,
            DueDate=self.due_date,
            Notes=self.notes,
        )

        # If services exist then merge rows in the table also
        if len(self.services) != 0:
            out_doc.merge_rows("Service", self.services)

        # Write the output docx
        out_doc.write(self.invoice_out)
