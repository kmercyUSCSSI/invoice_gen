# Class Name: Invoice
# Class Vars: provider information, client information, total, notes, due date,
# today date, services
# Class for generating a word document invoice using input information. Class will
# be used to automate retrieval of spreadsheet and git information to populate the
# invoice
#_____________________________________________________________________________________

class Invoice:
    # Provider vars - Set to My information if not passed in
    provider_name = "Kevin Mercy"
    provider_address = "12283 W Mississippi Ave Lakewood, CO 80228"
    provider_phone = "720 251 5563"
    provider_email = "kevn.mercy@gmail.com"

    # Client vars - Set to blank if not passed in
    client_name = ""
    client_address = ""
    client_phone = ""
    client_email = ""

    # Other vars - set to black if not passed in
    total = ""
    notes = ""

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
        total=None,
        notes=None,
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

        if total != None:
            self.total = total

        if notes != None:
            self.notes = notes

    def print_atts(self):
        print("Provider Name:", self.provider_name)
        print("Provider Address:", self.provider_address)
        print("Provider Phone:", self.provider_phone)
        print("Provider Email:", self.provider_email)

        print("Client Name:", self.client_name)
        print("Client Address:", self.client_address)
        print("Client Phone:", self.client_phone)
        print("Client Email:", self.client_email)

        print("Total Due:", self.total)

        print("Notes:", self.notes)

# Client vars - Set to blank if not passed in
client_name = "EvariLABS LLC."
client_address = "4703 51st St, San Diego, CA, 92115"
client_email = "ari@sdgis.com"

# Other vars
total = "$3,500.00"
notes = "Great doing business with you, Ari"

today_invoice = Invoice(
    client_name=client_name,
    client_address=client_address,
    client_email=client_email,
    total=total,
    notes=notes
)

today_invoice.print_atts()