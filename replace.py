class TeacherHome(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.Element_2_IMG_label = tk.Label(self)

        try:
            self.img_ElementIMG2Label = tk.PhotoImage(file='ElementIMG2Label.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "ElementIMG2Label.png is missing")

        self.Element_2_IMG_label.configure(activebackground=self.bgcolor,
                                           activeforeground=self.bgcolor,
                                           background=self.bgcolor,
                                           borderwidth='0')
        self.Element_2_IMG_label.configure(image=self.img_ElementIMG2Label, text='label1')
        self.Element_2_IMG_label.place(y='0', x='0')

        try:
            self.img_TeacherHomeAddButton = tk.PhotoImage(file='TeacherHomeAddButton.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "TeacherHomeAddButton.png is missing")

        self.register_button = tk.Button(self)
        self.register_button.configure(borderwidth='0',
                                       background=self.bgcolor,
                                       activeforeground=self.bgcolor,
                                       activebackground=self.bgcolor,
                                       image=self.img_TeacherHomeAddButton,
                                       command=lambda: master.switch_frame(TeacherRegistation))
        self.register_button.place(anchor='nw',
                                   x='196',
                                   y='111')

        try:
            self.img_TeacherHomeUpdateButton = tk.PhotoImage(file='TeacherHomeUpdateButton.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "TeacherHomeView Button.png is missing")

        self.update_button = tk.Button(self)
        self.update_button.configure(borderwidth='0',
                                     background=self.bgcolor,
                                     activeforeground=self.bgcolor,
                                     activebackground=self.bgcolor,
                                     image=self.img_TeacherHomeUpdateButton,
                                     command=lambda: master.switch_frame(TeacherUpdate))
        self.update_button.place(anchor='nw',
                                 x='441',
                                 y='111')

        try:
            self.img_TeacherHomeViewButton = tk.PhotoImage(file='TeacherHomeView Button.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "TeacherHomeView Button.png is missing")

        self.view_button = tk.Button(self)
        self.view_button.configure(borderwidth='0',
                                   activebackground=self.bgcolor,
                                   activeforeground=self.bgcolor,
                                   background=self.bgcolor,
                                   image=self.img_TeacherHomeViewButton,
                                   command=lambda: master.switch_frame(TeacherView))
        self.view_button.place(anchor='nw',
                               x='196',
                               y='317')

        try:
            self.img_TeacherHomeRemoveButton = tk.PhotoImage(file='TeacherHomeRemoveButton.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "TeacherHomeRemoveButton.png is missing")

        self.Delete_button = tk.Button(self)
        self.Delete_button.configure(borderwidth='0',
                                     image=self.img_TeacherHomeRemoveButton,
                                     activeforeground=self.bgcolor,
                                     activebackground=self.bgcolor,
                                     background=self.bgcolor,
                                     command=lambda: master.switch_frame(TeacherDelete))
        self.Delete_button.place(anchor='nw',
                                 x='441',
                                 y='317')

        self.Manege_Teacher_label = tk.Label(self)
        self.Manege_Teacher_label.configure(background=self.bgcolor,
                                            borderwidth='0',
                                            font='{Poppins} 28 {bold}',
                                            foreground=self.fgcolor)
        self.Manege_Teacher_label.configure(text='Manage Teacher')
        self.Manege_Teacher_label.place(anchor='nw',
                                        x='274',
                                        y='28')
        try:
            self.img_img4 = tk.PhotoImage(file='img4.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "img_img4.png is missing")

        self.Teacher_Manege_close_button = tk.Button(self)
        self.Teacher_Manege_close_button.configure(activebackground=self.bgcolor,
                                                   activeforeground=self.bgcolor,
                                                   background=self.bgcolor,
                                                   borderwidth='0')
        self.Teacher_Manege_close_button.configure(cursor='hand2',
                                                   foreground=self.bgcolor,
                                                   highlightbackground=self.bgcolor,
                                                   highlightcolor=self.bgcolor)
        self.Teacher_Manege_close_button.configure(highlightthickness='1',
                                                   image=self.img_img4,
                                                   relief='flat',
                                                   command=self.master.on_close)

        self.Teacher_Manege_close_button.place(anchor='nw',
                                               x='760',
                                               y='8')

        self.teacher_Manege_theme_change_button = tk.Button(self)

        try:
            self.img_DarkThemeimg = tk.PhotoImage(file='DarkThemeimg.png')
        except Exception as e:
            messagebox.showerror("DarkThemeimg.png Missing")
            print(e)

        self.teacher_Manege_theme_change_button.configure(activebackground=self.bgcolor,
                                                          activeforeground=self.bgcolor,
                                                          background=self.bgcolor,
                                                          borderwidth='0',
                                                          command=self.changeTeacherHomeTheme)
        self.teacher_Manege_theme_change_button.configure(image=self.img_DarkThemeimg)
        self.teacher_Manege_theme_change_button.place(anchor='nw',
                                                      x='60',
                                                      y='10')

        self.Teacher_home_back_page_img_button = tk.Button(self)

        try:
            self.img_BackPageIMG = tk.PhotoImage(file='BackPageIMG.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "BackPageIMG.png is missing")

        self.Teacher_home_back_page_img_button.configure(activebackground=self.bgcolor,
                                                         activeforeground=self.bgcolor,
                                                         background=self.bgcolor,
                                                         borderwidth='0',
                                                         command=self.goHome)
        self.Teacher_home_back_page_img_button.configure(image=self.img_BackPageIMG)
        self.Teacher_home_back_page_img_button.place(anchor='nw',
                                                     x='15',
                                                     y='15')

        self.configure(background=self.bgcolor,
                       height='515',
                       takefocus=False,
                       width='791')
        self.place(anchor='nw',
                   x='0',
                   y='0')

    def changeTeacherHomeTheme(self):
        if self["background"] == self.bgcolor:
            TeacherHomeBGColor = self.fgcolor
            TeacherHomeFGColor = "#000000"

            try:
                self.img_DarkThemeimg = tk.PhotoImage(file='DarkThemeimg.png')
            except Exception as e:
                print(e)
                messagebox.showerror("File Missing", "DarkThemeimg.png IS Missing")

            try:
                self.img_lightThemeimg = tk.PhotoImage(file='LightThemeimg.png')
            except Exception as e:
                print(e)
                messagebox.showerror("File Missing", "LightThemeimg.png IS Missing")

            self.configure(background=TeacherHomeBGColor)
            self.register_button.configure(background=TeacherHomeBGColor,
                                           foreground=TeacherHomeBGColor,
                                           activebackground=TeacherHomeBGColor,
                                           activeforeground=TeacherHomeBGColor)
            self.Element_2_IMG_label.configure(background=TeacherHomeBGColor,
                                               foreground=TeacherHomeFGColor)
            self.update_button.configure(background=TeacherHomeBGColor,
                                         foreground=TeacherHomeBGColor,
                                         activebackground=TeacherHomeBGColor,
                                         activeforeground=TeacherHomeBGColor)
            self.view_button.configure(background=TeacherHomeBGColor,
                                       foreground=TeacherHomeBGColor,
                                       activebackground=TeacherHomeBGColor,
                                       activeforeground=TeacherHomeBGColor)
            self.Delete_button.configure(background=TeacherHomeBGColor,
                                         foreground=TeacherHomeBGColor,
                                         activebackground=TeacherHomeBGColor,
                                         activeforeground=TeacherHomeBGColor)
            self.Manege_Teacher_label.configure(background=TeacherHomeBGColor,
                                                foreground=TeacherHomeFGColor,
                                                activebackground=TeacherHomeBGColor,
                                                activeforeground=TeacherHomeBGColor)
            self.Teacher_Manege_close_button.configure(background=TeacherHomeBGColor,
                                                       foreground=TeacherHomeBGColor,
                                                       activebackground=TeacherHomeBGColor,
                                                       activeforeground=TeacherHomeBGColor)
            self.teacher_Manege_theme_change_button.configure(background=TeacherHomeBGColor,
                                                              foreground=TeacherHomeBGColor,
                                                              activebackground=TeacherHomeBGColor,
                                                              activeforeground=TeacherHomeBGColor,
                                                              image=self.img_lightThemeimg)
            self.Teacher_home_back_page_img_button.configure(background=TeacherHomeBGColor,
                                                             foreground=TeacherHomeBGColor,
                                                             activebackground=TeacherHomeBGColor,
                                                             activeforeground=TeacherHomeBGColor, )
        else:
            DTeacherHomeBGColor = self.bgcolor
            DTeacherHomeFGColor = self.fgcolor

            self.configure(background=DTeacherHomeBGColor)
            self.register_button.configure(background=DTeacherHomeBGColor,
                                           foreground=DTeacherHomeBGColor,
                                           activebackground=DTeacherHomeBGColor,
                                           activeforeground=DTeacherHomeBGColor)
            self.Element_2_IMG_label.configure(background=DTeacherHomeBGColor,
                                               foreground=DTeacherHomeFGColor)
            self.update_button.configure(background=DTeacherHomeBGColor,
                                         foreground=DTeacherHomeBGColor,
                                         activebackground=DTeacherHomeBGColor,
                                         activeforeground=DTeacherHomeBGColor)
            self.view_button.configure(background=DTeacherHomeBGColor,
                                       foreground=DTeacherHomeBGColor,
                                       activebackground=DTeacherHomeBGColor,
                                       activeforeground=DTeacherHomeBGColor)
            self.Delete_button.configure(background=DTeacherHomeBGColor,
                                         foreground=DTeacherHomeBGColor,
                                         activebackground=DTeacherHomeBGColor,
                                         activeforeground=DTeacherHomeBGColor)
            self.Manege_Teacher_label.configure(background=DTeacherHomeBGColor,
                                                foreground=DTeacherHomeFGColor,
                                                activebackground=DTeacherHomeBGColor,
                                                activeforeground=DTeacherHomeBGColor)
            self.Teacher_Manege_close_button.configure(background=DTeacherHomeBGColor,
                                                       foreground=DTeacherHomeBGColor,
                                                       activebackground=DTeacherHomeBGColor,
                                                       activeforeground=DTeacherHomeBGColor)
            self.teacher_Manege_theme_change_button.configure(background=DTeacherHomeBGColor,
                                                              foreground=DTeacherHomeBGColor,
                                                              activebackground=DTeacherHomeBGColor,
                                                              activeforeground=DTeacherHomeBGColor,
                                                              image=self.img_DarkThemeimg)
            self.Teacher_home_back_page_img_button.configure(background=DTeacherHomeBGColor,
                                                             foreground=DTeacherHomeBGColor,
                                                             activebackground=DTeacherHomeBGColor,
                                                             activeforeground=DTeacherHomeBGColor, )

    def goHome(self):
        self.master.switch_frame(Home)
