class StudentUpdate(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.Update_Student__element_img_label = tk.Label(self)

        try:
            self.img_Element_1_img_label = tk.PhotoImage(file='Element_1_img_label.png')
        except Exception as e:
            messagebox.showerror("Element_1_img_label.png' Missing")
            print(e)

        self.Update_Student__element_img_label.configure(background=self.bgcolor,
                                                         image=self.img_Element_1_img_label)
        self.Update_Student__element_img_label.place(anchor='nw',
                                                     x='0',
                                                     y='0')

        try:
            self.img_StudentRegiusterEntery = tk.PhotoImage(file='TeacherRegiusterEntery.png')
        except Exception as e:
            messagebox.showerror("TeacherAddButton.png Missing")
            print(e)

        try:
            self.img_StudentidbgEntery = tk.PhotoImage(file='Update_id_bg_IMG.png')
        except Exception as e:
            messagebox.showerror("Update_id_bg_IMG.png")
            print(e)
        self.Update_Student__Id_bg_label = tk.Label(self)
        self.Update_Student__Id_bg_label.configure(background=self.bgcolor,
                                                   borderwidth='0',
                                                   image=self.img_StudentidbgEntery)
        self.Update_Student__Id_bg_label.place(anchor='nw',
                                               x='386',
                                               y='100')

        self.Update_Student_First_name_Entry_bg_label = tk.Label(self)

        self.Update_Student_First_name_Entry_bg_label.configure(background=self.bgcolor,
                                                                borderwidth='0',
                                                                image=self.img_StudentRegiusterEntery)
        self.Update_Student_First_name_Entry_bg_label.place(anchor='nw',
                                                            x='386',
                                                            y='146')

        self.Update_Student_Last_name_Entry_bg_label = tk.Label(self)
        self.Update_Student_Last_name_Entry_bg_label.configure(background=self.bgcolor,
                                                               borderwidth='0',
                                                               image=self.img_StudentRegiusterEntery)
        self.Update_Student_Last_name_Entry_bg_label.place(anchor='nw',
                                                           x='386',
                                                           y='196')

        self.Update_Student_age_Entry_bg_label = tk.Label(self)
        self.Update_Student_age_Entry_bg_label.configure(background=self.bgcolor,
                                                         borderwidth='0',
                                                         image=self.img_StudentRegiusterEntery)
        self.Update_Student_age_Entry_bg_label.place(anchor='nw',
                                                     x='386',
                                                     y='246')

        self.Update_Student_phone_number_Entry_bg_label = tk.Label(self)
        self.Update_Student_phone_number_Entry_bg_label.configure(background=self.bgcolor,
                                                                  borderwidth='0',
                                                                  image=self.img_StudentRegiusterEntery)
        self.Update_Student_phone_number_Entry_bg_label.place(anchor='nw',
                                                              x='386',
                                                              y='290')

        self.Update_Student_gender_Entry_bg_label = tk.Label(self)
        self.Update_Student_gender_Entry_bg_label.configure(background=self.bgcolor,
                                                            borderwidth='0',
                                                            image=self.img_StudentRegiusterEntery)
        self.Update_Student_gender_Entry_bg_label.place(anchor='nw',
                                                        x='386',
                                                        y='340')

        self.Update_Student_subject_Entry_bg_label = tk.Label(self)
        self.Update_Student_subject_Entry_bg_label.configure(background=self.bgcolor,
                                                             borderwidth='0',
                                                             image=self.img_StudentRegiusterEntery)
        self.Update_Student_subject_Entry_bg_label.place(anchor='nw',
                                                         x='386',
                                                         y='390')

        self.Student_Update_Id_entry = tk.Entry(self)
        self.Student_Update_Id_entry.configure(borderwidth='0')
        self.Student_Update_Id_entry.configure(font='{Poppins} 10 {bold}',
                                               insertwidth='1',
                                               relief='flat')
        self.Student_Update_Id_entry.place(anchor='nw',
                                           height='24',
                                           width='120',
                                           x='395',
                                           y='103  ')

        self.Student_Update_Id_label = tk.Label(self)
        self.Student_Update_Id_label.configure(background=self.bgcolor,
                                               font='{Poppins} 17 {bold}',
                                               foreground=self.fgcolor,
                                               text='ChangeID')
        self.Student_Update_Id_label.place(anchor='nw',
                                           x='166',
                                           y='96')

        self.Student_Update_first_name_entry = tk.Entry(self)
        self.Student_Update_first_name_entry.configure(borderwidth='0')
        self.Student_Update_first_name_entry.configure(font='{Poppins} 10 {bold}',
                                                       insertwidth='1',
                                                       relief='flat')
        self.Student_Update_first_name_entry.place(anchor='nw',
                                                   height='24',
                                                   width='229',
                                                   x='395',
                                                   y='149')

        self.Student_Update_first_name_label = tk.Label(self)
        self.Student_Update_first_name_label.configure(background=self.bgcolor,
                                                       font='{Poppins} 17 {bold}',
                                                       foreground=self.fgcolor,
                                                       text='First Name')
        self.Student_Update_first_name_label.place(anchor='nw',
                                                   x='166',
                                                   y='146')

        self.Student_Update_last_name_entry = tk.Entry(self)
        self.Student_Update_last_name_entry.configure(borderwidth='0')
        self.Student_Update_last_name_entry.configure(font='{Poppins} 10 {bold}',
                                                      insertwidth='1',
                                                      relief='flat')
        self.Student_Update_last_name_entry.place(anchor='nw',
                                                  height='24',
                                                  width='229',
                                                  x='397',
                                                  y='199')

        self.Student_Update_last_name_label = tk.Label(self)
        self.Student_Update_last_name_label.configure(background=self.bgcolor,
                                                      font='{Poppins} 17 {bold}',
                                                      foreground=self.fgcolor,
                                                      text='Last Name')
        self.Student_Update_last_name_label.place(anchor='nw',
                                                  x='166',
                                                  y='198')

        self.Student_Update_phone_number_entry = tk.Entry(self)
        self.Student_Update_phone_number_entry.configure(borderwidth='0')
        self.Student_Update_phone_number_entry.configure(font='{Poppins} 10 {bold}',
                                                         insertwidth='1',
                                                         relief='flat')
        self.Student_Update_phone_number_entry.place(anchor='nw',
                                                     height='24',
                                                     width='229',
                                                     x='397',
                                                     y='293')

        self.Student_Update_phone_number_label = tk.Label(self)
        self.Student_Update_phone_number_label.configure(background=self.bgcolor,
                                                         font='{Poppins} 17 {bold}',
                                                         foreground=self.fgcolor,
                                                         text='Phone number')
        self.Student_Update_phone_number_label.place(anchor='nw',
                                                     x='166',
                                                     y='289')

        self.Student_Update_age_entry = tk.Entry(self)
        self.Student_Update_age_entry.configure(borderwidth='0')
        self.Student_Update_age_entry.configure(font='{Poppins} 10 {bold}',
                                                insertwidth='1',
                                                relief='flat')
        self.Student_Update_age_entry.place(anchor='nw',
                                            height='24',
                                            width='229',
                                            x='395',
                                            y='249')

        self.Student_Update_age_label = tk.Label(self)
        self.Student_Update_age_label.configure(background=self.bgcolor,
                                                font='{Poppins} 17 {bold}',
                                                foreground=self.fgcolor,
                                                text='Age')
        self.Student_Update_age_label.place(anchor='nw',
                                            x='166',
                                            y='239')

        self.Student_Update_gender_label = tk.Label(self)
        self.Student_Update_gender_label.configure(background=self.bgcolor,
                                                   font='{Poppins} 17 {bold}',
                                                   foreground=self.fgcolor,
                                                   text='AdmissionNo')
        self.Student_Update_gender_label.place(anchor='nw',
                                               x='166',
                                               y='331')

        self.Student_Update_gender_entry = tk.Entry(self)
        self.Student_Update_gender_entry.configure(borderwidth="0")
        self.Student_Update_gender_entry.configure(font='{Poppins} 10 {bold}',
                                                   insertwidth='1',
                                                   relief='flat')
        self.Student_Update_gender_entry.place(anchor='nw',
                                               height='24',
                                               width='229',
                                               x='395',
                                               y='343')

        self.Student_Update_subects_label = tk.Label(self)
        self.Student_Update_subects_label.configure(background=self.bgcolor,
                                                    font='{Poppins} 17 {bold}',
                                                    foreground=self.fgcolor,
                                                    text='MaIn Subject')
        self.Student_Update_subects_label.place(anchor='nw',
                                                x='166',
                                                y='389')

        self.Student_Update_subject_entry = tk.Entry(self)
        self.Student_Update_subject_entry.configure(borderwidth="0")
        self.Student_Update_subject_entry.configure(font='{Poppins} 10 {bold}',
                                                    insertwidth='1',
                                                    relief='flat')
        self.Student_Update_subject_entry.place(anchor='nw',
                                                height='24',
                                                width='229',
                                                x='395',
                                                y='393')

        try:
            self.img_StudentUpdateButton = tk.PhotoImage(file='Teacher_Update_Button.png')
        except Exception as e:
            messagebox.showerror("Update_Student_Btn_img.png Missing")
            print(e)

        self.Student_Update_Update_teachet_button = tk.Button(self)
        self.Student_Update_Update_teachet_button.configure(background=self.bgcolor,
                                                            activebackground=self.bgcolor,
                                                            activeforeground=self.bgcolor,
                                                            borderwidth='0',
                                                            image=self.img_StudentUpdateButton,
                                                            relief='flat',
                                                            command=self.clickUpdate)
        self.Student_Update_Update_teachet_button.place(anchor='nw',
                                                        x='412',
                                                        y='448')

        try:
            self.img_StudentGoButton = tk.PhotoImage(file='Update_Go_button_img.png')
        except Exception as e:
            messagebox.showerror("Update_Go_button_img.png Missing")
            print(e)

        self.Student_Update_Update_Go_button = tk.Button(self)
        self.Student_Update_Update_Go_button.configure(background=self.bgcolor,
                                                       activebackground=self.bgcolor,
                                                       activeforeground=self.bgcolor,
                                                       borderwidth='0',
                                                       image=self.img_StudentGoButton,
                                                       relief='flat',
                                                       command=self.clickGo)
        self.Student_Update_Update_Go_button.place(anchor='nw',
                                                   x='527',
                                                   y='95')

        try:
            self.img_img4 = tk.PhotoImage(file='img4.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "img_img4.png is missing")
        self.Student_Update_Student_registation_close_button = tk.Button(self)
        self.Student_Update_Student_registation_close_button.configure(activebackground=self.bgcolor,
                                                                       activeforeground=self.bgcolor,
                                                                       background=self.bgcolor,
                                                                       borderwidth='0')
        self.Student_Update_Student_registation_close_button.configure(cursor='hand2',
                                                                       foreground=self.bgcolor,
                                                                       highlightbackground=self.bgcolor,
                                                                       highlightcolor=self.bgcolor)
        self.Student_Update_Student_registation_close_button.configure(highlightthickness='1',
                                                                       image=self.img_img4,
                                                                       relief='flat',
                                                                       command=self.master.on_close)
        self.Student_Update_Student_registation_close_button.place(anchor='nw',
                                                                   x='760',
                                                                   y='8')

        self.Update_Student_label = tk.Label(self)
        self.Update_Student_label.configure(background=self.bgcolor,
                                            borderwidth='0',
                                            font='{Poppins} 28 {bold}',
                                            foreground=self.fgcolor)
        self.Update_Student_label.configure(text='Update Student')
        self.Update_Student_label.place(anchor='nw',
                                        x='274',
                                        y='28')

        self.Student_Update_back_page_img_button = tk.Button(self)

        try:
            self.img_BackPageIMG = tk.PhotoImage(file='BackPageIMG.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "BackPageIMG.png is missing")

        self.Student_Update_back_page_img_button.configure(activebackground=self.bgcolor,
                                                           activeforeground=self.bgcolor,
                                                           background=self.bgcolor,
                                                           borderwidth='0',
                                                           command=self.goBackToStudentHome)
        self.Student_Update_back_page_img_button.configure(image=self.img_BackPageIMG)
        self.Student_Update_back_page_img_button.place(anchor='nw', x='15', y='15')

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
                                                                              command=self.changeStudentUpdateTheme)
        self.Student_Update_Student_registation_theme_change_button.configure(image=self.img_DarkThemeimg,
                                                                              text='button2')
        self.Student_Update_Student_registation_theme_change_button.place(anchor='nw',
                                                                          x='60',
                                                                          y='10')
        self.configure(background=self.bgcolor,
                       borderwidth='0',
                       height='515',
                       width='791')
        self.pack(fill='both',
                  side='top')

    def clickGo(self):
#####################################################Clear#######################################################
        self.Clearerrors()
        self.ClearCommited()
####################################################Clear########################################################

        global Student_changeId

        Student_changeId = self.Student_Update_Id_entry.get()

        if Student_changeId == "":
            # messagebox.showerror("ID Name Error", "ID Need To Enter ID")
            
            ##########################clear Error ########################################################
            try:
                self.clearEmptyChangeIdError()
                self.clearStudentUpdate()
                        #####################################################Clear#######################################################
                self.Clearerrors()
                self.ClearCommited()
        ####################################################Clear########################################################

            except:
                pass
            #############################################################################################

            #############################Place The Error###############################
            self.EmptyChangeIdError()
            ####################################################################################
        
        else:
            self.clearStudentUpdate()
            ##########################clear Error ########################################################
            try:
                self.clearEmptyChangeIdError()
            except:
                pass
            #############################################################################################
            
            try:
                int(Student_changeId)
                try:
                    self.clearChangeIdTypeError()
                except:
                    pass
            except:
                # messagebox.showerror("ID Name Error", "ID Need To Enter Numbers")
                #######################################Place Error################################################
                self.ChangeIdTypoeError()
                ####################################################################################################
            try:
                self.clearChangeIdTypeError()
            except:
                pass
            try:
                ############Conectdb#############################
                self.connectDB()
                #########################################
            except:
                ##############################DB ERROR#######################
                self.DatabaseNotConnectedError()
                ##############################################################

            self.connetc = self.conn.cursor()
            #########################Select Id#################################
            self.SelectChangedId()
            ##############################################################
            self.connetc.close()
            self.conn.close()
            if Student_changeId =="":
                self.EmptyChangeIdError()


    def changeStudentUpdateTheme(self):
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

        if self.Student_Update_back_page_img_button["background"] == "#121212":
            self.Update_StudentRegistationBGColor = self.fgcolor
            self.Update_StudentRegistationFGColor = "#000000"
            self.configure(background=self.Update_StudentRegistationBGColor)
            self.Update_Student__Id_bg_label.configure(background=self.Update_StudentRegistationBGColor,
                                                       foreground=self.Update_StudentRegistationFGColor)
            self.Student_Update_Id_label.configure(background=self.Update_StudentRegistationBGColor,
                                                   foreground=self.Update_StudentRegistationFGColor)

            self.Student_Update_Update_Go_button.configure(background=self.Update_StudentRegistationBGColor,
                                                           foreground=self.Update_StudentRegistationFGColor,
                                                           activebackground=self.Update_StudentRegistationBGColor,
                                                           activeforeground=self.Update_StudentRegistationBGColor)
            self.Update_Student__element_img_label.configure(background=self.Update_StudentRegistationBGColor,
                                                             foreground=self.Update_StudentRegistationFGColor)
            self.Update_Student_First_name_Entry_bg_label.configure(background=self.Update_StudentRegistationBGColor,
                                                                    foreground=self.Update_StudentRegistationFGColor)
            self.Update_Student_Last_name_Entry_bg_label.configure(background=self.Update_StudentRegistationBGColor,
                                                                   foreground=self.Update_StudentRegistationFGColor)
            self.Update_Student_age_Entry_bg_label.configure(background=self.Update_StudentRegistationBGColor,
                                                             foreground=self.Update_StudentRegistationFGColor)
            self.Update_Student_phone_number_Entry_bg_label.configure(background=self.Update_StudentRegistationBGColor,
                                                                      foreground=self.Update_StudentRegistationFGColor)
            self.Update_Student_phone_number_Entry_bg_label.configure(background=self.Update_StudentRegistationBGColor,
                                                                      foreground=self.Update_StudentRegistationFGColor)
            self.Update_Student_gender_Entry_bg_label.configure(background=self.Update_StudentRegistationBGColor,
                                                                foreground=self.Update_StudentRegistationFGColor)
            self.Update_Student_subject_Entry_bg_label.configure(background=self.Update_StudentRegistationBGColor,
                                                                 foreground=self.Update_StudentRegistationFGColor)
            self.Student_Update_first_name_entry.configure(background=self.Update_StudentRegistationBGColor,
                                                           foreground=self.Update_StudentRegistationFGColor)
            self.Student_Update_first_name_label.configure(background=self.Update_StudentRegistationBGColor,
                                                           foreground=self.Update_StudentRegistationFGColor)
            self.Student_Update_last_name_entry.configure(background=self.Update_StudentRegistationBGColor,
                                                          foreground=self.Update_StudentRegistationFGColor)
            self.Student_Update_last_name_label.configure(background=self.Update_StudentRegistationBGColor,
                                                          foreground=self.Update_StudentRegistationFGColor)
            self.Student_Update_phone_number_entry.configure(background=self.Update_StudentRegistationBGColor,
                                                             foreground=self.Update_StudentRegistationFGColor)
            self.Student_Update_phone_number_label.configure(background=self.Update_StudentRegistationBGColor,
                                                             foreground=self.Update_StudentRegistationFGColor)
            self.Student_Update_age_entry.configure(background=self.Update_StudentRegistationBGColor,
                                                    foreground=self.Update_StudentRegistationFGColor)
            self.Student_Update_age_label.configure(background=self.Update_StudentRegistationBGColor,
                                                    foreground=self.Update_StudentRegistationFGColor)
            self.Student_Update_gender_entry.configure(background=self.Update_StudentRegistationBGColor,
                                                       foreground=self.Update_StudentRegistationFGColor)
            self.Student_Update_gender_label.configure(background=self.Update_StudentRegistationBGColor,
                                                       foreground=self.Update_StudentRegistationFGColor)
            self.Student_Update_subject_entry.configure(background=self.Update_StudentRegistationBGColor,
                                                        foreground=self.Update_StudentRegistationFGColor)
            self.Student_Update_subects_label.configure(background=self.Update_StudentRegistationBGColor,
                                                        foreground=self.Update_StudentRegistationFGColor)
            self.Student_Update_Update_teachet_button.configure(background=self.Update_StudentRegistationBGColor,
                                                                foreground=self.Update_StudentRegistationFGColor,
                                                                activebackground=self.Update_StudentRegistationBGColor,
                                                                activeforeground=self.Update_StudentRegistationBGColor)
            self.Student_Update_Student_registation_close_button.configure(
                background=self.Update_StudentRegistationBGColor,
                foreground=self.Update_StudentRegistationFGColor)
            self.Update_Student_label.configure(background=self.Update_StudentRegistationBGColor,
                                                foreground=self.Update_StudentRegistationFGColor)
            self.Student_Update_back_page_img_button.configure(background=self.Update_StudentRegistationBGColor,
                                                               foreground=self.Update_StudentRegistationFGColor,
                                                               activebackground=self.Update_StudentRegistationBGColor,
                                                               activeforeground=self.Update_StudentRegistationBGColor)
            self.Student_Update_Student_registation_theme_change_button.configure(
                background=self.Update_StudentRegistationBGColor,
                foreground=self.Update_StudentRegistationFGColor,
                activebackground=self.Update_StudentRegistationBGColor,
                activeforeground=self.Update_StudentRegistationBGColor,
                image=self.img_lightThemeimg)
            self.Clearerrors()
            self.ClearCommited()
    ####################################################Clear########################################################

    #*******************************************************************************************************************
    #########################################Create variabels###########################################################
            #^^^^^^This is All variabels

            Student_Update_first_name = self.Student_Update_first_name_entry.get()
            
            Student_Update_last_name = self.Student_Update_last_name_entry.get()
            
            Student_Update_phone_number = self.Student_Update_phone_number_entry.get()
            
            Student_Update_age = self.Student_Update_age_entry.get()
            
            Student_Update_gender = self.Student_Update_gender_entry.get()
            
            Student_Update_subjects = self.Student_Update_subject_entry.get()
            if self.Student_Update_Id_entry.get() == "":
                self.clickGo()
            else:
                if Student_Update_first_name == "" or Student_Update_last_name == "" or Student_Update_phone_number == "" or Student_Update_age == "" or Student_Update_gender == "" or Student_Update_subjects == "":
                    # messagebox.showerror("insert status", "All Fields Are Required")
                    ##############################Clear All Erorr##################################
                    try:
                        self.Clearerrors()
                    except:
                        pass
                    #################################Distroy Student First Name########################
                    #################################Place The Erorr################################### 
                    self.AllFildsRequiredErorrDestroy() 
                    try:          
                        self.WAllFildsRequiredErorr()
                    except:
                        pass
                else:
                                ################################Distroy All Fields Erore#####################
                    self.AllFildsRequiredErorrDestroy()
                    ##################################Student First Name Lenth Check#############

                    if len(Student_Update_first_name) > 50:
                        # messagebox.showerror("First Name Error", "Your Name Is Too Long")
                        ###################################Distroy Studetn_First_Name_No_error_label#####################
                        self.WFirstNameErorr()

                        
                    else:
                        # self.FirstNameNoErorr()
                        
                        ############################Distroy First name Error##################################
                        try:
                            self.WStudetn_First_Name_error_label.destroy()
                        except:
                            pass

                        if len(Student_Update_last_name) > 50:
                            # messagebox.showerror("Second Name Error", "Your Name Is Too Long")
                            #####################################Distroy Studetn_Last_Name_No_error_label###############
                            try:
                                self.WLastNameError()
                            except:
                                pass
                        else:
                                ####################################Distroy Last Name Error#################################
                            try:
                                self.ClearLastNameError()
                            except:
                                pass
                            # self.NoLastNameError()

                            Student_Update_last_name.capitalize()
                            if Student_Update_first_name == Student_Update_last_name:
                                # messagebox.showerror("Copied Name Error", "Your First Name And Secont Name Is Duplicated")
                                ###############################Clear LAST NAME#######################
                                try:
                                    self.ClearNoLastNameError()
                                except:
                                    pass
                                ################################Add Duplicated Error#################
                                try:
                                    self.WNameDuplicatedErorr()
                                except:
                                    pass


                            else:
                                    #############################Clear Duplicate error########################
                                try: 
                                    self.ClearNameDuplicatedErorr()
                                except:
                                    pass
                                # self.NoDuplicateNameError()

                                    ################################Numeber Lenth Check########################################

                                if len(Student_Update_phone_number) != 10:
                                    # messagebox.showerror("Phone Number Error", "You Can Add Only 10 Digit number")
                                        ##################################Distroy Number No Eror################# 
                                    try:                         
                                        self.clearAllPhoneErors()
                                    except:
                                        pass

                                    ##################################PHONE NUMBER LENTH ERROR#####################
                                    try:
                                        self.WPhoneNumberLenthErorr()
                                    except:
                                        pass

        ###################################################Distroy Studetn_lenth_Phone_number_error_label############
                                else:
                                        ###############################Clear phone number lenth erorr####################
                                    try:
                                        self.ClearPhoneNumberLenthErorr()
                                    except:
                                        pass

                                    try:
                                        int(Student_Update_phone_number)
                                    except Exception as e:
                                        pass

                                    if int(Student_Update_phone_number[0]) != 0:
                                        # messagebox.showerror("Type Error", "This is Not Phone Number")
                                            ######################################################Distroy All Error##################################
                                        try:
                                            self.clearAllPhoneErors()
                                        except:
                                            pass
        #####################################################Place Studetn_int_Phone_number_error_label####################
                                        try:
                                            self.WPhoneNumberTypeErorr()
                                        except:
                                            pass
                                    else:
                                            
        ####################################################Distroy Studetn_int_Phone_number_error_label ##################
                                        try:
                                            self.clearAllPhoneErors()
                                        except:
                                            pass
        ##################################################Place  Studetn_int_Phone_Number_No_error_label####################
                                        # self.PhoneNumberNoTypeErorr()
        ################################
                                        try:
                                            self.Student_Admission_Number = int(Student_Update_gender)
                                        except:
                                            # messagebox.showerror("AdmissionNumber Error",
                                            #                     "You Can Only Type  Numbers For AdmissionNumber ")
                                            pass

                                        if len(Student_Update_age) > 2:
                                            # messagebox.showerror("Age Error", "You Can Only Type Two Numbers For Age ")
                                            self.WAgeError()
                                        else:
                                            try:
                                                self.ClearAgeError()
                                            except:
                                                pass
                                            if isinstance(self.Student_Admission_Number, int):

                                                AllSubjects = ['Sinhala', 'SINHALA', 'Sin', 'sin', "sinhala",
                                                            'Tamil', 'tamil', 'tam', 'Tam', "TAMIL",
                                                            'English', 'english', "En", 'en',
                                                            'Mathematics', 'mathematics', "MATHEMATICS", "math", 'Math',
                                                            'MATH',
                                                            "Health", 'HEALTH', "HEAL", "health",
                                                            "Geography", 'geography', 'GEOGRAPHY', 'geo', "Geo", "GEO",
                                                            'French', "french", 'FRENCH',
                                                            'Spanish', 'SPANISH', "spanish",
                                                            'Computer Science', 'computer science', 'COMPUTER SCIENCE',
                                                            'Art', 'ART', 'art',
                                                            'Band', 'band', 'BAND',
                                                            'Choir', "choir", 'CHOIR',
                                                            'Drama', "drama", "DRAMA",
                                                            "Sports", "SPORTS", "sports",
                                                            'Science', 'science', "SCIENCE",
                                                            'History', 'history', 'HISTORY',
                                                            'Chess', 'CHESS', 'chess',
                                                            "music", 'Music', 'MUSIC',
                                                            "ict", 'ICT', "Ict",
                                                            'Japan', 'japan', 'JAPAN',
                                                            'China', 'china', 'CHINA',
                                                            'Accounting', 'accounting', 'ACCOUNTING',
                                                            'Latin', 'latin', 'LATIN',
                                                            'Greek', 'greek', "GREEK",
                                                            'Hebrew', 'HEBREW', "hebrew",
                                                            'Zoology', "ZOOLOGY", "zoology",
                                                            ]

                                                checkSubject = all(item in AllSubjects for item in Student_Update_subjects.split(","))
                                                    ##########################Clear Error###############################
                                                self.ClearSubjectError()
                                                ###################################################################
                                                if checkSubject is False:
                                                    # messagebox.showerror("Subject Error", "You Can Add Only Subjects ")
                                                        ########################Subject Error############################
                                                    self.WSubjectError()
                                                    ################################################################
                                                else:
                                                        # try:
                                                    #     self.AgeNoError()
                                                    # except:
                                                    #     pass
                                                    try: 
                                                        ##################Chekc db######################### 
                                                        self.connectDB()
                                                        ###################################################
                                                    except:
                                                        #AddDB ERROR
                                                        self.WDatabaseNotConnectedError()
                                                    # self.master.switch_frame(StudentView)
                                            else:
                                                # messagebox.showerror("AdmissionNumber Error",
                                                #                     "You Can Only Type  Numbers For AdmissionNumber ")
                                                pass
            
        else:
            self.Update_DStudentRegistationBGColor = "#121212"
            self.Update_DStudentRegistationFGColor = self.fgcolor
            self.configure(background=self.Update_DStudentRegistationBGColor)
            self.Update_Student__Id_bg_label.configure(background=self.Update_DStudentRegistationBGColor,
                                                       foreground=self.Update_DStudentRegistationFGColor)
            self.Student_Update_Id_label.configure(background=self.Update_DStudentRegistationBGColor,
                                                   foreground=self.Update_DStudentRegistationFGColor)
            self.Student_Update_Update_Go_button.configure(background=self.Update_DStudentRegistationBGColor,
                                                           foreground=self.Update_DStudentRegistationFGColor,
                                                           activebackground=self.Update_DStudentRegistationBGColor,
                                                           activeforeground=self.Update_DStudentRegistationBGColor)
            self.Update_Student__element_img_label.configure(background=self.Update_DStudentRegistationBGColor,
                                                             foreground=self.Update_DStudentRegistationFGColor)
            self.Update_Student_First_name_Entry_bg_label.configure(background=self.Update_DStudentRegistationBGColor,
                                                                    foreground=self.Update_DStudentRegistationFGColor)
            self.Update_Student_Last_name_Entry_bg_label.configure(background=self.Update_DStudentRegistationBGColor,
                                                                   foreground=self.Update_DStudentRegistationFGColor)
            self.Update_Student_age_Entry_bg_label.configure(background=self.Update_DStudentRegistationBGColor,
                                                             foreground=self.Update_DStudentRegistationFGColor)
            self.Update_Student_phone_number_Entry_bg_label.configure(background=self.Update_DStudentRegistationBGColor,
                                                                      foreground=self.Update_DStudentRegistationFGColor)
            self.Update_Student_phone_number_Entry_bg_label.configure(background=self.Update_DStudentRegistationBGColor,
                                                                      foreground=self.Update_DStudentRegistationFGColor)
            self.Update_Student_gender_Entry_bg_label.configure(background=self.Update_DStudentRegistationBGColor,
                                                                foreground=self.Update_DStudentRegistationFGColor)
            self.Update_Student_subject_Entry_bg_label.configure(background=self.Update_DStudentRegistationBGColor,
                                                                 foreground=self.Update_DStudentRegistationFGColor)
            self.Student_Update_first_name_label.configure(background=self.Update_DStudentRegistationBGColor,
                                                           foreground=self.Update_DStudentRegistationFGColor)
            self.Student_Update_last_name_label.configure(background=self.Update_DStudentRegistationBGColor,
                                                          foreground=self.Update_DStudentRegistationFGColor)
            self.Student_Update_phone_number_label.configure(background=self.Update_DStudentRegistationBGColor,
                                                             foreground=self.Update_DStudentRegistationFGColor)
            self.Student_Update_age_label.configure(background=self.Update_DStudentRegistationBGColor,
                                                    foreground=self.Update_DStudentRegistationFGColor)
            self.Student_Update_gender_label.configure(background=self.Update_DStudentRegistationBGColor,
                                                       foreground=self.Update_DStudentRegistationFGColor)
            self.Student_Update_subects_label.configure(background=self.Update_DStudentRegistationBGColor,
                                                        foreground=self.Update_DStudentRegistationFGColor)
            self.Student_Update_Update_teachet_button.configure(background=self.Update_DStudentRegistationBGColor,
                                                                foreground=self.Update_DStudentRegistationFGColor,
                                                                activebackground=self.Update_DStudentRegistationBGColor,
                                                                activeforeground=self.Update_DStudentRegistationBGColor)
            self.Student_Update_Student_registation_close_button.configure(
                background=self.Update_DStudentRegistationBGColor,
                foreground=self.Update_DStudentRegistationFGColor)
            self.Update_Student_label.configure(background=self.Update_DStudentRegistationBGColor,
                                                foreground=self.Update_DStudentRegistationFGColor)
            self.Student_Update_back_page_img_button.configure(background=self.Update_DStudentRegistationBGColor,
                                                               foreground=self.Update_DStudentRegistationFGColor)
            self.Student_Update_Student_registation_theme_change_button.configure(
                background=self.Update_DStudentRegistationBGColor,
                foreground=self.Update_DStudentRegistationFGColor,
                activebackground=self.Update_DStudentRegistationBGColor,
                activeforeground=self.Update_DStudentRegistationBGColor,
                image=self.img_DarkThemeimg)
             #####################################################Clear#######################################################
            self.Clearerrors()
            self.ClearCommited()
    ####################################################Clear########################################################

    #*******************************************************************************************************************
    #########################################Create variabels###########################################################
            #^^^^^^This is All variabels

            Student_Update_first_name = self.Student_Update_first_name_entry.get()
            
            Student_Update_last_name = self.Student_Update_last_name_entry.get()
            
            Student_Update_phone_number = self.Student_Update_phone_number_entry.get()
            
            Student_Update_age = self.Student_Update_age_entry.get()
            
            Student_Update_gender = self.Student_Update_gender_entry.get()
            
            Student_Update_subjects = self.Student_Update_subject_entry.get()
            if self.Student_Update_Id_entry.get() == "":
                self.clickGo()
            else:
                if Student_Update_first_name == "" or Student_Update_last_name == "" or Student_Update_phone_number == "" or Student_Update_age == "" or Student_Update_gender == "" or Student_Update_subjects == "":
                    # messagebox.showerror("insert status", "All Fields Are Required")
                    ##############################Clear All Erorr##################################
                    try:
                        self.Clearerrors()
                    except:
                        pass
                    self.AllFildsRequiredErorrDestroy() 
                    #################################Distroy Student First Name########################
                    #################################Place The Erorr###################################  
                    try:          
                        self.AllFildsRequiredErorr()
                    except:
                        pass
                else:
                                ################################Distroy All Fields Erore#####################
                    self.AllFildsRequiredErorrDestroy()
                    ##################################Student First Name Lenth Check#############

                    if len(Student_Update_first_name) > 50:
                        # messagebox.showerror("First Name Error", "Your Name Is Too Long")
                        ###################################Distroy Studetn_First_Name_No_error_label#####################
                        self.FirstNameErorr()

                        
                    else:
                        # self.FirstNameNoErorr()
                        
                        ############################Distroy First name Error##################################
                        try:
                            self.Studetn_First_Name_error_label.destroy()
                        except:
                            pass

                        if len(Student_Update_last_name) > 50:
                            # messagebox.showerror("Second Name Error", "Your Name Is Too Long")
                            #####################################Distroy Studetn_Last_Name_No_error_label###############
                            try:
                                self.LastNameError()
                            except:
                                pass
                        else:
                                ####################################Distroy Last Name Error#################################
                            try:
                                self.ClearLastNameError()
                            except:
                                pass
                            # self.NoLastNameError()

                            Student_Update_last_name.capitalize()
                            if Student_Update_first_name == Student_Update_last_name:
                                # messagebox.showerror("Copied Name Error", "Your First Name And Secont Name Is Duplicated")
                                ###############################Clear LAST NAME#######################
                                try:
                                    self.ClearNoLastNameError()
                                except:
                                    pass
                                ################################Add Duplicated Error#################
                                try:
                                    self.NameDuplicatedErorr()
                                except:
                                    pass


                            else:
                                    #############################Clear Duplicate error########################
                                try: 
                                    self.ClearNameDuplicatedErorr()
                                except:
                                    pass
                                # self.NoDuplicateNameError()

                                    ################################Numeber Lenth Check########################################

                                if len(Student_Update_phone_number) != 10:
                                    # messagebox.showerror("Phone Number Error", "You Can Add Only 10 Digit number")
                                        ##################################Distroy Number No Eror################# 
                                    try:                         
                                        self.clearAllPhoneErors()
                                    except:
                                        pass

                                    ##################################PHONE NUMBER LENTH ERROR#####################
                                    try:
                                        self.PhoneNumberLenthErorr()
                                    except:
                                        pass

        ###################################################Distroy Studetn_lenth_Phone_number_error_label############
                                else:
                                        ###############################Clear phone number lenth erorr####################
                                    try:
                                        self.ClearPhoneNumberLenthErorr()
                                    except:
                                        pass

                                    try:
                                        int(Student_Update_phone_number)
                                    except Exception as e:
                                        pass

                                    if int(Student_Update_phone_number[0]) != 0:
                                        # messagebox.showerror("Type Error", "This is Not Phone Number")
                                            ######################################################Distroy All Error##################################
                                        try:
                                            self.clearAllPhoneErors()
                                        except:
                                            pass
        #####################################################Place Studetn_int_Phone_number_error_label####################
                                        try:
                                            self.PhoneNumberTypeErorr()
                                        except:
                                            pass
                                    else:
                                            
        ####################################################Distroy Studetn_int_Phone_number_error_label ##################
                                        try:
                                            self.clearAllPhoneErors()
                                        except:
                                            pass
        ##################################################Place  Studetn_int_Phone_Number_No_error_label####################
                                        # self.PhoneNumberNoTypeErorr()
        ################################
                                        try:
                                            self.Student_Admission_Number = int(Student_Update_gender)
                                        except:
                                            # messagebox.showerror("AdmissionNumber Error",
                                            #                     "You Can Only Type  Numbers For AdmissionNumber ")
                                            pass

                                        if len(Student_Update_age) > 2:
                                            # messagebox.showerror("Age Error", "You Can Only Type Two Numbers For Age ")
                                            self.AgeError()
                                        else:
                                            try:
                                                self.ClearAgeError()
                                            except:
                                                pass
                                            if isinstance(self.Student_Admission_Number, int):

                                                AllSubjects = ['Sinhala', 'SINHALA', 'Sin', 'sin', "sinhala",
                                                            'Tamil', 'tamil', 'tam', 'Tam', "TAMIL",
                                                            'English', 'english', "En", 'en',
                                                            'Mathematics', 'mathematics', "MATHEMATICS", "math", 'Math',
                                                            'MATH',
                                                            "Health", 'HEALTH', "HEAL", "health",
                                                            "Geography", 'geography', 'GEOGRAPHY', 'geo', "Geo", "GEO",
                                                            'French', "french", 'FRENCH',
                                                            'Spanish', 'SPANISH', "spanish",
                                                            'Computer Science', 'computer science', 'COMPUTER SCIENCE',
                                                            'Art', 'ART', 'art',
                                                            'Band', 'band', 'BAND',
                                                            'Choir', "choir", 'CHOIR',
                                                            'Drama', "drama", "DRAMA",
                                                            "Sports", "SPORTS", "sports",
                                                            'Science', 'science', "SCIENCE",
                                                            'History', 'history', 'HISTORY',
                                                            'Chess', 'CHESS', 'chess',
                                                            "music", 'Music', 'MUSIC',
                                                            "ict", 'ICT', "Ict",
                                                            'Japan', 'japan', 'JAPAN',
                                                            'China', 'china', 'CHINA',
                                                            'Accounting', 'accounting', 'ACCOUNTING',
                                                            'Latin', 'latin', 'LATIN',
                                                            'Greek', 'greek', "GREEK",
                                                            'Hebrew', 'HEBREW', "hebrew",
                                                            'Zoology', "ZOOLOGY", "zoology",
                                                            ]

                                                checkSubject = all(item in AllSubjects for item in Student_Update_subjects.split(","))
                                                    ##########################Clear Error###############################
                                                self.ClearSubjectError()
                                                ###################################################################
                                                if checkSubject is False:
                                                    # messagebox.showerror("Subject Error", "You Can Add Only Subjects ")
                                                        ########################Subject Error############################
                                                    self.SubjectError()
                                                    ################################################################
                                                else:
                                                        # try:
                                                    #     self.AgeNoError()
                                                    # except:
                                                    #     pass
                                                    try: 
                                                        ##################Chekc db######################### 
                                                        self.connectDB()
                                                        ###################################################
                                                    except:
                                                        #AddDB ERROR
                                                        self.DatabaseNotConnectedError()
                                                    # self.master.switch_frame(StudentView)
                                            else:
                                                # messagebox.showerror("AdmissionNumber Error",
                                                #                     "You Can Only Type  Numbers For AdmissionNumber ")
                                                pass

    def goBackToStudentHome(self):
        self.master.switch_frame(StudentHome)

    def clickUpdate(self):
        #####################################################Clear#######################################################
        self.Clearerrors()
        self.ClearCommited()
####################################################Clear########################################################

#*******************************************************************************************************************
#########################################Create variabels###########################################################
        global Student_Update_first_name, Student_Update_last_name, Student_Update_phone_number, Student_Update_age, Student_Update_gender, Student_Update_subjects
        #^^^^^^This is All variabels

        Student_Update_first_name = self.Student_Update_first_name_entry.get()
        
        Student_Update_last_name = self.Student_Update_last_name_entry.get()
        
        Student_Update_phone_number = self.Student_Update_phone_number_entry.get()
        
        Student_Update_age = self.Student_Update_age_entry.get()
        
        Student_Update_gender = self.Student_Update_gender_entry.get()
        
        Student_Update_subjects = self.Student_Update_subject_entry.get()
        if self.Student_Update_Id_entry.get() == "":
            self.clickGo()
        else:
            if Student_Update_first_name == "" or Student_Update_last_name == "" or Student_Update_phone_number == "" or Student_Update_age == "" or Student_Update_gender == "" or Student_Update_subjects == "":
                # messagebox.showerror("insert status", "All Fields Are Required")
                ##############################Clear All Erorr##################################
                try:
                    self.Clearerrors()
                except:
                    pass
                self.AllFildsRequiredErorrDestroy() 
                #################################Distroy Student First Name########################
                #################################Place The Erorr###################################  
                try:          
                    self.AllFildsRequiredErorr()
                except:
                    pass
            else:
                            ################################Distroy All Fields Erore#####################
                self.AllFildsRequiredErorrDestroy()
                 ##################################Student First Name Lenth Check#############

                if len(Student_Update_first_name) > 50:
                    # messagebox.showerror("First Name Error", "Your Name Is Too Long")
                    ###################################Distroy Studetn_First_Name_No_error_label#####################
                    self.FirstNameErorr()

                    
                else:
                    # self.FirstNameNoErorr()
                    
                    ############################Distroy First name Error##################################
                    try:
                        self.Studetn_First_Name_error_label.destroy()
                    except:
                        pass

                    if len(Student_Update_last_name) > 50:
                        # messagebox.showerror("Second Name Error", "Your Name Is Too Long")
                        #####################################Distroy Studetn_Last_Name_No_error_label###############
                        try:
                            self.LastNameError()
                        except:
                            pass
                    else:
                            ####################################Distroy Last Name Error#################################
                        try:
                            self.ClearLastNameError()
                        except:
                            pass
                        # self.NoLastNameError()

                        Student_Update_last_name.capitalize()
                        if Student_Update_first_name == Student_Update_last_name:
                            # messagebox.showerror("Copied Name Error", "Your First Name And Secont Name Is Duplicated")
                            ###############################Clear LAST NAME#######################
                            try:
                                self.ClearNoLastNameError()
                            except:
                                pass
                            ################################Add Duplicated Error#################
                            try:
                                self.NameDuplicatedErorr()
                            except:
                                pass


                        else:
                                #############################Clear Duplicate error########################
                            try: 
                                self.ClearNameDuplicatedErorr()
                            except:
                                pass
                            # self.NoDuplicateNameError()

                                ################################Numeber Lenth Check########################################

                            if len(Student_Update_phone_number) != 10:
                                # messagebox.showerror("Phone Number Error", "You Can Add Only 10 Digit number")
                                    ##################################Distroy Number No Eror################# 
                                try:                         
                                    self.clearAllPhoneErors()
                                except:
                                    pass

                                ##################################PHONE NUMBER LENTH ERROR#####################
                                try:
                                    self.PhoneNumberLenthErorr()
                                except:
                                    pass

    ###################################################Distroy Studetn_lenth_Phone_number_error_label############
                            else:
                                    ###############################Clear phone number lenth erorr####################
                                try:
                                    self.ClearPhoneNumberLenthErorr()
                                except:
                                    pass

                                try:
                                    int(Student_Update_phone_number)
                                except Exception as e:
                                    pass

                                if int(Student_Update_phone_number[0]) != 0:
                                    # messagebox.showerror("Type Error", "This is Not Phone Number")
                                        ######################################################Distroy All Error##################################
                                    try:
                                        self.clearAllPhoneErors()
                                    except:
                                        pass
    #####################################################Place Studetn_int_Phone_number_error_label####################
                                    try:
                                        self.PhoneNumberTypeErorr()
                                    except:
                                        pass
                                else:
                                        
    ####################################################Distroy Studetn_int_Phone_number_error_label ##################
                                    try:
                                        self.clearAllPhoneErors()
                                    except:
                                        pass
    ##################################################Place  Studetn_int_Phone_Number_No_error_label####################
                                    # self.PhoneNumberNoTypeErorr()
    ################################
                                    try:
                                        self.Student_Admission_Number = int(Student_Update_gender)
                                    except:
                                        # messagebox.showerror("AdmissionNumber Error",
                                        #                     "You Can Only Type  Numbers For AdmissionNumber ")
                                        pass

                                    if len(Student_Update_age) > 2:
                                        # messagebox.showerror("Age Error", "You Can Only Type Two Numbers For Age ")
                                        self.AgeError()
                                    else:
                                        try:
                                            self.ClearAgeError()
                                        except:
                                            pass
                                        if isinstance(self.Student_Admission_Number, int):

                                            AllSubjects = ['Sinhala', 'SINHALA', 'Sin', 'sin', "sinhala",
                                                        'Tamil', 'tamil', 'tam', 'Tam', "TAMIL",
                                                        'English', 'english', "En", 'en',
                                                        'Mathematics', 'mathematics', "MATHEMATICS", "math", 'Math',
                                                        'MATH',
                                                        "Health", 'HEALTH', "HEAL", "health",
                                                        "Geography", 'geography', 'GEOGRAPHY', 'geo', "Geo", "GEO",
                                                        'French', "french", 'FRENCH',
                                                        'Spanish', 'SPANISH', "spanish",
                                                        'Computer Science', 'computer science', 'COMPUTER SCIENCE',
                                                        'Art', 'ART', 'art',
                                                        'Band', 'band', 'BAND',
                                                        'Choir', "choir", 'CHOIR',
                                                        'Drama', "drama", "DRAMA",
                                                        "Sports", "SPORTS", "sports",
                                                        'Science', 'science', "SCIENCE",
                                                        'History', 'history', 'HISTORY',
                                                        'Chess', 'CHESS', 'chess',
                                                        "music", 'Music', 'MUSIC',
                                                        "ict", 'ICT', "Ict",
                                                        'Japan', 'japan', 'JAPAN',
                                                        'China', 'china', 'CHINA',
                                                        'Accounting', 'accounting', 'ACCOUNTING',
                                                        'Latin', 'latin', 'LATIN',
                                                        'Greek', 'greek', "GREEK",
                                                        'Hebrew', 'HEBREW', "hebrew",
                                                        'Zoology', "ZOOLOGY", "zoology",
                                                        ]

                                            checkSubject = all(item in AllSubjects for item in Student_Update_subjects.split(","))
                                                ##########################Clear Error###############################
                                            self.ClearSubjectError()
                                            ###################################################################
                                            if checkSubject is False:
                                                # messagebox.showerror("Subject Error", "You Can Add Only Subjects ")
                                                    ########################Subject Error############################
                                                self.SubjectError()
                                                ################################################################
                                            else:
                                                    # try:
                                                #     self.AgeNoError()
                                                # except:
                                                #     pass
                                                try: 
                                                    ##################Chekc db######################### 
                                                    self.connectDB()
                                                    ###################################################
                                                except:
                                                    #AddDB ERROR
                                                    self.DatabaseNotConnectedError()


                                                int(Student_Update_phone_number)
                                                int(Student_Update_age)
                                                self.connetc = self.conn.cursor()
                                                self.connetc.execute(
                                                    f"UPDATE Student SET FirstName='{Student_Update_first_name}',LAstName='{Student_Update_last_name}',PhoneNumber='{Student_Update_phone_number}',Age='{Student_Update_age}',Student_Admission_Number='{(Student_Update_gender)}',Subjects='{Student_Update_subjects}' WHERE id={Student_changeId}")
                                                # self.connetc.execute()
                                                self.conn.commit()
                                                self.clearStudentUpdate()
                                                self.connetc.close()
                                                self.conn.close()
                                                self.Commited()
                                                # self.master.switch_frame(StudentView)
                                        else:
                                            # messagebox.showerror("AdmissionNumber Error",
                                            #                     "You Can Only Type  Numbers For AdmissionNumber ")
                                            pass

    def clearStudentUpdate(self):
        self.Student_Update_first_name_entry.delete(0, 'end')
        self.Student_Update_subject_entry.delete(0, 'end')
        self.Student_Update_last_name_entry.delete(0, 'end')
        self.Student_Update_gender_entry.delete(0, 'end')
        self.Student_Update_age_entry.delete(0, 'end')
        self.Student_Update_phone_number_entry.delete(0, 'end')
        # self.master.switch_frame(StudentView)

    def clearStudentUpdate(self):
        self.Student_Update_first_name_entry.delete(0, 'end')
        self.Student_Update_subject_entry.delete(0, 'end')
        self.Student_Update_last_name_entry.delete(0, 'end')
        self.Student_Update_gender_entry.delete(0, 'end')
        self.Student_Update_age_entry.delete(0, 'end')
        self.Student_Update_phone_number_entry.delete(0, 'end')

    def EmptyChangeIdError(self):
        ###############AGE Error##################################
        try:
            self.Studetn_Change_id_error_label = tk.Label(self)
            self.Studetn_Change_id_error_label.configure(background=self.bgcolor,
                                                                            borderwidth='0',
                                                                            font='{Poppins} 7 {}',
                                                                            foreground='#ff0f15')
            self.Studetn_Change_id_error_label.configure(text='Type Id')
            self.Studetn_Change_id_error_label.place(anchor='nw',
                                                                        x='450',
                                                                        y='80')
        except:
            pass
        ####################################################################

    def clearEmptyChangeIdError(self):
        try:
            self.Studetn_Change_id_error_label.destroy()
        except:
            pass

    def ChangeIdTypoeError(self):
        ###############AGE Error##################################
        try:
            self.Clearerrors()
            self.Studetn_Change_id_type_error_label = tk.Label(self)
            self.Studetn_Change_id_type_error_label.configure(background=self.bgcolor,
                                                                            borderwidth='0',
                                                                            font='{Poppins} 7 {}',
                                                                            foreground='#ff0f15')
            self.Studetn_Change_id_type_error_label.configure(text='Check Id And Type ')
            self.Studetn_Change_id_type_error_label.place(anchor='nw',
                                                                        x='450',
                                                                        y='80')
        except:
            pass
        ####################################################################

    def clearChangeIdTypeError(self):
        try:
            self.Studetn_Change_id_type_error_label.destroy()
        except:
            pass

    def SelectChangedId(self):
        try:
            self.Clearerrors()
            try:
                self.clearChangeIdTypeError()
            except:
                pass
            self.connetc.execute(
                    "SELECT * FROM Student WHERE id = {}".format(Student_changeId))
            self.IdRecode = self.connetc.fetchone()
            self.Student_Update_first_name_entry.delete(0, 'end')
            self.Student_Update_first_name_entry.insert(0, self.IdRecode[1])
            self.Student_Update_last_name_entry.delete(0, 'end')
            self.Student_Update_last_name_entry.insert(0, self.IdRecode[2])
            self.Student_Update_age_entry.delete(0, 'end')
            self.Student_Update_age_entry.insert(0, self.IdRecode[4])
            self.Student_Update_phone_number_entry.delete(0, 'end')
            Update_phone_number_add_o = '0' + str(self.IdRecode[3])
            self.Student_Update_phone_number_entry.insert(0, Update_phone_number_add_o)
            self.Student_Update_gender_entry.delete(0, 'end')
            self.Student_Update_gender_entry.insert(0, self.IdRecode[5])
            self.Student_Update_subject_entry.delete(0, 'end')
            self.Student_Update_subject_entry.insert(0, self.IdRecode[6])
        except:
            # messagebox.showerror("ID Name Error", "Invalid Id number Or No Id Number Finded")
            self.ChangeIdTypoeError()
            self.Clearerrors()

    def DatabaseNotConnectedError(self):
        ###############AGE Error##################################
        try:
            self.Database_not_Connected_error_label = tk.Label(self)
            self.Database_not_Connected_error_label.configure(background=self.bgcolor,
                                                                            borderwidth='0',
                                                                            font='{Poppins} 8 {}',
                                                                            foreground='#ff0f15')
            self.Database_not_Connected_error_label.configure(text='Database Not Connected or Not Found')
            self.Database_not_Connected_error_label.place(anchor='nw',
                                                                        x='400',
                                                                        y='420')
        except:
            pass
        ####################################################################

    def ClearCommited(self):
        try:
            self.Comited_label.destroy()
        except:
            pass


    def ClearDarabaseNotConnectedError(self):
        try:
            self.Database_not_Connected_error_label.destroy()
        except:
            pass

    def connectDB(self):
        try:
            ###############Clear Db Errors############
            self.ClearDarabaseNotConnectedError()
            ##########################################

            #################Conect Db#####################
            self.conn = mysql.connector.connect(
                    user="root",
                    password="",
                    database="eduway")
            ############################################
        except:
            ##############################DB ERROR#######################
            self.DatabaseNotConnectedError()
            ##############################################################

    def SubjectError(self):
                ############### Error##################################
        try:
            self.Studetn_Subject_error_label = tk.Label(self)
            self.Studetn_Subject_error_label.configure(background=self.bgcolor,
                                                                            borderwidth='0',
                                                                            font='{Poppins} 7 {}',
                                                                            foreground='#ff0f15')
            self.Studetn_Subject_error_label.configure(text='invalid Subject Check Again')
            self.Studetn_Subject_error_label.place(anchor='nw',
                                                                        x='500',
                                                                        y='370')
        except:
            pass
        ####################################################################

        ####################################################################
    
    def WSubjectError(self):
                ############### Error##################################
        try:
            self.WStudetn_Subject_error_label = tk.Label(self)
            self.WStudetn_Subject_error_label.configure(background=self.fgcolor,
                                                                            borderwidth='0',
                                                                            font='{Poppins} 7 {}',
                                                                            foreground='#ff0f15')
            self.WStudetn_Subject_error_label.configure(text='invalid Subject Check Again')
            self.WStudetn_Subject_error_label.place(anchor='nw',
                                                                        x='500',
                                                                        y='370')
        except:
            pass
        ####################################################################

    def ClearSubjectError(self):
        try:
            self.Studetn_Subject_error_label.destroy()
            self.WStudetn_Subject_error_label.destroy()
        except:
            pass



    def Commited(self):
        ###############AGE Error##################################
        try:
            self.Comited_label = tk.Label(self)
            self.Comited_label.configure(background=self.bgcolor,
                                                                            borderwidth='0',
                                                                            font='{Poppins} 8 {}',
                                                                            foreground='#2bff00')
            self.Comited_label.configure(text='Student Added')
            self.Comited_label.place(anchor='nw',
                                                                        x='400',
                                                                        y='420')
        except:
            pass
        ####################################################################


##############################################################Clear error labales###################################

    def Clearerrors(self):
        try:
            self.clearAllPhoneErors()
            self.clearChangeIdTypeError()
            self.ClearAllStuf()
            self.Studetn_All_Fields_Required_error_label.destroy()
            self.Studetn_First_Name_No_error_label.destroy()
            self.Studetn_Last_Name_No_error_label.destroy()
            self.Studetn_Last_Name_error_label.destroy()
            self.Studetn_Duplicate_Name_error_label.destroy()
            self.Studetn_Last_Name_No_error_label.destroy()
            self.Studetn_lenth_Phone_Number_No_error_label.destroy()
            self.Studetn_lenth_Phone_number_error_label.destroy()
            self.Studetn_0_Phone_number_error_label.destroy()
            self.Studetn_int_Phone_number_error_label.destroy()
            self.Studetn_0_Phone_Number_No_error_label.destroy()
            self.Studetn_int_Phone_Number_No_error_label.destroy()
            self.Studetn_Age_error_label.destroy()
            self.Studetn_Subject_error_label.destroy()

        except:
            pass
    
    
######################################################All Fields Required#########################################

    def AllFildsRequiredErorr(self):
        try:
                self.Studetn_First_Name_error_label.destroy()
                self.Studetn_First_Name_No_error_label.destroy()
        except:
            pass


            ################################Place Eror################################
        self.Studetn_All_Fields_Required_error_label = tk.Label(self)
        self.Studetn_All_Fields_Required_error_label.configure(background=self.bgcolor,
                                                    borderwidth='0',
                                                    font='{Poppins} 7 {}',
                                                    foreground='#ff0f15')
        self.Studetn_All_Fields_Required_error_label.configure(text='All Fields Are Required')
        self.Studetn_All_Fields_Required_error_label.place(anchor='nw',
                                                x='500',
                                                y='130')

    def WAllFildsRequiredErorr(self):
        try:
                self.WStudetn_First_Name_error_label.destroy()
                self.WStudetn_First_Name_No_error_label.destroy()
                self.Studetn_First_Name_error_label.destroy()
                self.Studetn_First_Name_No_error_label.destroy()
        except:
            pass


            ################################Place Eror################################
        self.WStudetn_All_Fields_Required_error_label = tk.Label(self)
        self.WStudetn_All_Fields_Required_error_label.configure(background=self.fgcolor,
                                                    borderwidth='0',
                                                    font='{Poppins} 7 {}',
                                                    foreground='#ff0f15')
        self.WStudetn_All_Fields_Required_error_label.configure(text='All Fields Are Required')
        self.WStudetn_All_Fields_Required_error_label.place(anchor='nw',
                                                x='500',
                                                y='130')

    def AllFildsRequiredErorrDestroy(self):
        try:
            self.Studetn_All_Fields_Required_error_label.destroy()
            self.WStudetn_All_Fields_Required_error_label.destroy()
        except:
            pass
######################################################First Name###################################################

    def FirstNameErorr(self):
        try:
            self.Studetn_First_Name_error_label.destroy()
            self.Studetn_First_Name_No_error_label.destroy()
        except:
            pass
                
###################################################place Studetn_First_Name_error_label############################
        self.Studetn_First_Name_error_label = tk.Label(self)
        self.Studetn_First_Name_error_label.configure(background=self.bgcolor,
                                                    borderwidth='0',
                                                    font='{Poppins} 7 {}',
                                                    foreground='#ff0f15')
        self.Studetn_First_Name_error_label.configure(text='First Name Is Too Long')
        self.Studetn_First_Name_error_label.place(anchor='nw',
                                                x='500',
                                                y='130')
    
    def FirstNameNoErorr(self):
        try:
 ##############################Distroy Studetn_First_Name_error_label#######################
            self.Studetn_First_Name_error_label.destroy()
        except:
            pass

                ####################################Place Studetn_First_Name_No_error_label######################
            self.Studetn_First_Name_No_error_label = tk.Label(self)
            self.Studetn_First_Name_No_error_label.configure(background=self.bgcolor,
                                                    borderwidth='0',
                                                    font='{Poppins} 9 {}',
                                                    foreground='#09ff00')
            self.Studetn_First_Name_No_error_label.configure(text=""+u'\u2713')
            self.Studetn_First_Name_No_error_label.place(anchor='nw',
                                                x='610',
                                                y='123')


############################################################Last Name################################################
    def LastNameError(self):
        try:
            self.Studetn_Last_Name_No_error_label.destroy()
        except:
            pass
                    
        self.Studetn_Last_Name_error_label = tk.Label(self)
        self.Studetn_Last_Name_error_label.configure(background=self.bgcolor,
                                                        borderwidth='0',
                                                        font='{Poppins} 8 {}',
                                                        foreground='#ff0f15')
        self.Studetn_Last_Name_error_label.configure(text='Last Name Is Too Long')
        self.Studetn_Last_Name_error_label.place(anchor='nw',
                                                    x='500',
                                                    y='174')

    def WLastNameError(self):
        try:
            self.Studetn_First_Name_error_label.destroy()
            self.WStudetn_First_Name_error_label.destroy()
            self.WStudetn_Last_Name_error_label.destroy()
        except:
            pass
                    
        self.WStudetn_Last_Name_error_label = tk.Label(self)
        self.WStudetn_Last_Name_error_label.configure(background=self.fgcolor,
                                                        borderwidth='0',
                                                        font='{Poppins} 8 {}',
                                                        foreground='#ff0f15')
        self.WStudetn_Last_Name_error_label.configure(text='Last Name Is Too Long')
        self.WStudetn_Last_Name_error_label.place(anchor='nw',
                                                    x='500',
                                                    y='174')
 
    def ClearLastNameError(self):
        try:
            self.Studetn_Last_Name_error_label.destroy()
            self.WStudetn_Last_Name_error_label.destroy()
        except:
            pass

    def NoLastNameError(self):
        self.Studetn_Last_Name_No_error_label = tk.Label(self)
        self.Studetn_Last_Name_No_error_label.configure(background=self.bgcolor,
                                                        borderwidth='0',
                                                        font='{Poppins} 8 {}',
                                                        foreground='#09ff00')
        self.Studetn_Last_Name_No_error_label.configure(text=""+u'\u2713')
        self.Studetn_Last_Name_No_error_label.place(anchor='nw',
                                                    x='610',
                                                    y='174')

    def NoDuplicateNameError(self):
        self.Studetn_Duplicate_Name_No_error_label = tk.Label(self)
        self.Studetn_Duplicate_Name_No_error_label.configure(background=self.bgcolor,
                                                        borderwidth='0',
                                                        font='{Poppins} 8 {}',
                                                        foreground='#09ff00')
        self.Studetn_Duplicate_Name_No_error_label.configure(text=""+u'\u2713')
        self.Studetn_Duplicate_Name_No_error_label.place(anchor='nw',
                                                    x='610',
                                                    y='174')

    def ClearNoLastNameError(self):
        try:
            self.Studetn_Last_Name_No_error_label.destroy()
        except:
            pass
    
    def NameDuplicatedErorr(self):
        self.Studetn_Duplicate_Name_error_label = tk.Label(self)
        self.Studetn_Duplicate_Name_error_label.configure(background=self.bgcolor,
                                                            borderwidth='0',
                                                            font='{Poppins} 8 {}',
                                                            foreground='#ff0f15')
        self.Studetn_Duplicate_Name_error_label.configure(text='Name Duplicated')
        self.Studetn_Duplicate_Name_error_label.place(anchor='nw',
                                                        x='500',
                                                        y='174')
    def WNameDuplicatedErorr(self):
        self.WStudetn_Duplicate_Name_error_label = tk.Label(self)
        self.WStudetn_Duplicate_Name_error_label.configure(background=self.fgcolor,
                                                            borderwidth='0',
                                                            font='{Poppins} 8 {}',
                                                            foreground='#ff0f15')
        self.WStudetn_Duplicate_Name_error_label.configure(text='Name Duplicated')
        self.WStudetn_Duplicate_Name_error_label.place(anchor='nw',
                                                        x='500',
                                                        y='174')
    def ClearNameDuplicatedErorr(self):

        try:
            self.Studetn_Duplicate_Name_error_label.destroy()
            self.WStudetn_Duplicate_Name_error_label.destroy()

        except:
            pass

    def clearAllPhoneErors(self):

        try:
            self.ClearPhoneNumberLenthErorr()
            self.ClearPhoneNumberTypeErorr()
            self.ClearPhoneNumberZeroError()
            self.Studetn_int_Phone_number_error_label.destroy()
            self.Studetn_0_Phone_Number_No_error_label.destroy()
            self.Studetn_int_Phone_Number_No_error_label.destroy()
        except:
            pass

    def PhoneNumberLenthErorr(self):

        #####################PHONE NUMBER LENTH ERROR ##########################
        self.Studetn_lenth_Phone_number_error_label = tk.Label(self)
        self.Studetn_lenth_Phone_number_error_label.configure(background=self.bgcolor,
                                                                borderwidth='0',
                                                                font='{Poppins} 7 {}',
                                                                foreground='#ff0f15')
        self.Studetn_lenth_Phone_number_error_label.configure(text='Not Phone Number')
        self.Studetn_lenth_Phone_number_error_label.place(anchor='nw',
                                                            x='500',
                                                            y='274')
        #########################################################################

    def WPhoneNumberLenthErorr(self):

        #####################PHONE NUMBER LENTH ERROR ##########################
        self.WStudetn_lenth_Phone_number_error_label = tk.Label(self)
        self.WStudetn_lenth_Phone_number_error_label.configure(background=self.fgcolor,
                                                                borderwidth='0',
                                                                font='{Poppins} 7 {}',
                                                                foreground='#ff0f15')
        self.WStudetn_lenth_Phone_number_error_label.configure(text='Not Phone Number')
        self.WStudetn_lenth_Phone_number_error_label.place(anchor='nw',
                                                            x='500',
                                                            y='274')
        #########################################################################

    def ClearPhoneNumberLenthErorr(self):

        ##################DISTROY PHONE NUMBER ERROR###################
        try:
            self.Studetn_lenth_Phone_number_error_label.destroy()
            self.WStudetn_lenth_Phone_number_error_label.destroy()
        except:
            pass
        ##############################################################

    def PhoneNumberLenthNoErorr(self):

        ####################NO ERROR PHONE NUMBER LENTH######################
        self.Studetn_lenth_Phone_Number_No_error_label = tk.Label(self)
        self.Studetn_lenth_Phone_Number_No_error_label.configure(background=self.bgcolor,
                                                                borderwidth='0',
                                                                font='{Poppins} 7 {}',
                                                                foreground='#09ff00')
        self.Studetn_lenth_Phone_Number_No_error_label.configure(text=""+u'\u2713')
        self.Studetn_lenth_Phone_Number_No_error_label.place(anchor='nw',
                                                            x='610',
                                                            y='274')    
        #####################################################################


    def PhoneNumberTypeErorr(self):
        ####################PHONE NUMBER TYPE ERORR########################
        self.Studetn_int_Phone_number_error_label = tk.Label(self)
        self.Studetn_int_Phone_number_error_label.configure(background=self.bgcolor,
                                                                    borderwidth='0',
                                                                    font='{Poppins} 7 {}',
                                                                    foreground='#ff0f15')
        self.Studetn_int_Phone_number_error_label.configure(text='Type Number')
        self.Studetn_int_Phone_number_error_label.place(anchor='nw',
                                                                x='500',
                                                                y='274')
        ########################################################################

    def WPhoneNumberTypeErorr(self):
        ####################PHONE NUMBER TYPE ERORR########################
        self.WStudetn_int_Phone_number_error_label = tk.Label(self)
        self.WStudetn_int_Phone_number_error_label.configure(background=self.fgcolor,
                                                                    borderwidth='0',
                                                                    font='{Poppins} 7 {}',
                                                                    foreground='#ff0f15')
        self.WStudetn_int_Phone_number_error_label.configure(text='Type Number')
        self.WStudetn_int_Phone_number_error_label.place(anchor='nw',
                                                                x='500',
                                                                y='274')
        ########################################################################

    def ClearPhoneNumberTypeErorr(self):
        ###############PHONE NUMBER CLEAR#################
        try:
            self.Studetn_int_Phone_number_error_label.destroy()
            self.WStudetn_int_Phone_number_error_label.destroy()
        except:
            pass
        ##################################################
##################################################

    def PhoneNumberNoTypeErorr(self):

        #####################PHONE NUMBER TYPE ERROR##############
        self.Studetn_int_Phone_Number_No_error_label = tk.Label(self)
        self.Studetn_int_Phone_Number_No_error_label.configure(background=self.bgcolor,
                                                                    borderwidth='0',
                                                                    font='{Poppins} 7 {}',
                                                                    foreground='#09ff00')
        self.Studetn_int_Phone_Number_No_error_label.configure(text=""+u'\u2713')
        self.Studetn_int_Phone_Number_No_error_label.place(anchor='nw',
                                                                x='610',
                                                                y='274')
        ##########################################################

    def PhoneNumberZeroError(self):

        #####################PHONE NUMBER ZERO ERROR################
        self.Studetn_0_Phone_number_error_label = tk.Label(self)
        self.Studetn_0_Phone_number_error_label.configure(background=self.bgcolor,
                                                                        borderwidth='0',
                                                                        font='{Poppins} 7 {}',
                                                                        foreground='#ff0f15')
        self.Studetn_0_Phone_number_error_label.configure(text='Invalid Phone Number')
        self.Studetn_0_Phone_number_error_label.place(anchor='nw',
                                                                    x='500',
                                                                    y='274')
        ############################################################

    def WPhoneNumberZeroError(self):

        #####################PHONE NUMBER ZERO ERROR################
        self.WStudetn_0_Phone_number_error_label = tk.Label(self)
        self.WStudetn_0_Phone_number_error_label.configure(background=self.fgcolor,
                                                                        borderwidth='0',
                                                                        font='{Poppins} 7 {}',
                                                                        foreground='#ff0f15')
        self.WStudetn_0_Phone_number_error_label.configure(text='Invalid Phone Number')
        self.WStudetn_0_Phone_number_error_label.place(anchor='nw',
                                                                    x='500',
                                                                    y='274')
        ############################################################
    

    def ClearPhoneNumberZeroError(self):
        ##########CLEAR PHONE NUMBER###############################
        try:
            self.Studetn_0_Phone_number_error_label.configure(background=self.bgcolor,
                                                                        borderwidth='0',
                                                                        font='{Poppins} 0 {}',
                                                                        foreground=self.bgcolor)
            self.Studetn_0_Phone_number_error_label.destroy()
        except:
            pass
        ##########################################################

    def PhoneNumberNoZeroError(self):

        #################PHONE NUMBER ZERO NO ERROR################################
        self.Studetn_0_Phone_Number_No_error_label = tk.Label(self)
        self.Studetn_0_Phone_Number_No_error_label.configure(background=self.bgcolor,
                                                                        borderwidth='0',
                                                                        font='{Poppins} 7 {}',
                                                                        foreground='#09ff00')
        self.Studetn_0_Phone_Number_No_error_label.configure(text=""+u'\u2713')
        self.Studetn_0_Phone_Number_No_error_label.place(anchor='nw',
                                                                    x='610',
                                                                    y='274')   
        ############################################################################

    def AgeError(self):

        ###############AGE Error##################################
        try:
            self.Studetn_Age_error_label = tk.Label(self)
            self.Studetn_Age_error_label.configure(background=self.bgcolor,
                                                                            borderwidth='0',
                                                                            font='{Poppins} 7 {}',
                                                                            foreground='#ff0f15')
            self.Studetn_Age_error_label.configure(text='Number Too Long')
            self.Studetn_Age_error_label.place(anchor='nw',
                                                                        x='500',
                                                                        y='225')
        except:
            pass
        ####################################################################

    def ClearAgeError(self):

        ################CLEAR AGE ERROR#############
        try:
            self.Studetn_Age_error_label.destroy()
            self.WStudetn_Age_error_label.destroy()
        except:
            pass
        ###############################################################

    def WAgeError(self):

        ###############AGE Error##################################
        try:
            self.Studetn_Age_error_label.destroy()
            self.WStudetn_Age_error_label = tk.Label(self)
            self.WStudetn_Age_error_label.configure(background=self.fgcolor,
                                                                            borderwidth='0',
                                                                            font='{Poppins} 7 {}',
                                                                            foreground='#ff0f15')
            self.WStudetn_Age_error_label.configure(text='Number Too Long')
            self.WStudetn_Age_error_label.place(anchor='nw',
                                                                        x='500',
                                                                        y='227')
        except:
            pass
        ####################################################################

    def AgeNoError(self):

        #################PHONE NUMBER ZERO NO ERROR################################
        self.Studetn_Age_No_error_label = tk.Label(self)
        self.Studetn_Age_No_error_label.configure(background=self.bgcolor,
                                                                        borderwidth='0',
                                                                        font='{Poppins} 7 {}',
                                                                        foreground='#09ff00')
        self.Studetn_Age_No_error_label.configure(text=""+u'\u2713')
        self.Studetn_Age_No_error_label.place(anchor='nw',
                                                                    x='610',
                                                                    y='225')   
        ############################################################################     

    def ClearAllStuf(self):
        ########################Clear No ERRORS###################################
        try:
            self.Studetn_First_Name_No_error_label.destroy()
            self.Studetn_lenth_Phone_Number_No_error_label.destroy()
            self.Studetn_int_Phone_Number_No_error_label.destroy()
            self.Studetn_Age_No_error_label.destroy()
            self.Studetn_Duplicate_Name_No_error_label.destroy()
        except:
            pass
    
    def WDatabaseNotConnectedError(self):
        ###############AGE Error##################################
        try:
            self.Database_not_Connected_error_label.destroy()
            self.WDatabase_not_Connected_error_label = tk.Label(self)
            self.WDatabase_not_Connected_error_label.configure(background=self.fgcolor,
                                                                            borderwidth='0',
                                                                            font='{Poppins} 8 {}',
                                                                            foreground='#ff0f15')
            self.WDatabase_not_Connected_error_label.configure(text='Database Not Connected or Not Found')
            self.WDatabase_not_Connected_error_label.place(anchor='nw',
                                                                        x='400',
                                                                        y='420')
        except:
            pass
        ####################################################################
