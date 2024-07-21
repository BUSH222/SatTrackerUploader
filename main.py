from tkinter import Tk, Menu, Label
from tkinter.filedialog import askopenfilename
import qrcode
from PIL import ImageTk


def openfile(w):
    filename = askopenfilename(parent=root)
    if filename == '':
        return
    f = open(filename)
    data = f.readlines()
    # CLEANUP
    out = []
    for line in data:
        line = line.split()
        if len(line) == 7:
            time = line[1].split(':')
            timestamp = int(time[0])*3600+int(time[1])*60+int(time[2])
            az = int(float(line[2]))
            el = int(float(line[3]))
            out.append(f'{timestamp} {az} {el}')
    cleaned = ' '.join(out)
    # CLEANUP END, QR GENERATING

    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(cleaned)
    qr.make(fit=True)
    res = qr.make_image(fill_color='black', back_color='white')
    img = ImageTk.PhotoImage(res)
    panel = Label(w, image=img)
    panel.pack(side='bottom', fill='both', expand='yes')


root = Tk()
root.title('QR Code generator for sattracker')
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Open', command=lambda: openfile(root))
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
menubar.add_cascade(label='File', menu=filemenu)

root.config(menu=menubar)
root.mainloop()
