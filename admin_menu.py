from customtkinter import *

class adminMenu(CTk):
    def __init__(self):
        super().__init__()
        self.title("Admin Menu - Bank of Paradise - Secure Portal")
        self.geometry("1920x1080")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)

        self.menu = CTkFrame(self, fg_color="white")
        self.menu.grid(row=0, column=0, sticky="nsew")
        self.menu.grid_columnconfigure(0, weight=1)
        self.menu.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=1)

        self.content = CTkFrame(self, fg_color="black")
        self.content.grid(row=0, column=1, sticky="nsew")
        self.content.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
        self.content.grid_columnconfigure((0,1), weight=1)

        CTkLabel(self.menu, text="Admin menu", font=("Jokerman",40,"bold"), text_color="black").grid(row=0, column=0, sticky="nsew")
        button = ["Dashboard", "Customers", "Accounts", "KYC", "Transactions", "Reports", "Settings"]
        for item in button:
            CTkButton(
               self.menu,
               text=item,
               font=("Helvetica",18,"bold"),
               height=50,
               hover_color="green",
               width=150,
               corner_radius=25,
               border_color="black",
               text_color="white",
               fg_color="darkblue",
               border_width=5,
               command=lambda page=item: self.menu_clicked(page)
               ).grid(pady=8)

    def menu_clicked(self, page):
        for i in self.content.winfo_children():
            i.destroy()
        CTkLabel(self.content,
                 text=page,
                 text_color="white",
                 font=("Helvetica",24,"bold")).grid(row=0, column=0, sticky="e")
        pages = {
            "Dashboard": self.dashboard,
            "Customers": self.customers,
            "Accounts": self.accounts,
            "KYC": self.kyc,
            "Transactions": self.transactions,
            "Reports": self.reports,
            "Settings": self.settings
            }
        pages.get(page, lambda: None)()

    def dashboard(self):
        pass

    def customers(self):
        self.custFrame = CTkFrame(self.content, fg_color="black")
        self.custFrame.grid(row=1, column=0, sticky="nsew")
        self.custFrame.grid_rowconfigure(tuple(range(9)), weight=1)  # 0 = buttons, 1-8 = form rows
        self.custFrame.grid_columnconfigure((0,1,2,3), weight=1)

        self.custButtons = CTkFrame(self.custFrame, fg_color="black")
        self.custButtons.grid(row=0, column=0, columnspan=4)

        CTkButton(self.custButtons, text="Add Customer", height=50, width=150,
                  corner_radius=20, command=self.addc, hover_color="red").grid(row=0, column=0, padx=10)
        CTkButton(self.custButtons, text="Search Customer", height=50, width=150,
                  corner_radius=20, command=self.searchc, hover_color="red").grid(row=0, column=1, padx=10)
        CTkButton(self.custButtons, text="Update Customer", height=50, width=150,
                  corner_radius=20, command=self.updatec, hover_color="red").grid(row=0, column=2, padx=10)

        self.custForm = CTkFrame(self.custFrame, fg_color="black")
        self.custForm.grid(row=1, column=0, columnspan=4, sticky="nsew")

    def addc(self):
        # clear only the form area — leave custButtons alone
        for widget in self.custForm.winfo_children():
            widget.destroy()

        fields = {
            "First Name": "John",
            "Last Name": "Henry",
            "DOB": "01-01-2000",
            "Gender": "Male/Female",
            "e-mail": "abc@gmail.com",
            "Phone Number": "9876543210",
            "PAN Number": "AWR856970",
            "Identity Type": "Aadhar",
            "Identity Number": "1234 5678 9876",
            "Address Line1": "a",
            "Address Line2": "a",
            "Address Line3": "a",
            "District": "a",
            "State": "a",
            "Occupation": "a",
        }

        half = len(fields) // 2 + len(fields) % 2
        row = col = 0

        for i, (name, placeholder) in enumerate(fields.items()):
            if i == half:
                col = 1
                row = 0
            # everything grids into custForm now, not custFrame
            CTkLabel(self.custForm, text=name, font=("Helvetica", 20), text_color="white").grid(
                row=row, column=col*2, sticky="e", padx=5, pady=5
            )
            entry = CTkEntry(self.custForm, placeholder_text=placeholder)
            entry.grid(row=row, column=col*2+1, sticky="w", padx=5, pady=5)
            row += 1

    def searchc(self):
        for widget in self.custForm.winfo_children():
            widget.destroy()
        CTkLabel(self.custForm, text="Search Customer form goes here",
                 font=("Helvetica", 20), text_color="white").grid(row=0, column=0)

    def updatec(self):
        for widget in self.custForm.winfo_children():
            widget.destroy()
        CTkLabel(self.custForm, text="Update Customer form goes here",
                 font=("Helvetica", 20), text_color="white").grid(row=0, column=0)

    def accounts(self):
        pass

    def kyc(self):
        pass

    def transactions(self):
        pass

    def reports(self):
        pass

    def settings(self):
        pass

if __name__ == "__main__":
    app = adminMenu()
    app.mainloop()
