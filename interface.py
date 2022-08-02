from tkinter import *
from PIL import ImageTk, Image
import cv2



root = Tk()
# Create a frame
app = Frame(root, bg="white")
app.pack()
# Create a label in the frame
lmain = Label(app)
lmain.grid()

# Capture from camera
cap = cv2.VideoCapture(0)


# function for video streaming
def video_stream():
    _, frame = cap.read()
    virtual_ms.video_stream()
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream)     


btn2 = Button(root, text='Start', width=25, height=2,command=video_stream)
btn2.pack()

btn = Button(root, text='Stop',width=25, height=2,command=root.destroy)
btn.pack()
root.mainloop()




