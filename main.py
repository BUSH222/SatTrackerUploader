from tkinter import Tk, Button
from tkinter.filedialog import askopenfilename
from tkinter import font as tkFont
import qrcode


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
    res.show()


root = Tk()
root.title('SatTracker QR Generator')

helv36 = tkFont.Font(family='Helvetica', size=36, weight='bold')

b = Button(root, bg='black', text='open file', height=6, width=12, command=lambda: openfile(root))
b['font'] = helv36
b.pack()

root.mainloop()
