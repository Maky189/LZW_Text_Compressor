from tkinter import *
from tkinter import ttk
from algorithm import encode, decode

def show_entry(frm):
    entry_label = ttk.Label(frm, text="Enter text:")
    entry_label.grid(column=0, row=1)

    entry = ttk.Entry(frm, width=30)
    entry.grid(column=1, row=1)

    def convert():
        user_input = entry.get()
        result = encode(user_input)
        result_label.config(text=f"Result: {result}")

    convert_button = ttk.Button(frm, text="Run LZW", command=convert)
    convert_button.grid(column=0, row=2)

    result_label = ttk.Label(frm, text="")
    result_label.grid(column=1, row=2)

    def decompress():
        user_input = entry.get()
        result = decode(user_input)
        result_label.config(text=f"Result: {result}")

    decompress_button = ttk.Button(frm, text="Decompress", command=decompress)
    decompress_button.grid(column=0, row=3)

    result_label = ttk.Label(frm, text="")
    result_label.grid(column=1, row=3)

def main():
    root = Tk()
    root.title("LZW Converter")
    frm = ttk.Frame(root, padding=20)
    frm.grid()

    ttk.Label(frm, text="LZW Algorithm Converter").grid(column=0, row=0)

    ttk.Button(frm, text="Convert", command=lambda: show_entry(frm)).grid(column=0, row=1)

    ttk.Button(frm, text="Decompress", command=lambda: show_entry(frm)).grid(column=0, row=2)

    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=4)

    root.mainloop()

if __name__ == "__main__":
    main()
