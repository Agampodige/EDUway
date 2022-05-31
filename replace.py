class DarkTeacherView(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.sty = ttk.Style()
        self.sty.configure('Treeview', rowheight=46, fieldbackground="#000000")
        self.sty.map('Treeview', background=[('selected', '#3B3B3B'), ('focus', '#212121')])
        self.sty.configure("Vertical.TScrollbar",
                           background="#000000", darkcolor="#000000", lightcolor="#000000",
                           troughcolor="gray", bordercolor="gray", arrowcolor="#000000")
        self.teacher_recodes_scroll = ttk.Scrollbar(self)
        self.columns = ('ID',
                        'First name',
                        'Last name',
                        'Age',
                        'Phone Number',
                        'Gender',
                        'Subjects')
        self.teacher_recodes = ttk.Treeview(height=8, columns=self.columns, show="tree",
                                            yscrollcommand=self.teacher_recodes_scroll.set)

        # self.teacher_recodes.heading("ID", text="ID")
        # self.teacher_recodes.heading("First name", text="First name")
        # self.teacher_recodes.heading("Last name", text="Last name")
        # self.teacher_recodes.heading("Age", text="Age")
        # self.teacher_recodes.heading("Phone Number", text="Phone Number")
        # self.teacher_recodes.heading("Gender", text="Gender")
        # self.teacher_recodes.heading("Subjects", text="Subjects")

        self.teacher_recodes.column("ID", width=50)
        self.teacher_recodes.column("First name", width=150)
        self.teacher_recodes.column("Last name", width=130)
        self.teacher_recodes.column("Age", width=50)
        self.teacher_recodes.column("Phone Number", width=130)
        self.teacher_recodes.column("Gender", width=80)
        self.teacher_recodes.column("Subjects", width=220)

        # Add data
        self.conn = mysql.connector.connect(user="root",
                                            password="",
                                            database="eduway")

        self.connetc = self.conn.cursor()
        self.connetc.execute("SELECT * FROM teacher")
        self.recodes = self.connetc.fetchall()
        global count

        count = 0
        self.teacher_recodes.tag_configure("oneColor", background="#121212",
                                           font='{Poppins} 8 {bold}',
                                           foreground="#c2c2c2")

        self.teacher_recodes.tag_configure("secondColor", background="#0a0a0a",
                                           font='{Poppins} 8 {bold}',
                                           foreground="#c2c2c2")

        for record in self.recodes:
            if count % 2 == 0:
                self.teacher_recodes.insert(parent="", index='end', iid=count, values=(
                    record[0], record[1], record[2], record[4], "0" + str(record[3]), record[5], record[6]),
                                            tags=("oneColor"))
                if count <=7:
                    self.teacher_recodes.configure(height=int(count))
                else:
                    self.teacher_recodes.configure(height="8")
                    print("hi")
            else:
                self.teacher_recodes.insert(parent="", index='end', iid=count, values=(
                    record[0], record[1], record[2], record[4], "0" + str(record[3]), record[5], record[6]),
                                            tags=("secondColor"))
                if count <=7:
                    self.teacher_recodes.configure(height=int(count))
                else:
                    self.teacher_recodes.configure(height="8")
                    print("hi")
                    
                                                
            count += 1
        self.teacher_recodes.configure(height=int(count))
        self.connetc.close()
        self.conn.close()

        # self.teacher_recodes.insert()

        self.teacher_recodes.place(anchor='nw', x='0', y='146', relx="-0.24", bordermode='ignore')
        self.teacher_recodes_scroll.configure(command=self.teacher_recodes.yview)
        self.teacher_recodes_scroll.configure(orient='vertical', )
        self.teacher_recodes_scroll.place(anchor='nw', height='44', x='0', y='150')

        self.teacher_view_theme_change_button = tk.Button(self)

        try:
            self.img_DarkThemeimg = tk.PhotoImage(file='DarkThemeimg.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "DarkThemeimg.png is missing")

        self.teacher_view_theme_change_button.configure(activebackground='#121212',
                                                        activeforeground='#121212',
                                                        background='#121212',
                                                        borderwidth='0',
                                                        relief="flat",
                                                        overrelief="flat")
        self.teacher_view_theme_change_button.configure(image=self.img_DarkThemeimg,
                                                        text='button2',
                                                        command=self.changeTeacherViewTheme)
        self.teacher_view_theme_change_button.place(anchor='nw',
                                                    x='60',
                                                    y='10')

        self.teacher_home_back_page_img_button = tk.Button(self)

        try:
            self.img_BackPageIMG = tk.PhotoImage(file='BackPageIMG.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "BackPageIMG.png is missing")

        self.teacher_home_back_page_img_button.configure(activebackground='#121212',
                                                         activeforeground='#121212',
                                                         background='#121212',
                                                         borderwidth='0',
                                                         command=self.goBackToTeacherHome)
        self.teacher_home_back_page_img_button.configure(image=self.img_BackPageIMG)
        self.teacher_home_back_page_img_button.place(anchor='nw', x='15', y='15')

        try:
            self.img_img4 = tk.PhotoImage(file='img4.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "img_img4.png is missing")
        self.Teacher_view_close_button = tk.Button(self)
        self.Teacher_view_close_button.configure(activebackground='#121212',
                                                 activeforeground='#121212',
                                                 background='#121212',
                                                 borderwidth='0')
        self.Teacher_view_close_button.configure(cursor='hand2',
                                                 foreground='#121212',
                                                 highlightbackground='#121212',
                                                 highlightcolor='#121212')
        self.Teacher_view_close_button.configure(highlightthickness='1',
                                                 image=self.img_img4,
                                                 relief='flat',
                                                 command=self.master.on_close)
        self.Teacher_view_close_button.place(anchor='nw',
                                             x='760',
                                             y='8')
        self.View_Teacher_label = tk.Label(self)
        self.View_Teacher_label.configure(background='#121212',
                                          borderwidth='0',
                                          font='{Poppins} 28 {bold}',
                                          foreground='#ffffff')
        self.View_Teacher_label.configure(text='View Teacher')
        self.View_Teacher_label.place(anchor='nw',
                                      x='274',
                                      y='28')

        self.Teacher_ID_label = tk.Label(self)
        self.Teacher_ID_label.configure(background='#121212',
                                        borderwidth='0',
                                        font='{Poppins} 10 {bold}',
                                        foreground='#ffffff')
        self.Teacher_ID_label.configure(text='ID')
        self.Teacher_ID_label.place(anchor='nw',
                                    x='16',
                                    y='115')

        self.Teacher_First_Name_label = tk.Label(self)
        self.Teacher_First_Name_label.configure(background='#121212',
                                                borderwidth='0',
                                                font='{Poppins} 10 {bold}',
                                                foreground='#ffffff')
        self.Teacher_First_Name_label.configure(text='First Name')
        self.Teacher_First_Name_label.place(anchor='nw',
                                            x='55',
                                            y='115')

        self.Teacher_Second_Name_label = tk.Label(self)
        self.Teacher_Second_Name_label.configure(background='#121212',
                                                 borderwidth='0',
                                                 font='{Poppins} 10 {bold}',
                                                 foreground='#ffffff')
        self.Teacher_Second_Name_label.configure(text='Second Name')
        self.Teacher_Second_Name_label.place(anchor='nw',
                                             x='180',
                                             y='115')

        self.Teacher_Age_label = tk.Label(self)
        self.Teacher_Age_label.configure(background='#121212',
                                         borderwidth='0',
                                         font='{Poppins} 10 {bold}',
                                         foreground='#ffffff')
        self.Teacher_Age_label.configure(text='Age')
        self.Teacher_Age_label.place(anchor='nw',
                                     x='340',
                                     y='115')

        self.Teacher_Phone_Number_label = tk.Label(self)
        self.Teacher_Phone_Number_label.configure(background='#121212',
                                                  borderwidth='0',
                                                  font='{Poppins} 10 {bold}',
                                                  foreground='#ffffff')
        self.Teacher_Phone_Number_label.configure(text='Phone Number')
        self.Teacher_Phone_Number_label.place(anchor='nw',
                                              x='390',
                                              y='115')

        self.Teacher_Gender_label = tk.Label(self)
        self.Teacher_Gender_label.configure(background='#121212',
                                            borderwidth='0',
                                            font='{Poppins} 10 {bold}',
                                            foreground='#ffffff')
        self.Teacher_Gender_label.configure(text='Gender')
        self.Teacher_Gender_label.place(anchor='nw',
                                        x='520',
                                        y='115')

        self.Teacher_Main_Subject_label = tk.Label(self)
        self.Teacher_Main_Subject_label.configure(background='#121212',
                                                  borderwidth='0',
                                                  font='{Poppins} 10 {bold}',
                                                  foreground='#ffffff')
        self.Teacher_Main_Subject_label.configure(text='Main Subject')
        self.Teacher_Main_Subject_label.place(anchor='nw',
                                              x='600',
                                              y='115')

        self.configure(background='#121212',
                       height='515',
                       width='791')

        self.place(anchor='nw',
                   x='0',
                   y='0')

    def goBackToTeacherHome(self):
        self.master.switch_frame(TeacherHome)

    def changeTeacherViewTheme(self):

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

        if self["background"] == "#121212":
            TeacherViewBackgroundColor = "#ffffff"
            TeacherViewForegroundColor = "#000000"

            self.configure(background=TeacherViewBackgroundColor)
            self.sty.map('Treeview', background=[('selected', '#4d4d4d'), ('focus', '#212121')])
            self.teacher_recodes.tag_configure("secondColor", background=TeacherViewBackgroundColor,
                                               font='{Poppins} 8 {bold}',
                                               foreground=TeacherViewForegroundColor)
            self.teacher_recodes.tag_configure("oneColor", background="#e6e6e6",
                                               font='{Poppins} 8 {bold}',
                                               foreground=TeacherViewForegroundColor)
            # self.teacher_view_theme_change_button  
            self.teacher_home_back_page_img_button.configure(background=TeacherViewBackgroundColor,
                                                             foreground=TeacherViewForegroundColor)
            self.Teacher_view_close_button.configure(background=TeacherViewBackgroundColor,
                                                     foreground=TeacherViewForegroundColor)
            self.View_Teacher_label.configure(background=TeacherViewBackgroundColor,
                                              foreground=TeacherViewForegroundColor)
            self.Teacher_ID_label.configure(background=TeacherViewBackgroundColor,
                                            foreground=TeacherViewForegroundColor)
            self.Teacher_First_Name_label.configure(background=TeacherViewBackgroundColor,
                                                    foreground=TeacherViewForegroundColor)
            self.Teacher_Second_Name_label.configure(background=TeacherViewBackgroundColor,
                                                     foreground=TeacherViewForegroundColor)
            self.Teacher_Age_label.configure(background=TeacherViewBackgroundColor,
                                             foreground=TeacherViewForegroundColor)
            self.Teacher_Phone_Number_label.configure(background=TeacherViewBackgroundColor,
                                                      foreground=TeacherViewForegroundColor)
            self.Teacher_Gender_label.configure(background=TeacherViewBackgroundColor,
                                                foreground=TeacherViewForegroundColor)
            self.Teacher_Main_Subject_label.configure(background=TeacherViewBackgroundColor,
                                                      foreground=TeacherViewForegroundColor)
            self.teacher_view_theme_change_button.configure(background=TeacherViewBackgroundColor,
                                                            foreground=TeacherViewForegroundColor,
                                                            image=self.img_lightThemeimg)
        else:
            DTeacherViewBackgroundColor = "#121212"
            DTeacherViewForegroundColor = "#ffffff"

            self.configure(background=DTeacherViewBackgroundColor)
            self.sty.map('Treeview', background=[('selected', '#3B3B3B'), ('focus', '#212121')])
            self.teacher_recodes.tag_configure("secondColor", background=DTeacherViewBackgroundColor,
                                               font='{Poppins} 8 {bold}',
                                               foreground="#c2c2c2")
            self.teacher_recodes.tag_configure("oneColor", background="#0a0a0a",
                                               font='{Poppins} 8 {bold}',
                                               foreground="#c2c2c2")
            # self.teacher_view_theme_change_button
            self.teacher_home_back_page_img_button.configure(background=DTeacherViewBackgroundColor,
                                                             foreground=DTeacherViewForegroundColor)
            self.Teacher_view_close_button.configure(background=DTeacherViewBackgroundColor,
                                                     foreground=DTeacherViewForegroundColor)
            self.View_Teacher_label.configure(background=DTeacherViewBackgroundColor,
                                              foreground=DTeacherViewForegroundColor)
            self.Teacher_ID_label.configure(background=DTeacherViewBackgroundColor,
                                            foreground=DTeacherViewForegroundColor)
            self.Teacher_First_Name_label.configure(background=DTeacherViewBackgroundColor,
                                                    foreground=DTeacherViewForegroundColor)
            self.Teacher_Second_Name_label.configure(background=DTeacherViewBackgroundColor,
                                                     foreground=DTeacherViewForegroundColor)
            self.Teacher_Age_label.configure(background=DTeacherViewBackgroundColor,
                                             foreground=DTeacherViewForegroundColor)
            self.Teacher_Phone_Number_label.configure(background=DTeacherViewBackgroundColor,
                                                      foreground=DTeacherViewForegroundColor)
            self.Teacher_Gender_label.configure(background=DTeacherViewBackgroundColor,
                                                foreground=DTeacherViewForegroundColor)
            self.Teacher_Main_Subject_label.configure(background=DTeacherViewBackgroundColor,
                                                      foreground=DTeacherViewForegroundColor)
            self.teacher_view_theme_change_button.configure(background=DTeacherViewBackgroundColor,
                                                            foreground=DTeacherViewForegroundColor,
                                                            image=self.img_DarkThemeimg)

