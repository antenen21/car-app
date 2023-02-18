# ╔══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
#        ██  ███    ██  ███████  ██████   ██████   ███    ███   █████   ████████  ██   ██████   ███    ██ 
#        ██  ████   ██  ██      ██    ██  ██   ██  ████  ████  ██   ██     ██     ██  ██    ██  ████   ██ 
#        ██  ██ ██  ██  █████   ██    ██  ██████   ██ ████ ██  ███████     ██     ██  ██    ██  ██ ██  ██ 
#        ██  ██  ██ ██  ██      ██    ██  ██   ██  ██  ██  ██  ██   ██     ██     ██  ██    ██  ██  ██ ██ 
#        ██  ██   ████  ██       ██████   ██   ██  ██      ██  ██   ██     ██     ██   ██████   ██   ████                                                                                                                                                                                   
# ╚══════════════════════════════════════════════════════════════════════════════════════════════════════════╝
# The Class Login  is the main root itself
# Customtkinter, os and PIL are only imported for background image
# Font Test
# ╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
#      ██████   ██████    ██████   ██████   ██       ███████  ███    ███  ███████      ████████   ██████       ███████   ██████   ██       ██    ██  ███████ 
#      ██   ██  ██   ██  ██    ██  ██   ██  ██       ██       ████  ████  ██              ██     ██    ██      ██       ██    ██  ██       ██    ██  ██      
#      ██████   ██████   ██    ██  ██████   ██       █████    ██ ████ ██  ███████         ██     ██    ██      ███████  ██    ██  ██       ██    ██  █████   
#      ██       ██   ██  ██    ██  ██   ██  ██       ██       ██  ██  ██       ██         ██     ██    ██           ██  ██    ██  ██        ██  ██   ██      
#      ██       ██   ██   ██████   ██████   ███████  ███████  ██      ██  ███████         ██      ██████       ███████   ██████   ███████    ████    ███████                                                                                                                                                                                                                                                                                               
# ╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
# from button pressed in guest and admin we can go out but the Login window is showing only blank
# Theme changer spinbox, customer can write in spinbox and input what he wants
#
# ╔═══════════════════════════════════════════════════════════════════════════════════╗
#      ██████   ██████   ██████  ████████ ███████ ████████ ██████   █████  ██████  
#      ██   ██ ██    ██ ██    ██    ██    ██         ██    ██   ██ ██   ██ ██   ██ 
#      ██████  ██    ██ ██    ██    ██    ███████    ██    ██████  ███████ ██████  
#      ██   ██ ██    ██ ██    ██    ██         ██    ██    ██   ██ ██   ██ ██      
#      ██████   ██████   ██████     ██    ███████    ██    ██   ██ ██   ██ ██                                                                                                                                                                                                                                                       
# ╚═══════════════════════════════════════════════════════════════════════════════════╝
#       STYLES:
#       List of styles available with ttkbootstrap are PRIMARY, SECONDARY, SUCCESS, INFO, WARNING, DANGER, LIGHT, DARK#
# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝


                                  
                                   

# Imports
import tkinter as tk 

import customtkinter as ct
import ttkbootstrap as tkb
from customtkinter import *
from PIL import Image
from ThemesData import *
from UserData import *
import os


# SEARCH FRAME - ADMIN SLAVE - inside main container
class CustSearch(tkb.Toplevel):
    def __init__(self, which_root):
        super().__init__(which_root)
        # Configs
        self.geometry("1000x600+200+0")
        self.title("SEARCH CUSTOMER")

        # Search frame
        self.label_frame = tkb.LabelFrame(self, text="SEARCH CUSTOMER", border=10, borderwidth=100, width=900,
                                          height=200,
                                          relief=SUNKEN)
        self.label_frame.place(x=50, y=30)

        # Back to Login Button
        ct.CTkButton(self, text="BACK TO ADMIN MENU", command=self.back_to_login).place(x=800, y=500)

        # Entry label Search Customer
        self.customer_search = tkb.StringVar()
        ct.CTkEntry(self, textvariable=self.customer_search).place(x=120, y=70)

        # Button Search Customer
        ct.CTkButton(self, text="SEARCH CUSTOMER",
                     command=self.search_customer_and_compare).place(x=120, y=110)
        # Radio Buttons "Name"
        ct.CTkRadioButton(self, text="Search per 'Name'",
                          hover_color="powder blue", radiobutton_height=19, radiobutton_width=19).place(x=120, y=160)
        ct.CTkRadioButton(self, text="Search per 'Lastname'",
                          hover_color="powder blue", radiobutton_height=19, radiobutton_width=19).place(x=300, y=160)
        ct.CTkRadioButton(self, text="Search per 'Username'",
                          hover_color="powder blue", radiobutton_height=19, radiobutton_width=19).place(x=500, y=160)

    def search_customer_and_compare(self):
        self.customer_input = self.customer_search.get()
        print("[[[[INFO]]]]         the searched username was : ", self.customer_input)
        for cust in user_list:
            if cust["username"] == self.customer_input:
                print(cust)

    def back_to_login(self):
        self.destroy()
        xx = Admin(myapp)


# SETTINGS FRAME - ADMIN SLAVE - inside main container
class Settings(tkb.Toplevel):
    def __init__(self, which_root):
        super().__init__(which_root)
        # Configs
        self.geometry("1000x600+200+0")
        self.title("SETTINGS")
        # Settings frame
        self.label_frame = tkb.LabelFrame(self, text="SETTINGS", border=10, borderwidth=100, width=900, height=200,
                                          relief=SUNKEN)
        self.label_frame.place(x=50, y=30)
        # Themes Spinbox
        self.var_themes = tkb.StringVar()
        tkb.Spinbox(self, values=themes_list, exportselection=True,
                    textvariable=self.var_themes, ).place(x=100, y=80)
        # Theme try Button
        tkb.Button(self, text="Try this theme", command=self.theme_changer).place(x=100, y=150)
        # Back to Login Button
        tkb.Button(self, text="BACK TO ADMIN MENU", command=self.back_to_login).place(x=800, y=500)

        # Method - Gets info trough StringVar from Spinbox


    def theme_changer(self):
        xxx = self.var_themes.get()
        tkb.Style(xxx)
        self.destroy()
        x = Settings(myapp)
        print("[[[INFO]]]           def theme_changer(admin) was called")
        print("[[[INFO]]]           Chosen Theme: ", xxx)

    def back_to_login(self):
        self.destroy()
        xx = Admin(myapp)


# ADMIN FRAME - inside main container
class Admin(tkb.Toplevel):
    def __init__(self, which_root):
        super().__init__(which_root)
        # Configs
        self.geometry("1000x600+200+0")
        self.title("ADMIN")
        # Style("darkly")

        # Top frame
        self.top_frame = ct.CTkFrame(self, height=63, border_width=5, corner_radius=10, border_color="black")
        self.top_frame.pack(side=TOP, fill=BOTH, expand=NO)
        # Setting Button
        self.log_path = os.path.dirname(os.path.realpath(__file__))
        self.logo_image = ct.CTkImage(Image.open(self.log_path + "/Images/settings.png"), size=(40, 40))
        self.set_but = ct.CTkButton(self.top_frame, image=self.logo_image, text="Settings",
                                    command=self.open_settings)
        self.set_but.place(x=15, y=7)

        # Search Customer Button
        self.log_path = os.path.dirname(os.path.realpath(__file__))
        self.logo_image = ct.CTkImage(Image.open(self.log_path + "/Images/search.png"), size=(40, 40))
        self.set_but = ct.CTkButton(self.top_frame, border_width=0, image=self.logo_image, text="Search Customer",
                                    command=self.open_customer_search)
        self.set_but.place(x=165, y=7)
        # Back to Login Button
        ct.CTkButton(self, text="BACK TO LOGIN", command=self.back_to_login).place(x=800, y=500)

    def back_to_login(self):
        self.destroy()
        xx = Login(myapp)

    def open_customer_search(self):
        self.destroy()
        cc = CustSearch(myapp)

    def open_settings(self):
        self.destroy()
        xxxx = Settings(myapp)


# GUEST FRAME - inside main container
class Guest(tkb.Toplevel):
    def __init__(self, which_root):
        super().__init__(which_root)
        self.geometry("1000x600+800+0")
        self.title("GUEST")
        self.resizable(False, False)
        # ---- BACK TO LOGIN BUTTON ----
        self.back_but = tkb.Button(self, text="BACK TO LOGIN", command=self.back_to_login)
        self.back_but.place(x=100, y=300)

    def back_to_login(self):
        self.destroy()
        xx = Login(myapp)


# LOGIN FRAME - inside main container
class Login(tkb.Toplevel):
    def __init__(self, which_root):
        super().__init__(self, which_root)
        self.geometry("700x400+350+0")
        self.title("APPLICATION")
        self.resizable(False, False)
        # Background image path
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        # Background image load
        self.bg_image = ct.CTkImage(Image.open(self.current_path + "/Images/carkey.png"), size=(700, 400))
        # Background image display
        self.bg_image_frame = ct.CTkLabel(self, image=self.bg_image, text="")
        self.bg_image_frame.pack()

        # Labels before entry
        tkb.Label(self.bg_image_frame, text="Username: ", background=None, foreground=None).place(x=30, y=80)
        tkb.Label(self.bg_image_frame, text="Password: ").place(x=30, y=140)
        # Entry Username
        self.user_var = tkb.StringVar()
        tkb.Entry(self.bg_image_frame, textvariable=self.user_var).place(x=110, y=80)
        # Entry Password
        self.pw_var = tkb.StringVar()
        tkb.Entry(self.bg_image_frame, textvariable=self.pw_var, show="*").place(x=110, y=140)
        # Login Button
        tkb.Button(self.bg_image_frame, text="LOGIN",
                   command=self.validate_login).place(x=110, y=190)
        # Quit Button
        tkb.Button(self.bg_image_frame, text="QUIT APP",
                   command=self.quit_app).place(x=480, y=350)

    # Takes the input data from the Entry's and compares it with the DATA from the system to give access
    # to either admin or guest"""

    def validate_login(self):
        username_input = self.user_var.get()
        password_input = self.pw_var.get()
        print("[[[INFO]]]           Entered Username: ", username_input)
        print("[[[INFO]]]           Entered Password: ", password_input)
        for user_loop_data in user_list:

            # ---- CHECK INPUTS
            if username_input == user_loop_data["username"]:
                if password_input == user_loop_data["password"]:
                    print("[[[INFO]]]           Login Inputs matches with those from UserData.py")
                    self.destroy()

                    # ---- CHECK IF ADMIN -------------------------
                    if user_loop_data["type"] == "admin":
                        print(f"[[[INFO]]]           {user_loop_data['firstname']} logged in as admin")
                        x = Admin(myapp)
                        return None

                    # ---- CHECK IF GUEST -------------------------
                    else:
                        print(f"[[[INFO]]]           {user_loop_data['firstname']} logged in as guest")
                        c = Guest(myapp)
                        return None
        else:  # ---- LABEL WRONG -----------------------------
            self.wrong_lab = tkb.Label(text="Wrong Username or Password entered")
            self.wrong_lab.place(x=110, y=170)
            print("[[[INFO]]]           Login Inputs are wrong")

    def quit_app(self):
        self.quit()
        print("[[[INFO]]]           App was closed")


# MAIN CONTAINER - is hidden
class MyAppContainer(tkb.Window):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # ---- MAIN ROOT CONFIG----
        self.geometry("700x400+800+0")
        self.title("APPLICATION")
        self.withdraw()


if __name__ == "__main__":
    myapp = MyAppContainer()


    bla = Login(myapp)
    bla.mainloop()
# ╔════════════════════════════════════════════════════════════════════════════════════════╗
# ---- THEMES ----
# cosmo flatly litera minty lumen
# sandstone yeti pulse united morph
# journal darkly superhero solar
# cyborg vapor simplex cerculean
# ╚═════════════════════════════════════════════════════════════════════════════════════════╝
