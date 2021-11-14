"""
this An application for:
Download images by URL Address
Returns different IP types and displays your IP by clicking on a button
"""

from tkinter import *
from tkinter import messagebox
import functions

# initialization interface with tkinter module
window = Tk()
window.title('meme')
window.geometry("600x400")
window.config(bg="grey90")
window.iconbitmap('./image/appicon.ico')
window.resizable(False, False)


class App:
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        """
            set_img_url function:
            this function send a image url address to a function from functions.py file
            for check url validation, if its valid the image will downloaded.
            else, the user will got An Error message.
        """
        def set_img_url():
            try:
                if functions.get_image(self.ent1.get()):
                    messagebox.showinfo("message",
                                        "Download completed!")
            except:
                if len(self.ent1.get()) == 0:
                    messagebox.showerror("Error",
                                         "An Empty input, Enter img URL Address")
                else:
                    messagebox.showerror("Error", "this application does not support this URL Address >>>\n"
                                                  "Please try another URL Address")

        """
            get_url_IpAddress function:
            this function send a url address to a function from functions.py file
            for check url validation, if its valid URL then it will return and URL IP Address
            else, the user will got An Error message.
        """
        def get_url_IpAddress():
            url = self.ent2.get()
            if len(url) == 0:
                messagebox.showerror("Error",
                                     "An Empty input, Enter URL Address")
            elif functions.get_dns_ipAddress(url):
                ip = functions.get_dns_ipAddress(url)
                txt.insert(END, f"Results:\n"
                                f"{url}: IP Adress is \n>>>{ip}<<<")
                text_window()
            else:
                messagebox.showerror("Error",
                                     "Enter Invalid URL! An example ===> www.google.com")

        """
            get_ip_function1 function:
            this function shows in a TEXT box by clicking on "My Windows IP Configuration" Button:
            my ipv4 
            my ipv6
            my Physical Address(mac Address)
            it will call a functions from functions.py file.
        """
        def get_ip_function1():
            ipv4_adress = "IPv4 Address >>>"
            ipv6_adress = "IPv6 Address >>>"
            mac_adress = "mac Address >>>"
            txt.insert(END, f"Results:\n{ipv4_adress} {functions.get_ipv4()}\n"
                            f"{ipv6_adress} {functions.get_ipv6()}\n"
                            f"{mac_adress} {functions.get_mac_address()}\n")
            text_window()

        def text_window():
            txt.place(x=255, y=35)

        def clear_result():
            txt.delete("1.0", "end")

        txt = Text(window, width=40)

        self.lbl1 = Label(master, text="Enter img url Adress:")
        self.lbl1.place(x=5, y=10)

        self.ent1 = Entry(master, width="49")
        self.ent1.place(x=120, y=10)

        self.btn1 = Button(master, text="download", command=set_img_url)
        self.btn1.place(x=430, y=5)

        self.lbl2 = Label(master, text="Enter url:", font=('Arial', 12, 'bold'), bg="#c1c1c1")
        self.lbl2.place(x=10, y=60)

        self.ent2 = Entry(master, width=36, bd=4)
        self.ent2.place(x=10, y=90)

        self.btn = Button(master, text="Get url ip", pady=5, bd=2, width=10, font=('Arial', 12, 'bold'), bg='gray73',
                          activebackground="white", command=get_url_IpAddress)
        self.btn.place(x=10, y=120)

        self.btn2 = Button(master, pady=5, text="My Windows IP Configuration", bd=2, width=24,
                           font=('Arial', 8, 'bold'), bg='gray76',
                           activebackground="white", command=get_ip_function1)
        self.btn2.place(x=10, y=200)

        self.btn3 = Button(master, text="clear", width=8, bg='green', font=("Arial", 10, "bold"), command=clear_result)
        self.btn3.place(x=10, y=310)

        self.btn3 = Button(master, text="EXIT", width=10, bd=5, bg="red4", font=("Arial", 12, "bold"),
                           command=master.destroy)
        self.btn3.place(x=10, y=350)


e = App(window)
window.mainloop()
