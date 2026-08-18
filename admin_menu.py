import tkinter as tk
from customtkinter import *
from api_client import *
from CTkMessagebox import CTkMessagebox

class adminMenu(CTk):
    def __init__(self, token, name):
        self.token = token
        self.name = name
        super().__init__()
        self.title("Admin Portal - Bank of Paradise - Secure Portal")
        self.geometry("1920x1080")
        self.configure(fg_color="#090A0F")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=16)

        self.custFrame = None
        self.table_inner = None
        self.entry_widgets = {}
        self.fields = {
            "First Name": "John",
            "Last Name": "Henry",
            "DOB": "01-01-2000",
            "Gender": "Male/Female",
            "e-mail": "abc@gmail.com",
            "Phone Number": "9876543210",
            "PAN Number": "AWR856970",
            "Identity Type": "Identity Doc",
            "Identity Number": "[Identity Number Redacted]",
            "Address Line 1": "123, Maple Street",
            "Address Line 2": "Near Central Park",
            "Address Line 3": "Apartment 48",
            "District": "Springfield",
            "State": "California",
            "Occupation": "Job"
        }
        self.menu = CTkFrame(self, fg_color="#121622", border_color="#1F2638", border_width=2, corner_radius=20)
        self.menu.grid(row=0, column=0, sticky="nsew")
        self.menu.grid_columnconfigure(0, weight=1)
        self.menu.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        self.content = CTkFrame(self, fg_color="#090A0F", corner_radius=0)
        self.content.grid(row=0, column=1, sticky="nsew")
        self.content.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)
        self.content.grid_columnconfigure((0, 1), weight=1)

        CTkLabel(
            self.menu, 
            text="ADMIN PORTAL", 
            font=("Segoe UI", 22, "bold"), 
            text_color="#58A6FF"
        ).grid(row=0, column=0, sticky="nsew", padx=20)
        
        buttons = ["Pulse", "Profiles and Accounts", "Activity", "Insights", "Preferences"]
        for i, item in enumerate(buttons, start=1):
            CTkButton(
                self.menu,
                text=item,
                font=("Segoe UI", 24, "bold"),
                height=55,
                width=220,
                hover_color="#1F293D",
                text_color="#C9D1D9", 
                fg_color="#161B26", 
                border_color="#30363D",  
                border_width=1,
                corner_radius=12,
                anchor="c",
                command=lambda page=item: self.menu_clicked(page)
            ).grid(row=i, column=0, sticky="nsew", padx=20)

    def menu_clicked(self, page):
        for i in self.content.winfo_children():
            i.destroy()
        
        CTkLabel(
            self.content,
            text=page,
            text_color="#F0F6FC",
            font=("Segoe UI", 32, "bold")
        ).grid(row=0, column=0, sticky="nw", padx=30, pady=20)
        
        pages = {
            "Pulse": self.dashboard,
            "Profiles and Accounts": self.customers,
            "Activity": self.transactions,
            "Insights": self.reports,
            "Preferences": self.settings,
            "Express Onboard": self.addCustomer,
            "Directory": self.searchCustomer,
            "Manage Profiles": None,
            "Security Freeze": None
        }
        action = pages.get(page)
        if action:
            action()

    def dashboard(self):
        pass

    def customers(self):
        self.custFrame = CTkFrame(
            self.content, 
            fg_color="#0F1117",
            border_color="#1E222B",
            border_width=1,
            corner_radius=16
        )
        self.custFrame.grid(row=1, column=0, sticky="nsew", padx=30, pady=20)
        self.custFrame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
        self.custFrame.grid_columnconfigure((0, 1, 2, 3), weight=1)
            
        paaButtons = ["Express Onboard", "Directory", "Manage Profiles", "Security Freeze"]
        for item, j in enumerate(paaButtons, start=2):
            CTkButton(
                self.custFrame,
                text=j,
                fg_color="#161B26",
                border_color="#30363D",
                font=("Segoe UI", 18, "bold"),
                border_width=1,
                width=240,
                height=55,
                hover_color="#1F293D",
                text_color="#58A6FF",
                corner_radius=12,
                command=lambda page=j: self.menu_clicked(page),
            ).grid(row=item, column=0, sticky="e", pady=20, padx=30)
            
    def clear(self):
        if hasattr(self, 'custFrame') and self.custFrame is not None and self.custFrame.winfo_exists():
            for i in self.custFrame.winfo_children():
                i.destroy()
        else:
            self.custFrame = CTkFrame(
                self.content, 
                fg_color="#0F1117",
                border_color="#1E222B",
                border_width=1,
                corner_radius=16
            )
            self.custFrame.grid(row=1, column=0, sticky="nsew", padx=30, pady=0)

    def addCustomer(self):
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
                text_color="#58A6FF", 
                font=("Segoe UI", 15, "bold")
            ).grid(row=row_idx, column=col_label, sticky="e", padx=15, pady=12)
                
            entry = CTkEntry(
                self.custFrame, 
                placeholder_text=val,
                width=280,
                height=45,
                font=("Segoe UI", 15),
                fg_color="#161B26",
                border_color="#30363D",
                border_width=1,
                text_color="#C9D1D9",
                placeholder_text_color="#484F58",
                corner_radius=10
            )
            entry.grid(row=row_idx, column=col_entry, sticky="w", padx=15, pady=12)
            self.entry_widgets[key] = entry

        CTkLabel(
            self.custFrame, 
            text="Password", 
            text_color="#58A6FF", 
            font=("Segoe UI", 15, "bold")
        ).grid(row=row_idx + 1, column=2, sticky="e", padx=15, pady=12)

        entry = CTkEntry(
            self.custFrame, 
            width=280,
            height=45,
            show="*",
            font=("Segoe UI", 15),
            fg_color="#161B26",
            border_color="#30363D",
            border_width=1,
            text_color="#C9D1D9",
            corner_radius=10
        )
        entry.grid(row=row_idx + 1, column=3, sticky="w", padx=15, pady=12)
        
        toggle_btn = CTkButton(
            self.custFrame,
            text="Show",
            width=50,
            height=45,
            fg_color="#21262D",
            hover_color="#30363D",
            text_color="#C9D1D9",
            font=("Segoe UI", 12),
            corner_radius=8,
            command=toggle_pwd
        )
        toggle_btn.grid(row=row_idx + 1, column=4, sticky="w", padx=(5, 10), pady=12)
        
        self.entry_widgets["Password"] = entry
        
        CTkButton(
            self.custFrame,
            text="Submit",
            font=("Segoe UI", 16, "bold"),
            fg_color="#238636",
            hover_color="#2ea043",
            text_color="white",
            corner_radius=10,
            height=45,
            width=150,
            command=self.customerDetails
        ).grid(row=row_idx + 2, column=3, sticky="w", padx=15, pady=25)

    def customerDetails(self):
        details = {}
        for field, widget in self.entry_widgets.items():
            details[field] = widget.get().strip()
            
        try:
            acn = create_account(self.token, details)
            CTkMessagebox(
                title="200 Success", 
                message=f"Account Created Successfully\nAccount Number: {acn}", 
                icon="check"
            )
            for widget in self.entry_widgets.values():
                widget.delete(0, END)
                
        except Exception:
            CTkMessagebox(
                title="Connection Error",
                message="Unable to reach the server. Please check your internet connection or try again later.",
                icon="cancel"
            )

    def searchCustomer(self):
        self.clear()

        CTkLabel(
            self.custFrame,
            text="Account Number",
            text_color="#8B949E",
            font=("Segoe UI", 16, "bold")
        ).grid(row=0, column=0, sticky="e", padx=15, pady=20)

        self.ent = CTkEntry(
            self.custFrame,
            font=("Segoe UI", 16),
            placeholder_text="Enter Account Number...",
            fg_color="#161B26",
            border_color="#30363D",
            border_width=1,
            text_color="#C9D1D9",
            placeholder_text_color="#484F58",
            corner_radius=10,
            height=45,
            width=300
        )
        self.ent.grid(row=0, column=1, sticky="w", padx=15, pady=20)

        CTkButton(
            self.custFrame,
            text="Search",
            font=("Segoe UI", 16, "bold"),
            fg_color="#1F6FEB",
            hover_color="#388BFD",
            text_color="white",
            corner_radius=10,
            height=45,
            width=120,
            command=self.search
        ).grid(row=0, column=2, sticky="w", padx=10, pady=20)
        table_wrapper = CTkFrame(self.content, fg_color="#0F1117", border_color="#1E222B", border_width=1, corner_radius=12)
        table_wrapper.grid(row=3, column=0, columnspan=2, padx=30, pady=10, sticky="nsew")
        table_wrapper.grid_rowconfigure(0, weight=1)
        table_wrapper.grid_columnconfigure(0, weight=1)

        self.canvas = tk.Canvas(table_wrapper, bg="#0F1117", highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky="nsew", padx=(10, 0), pady=(10, 0))

        v_bar = CTkScrollbar(table_wrapper, orientation="vertical", command=self.canvas.yview)
        v_bar.grid(row=0, column=1, sticky="ns", pady=(10, 0))

        h_bar = CTkScrollbar(table_wrapper, orientation="horizontal", command=self.canvas.xview)
        h_bar.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        self.canvas.configure(xscrollcommand=h_bar.set, yscrollcommand=v_bar.set)

        self.table_inner = CTkFrame(self.canvas, fg_color="#0F1117")
        self.canvas.create_window((0, 0), window=self.table_inner, anchor="nw")

        self.table_inner.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

    def search(self):
        try:
            if not hasattr(self, 'table_inner') or self.table_inner is None or not self.table_inner.winfo_exists():
                return

            det = search_customer(self.token, int(self.ent.get()) if self.ent.get() else 0)
            
            if not det:
                CTkMessagebox(title="Not Found", message="No customer records found.", icon="cancel", option_1="OK")
                return
                
            for i in self.table_inner.winfo_children():
                i.destroy()

            headers = [
                "Account No", "Name", "DOB", "Gender", 
                "Email", "Phone", "PAN", "ID Type", "ID Number", 
                "Addr 1", "Addr 2", "Addr 3", "District", "State", 
                "Occupation", "Status"
            ]

            for col_idx, header in enumerate(headers):
                CTkLabel(
                    self.table_inner,
                    text=header,
                    text_color="#58A6FF",
                    font=("Segoe UI", 13, "bold"),
                    anchor="w"
                ).grid(row=0, column=col_idx, padx=15, pady=8, sticky="w")

            for row_idx, record in enumerate(det, start=1):
                for col_idx, val in enumerate(record):
                    CTkLabel(
                        self.table_inner,
                        text=str(val),
                        text_color="#C9D1D9",
                        font=("Segoe UI", 12),
                        anchor="w"
                    ).grid(row=row_idx, column=col_idx, padx=15, pady=6, sticky="w")
                
        except ValueError:
            CTkMessagebox(
                title="Message", 
                message="Enter correct format", 
                icon="warning", 
                option_1="OK"
            )
            self.ent.delete(0, END)
        except Exception:
            CTkMessagebox(
                title="Connection Error",
                message="Unable to reach the server. Please check your internet connection or try again later.",
                icon="cancel"
            )

    def manageProfiles(self):
        pass

    def transactions(self):
        pass

    def reports(self):
        pass

    def settings(self):
        pass

if __name__ == "__main__":
    app = adminMenu("1234", "a")
    app.mainloop()
