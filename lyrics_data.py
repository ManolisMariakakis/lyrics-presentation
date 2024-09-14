import obspython as obs
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox 
import tkinter as tk
import os
import shutil
from pathlib import Path
import tkinter.colorchooser
from tkinter.messagebox import askokcancel, showinfo, WARNING
from PIL import Image, ImageTk

global my_path
my_path = "C:\\inetpub\\wwwroot\\lyrics"

# --1. Add/Change Hymns----------------------------------------------------------

class PrepareEditApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x600")
        self.root.title("Untitled - Notepad")
        self.root.config(bg = "white")
        self.root.wm_attributes("-topmost", True)
        frame = tk.Frame(root)
        frame.pack(padx = 10, pady = 5, anchor = 'nw')

        b1 = tk.Button(root, width=10, text="Open", bg = "white", command = self.openFile)
        b1.pack(in_ = frame, side=tk.LEFT)

        b2 = tk.Button(root, width=10, text="Save", bg = "white", command = self.saveFile)
        b2.pack(in_ = frame, side=tk.LEFT)

        b3 = tk.Button(root, width=10, text="Clear", bg = "white", command = self.clearFile)
        b3.pack(in_ = frame, side=tk.LEFT)

        b4 = tk.Button(root, width=10, text="Exit", bg = "white", command = self.closeFile)
        b4.pack(in_ = frame, side=tk.LEFT)

        root.entry = tk.Text(root, wrap = tk.WORD, bg = "#F9DDA4", font = ("Arial", 12))
        root.entry.pack(padx = 10, pady = 5, expand = tk.TRUE, fill = tk.BOTH)

    def openFile(self): 
        filename = filedialog.askopenfilename(initialdir=my_path + "\\my_hymns", title="Select A lyrics file")
        if filename:
            file = open(filename, 'r', encoding='utf8')
            content = file.read()
            self.root.entry.delete(1.0, tk.END)
            self.root.entry.insert(tk.INSERT, content)
            tk.myFile = os.path.basename(filename)
            self.root.title(tk.myFile)

    def saveFile(self):
        if self.root.title() == "Untitled - Notepad":
            list_of_files = Path(my_path + "\\my_hymns").glob('[0-9][0-9][0-9]*.txt')
            maxs = max((Path(fn).name for fn in list_of_files), key=lambda fn: Path(fn).stem)[0:3]
            maxi = int(maxs) + 1
            arr = str(self.root.entry.get(1.0, tk.END)).split('\n')
            tk.myFile =  ("000" + str(maxi))[-3:] + ". " +  arr[0] + ".txt"
            filename = filedialog.asksaveasfilename(initialdir=my_path + "\\my_hymns", initialfile = tk.myFile, filetypes=[("Plain text", ".txt")])
        else:
            filename=my_path + "\\my_hymns" + "\\" + os.path.basename(tk.myFile)
        if filename:
            fh = open(filename, 'w', encoding='utf-8')
            text = str(self.root.entry.get(1.0, tk.END))
            fh.write(text)
            fh.close()
            self.root.entry.delete(1.0, tk.END)
            self.root.title("Untitled - Notepad")

    def clearFile(self):
        self.root.entry.delete(1.0, tk.END)
        
    def closeFile(self):
        self.root.destroy()

# --2. Prepare Hymns----------------------------------------------------------

class PrepareHymnsApp:
    def __init__(self):
        with open(my_path + "\\data\\titles.txt", mode="w",  encoding="utf-8") as titles:
            for path, subdirs, files in os.walk(my_path + "\\my_hymns"):
                for filename in files:
                    shutil.copyfile(my_path + "\\my_hymns\\" +str(filename), my_path + "\\data\\" + str(filename)[0:3] + ".txt")
                    titles.write(str(filename) + os.linesep) 
        messagebox.showinfo("2. Prepare Hymns", "Completed\nPlease restart OBS Studio or Refresh Titles dock page!") 

#---Colors Palette----------------------------------------------------------------

class PrepareColorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Colors palette!")
        self.root.config(bg = "white")
        self.root.wm_attributes("-topmost", True)

        self.frame1 = Frame(root) 
        self.frame1.grid(row=0, column=0, sticky="nsew") 
        self.frame1.grid(padx=10, pady=5)
        

        self.new_line_btn = tk.Button(self.frame1, width=10, text='New line', command=self.new_line)
        self.new_line_btn.grid(column=0, row=0)
        self.save_colors_btn = tk.Button(self.frame1, width=10, text='Save Colors', command=self.save_colors)
        self.save_colors_btn.grid(column=1, row=0)
        self.exit_btn = tk.Button(self.frame1, width=10, text='Exit', command=self.exit_colors)
        self.exit_btn.grid(column=2, row=0)

        self.frame2 = Frame(root, bg="white") 
        self.frame2.grid(row=1, column=0) 
        self.frame2.grid(padx=10, pady=5)
        global grid
        grid={}

        file = open(my_path+"\\data\\colors.txt", 'r', encoding='utf8')
        content = file.read()
        file.close

        arr = content.split("\n")

        id=0
        col0 = tk.Label(self.frame2,width=5, height=1, bg='grey', text="#", font=("Arial", 10, "bold"))
        grid[(id,0)] = col0
        col0.grid(row=id,column=0)

        col1 = tk.Label(self.frame2,width=20, height=1, bg='grey', text="Title", font=("Arial", 10, "bold"))
        grid[(id,1)] = col1
        col1.grid(row=id,column=1)

        col2 = tk.Label(self.frame2,width=15, height=1, bg='grey', text="Text color", font=("Arial", 10, "bold"))
        grid[(id,2)] = col2
        col2.grid(row=id,column=2)

        col3 = tk.Label(self.frame2,width=15, height=1, bg='grey', text="Shadow color", font=("Arial", 10, "bold"))
        grid[(id,3)] = col3 
        col3.grid(row=id,column=3)

        col4 = tk.Label(self.frame2,width=20, height=1, bg='grey', text="Color1", font=("Arial", 10, "bold"))
        grid[(id,4)] = col4 
        col4.grid(row=id,column=4)

        col5 = tk.Label(self.frame2,width=20, height=1, bg='grey', text="Color2", font=("Arial", 10, "bold"))
        grid[(id,5)] = col5
        col5.grid(row=id,column=5)

        col6 = tk.Label(self.frame2,width=20, height=1, bg='grey', text="Color3", font=("Arial", 10, "bold"))
        grid[(id,6)] = col6
        col6.grid(row=id,column=6)

        col7 = tk.Label(self.frame2,width=10, height=1, bg='grey', text="Stop", font=("Arial", 10, "bold"))
        grid[(id,7)] = col7
        col7.grid(row=id,column=7)

        col8 = tk.Label(self.frame2,width=10, height=1, bg='grey', text="Degrees", font=("Arial", 10, "bold"))
        grid[(id,8)] = col8
        col8.grid(row=id,column=8)

        for rows in arr:
            cols = rows.split(";")
            if len(cols) == 8 and cols[0][0:1] != "#" and cols[0] != "W_Transparent" and cols[0] != "B_Transparent":
                id = id + 1
                col0 = tk.Button(self.frame2,width=5, height=1, bg='lightgrey', text="DEL", font=("Arial", 10), command = lambda id=id: self.remove_line(id))
                grid[(id,0)] = col0
                col0.grid(row=id,column=0)

                col1 = tk.Text(self.frame2,width=20, height=1, bg='white')
                grid[(id,1)] = col1
                col1.grid(row=id,column=1)
                col1.insert('0.1',cols[0])

                col2 = tk.Button(self.frame2,cursor="hand2", font=("Arial", 9), text=cols[1],width=15, height=1, fg=self.bg_to_fg(cols[1]), bg= cols[1], command= lambda id=id,t=cols[1],c=2: self.update_color(id,c,t))
                grid[(id,2)] = col2
                col2.grid(row=id,column=2)

                col3 = tk.Button(self.frame2,cursor="hand2", font=("Arial", 9), text=cols[2],width=15, height=1, fg=self.bg_to_fg(cols[2]), bg= cols[2], command= lambda id=id,t=cols[2],c=3: self.update_color(id,c,t))
                grid[(id,3)] = col3
                col3.grid(row=id,column=3)

                col4 = tk.Button(self.frame2,cursor="hand2", font=("Arial", 9), text=cols[3],width=20, height=1, fg=self.bg_to_fg(cols[3]), bg= cols[3], command= lambda id=id,t=cols[3],c=4: self.update_color(id,c,t))
                grid[(id,4)] = col4
                col4.grid(row=id,column=4)

                col5 = tk.Button(self.frame2,cursor="hand2", font=("Arial", 9), text=cols[4],width=20, height=1, fg=self.bg_to_fg(cols[4]), bg= cols[4], command= lambda id=id,t=cols[4],c=5: self.update_color(id,c,t))
                grid[(id,5)] = col5
                col5.grid(row=id,column=5)

                col6 = tk.Button(self.frame2,cursor="hand2", font=("Arial", 9), text=cols[5],width=20, height=1, fg=self.bg_to_fg(cols[5]), bg= cols[5], command= lambda id=id,t=cols[5],c=6: self.update_color(id,c,t))
                grid[(id,6)] = col6
                col6.grid(row=id,column=6)

                var7 = tk.StringVar(value=cols[6])
                col7 = tk.Spinbox(self.frame2, from_=0, to=100, textvariable=var7,width=10)
                grid[(id,7)] = col7
                col7.grid(row=id,column=7)

                var8 = tk.StringVar(value=cols[7])
                col8 = tk.Spinbox(self.frame2, from_=0, to=360, textvariable=var8,width=10)
                grid[(id,8)] = col8
                col8.grid(row=id,column=8)

    def bg_to_fg(self, hex):
        if hex == "white":
            hex="ffffff"
        elif hex == "black":
            hex = "000000"

        hex = hex.replace("#","")
        rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
        if (rgb[0] * 0.299 + rgb[1] * 0.587 + rgb[2] * 0.114) > 186:
            fg="#000000"
        else:
            fg="#ffffff"
        return fg

    def exit_colors(self):
        self.root.destroy()

    def new_line(self):
        last_row = self.frame2.grid_size()[1]
        id = last_row
        t = 'New Title'
        w = "#ffffff"

        col0 = tk.Button(self.frame2,width=5, height=1, bg='lightgrey', text="DEL", font=("Arial", 10), command = lambda id=id: self.remove_line(id))
        grid[(id,0)] = col0
        col0.grid(row=id,column=0)

        col1 = tk.Text(self.frame2,width=20, height=1, bg='white')
        grid[(id,1)] = col1
        col1.grid(row=id,column=1)
        col1.insert('0.1',t)

        col2 = tk.Button(self.frame2,cursor="hand2", font=("Arial", 9), text=w,width=15, height=1, fg=self.bg_to_fg(w), bg= w, command= lambda id=id,t=w,c=2: self.update_color(id,c,t))
        grid[(id,2)] = col2
        col2.grid(row=id,column=2)

        col3 = tk.Button(self.frame2,cursor="hand2", font=("Arial", 9), text=w,width=15, height=1, fg=self.bg_to_fg(w), bg= w, command= lambda id=id,t=w,c=3: self.update_color(id,c,t))
        grid[(id,3)] = col3
        col3.grid(row=id,column=3)

        col4 = tk.Button(self.frame2,cursor="hand2", font=("Arial", 9), text=w,width=20, height=1, fg=self.bg_to_fg(w), bg= w, command= lambda id=id,t=w,c=4: self.update_color(id,c,t))
        grid[(id,4)] = col4
        col4.grid(row=id,column=4)

        col5 = tk.Button(self.frame2,cursor="hand2", font=("Arial", 9), text=w,width=20, height=1, fg=self.bg_to_fg(w), bg= w, command= lambda id=id,t=w,c=5: self.update_color(id,c,t))
        grid[(id,5)] = col5
        col5.grid(row=id,column=5)

        col6 = tk.Button(self.frame2,cursor="hand2", font=("Arial", 9), text=w,width=20, height=1, fg=self.bg_to_fg(w), bg= w, command= lambda id=id,t=w,c=6: self.update_color(id,c,t))
        grid[(id,6)] = col6
        col6.grid(row=id,column=6)

        var7 = tk.StringVar(value=50)
        col7 = tk.Spinbox(self.frame2, from_=0, to=100, textvariable=var7,width=10)
        grid[(id,7)] = col7
        col7.grid(row=id,column=7)

        var8 = tk.StringVar(value=0)
        col8 = tk.Spinbox(self.frame2, from_=0, to=360, textvariable=var8,width=10)
        grid[(id,8)] = col8
        col8.grid(row=id,column=8)

    def remove_line(self,id):
        grid[(id,0)].destroy()
        grid[(id,1)].delete('1.0', END)
        grid[(id,1)].insert('0.1',"del")
        grid[(id,1)].grid_remove()
        grid[(id,2)].grid_remove()
        grid[(id,3)].grid_remove()
        grid[(id,4)].grid_remove()
        grid[(id,5)].grid_remove()
        grid[(id,6)].grid_remove()
        grid[(id,7)].grid_remove()
        grid[(id,8)].grid_remove()



    def save_colors(self):
        header_line="#" + grid[(0,1)].cget("text")
        c = 2
        while c < 9:
            header_line +=  ";" + grid[(0,c)].cget("text")
            c += 1
        content = header_line + '\n'
        
        r = 1
        while r < self.frame2.grid_size()[1]:
            detail_line= grid[(r,1)].get('1.0', tk.END).replace('\n','')
            if detail_line !="del":
                detail_line +=  ";" + grid[(r,2)].cget("text")
                detail_line +=  ";" + grid[(r,3)].cget("text")
                detail_line +=  ";" + grid[(r,4)].cget("text")
                detail_line +=  ";" + grid[(r,5)].cget("text")
                detail_line +=  ";" + grid[(r,6)].cget("text")
                detail_line +=  ";" + grid.get((r, 7)).get()
                detail_line +=  ";" + grid.get((r, 8)).get()
            content += detail_line + '\n'
            r += 1

        content += "B_Transparent;#000000;#003366;rgba(255,255,255,0);rgba(255,255,255,0);rgba(255,255,255,0);50;0\n" 
        content += "W_Transparent;#ffffff;#000000;rgba(255,255,254,0);rgba(255,255,254,0);rgba(255,255,254,0);50;0\n" 
        file = open(my_path+"\\data\\colors.txt", 'w', encoding='utf8')
        file.write(content)
        file.close
        messagebox.showinfo("3. Colors Palette", "Completed\nPlease restart OBS Studio or Refresh dock pages!")


    def update_color(self,id,c,t):
        color = tk.colorchooser.askcolor(parent=self.root,color=t)
        if color[1] != None:
            grid[(id,c)].configure(fg=self.bg_to_fg(color[1]), bg=color[1],text=color[1])

# ---Image Viewer-----------------------------------------------------------------

class ImageViewerApp:
    def __init__(self, root, folder):
        self.root = root
        self.root.title("Image Viewer")
        self.folder = folder
        self.image_files = [f for f in os.listdir(folder) if f.endswith(('img001.jpg','img002.jpg','img003.jpg','img004.jpg','img005.jpg','img006.jpg','img007.jpg','img008.jpg','img009.jpg','img0010.jpg','img011.jpg','img012.jpg','img013.jpg','img014.jpg','img015.jpg','img016.jpg','img017.jpg','img018.jpg','img019.jpg','img020.jpg'))]
        self.image_index = 0

        self.label = Label(root)
        self.label.pack()

        self.prev_button = Button(root, text="Previous", width=8, command=self.prev_image)
        self.prev_button.pack(padx=10, pady=10,side="left")
        self.next_button = Button(root, text="Next", width=8, command=self.next_image)
        self.next_button.pack(padx=10, pady=10,side="left")
        self.open_button = Button(root, text="Replace Image", command=self.replace_with_new_image)
        self.open_button.pack(padx=10, pady=10,side="left")
        self.exit_button = Button(root, width=8, text="Exit", command=self.exit_image)
        self.exit_button.pack(padx=10, pady=10,side="left")

        self.filename = Label(root, text="", font='Arial 12 bold')
        self.filename.pack(padx=10, pady=10,side="right")

        self.show_image()

    def exit_image(self):
        self.root.destroy()

    def show_image(self):
        image_path = os.path.join(self.folder, self.image_files[self.image_index])
        image = Image.open(image_path)
        image = image.resize((550, 550))
        image = ImageTk.PhotoImage(image)

        self.label.config(image=image)
        self.label.image = image
        self.filename.config(text = self.image_files[self.image_index])

    def prev_image(self):
        self.image_index = (self.image_index - 1) % len(self.image_files)
        self.show_image()

    def next_image(self):
        self.image_index = (self.image_index + 1) % len(self.image_files)
        self.show_image()

    def replace_with_new_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg")])
        if file_path:
            try:
                self.image_path = file_path
                self.image = Image.open(self.image_path)
                if self.image:
                    image = self.image.resize((550, 550))
                    image = ImageTk.PhotoImage(image)

                    self.label.config(image=image)
                    self.label.image = image 
                    answer = askokcancel(title='Confirmation', message='Replace Image ' + self.image_files[self.image_index] + '?', icon=WARNING)
                    if answer:
                        try:
                            save_path = self.folder + "\\" + self.image_files[self.image_index]
                            self.image.save(save_path)
                            messagebox.showinfo("Image Replaced", f"Image {self.image_files[self.image_index]} replaced!")
                        except Exception as e:
                            messagebox.showerror("Error", f"Failed to save image: {e}")
                    else:
                        self.show_image()

            except Exception as e:
                messagebox.showerror("Error", f"Failed to open image: {e}")


# -------------------------------------------------------------------------------

def edit_pressed(props, prop):
    root = tk.Tk()
    app = PrepareEditApp(root)
    root.mainloop()

def prepare_pressed(props, prop):
    app = PrepareHymnsApp()

def prepare_colors(props, prop):
    root = tk.Tk()
    app = PrepareColorsApp(root)
    root.mainloop()

def prepare_images(props, prop):
    root = tk.Tk()
    app = ImageViewerApp(root,my_path + "\\images")
    root.mainloop()

def script_description():
	return " Hymns maintenance!"

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(props, "button1", "1. Add/Change Hymns", edit_pressed)
    obs.obs_properties_add_button(props, "button2", "2. Prepare Hymns", prepare_pressed)
    obs.obs_properties_add_button(props, "button3", "Colors Palette", prepare_colors)
    obs.obs_properties_add_button(props, "button4", "Image Viewer", prepare_images)
    return props

