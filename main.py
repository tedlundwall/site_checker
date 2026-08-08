import tkinter
import tkinter.messagebox

import requests


def main():
    title = "Ferrofish Pulse8 AE"

    root = tkinter.Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    try:
        site = requests.get(
            "https://www.thomann.se/ferrofish_pulse8_ae_b_stock.htm"
        )
        if site.status_code == 200:
            tkinter.messagebox.showwarning(
                title=title, message="B-stock available!!", parent=root
            )
        elif site.status_code == 429:
            tkinter.messagebox.showerror(
                title=title, message="Check blocked by CAPTCHA.", parent=root
            )
        elif site.status_code == 404:
            tkinter.messagebox.showinfo(
                title=title, message="No B-stock available.", parent=root
            )
        else:
            tkinter.messagebox.showerror(
                title=title, message="Unknown status code.", parent=root
            )
    except requests.ConnectionError:
        tkinter.messagebox.showerror(
            title=title, message="Connection error.", parent=root
        )

    globals().update(locals())


if __name__ == "__main__":
    main()
