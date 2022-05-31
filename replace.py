class DarkAboutMe(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        try:
            self.aboutmeimg = tk.PhotoImage(file='About_Me.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "About_Me.png Is Missing")

        self.about_bg_img = tk.Label(self)
        self.about_bg_img.configure(image=self.aboutmeimg, borderwidth='0')
        self.about_bg_img.place(x='0', y="0")

        try:
            self.img_img4 = tk.PhotoImage(file='img4.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "img_img4.png is missing")

        self.About_Me_close_button = tk.Button(self)
        self.About_Me_close_button.configure(activebackground='#121212',
                                             activeforeground='#121212',
                                             background='#121212',
                                             borderwidth='0')
        self.About_Me_close_button.configure(cursor='hand2',
                                             foreground='#121212',
                                             highlightbackground='#121212',
                                             highlightcolor='#121212')
        self.About_Me_close_button.configure(highlightthickness='1',
                                             image=self.img_img4,
                                             relief='flat',
                                             command=self.master.on_close)

        self.About_Me_close_button.place(anchor='nw',
                                         x='760',
                                         y='8')

        self.About_Me_back_page_img_button = tk.Button(self)

        try:
            self.img_BackPageIMG = tk.PhotoImage(file='BackPageIMG.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "BackPageIMG.png is missing")

        self.About_Me_back_page_img_button.configure(activebackground='#121212',
                                                     activeforeground='#121212',
                                                     background='#121212',
                                                     borderwidth='0',
                                                     command=self.goAboutMeHome)
        self.About_Me_back_page_img_button.configure(image=self.img_BackPageIMG)
        self.About_Me_back_page_img_button.place(anchor='nw',
                                                 x='15',
                                                 y='15')

        self.Student_Update_Student_registation_theme_change_button = tk.Button(self)

        try:
            self.img_DarkThemeimg = tk.PhotoImage(file='DarkThemeimg.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "DarkThemeimg.png is missing")

        self.Student_Update_Student_registation_theme_change_button.configure(activebackground=self.bgcolor,
                                                                              activeforeground=self.bgcolor,
                                                                              background=self.bgcolor,
                                                                              borderwidth='0',
                                                                              relief="flat",
                                                                              overrelief="flat",
                                                                              command=self.changeAboutMeTheme)
        self.Student_Update_Student_registation_theme_change_button.configure(image=self.img_DarkThemeimg,
                                                                              text='button2')
        self.Student_Update_Student_registation_theme_change_button.place(anchor='nw',
                                                                          x='60',
                                                                          y='10')
        self.configure(background='#121212',
                       height='515',
                       width='791')
        self.place(x='0', y="0")

    def goAboutMeHome(self):
        self.master.switch_frame(DarkHome)

    def  changeAboutMeTheme(self):
        self.master.switch_frame(LightAboutMe)

