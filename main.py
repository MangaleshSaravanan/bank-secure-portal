from customtkinter import *
from tkinter import END
from CTkMessagebox import CTkMessagebox

class BankApp(CTk):
    set_appearance_mode("dark")
    set_default_color_theme("blue")

    def __init__(self):
        super().__init__()

        self.title("Bank of Paradise - Secure Portal")
        self.geometry("1920x1080")
        self.configure(fg_color="#0F172A")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.main_container = CTkFrame(self, fg_color="transparent")
        self.main_container.grid(row=0, column=0, sticky="ns")
        self.main_container.grid_rowconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)

        self.login = CTkFrame(
            self.main_container, 
            fg_color="#1E293B", 
            corner_radius=20, 
            border_width=1, 
            border_color="#334155"
        )
        self.admin_login = CTkFrame(
            self.main_container, 
            fg_color="#1E293B", 
            corner_radius=20, 
            border_width=1, 
            border_color="#334155"
        )
        self.customer_login = CTkFrame(
            self.main_container, 
            fg_color="#1E293B", 
            corner_radius=20, 
            border_width=1, 
            border_color="#334155"
        )

        for frame in (self.login, self.admin_login, self.customer_login):
            frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=60)
        self.login.grid_columnconfigure(0, weight=1)

        CTkLabel(
            self.login,
            text="BANK OF PARADISE",
            font=("Segoe UI", 32, "bold"),
            text_color="#F8FAFC"
        ).grid(row=0, column=0, padx=60, pady=(60, 10))

        CTkLabel(
            self.login,
            text="Select your access portal to continue",
            font=("Segoe UI", 14),
            text_color="#94A3B8"
        ).grid(row=1, column=0, padx=60, pady=(0, 40))

        CTkButton(
            self.login,
            text="ADMIN LOGIN",
            font=("Segoe UI", 16, "bold"),
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            command=self.admin_page,
            height=50,
            width=360,
            corner_radius=12
        ).grid(row=2, column=0, padx=60, pady=15)

        CTkButton(
            self.login,
            text="CUSTOMER LOGIN",
            font=("Segoe UI", 16, "bold"),
            fg_color="#059669",
            hover_color="#047857",
            command=self.cust_page,
            height=50,
            width=360,
            corner_radius=12
        ).grid(row=3, column=0, padx=60, pady=(15, 60))

        self.admin_login.grid_columnconfigure(0, weight=1)

        CTkLabel(
            self.admin_login,
            text="Admin Portal",
            font=("Segoe UI", 28, "bold"),
            text_color="#F8FAFC"
        ).grid(row=0, column=0, columnspan=2, padx=50, pady=(40, 5))

        CTkLabel(
            self.admin_login,
            text="Sign in to manage system operations",
            font=("Segoe UI", 13),
            text_color="#94A3B8"
        ).grid(row=1, column=0, columnspan=2, padx=50, pady=(0, 30))

        CTkLabel(
            self.admin_login,
            text="Admin ID",
            font=("Segoe UI", 13, "bold"),
            text_color="#CBD5E1"
        ).grid(row=2, column=0, padx=(50, 10), pady=(10, 5), sticky="w")

        self.admid = CTkEntry(
            self.admin_login,
            placeholder_text="Enter your admin ID",
            placeholder_text_color="#64748B",
            fg_color="#0F172A",
            border_color="#334155",
            text_color="#F8FAFC",
            width=320,
            height=45,
            corner_radius=10
        )
        self.admid.grid(row=3, column=0, columnspan=2, padx=50, pady=(0, 15))

        CTkLabel(
            self.admin_login,
            text="Password",
            font=("Segoe UI", 13, "bold"),
            text_color="#CBD5E1"
        ).grid(row=4, column=0, padx=(50, 10), pady=(10, 5), sticky="w")

        self.admpwd = CTkEntry(
            self.admin_login,
            placeholder_text="Enter your password",
            placeholder_text_color="#64748B",
            fg_color="#0F172A",
            border_color="#334155",
            text_color="#F8FAFC",
            width=320,
            height=45,
            corner_radius=10,
            show="*"
        )
        self.admpwd.grid(row=5, column=0, columnspan=2, padx=50, pady=(0, 25))

        admin_btn_frame = CTkFrame(self.admin_login, fg_color="transparent")
        admin_btn_frame.grid(row=6, column=0, columnspan=2, pady=(10, 40))

        CTkButton(
            admin_btn_frame,
            text="Return Home",
            command=self.login_page,
            font=("Segoe UI", 14, "bold"),
            fg_color="#475569",
            hover_color="#334155",
            width=150,
            height=45,
            corner_radius=10
        ).pack(side="left", padx=10)

        CTkButton(
            admin_btn_frame,
            text="LOGIN",
            command=self.admin_entry,
            font=("Segoe UI", 14, "bold"),
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            width=150,
            height=45,
            corner_radius=10
        ).pack(side="left", padx=10)

        self.customer_login.grid_columnconfigure(0, weight=1)

        CTkLabel(
            self.customer_login,
            text="Customer Portal",
            font=("Segoe UI", 28, "bold"),
            text_color="#F8FAFC"
        ).grid(row=0, column=0, columnspan=2, padx=50, pady=(40, 5))

        CTkLabel(
            self.customer_login,
            text="Sign in to access your bank account",
            font=("Segoe UI", 13),
            text_color="#94A3B8"
        ).grid(row=1, column=0, columnspan=2, padx=50, pady=(0, 30))

        CTkLabel(
            self.customer_login,
            text="Customer ID",
            font=("Segoe UI", 13, "bold"),
            text_color="#CBD5E1"
        ).grid(row=2, column=0, padx=(50, 10), pady=(10, 5), sticky="w")

        self.custid = CTkEntry(
            self.customer_login,
            placeholder_text="Enter your customer ID",
            placeholder_text_color="#64748B",
            fg_color="#0F172A",
            border_color="#334155",
            text_color="#F8FAFC",
            width=320,
            height=45,
            corner_radius=10
        )
        self.custid.grid(row=3, column=0, columnspan=2, padx=50, pady=(0, 15))

        CTkLabel(
            self.customer_login,
            text="Password",
            font=("Segoe UI", 13, "bold"),
            text_color="#CBD5E1"
        ).grid(row=4, column=0, padx=(50, 10), pady=(10, 5), sticky="w")

        self.custpwd = CTkEntry(
            self.customer_login,
            placeholder_text="Enter your password",
            placeholder_text_color="#64748B",
            fg_color="#0F172A",
            border_color="#334155",
            text_color="#F8FAFC",
            width=320,
            height=45,
            corner_radius=10,
            show="*"
        )
        self.custpwd.grid(row=5, column=0, columnspan=2, padx=50, pady=(0, 25))

        cust_btn_frame = CTkFrame(self.customer_login, fg_color="transparent")
        cust_btn_frame.grid(row=6, column=0, columnspan=2, pady=(10, 40))

        CTkButton(
            cust_btn_frame,
            text="Return Home",
            command=self.login_page,
            font=("Segoe UI", 14, "bold"),
            fg_color="#475569",
            hover_color="#334155",
            width=150,
            height=45,
            corner_radius=10
        ).pack(side="left", padx=10)

        CTkButton(
            cust_btn_frame,
            text="LOGIN",
            command=self.customer_entry,
            font=("Segoe UI", 14, "bold"),
            fg_color="#059669",
            hover_color="#047857",
            width=150,
            height=45,
            corner_radius=10
        ).pack(side="left", padx=10)

        self.login_page()

    def customer_entry(self):
        usrid = self.custid.get()
        usrpwd = self.custpwd.get()

        if not (usrid and usrpwd):
            CTkMessagebox(
                title="Invalid Format",
                message="Please enter Customer ID and Password.",
                icon="warning"
            )
            return

        import api_client

        try:
            token = api_client.customer_entry(usrid, usrpwd)

            if token:
                self.custid.delete(0, END)
                self.custpwd.delete(0, END)

                import customer_menu
                self.destroy()
                app = customer_menu.customerMenu()
                app.mainloop()
            else:
                CTkMessagebox(
                    title="Login Failed",
                    message="The username or password you entered is incorrect.",
                    icon="cancel"
                )
                return

        except Exception as e:
            print(e)
            CTkMessagebox(
                title="Connection Error",
                message="Unable to reach the server. Please check your internet connection or try again later.",
                icon="cancel"
            )
            return

    def admin_entry(self):
        usrid = self.admid.get()
        usrpwd = self.admpwd.get()

        if not (usrid and usrpwd):
            CTkMessagebox(
                title="Invalid Format",
                message="Please enter Admin ID and Password.",
                icon="warning"
            )
            return

        import api_client

        try:
            token = api_client.admin_entry(usrid, usrpwd)

            if token:
                self.admid.delete(0, END)
                self.admpwd.delete(0, END)
                self.destroy()
                import admin_menu
                app = admin_menu.adminMenu(token, self.admid)
                app.mainloop()
            else:
                CTkMessagebox(
                    title="Login Failed",
                    message="The username or password you entered is incorrect.",
                    icon="cancel"
                )
                return

        except Exception as e:
            print(e)
            CTkMessagebox(
                title="Connection Error",
                message="Unable to reach the server. Please check your internet connection or try again later.",
                icon="cancel"
            )
            return

    def login_page(self):
        if self.admid.get(): self.admid.delete(0, END)
        if self.admpwd.get(): self.admpwd.delete(0, END)
        if self.custid.get(): self.custid.delete(0, END)
        if self.custpwd.get(): self.custpwd.delete(0, END)

        self.login.tkraise()

    def admin_page(self):
        self.admin_login.tkraise()

    def cust_page(self):
        self.customer_login.tkraise()


if __name__ == "__main__":
    app = BankApp()
    app.mainloop()
