import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk, ImageDraw, ImageFont
import matplotlib.pyplot as plt

window = tk.Tk()
window.geometry("600x500")
window.title('Upload your image')
open_file_path = None



label = tk.Label(window,text='Add Photo',width=30)
label.grid(row=0,column=0)
label.place(relx=0.25, rely=0.01)
button = tk.Button(window, text='Upload File', width=20,command = lambda:upload_file())
button.grid(row=1,column=0)
button.place(relx=0.29, rely=0.1)
text = tk.Text(width = 40,height = 5)
text.place(relx = 0.24, rely = 0.3)
button_confirm = tk.Button(window,text = "Confirm text watermark",command = lambda:retrieve_input())
button_confirm.place(relx = 0.33,rely = 0.5)

def retrieve_input():
   input_value = text.get('1.0','end-1c')
   return input_value
def upload_file():
   global open_file_path
   # font_type = ImageFont.truetype("arial.ttf", 18)
   input_text = retrieve_input()
   open_file_path = filedialog.askopenfilename()
   image = Image.open(open_file_path)
   width,height = image.size
   draw_watermark = ImageDraw.Draw(image)
   fill_color = (203, 201, 201)
   x = width/2-50
   y = height/2-50
   position = (x,y)
   draw_watermark.text(xy=position, text=input_text, fill=fill_color)
   image.save('watermark_image.jpg')
   # plt.imshow(image)

window.mainloop()