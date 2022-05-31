class DarkTeacherDelete(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        try:
            self.img_DarkThemeimg = tk.PhotoImage(file='DarkThemeimg.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "DarkThemeimg.png is missing")
        self.teacher_Delete_theme_change_button = tk.Button(self)
        self.teacher_Delete_theme_change_button.configure(activebackground=self.bgcolor,
                                                          activeforeground=self.bgcolor,
                                                          background=self.bgcolor,
                                                          borderwidth='0',
                                                          relief="flat",
                                                          overrelief="flat",
                                                          command=self.changeTeacherDeleteTheme)
        self.teacher_Delete_theme_change_button.configure(image=self.img_DarkThemeimg,
                                                          text='button2')
        self.teacher_Delete_theme_change_button.place(anchor='nw',
                                                      x='60',
                                                      y='10')
        self.Delete_Teacher_label = tk.Label(self)
        self.Delete_Teacher_label.configure(background=self.bgcolor,
                                            borderwidth='0',
                                            font='{Poppins} 28 {bold}',
                                            foreground=self.fgcolor)
        self.Delete_Teacher_label.configure(text='Delete Teacher')
        self.Delete_Teacher_label.place(anchor='nw',
                                        x='274',
                                        y='28')
        self.Delete_Teacher_back_page_img_button = tk.Button(self)

        try:
            self.img_BackPageIMG = tk.PhotoImage(file='BackPageIMG.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "BackPageIMG.png is missing")

        self.Delete_Teacher_back_page_img_button.configure(activebackground=self.bgcolor,
                                                           activeforeground=self.bgcolor,
                                                           background=self.bgcolor,
                                                           borderwidth='0',
                                                           command=lambda: master.switch_frame(DarkTeacherHome))
        self.Delete_Teacher_back_page_img_button.configure(image=self.img_BackPageIMG)
        self.Delete_Teacher_back_page_img_button.place(anchor='nw', x='15', y='15')
        self.Delete_Id_label = tk.Label(self)
        self.Delete_Id_label.configure(background=self.bgcolor,
                                       font='{Poppins} 17 {bold}',
                                       foreground=self.fgcolor,
                                       text='Delete ID')
        self.Delete_Id_label.place(anchor='nw',
                                   x='166',
                                   y='306')

        try:
            self.img_TeacherGoButton = tk.PhotoImage(file='Update_Go_button_img.png')
        except Exception as e:
            messagebox.showerror("Update_Go_button_img.png Missing")
            print(e)

        self.Delete_Go_button = tk.Button(self)
        self.Delete_Go_button.configure(background=self.bgcolor,
                                        activebackground=self.bgcolor,
                                        activeforeground=self.bgcolor,
                                        borderwidth='0',
                                        image=self.img_TeacherGoButton,
                                        relief='flat',
                                        command=self.DeleteGo)
        self.Delete_Go_button.place(anchor='nw',
                                    x='527',
                                    y='305')

        self.Delete_Id_bg_label = tk.Label(self)

        try:
            self.img_TeacheridbgEntery = tk.PhotoImage(file='Update_id_bg_IMG.png')
        except Exception as e:
            messagebox.showerror("TeacherAddButton.png Missing")
            print(e)

        self.Delete_Id_bg_label.configure(background=self.bgcolor,
                                          borderwidth='0',
                                          image=self.img_TeacheridbgEntery)
        self.Delete_Id_bg_label.place(anchor='nw',
                                      x='386',
                                      y='310')

        self.Delete_Id_entry = tk.Entry(self)
        self.Delete_Id_entry.configure(borderwidth='0')
        self.Delete_Id_entry.configure(font='{Poppins} 10 {bold}',
                                       insertwidth='1',
                                       relief='flat')
        self.Delete_Id_entry.place(anchor='nw',
                                   height='24',
                                   width='120',
                                   x='395',
                                   y='313')

        self.Deletesty = ttk.Style()
        self.Deletesty.configure('Treeview', rowheight=46, fieldbackground="#000000")
        self.Deletesty.map('Treeview', background=[('selected', '#3B3B3B'), ('focus', '#212121')])

        self.columns = ('ID',
                        'First name',
                        'Last name',
                        'Age',
                        'Phone Number',
                        'AdmissionNo',
                        'Subjects')

        self.Delete_Teacher_recodes = ttk.Treeview(height=1, columns=self.columns, show="tree")
        self.Delete_Teacher_recodes.configure(height=0)

        self.Delete_Teacher_recodes.column("ID", width=50)
        self.Delete_Teacher_recodes.column("First name", width=150)
        self.Delete_Teacher_recodes.column("Last name", width=130)
        self.Delete_Teacher_recodes.column("Age", width=50)
        self.Delete_Teacher_recodes.column("Phone Number", width=130)
        self.Delete_Teacher_recodes.column("AdmissionNo", width=100)
        self.Delete_Teacher_recodes.column("Subjects", width=220)

        self.configure(background=self.bgcolor,
                       height='515',
                       takefocus=False,
                       width='791')
        self.place(anchor='nw',
                   x='0',
                   y='0')

    def DeleteGo(self):
        global DeleteId

        DeleteId = self.Delete_Id_entry.get()

        if DeleteId == "":
            self.master.switch_frame(DarkTeacherDelete)
        else:
            try:
                int(DeleteId)
            except:
                # messagebox.showerror("Type Error", "You Can Only Type Numbers For ID ")
                self.Delete_Id_entry.delete(0, 'end')
                self.Delete_Teacher_recodes.configure(height=0)
                DeleteId = ""
                self.master.switch_frame(DarkTeacherDelete)
            self.conn = mysql.connector.connect(user="root",
                                                password="",
                                                database="eduway")
            self.connetc = self.conn.cursor()

            self.connetc.execute(f"SELECT * FROM teacher WHERE id = {DeleteId}")
            self.deleteRecode = self.connetc.fetchall()

            self.conn.commit()

            self.Delete_Teacher_ID_label = tk.Label(self)
            self.Delete_Teacher_ID_label.configure(background=self.bgcolor,
                                                   borderwidth='0',
                                                   font='{Poppins} 10 {bold}',
                                                   foreground=self.fgcolor)
            self.Delete_Teacher_ID_label.configure(text='ID')
            self.Delete_Teacher_ID_label.place(anchor='nw',
                                               x='16',
                                               y='265')

            self.Delete_Teacher_First_Name_label = tk.Label(self)
            self.Delete_Teacher_First_Name_label.configure(background=self.bgcolor,
                                                           borderwidth='0',
                                                           font='{Poppins} 10 {bold}',
                                                           foreground=self.fgcolor)
            self.Delete_Teacher_First_Name_label.configure(text='First Name')
            self.Delete_Teacher_First_Name_label.place(anchor='nw',
                                                       x='55',
                                                       y='265')

            self.Delete_Teacher_Second_Name_label = tk.Label(self)
            self.Delete_Teacher_Second_Name_label.configure(background=self.bgcolor,
                                                            borderwidth='0',
                                                            font='{Poppins} 10 {bold}',
                                                            foreground=self.fgcolor)
            self.Delete_Teacher_Second_Name_label.configure(text='Second Name')
            self.Delete_Teacher_Second_Name_label.place(anchor='nw',
                                                        x='180',
                                                        y='265')

            self.Delete_Teacher_Age_label = tk.Label(self)
            self.Delete_Teacher_Age_label.configure(background=self.bgcolor,
                                                    borderwidth='0',
                                                    font='{Poppins} 10 {bold}',
                                                    foreground=self.fgcolor)
            self.Delete_Teacher_Age_label.configure(text='Age')
            self.Delete_Teacher_Age_label.place(anchor='nw',
                                                x='340',
                                                y='265')

            self.Delete_Teacher_Phone_Number_label = tk.Label(self)
            self.Delete_Teacher_Phone_Number_label.configure(background=self.bgcolor,
                                                             borderwidth='0',
                                                             font='{Poppins} 10 {bold}',
                                                             foreground=self.fgcolor)
            self.Delete_Teacher_Phone_Number_label.configure(text='Phone Number')
            self.Delete_Teacher_Phone_Number_label.place(anchor='nw',
                                                         x='390',
                                                         y='265')

            self.Delete_Teacher_Gender_label = tk.Label(self)
            self.Delete_Teacher_Gender_label.configure(background=self.bgcolor,
                                                       borderwidth='0',
                                                       font='{Poppins} 10 {bold}',
                                                       foreground=self.fgcolor)
            self.Delete_Teacher_Gender_label.configure(text='Gender')
            self.Delete_Teacher_Gender_label.place(anchor='nw',
                                                   x='520',
                                                   y='265')

            self.Delete_Teacher_Main_Subject_label = tk.Label(self)
            self.Delete_Teacher_Main_Subject_label.configure(background=self.bgcolor,
                                                             borderwidth='0',
                                                             font='{Poppins} 10 {bold}',
                                                             foreground=self.fgcolor)
            self.Delete_Teacher_Main_Subject_label.configure(text='Main Subject')
            self.Delete_Teacher_Main_Subject_label.place(anchor='nw',
                                                         x='600',
                                                         y='265')
            try:
                self.img_TeacherAddButton = tk.PhotoImage(file='Teacher_Delete.png')
            except Exception as e:
                messagebox.showerror("Teacher_Delete.png Missing")
                print(e)

            self.Delete_teachet_button = tk.Button(self)
            self.Delete_teachet_button.configure(background=self.bgcolor,
                                                 activebackground=self.bgcolor,
                                                 activeforeground=self.bgcolor,
                                                 borderwidth='0',
                                                 image=self.img_TeacherAddButton,
                                                 relief='flat',
                                                 command=self.onClickDeleteRecodes)

            self.Delete_teachet_button.place(anchor='nw',
                                             x='412',
                                             y='448')
            if self.deleteRecode == []:
                # messagebox.showerror("Search Error", "ID You Entered is Already Deleted or Cannot Find That Id ")
                self.master.switch_frame(DarkTeacherDelete)

            self.Delete_Teacher_recodes.tag_configure("oneColorStudent", background=self.bgcolor,
                                                      font='{Poppins} 8 {bold}',
                                                      foreground="#c2c2c2")
            self.Delete_Teacher_recodes.configure(height=1)
            global count
            self.deleteRecodes()
            for record in self.deleteRecode:
                self.Delete_Teacher_recodes.insert(parent="", index='end', iid=0, values=(
                    record[0], record[1], record[2], record[4], "0" + str(record[3]), record[5], record[6]),
                                                   tags=("oneColorStudent"))

            self.Delete_Id_label.place(anchor='nw',
                                       x='166',
                                       y='156')
            self.Delete_Go_button.place(anchor='nw',
                                        x='527',
                                        y='155')
            self.Delete_Id_bg_label.place(anchor='nw',
                                          x='386',
                                          y='160')
            self.Delete_Id_entry.place(anchor='nw',
                                       height='24',
                                       width='120',
                                       x='395',
                                       y='163')
            self.Delete_Teacher_recodes.place(anchor='nw', x='0', y='300', relx="-0.24", bordermode='ignore')
            self.Delete_Id_entry.delete(0, "end")
            self.connetc.close()
            self.conn.close()

    def deleteRecodes(self):
        for item in self.Delete_Teacher_recodes.get_children():
            self.Delete_Teacher_recodes.delete(item)

    def onClickDeleteRecodes(self):
        self.conn = mysql.connector.connect(user="root",
                                            password="",
                                            database="eduway")
        self.connetc = self.conn.cursor()
        self.connetc.execute(f"DELETE FROM teacher WHERE id = {DeleteId}")
        self.conn.commit()
        self.connetc.close()
        self.conn.close()

    def changeTeacherDeleteTheme(self):
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

        if self["background"] == self.bgcolor:
            self.TeacherDeleteBGColor = self.fgcolor
            self.TeacherDeleteFGColor = "#000000"
            self.configure(background=self.TeacherDeleteBGColor)
            self.teacher_Delete_theme_change_button.configure(background=self.TeacherDeleteBGColor,
                                                              foreground=self.TeacherDeleteFGColor,
                                                              activeforeground=self.TeacherDeleteBGColor,
                                                              activebackground=self.TeacherDeleteBGColor,
                                                              image=self.img_lightThemeimg)

            self.Delete_Teacher_label.configure(background=self.TeacherDeleteBGColor,
                                                foreground=self.TeacherDeleteFGColor)
            self.Delete_Teacher_back_page_img_button.configure(background=self.TeacherDeleteBGColor,
                                                               foreground=self.TeacherDeleteFGColor,
                                                               activeforeground=self.TeacherDeleteBGColor,
                                                               activebackground=self.TeacherDeleteBGColor)
            self.Delete_Id_label.configure(background=self.TeacherDeleteBGColor,
                                           foreground=self.TeacherDeleteFGColor)

            self.Delete_Go_button.configure(background=self.TeacherDeleteBGColor,
                                            foreground=self.TeacherDeleteFGColor,
                                            activeforeground=self.TeacherDeleteBGColor,
                                            activebackground=self.TeacherDeleteBGColor)
            self.Delete_Id_bg_label.configure(background=self.TeacherDeleteBGColor,
                                              foreground=self.TeacherDeleteFGColor)

            self.Delete_Teacher_ID_label.configure(background=self.TeacherDeleteBGColor,
                                                   foreground=self.TeacherDeleteFGColor)

            self.Delete_Teacher_First_Name_label.configure(background=self.TeacherDeleteBGColor,
                                                           foreground=self.TeacherDeleteFGColor)
            self.Delete_Teacher_Second_Name_label.configure(background=self.TeacherDeleteBGColor,
                                                            foreground=self.TeacherDeleteFGColor)
            self.Delete_Teacher_Age_label.configure(background=self.TeacherDeleteBGColor,
                                                    foreground=self.TeacherDeleteFGColor)
            self.Delete_Teacher_Phone_Number_label.configure(background=self.TeacherDeleteBGColor,
                                                             foreground=self.TeacherDeleteFGColor)
            self.Delete_Teacher_Gender_label.configure(background=self.TeacherDeleteBGColor,
                                                       foreground=self.TeacherDeleteFGColor)

            self.Delete_Teacher_Main_Subject_label.configure(background=self.TeacherDeleteBGColor,
                                                             foreground=self.TeacherDeleteFGColor)

            self.Delete_teachet_button.configure(background=self.TeacherDeleteBGColor,
                                                 foreground=self.TeacherDeleteFGColor,
                                                 activeforeground=self.TeacherDeleteBGColor,
                                                 activebackground=self.TeacherDeleteBGColor)

            self.Delete_Teacher_recodes.tag_configure("oneColorStudent", background=self.fgcolor,
                                                      font='{Poppins} 8 {bold}',
                                                      foreground="#000000")
        else:
            self.DTeacherDeleteBGColor = self.bgcolor
            self.DTeacherDeleteFGColor = self.fgcolor
            self.configure(background=self.DTeacherDeleteBGColor)
            self.teacher_Delete_theme_change_button.configure(background=self.DTeacherDeleteBGColor,
                                                              foreground=self.DTeacherDeleteFGColor,
                                                              activeforeground=self.DTeacherDeleteBGColor,
                                                              activebackground=self.DTeacherDeleteBGColor,
                                                              image=self.img_DarkThemeimg)

            self.Delete_Teacher_label.configure(background=self.DTeacherDeleteBGColor,
                                                foreground=self.DTeacherDeleteFGColor)
            self.Delete_Teacher_back_page_img_button.configure(background=self.DTeacherDeleteBGColor,
                                                               foreground=self.DTeacherDeleteFGColor,
                                                               activeforeground=self.DTeacherDeleteBGColor,
                                                               activebackground=self.DTeacherDeleteBGColor)
            self.Delete_Id_label.configure(background=self.DTeacherDeleteBGColor,
                                           foreground=self.DTeacherDeleteFGColor)

            self.Delete_Go_button.configure(background=self.DTeacherDeleteBGColor,
                                            foreground=self.DTeacherDeleteFGColor,
                                            activeforeground=self.DTeacherDeleteBGColor,
                                            activebackground=self.DTeacherDeleteBGColor)
            self.Delete_Id_bg_label.configure(background=self.DTeacherDeleteBGColor,
                                              foreground=self.DTeacherDeleteFGColor)

            self.Delete_Teacher_ID_label.configure(background=self.DTeacherDeleteBGColor,
                                                   foreground=self.DTeacherDeleteFGColor)

            self.Delete_Teacher_First_Name_label.configure(background=self.DTeacherDeleteBGColor,
                                                           foreground=self.DTeacherDeleteFGColor)
            self.Delete_Teacher_Second_Name_label.configure(background=self.DTeacherDeleteBGColor,
                                                            foreground=self.DTeacherDeleteFGColor)
            self.Delete_Teacher_Age_label.configure(background=self.DTeacherDeleteBGColor,
                                                    foreground=self.DTeacherDeleteFGColor)
            self.Delete_Teacher_Phone_Number_label.configure(background=self.DTeacherDeleteBGColor,
                                                             foreground=self.DTeacherDeleteFGColor)
            self.Delete_Teacher_Gender_label.configure(background=self.DTeacherDeleteBGColor,
                                                       foreground=self.DTeacherDeleteFGColor)

            self.Delete_Teacher_Main_Subject_label.configure(background=self.DTeacherDeleteBGColor,
                                                             foreground=self.DTeacherDeleteFGColor)

            self.Delete_teachet_button.configure(background=self.DTeacherDeleteBGColor,
                                                 foreground=self.DTeacherDeleteFGColor,
                                                 activeforeground=self.DTeacherDeleteBGColor,
                                                 activebackground=self.DTeacherDeleteBGColor)

            self.Delete_Teacher_recodes.tag_configure("oneColorStudent", background=self.bgcolor,
                                                      font='{Poppins} 8 {bold}',
                                                      foreground=self.fgcolor)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

