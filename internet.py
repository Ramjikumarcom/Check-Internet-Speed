from tkinter import *
import speedtest
def speedcheck():
    st = speedtest.Speedtest()
    st.get_servers()
    down=str(round(st.download()/(10**6),3))+"Mbps"
    Upload=str(round(st.upload()/(10**6),3))+"Mbps"
    lab_upload.config(text=Upload)
    lab_down.config(text=down)



sp = Tk()
sp.title("inernet speed test")
sp.geometry("500x500")
sp.config(
    bg="green",
)
lab = Label(
    justify="center",
    text="Internet Speed Test",
    font=("Time New Roman", 25, "bold"),
    fg="yellow",
    bg="green"
)
lab.place(x=120, y=30, height=50, width=350)
lab = Label(
    text="Download Speed",
    font=("Time New Roman", 25, "bold"),
    fg="black",
)
lab.place(x=120, y=90, height=50, width=340)
lab_down = Label(
    text="00",
    font=("Time New Roman", 25, "bold"),
    fg="black",

)
lab_down.place(x=120, y=150, height=50, width=340)
lab = Label(
    text="Upload Speed",
    font=("Time New Roman", 25, "bold"),
    fg="black",
)
lab.place(x=120, y=220, height=50, width=340)
lab_upload = Label(
    text="00",
    font=("Time New Roman", 25, "bold"),
    fg="black",
)
lab_upload.place(
    x=120,
    y=290,
    height=50,
    width=340,
)
button = Button(
    sp,
    text="check speed",
    font=("Time New Roman", 25, "bold"),
    relief=RAISED,
    background="blue",
    command=speedcheck
)
button.place(  x=120,
    y=350,
    height=50,
    width=340,)
sp.mainloop()
