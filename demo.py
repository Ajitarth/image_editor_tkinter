from tkinter import GROOVE, RIDGE, ttk, Tk , PhotoImage, Canvas

class FrontEnd():
    def __init__(self,master):
        self.master = master
        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack()

        self.logo = PhotoImage('python_logo.png').subsample(5,5)
        print(self.logo)

        ttk.Label(self.frame_header,image=self.logo).grid(
            row=0,column=0,rowspan=2)
        
        ttk.Label(self.frame_header,text='Welcome to Image Editor app!').grid(
            row=0,column=0)

        ttk.Label(self.frame_header,text='Upload, edit and save your images easily!').grid(
            row=1,column=0)
        
        self.frame_menu = ttk.Frame(self.master)
        self.frame_menu.pack()
        self.frame_menu.config(relief=RIDGE, padding=(50,15))

        
        ttk.Button(self.frame_menu,text='Upload an image!',command=self.upload_action).grid(
            row=0,column=0,padx=5,pady=5,sticky='sw')
        
        ttk.Button(self.frame_menu,text='Crop Image',command=self.crop_action).grid(
            row=1,column=0,padx=5,pady=5,sticky='sw')
        
        ttk.Button(self.frame_menu,text='Add text',command=self.text_action_1).grid(
            row=2,column=0,padx=5,pady=5,sticky='sw')
        
        ttk.Button(self.frame_menu,text='Draw over image',command=self.draw_action).grid(
            row=3,column=0,padx=5,pady=5,sticky='sw')
        
        ttk.Button(self.frame_menu,text='Apply filters',command=self.filter_action).grid(
            row=4,column=0,padx=5,pady=5,sticky='sw')
        
        ttk.Button(self.frame_menu,text='Blurr/Smoothing',command=self.blurr_action).grid(
            row=5,column=0,padx=5,pady=5,sticky='sw')
        
        ttk.Button(self.frame_menu,text='Adjust levels',command=self.adjust_action).grid(
            row=6,column=0,padx=5,pady=5,sticky='sw')
        
        ttk.Button(self.frame_menu,text='Rotate',command=self.rotate_action).grid(
            row=7,column=0,padx=5,pady=5,sticky='sw')

        ttk.Button(self.frame_menu,text='Flip',command=self.flip_action).grid(
            row=8,column=0,padx=5,pady=5,sticky='sw')
        
        ttk.Button(self.frame_menu,text='Save As',command=self.save_action).grid(
            row=9,column=0,padx=5,pady=5,sticky='sw')
        
        self.apply_and_cancel = ttk.Frame(self.master)
        self.apply_and_cancel.pack()

        ttk.Button(
            self.apply_and_cancel,text='Apply!',command=self.apply_action).grid(row=0,column=0,padx=5,pady=5,sticky='sw')
        ttk.Button(
            self.apply_and_cancel,text='Cancel!',command=self.cancel_action).grid(row=0,column=1,padx=5,pady=5,sticky='sw')
        ttk.Button(
            self.apply_and_cancel,text='Revert All Changes!',command=self.revert_action).grid(row=0,column=2,padx=5,pady=5,sticky='sw')
        

        self.canvas = Canvas(self.frame_menu,bg = 'grey', width=300,height=400)
        self.canvas.grid(row=0,column=1,rowspan=10)

        self.side_frame = ttk.Frame(self.frame_menu)
        self.side_frame.grid(row=0,column=2,rowspan=10)
        self.side_frame.config(relief=GROOVE, padding=(50,15))

        ttk.Label(self.side_frame,text="Upload an Image...").grid(row=0,column=0)


    def refresh_side_frame(self):
        try:
            self.side_frame.grid_forget()
        except:
            pass    

        self.side_frame = ttk.Frame(self.frame_menu)
        self.side_frame.grid(row=0,column=2,rowspan=10)
        self.side_frame.config(relief=GROOVE, padding=(50,15))    

    def upload_action(self):
        self.refresh_side_frame()
        ttk.Label(self.side_frame,text="Please upload an image to edit!!").grid(row=0,column=0)

    def text_action_1(self):
        self.refresh_side_frame()
        ttk.Label(self.side_frame,text="Please upload an image to edit!!").grid(row=0,column=0)

    def crop_action(self):
        self.refresh_side_frame()
        ttk.Label(self.side_frame,text="Please upload an image to edit!!").grid(row=0,column=0)


    def draw_action(self):
        pass

    def filter_action(self):
        pass

    def blurr_action(self):
        pass

    def adjust_action(self):
        pass

    def rotate_action(self):
        pass

    def flip_action(self):
        pass

    def save_action(self):
        pass
    
    def apply_action(self):
        pass

    def cancel_action(self):
        pass
    

    def revert_action(self):
        pass


    



root = Tk()
FrontEnd(root)
root.mainloop()
