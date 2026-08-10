from customtkinter import *
from tkinter import messagebox
from api_client import *

class adminMenu(CTk):
    def __init__(self, token,name):
        self.token = token
        self.name=name
        super().__init__()
        self.title("Admin Menu - Bank of Paradise - Secure Portal")
        self.geometry("1920x1080")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=16)

        self.entry_widgets = {}
        self.fields = {
            "First Name": "John",
            "Last Name": "Henry",
            "DOB": "01-01-2000",
            "Gender": "Male/Female",
            "e-mail": "abc@gmail.com",
            "Phone Number": "9876543210",
            "PAN Number": "AWR856970",
            "Identity Type": "Aadhar",
            "Identity Number": "[Identity Number Redacted]",
            "Address Line 1": "123, Maple Street",
            "Address Line 2": "Near Central Park",
            "Address Line 3": "Apartment 48",
            "District": "Springfield",
            "State": "California",
            "Occupation": "Job"
        }

        self.menu = CTkFrame(self, fg_color="white")
        self.menu.grid(row=0, column=0, sticky="nsew")
        self.menu.grid_columnconfigure(0, weight=1)
        self.menu.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        self.content = CTkFrame(self, fg_color="black")
        self.content.grid(row=0, column=1, sticky="nsew")
        self.content.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)
        self.content.grid_columnconfigure((0, 1), weight=1)

        CTkLabel(self.menu, text="Admin menu", font=("Jokerman", 40, "bold"), text_color="black").grid(row=0, column=0, sticky="nsew")
        buttons = ["Dashboard", "Customers", "Accounts", "Transactions", "Reports", "Settings"]
        for item in buttons:
            CTkButton(
                self.menu,
                text=item,
                font=("Helvetica", 18, "bold","italic"),
                height=70,
                hover_color="green",
                text_color="blue",
                fg_color="white",
                corner_radius=0,
                command=lambda page=item: self.menu_clicked(page)
            ).grid(sticky="ew")

    def menu_clicked(self, page):
        for i in self.content.winfo_children():
            i.destroy()
        CTkLabel(
            self.content,
            text=page,
            text_color="white",
            font=("Helvetica", 24, "bold")
        ).grid(row=0, column=0, sticky="e")
        
        pages = {
            "Dashboard": self.dashboard,
            "Customers": self.customers,
            "Accounts": self.accounts,
            "Transactions": self.transactions,
            "Reports": self.reports,
            "Settings": self.settings
        }
        pages.get(page)()

    def dashboard(self):
        pass

    def customers(self):
        self.custFrame = CTkFrame(self.content, fg_color="black")
        self.custFrame.grid(row=1, column=0, sticky="nsew")
        self.custFrame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)
        self.custFrame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        
        CTkButton(
            self.custFrame,
            text="Add Customer",
            height=50,
            width=200,
            font=("Helvetica",20),
            corner_radius=20,
            command=self.addcustomer,
            hover_color="red"
        ).grid(row=2, column=0, sticky="e", pady=30)
        
        CTkButton(
            self.custFrame,
            text="Search Customer",
            height=50,
            width=200,
            font=("Helvetica",20),
            corner_radius=20,
            command=self.searchCustomer,
            hover_color="red"
        ).grid(row=3, column=0, sticky="e", pady=30)
        
        CTkButton(
            self.custFrame,
            text="Update Customer",
            height=50,
            width=200,
            font=("Helvetica",20),
            corner_radius=20,
            command=None,
            hover_color="red"
        ).grid(row=4, column=0, sticky="e", pady=20)

    def clear(self):
        for i in self.custFrame.winfo_children():
            i.destroy()
            
    def addcustomer(self):
        def toggle_pwd():
            if entry.cget("show") == "*":
                entry.configure(show="")
                toggle_btn.configure(text="Hide")
            else:
                entry.configure(show="*")
                toggle_btn.configure(text="Show")
        self.clear()
            
        items = list(self.fields.items())
        half = (len(items) + 1) // 2
        self.entry_widgets = {}
        
        row_idx = 0
        for idx, (key, val) in enumerate(items):
            if idx < half:
                col_label = 0
                col_entry = 1
                row_idx = idx
            else:
                col_label = 2
                col_entry = 3
                row_idx = idx - half
            
            CTkLabel(
                self.custFrame, 
                text=key, 
                text_color="white", 
                font=("Helvetica", 18, "bold")
            ).grid(row=row_idx, column=col_label, sticky="e", padx=10, pady=10)
            
            entry = CTkEntry(
                self.custFrame, 
                placeholder_text=val,
                width=250,
                font=("Helvetica", 18)
            )
            entry.grid(row=row_idx, column=col_entry, sticky="w", padx=10, pady=8)
            self.entry_widgets[key] = entry

        CTkLabel(
                self.custFrame, 
                text="Password", 
                text_color="white", 
                font=("Helvetica", 18, "bold")
            ).grid(row=row_idx + 1, column=2, sticky="e", padx=10, pady=10)

        entry = CTkEntry(
                self.custFrame, 
                width=250,
                show="*",
                font=("Helvetica", 18)
            )
        entry.grid(row=row_idx + 1, column=3, sticky="w", padx=10, pady=8)
        toggle_btn = CTkButton(
                self.custFrame,
                text="Show",
                width=50,
                command=toggle_pwd
            )
        toggle_btn.grid(row=row_idx + 1, column=4, sticky="w", padx=(2, 10), pady=8)
        self.entry_widgets["Password"]=entry
        CTkButton(
            self.custFrame,
            text="Submit",
            font=("Helvetica",20, "bold"),
            corner_radius=15,
            height=30,
            command=self.customerDetails
        ).grid(row=row_idx + 2, column=3, pady=15)

    def customerDetails(self):
        details = {}
        for field, widget in self.entry_widgets.items():
            details[field] = widget.get().strip()
        try:
            create_account(self.token, details)
        except Exception:
            messagebox.showinfo(
                "Connection Error",
                "Unable to reach the server. Please check your internet connection or try again later."
            )

    def searchCustomer(self):
        self.clear()
        self.scrlFrm=CTkScrollableFrame(self.content,fg_color="grey",label_text="Customer Details",width=1000).grid(row=3, column=0, padx=20, pady=10, sticky="nsew")
        CTkLabel(self.custFrame,
                 text="Account Number\t:",
                 text_color="white",
                 font=("Helvetica",20,"bold")).grid(row=0,column=0)
        CTkButton(self.custFrame,text=f"{chr(0x1F50E)} Search",font=("Helvetica",20,"bold")).grid(row=2,column=1,sticky="w")
        CTkEntry(self.custFrame,
                    placeholder_text="123456789101112",
                 font=("Helvetica",20),
                 height=30,
                 width=300).grid(row=0, column=1,sticky="ew")
        lab=list(self.fields.keys())
        for col, head in enumerate(lab):
            pass

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
    app = adminMenu("1234","h")
    app.mainloop()
