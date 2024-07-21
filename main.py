from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.iconbitmap('C:/Users/Umer/Desktop/projects GUI/smily_with_heart.ico')

my_image = ImageTk.PhotoImage(Image.open('C:/Users/Umer/Desktop/projects GUI/smily_with_heart.png'))
my_label = Label(image=my_image)
my_label.pack()

exit_button = Button(root,text='Exit',command=root.quit)
exit_button.config(font=('Helvtica',20),fg='blue',bg='yellow')
exit_button.pack()




root.mainloop()