class DarkTeacherRegistation(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.Teacher_element_img_label = tk.Label(self)

        try:
            self.Teacher_img_Element_1_img_label = tk.PhotoImage(file='Element_1_img_label.png')
        except Exception as e:
            messagebox.showerror("Element_1_img_label.png' Missing")
            print(e)

        self.Teacher_element_img_label.configure(background='#121212',
                                                 image=self.Teacher_img_Element_1_img_label)
        self.Teacher_element_img_label.place(anchor='nw',
                                             x='0',
                                             y='0')

        try:
            self.img_TeacherRegiusterEntery = tk.PhotoImage(file='TeacherRegiusterEntery.png')
        except Exception as e:
            messagebox.showerror("TeacherAddButton.png Missing")
            print(e)

        self.Teacher_Admission_Number_Entry_bg_label = tk.Label(self)
        self.Teacher_Admission_Number_Entry_bg_label.configure(background='#121212',
                                                               borderwidth='0',
                                                               image=self.img_TeacherRegiusterEntery)
        self.Teacher_Admission_Number_Entry_bg_label.place(anchor='nw',
                                                           x='386',
                                                           y='340')
        self.Teacher_First_name_Entry_bg_label = tk.Label(self)
        self.Teacher_First_name_Entry_bg_label.configure(background='#121212',
                                                         borderwidth='0',
                                                         image=self.img_TeacherRegiusterEntery)
        self.Teacher_First_name_Entry_bg_label.place(anchor='nw',
                                                     x='386',
                                                     y='146')

        self.Teacher_Last_name_Entry_bg_label = tk.Label(self)
        self.Teacher_Last_name_Entry_bg_label.configure(background='#121212',
                                                        borderwidth='0',
                                                        image=self.img_TeacherRegiusterEntery)
        self.Teacher_Last_name_Entry_bg_label.place(anchor='nw',
                                                    x='386',
                                                    y='196')

        self.Teacher_age_Entry_bg_label = tk.Label(self)
        self.Teacher_age_Entry_bg_label.configure(background='#121212',
                                                  borderwidth='0',
                                                  image=self.img_TeacherRegiusterEntery)
        self.Teacher_age_Entry_bg_label.place(anchor='nw',
                                              x='386',
                                              y='246')

        self.Teacher_phone_number_Entry_bg_label = tk.Label(self)
        self.Teacher_phone_number_Entry_bg_label.configure(background='#121212',
                                                           borderwidth='0',
                                                           image=self.img_TeacherRegiusterEntery)
        self.Teacher_phone_number_Entry_bg_label.place(anchor='nw',
                                                       x='386',
                                                       y='290')

        self.Teacher_Subject_Entry_bg_label = tk.Label(self)
        self.Teacher_Subject_Entry_bg_label.configure(background='#121212',
                                                      borderwidth='0',
                                                      image=self.img_TeacherRegiusterEntery)
        self.Teacher_Subject_Entry_bg_label.place(anchor='nw',
                                                  x='386',
                                                  y='390')

        self.Teacher_first_name_entry = tk.Entry(self)
        self.Teacher_first_name_entry.configure(borderwidth='0')
        self.Teacher_first_name_entry.configure(font='{Poppins} 10 {bold}',
                                                insertwidth='1',
                                                relief='flat')
        self.Teacher_first_name_entry.place(anchor='nw',
                                            height='24',
                                            width='229',
                                            x='395',
                                            y='149')

        self.Teacher_first_name_label = tk.Label(self)
        self.Teacher_first_name_label.configure(background='#121212',
                                                font='{Poppins} 17 {bold}',
                                                foreground='#ffffff',
                                                text='First Name')
        self.Teacher_first_name_label.place(anchor='nw',
                                            x='166',
                                            y='146')

        self.Teacher_last_name_entry = tk.Entry(self)
        self.Teacher_last_name_entry.configure(borderwidth='0')
        self.Teacher_last_name_entry.configure(font='{Poppins} 10 {bold}',
                                               insertwidth='1',
                                               relief='flat')
        self.Teacher_last_name_entry.place(anchor='nw',
                                           height='24',
                                           width='229',
                                           x='397',
                                           y='199')

        self.Teacher_last_name_label = tk.Label(self)
        self.Teacher_last_name_label.configure(background='#121212',
                                               font='{Poppins} 17 {bold}',
                                               foreground='#ffffff',
                                               text='Last Name')
        self.Teacher_last_name_label.place(anchor='nw',
                                           x='166',
                                           y='198')

        self.Teacher_phone_number_entry = tk.Entry(self)
        self.Teacher_phone_number_entry.configure(borderwidth='0')
        self.Teacher_phone_number_entry.configure(font='{Poppins} 10 {bold}',
                                                  insertwidth='1',
                                                  relief='flat')
        self.Teacher_phone_number_entry.place(anchor='nw',
                                              height='24',
                                              width='229',
                                              x='397',
                                              y='293')

        self.Teacher_phone_number_label = tk.Label(self)
        self.Teacher_phone_number_label.configure(background='#121212',
                                                  font='{Poppins} 17 {bold}',
                                                  foreground='#ffffff',
                                                  text='Phone number')
        self.Teacher_phone_number_label.place(anchor='nw',
                                              x='166',
                                              y='289')

        self.Teacher_age_entry = tk.Entry(self)
        self.Teacher_age_entry.configure(borderwidth='0')
        self.Teacher_age_entry.configure(font='{Poppins} 10 {bold}',
                                         insertwidth='1',
                                         relief='flat')
        self.Teacher_age_entry.place(anchor='nw',
                                     height='24',
                                     width='229',
                                     x='395',
                                     y='249')

        self.Teacher_age_label = tk.Label(self)
        self.Teacher_age_label.configure(background='#121212',
                                         font='{Poppins} 17 {bold}',
                                         foreground='#ffffff',
                                         text='Age')
        self.Teacher_age_label.place(anchor='nw',
                                     x='166',
                                     y='239')

        self.Teacher_Admission_Number_label = tk.Label(self)
        self.Teacher_Admission_Number_label.configure(background='#121212',
                                                      font='{Poppins} 17 {bold}',
                                                      foreground='#ffffff',
                                                      text='Gender')
        self.Teacher_Admission_Number_label.place(anchor='nw',
                                                  x='166',
                                                  y='331')

        self.Teacher_Admission_Number_entry = tk.Entry(self)
        self.Teacher_Admission_Number_entry.configure(borderwidth="0")
        self.Teacher_Admission_Number_entry.configure(font='{Poppins} 10 {bold}',
                                                      insertwidth='1',
                                                      relief='flat')
        self.Teacher_Admission_Number_entry.place(anchor='nw',
                                                  height='24',
                                                  width='229',
                                                  x='395',
                                                  y='343')

        self.Teacher_subects_label = tk.Label(self)
        self.Teacher_subects_label.configure(background='#121212',
                                             font='{Poppins} 17 {bold}',
                                             foreground='#ffffff',
                                             text='Main Subject')
        self.Teacher_subects_label.place(anchor='nw',
                                         x='166',
                                         y='389')

        self.Teacher_subject_entry = tk.Entry(self)
        self.Teacher_subject_entry.configure(borderwidth="0")
        self.Teacher_subject_entry.configure(font='{Poppins} 10 {bold}',
                                             insertwidth='1',
                                             relief='flat')
        self.Teacher_subject_entry.place(anchor='nw',
                                         height='24',
                                         width='229',
                                         x='395',
                                         y='393')

        try:
            self.img_TeacherAddButton = tk.PhotoImage(file='TeacherAddButton.png')
        except Exception as e:
            messagebox.showerror("TeacherAddButton.png Missing")
            print(e)

        self.add_Teacher_button = tk.Button(self)
        self.add_Teacher_button.configure(background='#121212',
                                          activebackground='#121212',
                                          activeforeground='#121212',
                                          borderwidth='0',
                                          image=self.img_TeacherAddButton,
                                          relief='flat',
                                          command=self.clickAdd)
        self.add_Teacher_button.place(anchor='nw',
                                      x='412',
                                      y='448')

        try:
            self.img_img4 = tk.PhotoImage(file='img4.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "img_img4.png is missing")
        self.Teacher_registation_close_button = tk.Button(self)
        self.Teacher_registation_close_button.configure(activebackground='#121212',
                                                        activeforeground='#121212',
                                                        background='#121212',
                                                        borderwidth='0')
        self.Teacher_registation_close_button.configure(cursor='hand2',
                                                        foreground='#121212',
                                                        highlightbackground='#121212',
                                                        highlightcolor='#121212')
        self.Teacher_registation_close_button.configure(highlightthickness='1',
                                                        image=self.img_img4,
                                                        relief='flat',
                                                        command=self.master.on_close)
        self.Teacher_registation_close_button.place(anchor='nw',
                                                    x='760',
                                                    y='8')

        self.Register_Teacher_label = tk.Label(self)
        self.Register_Teacher_label.configure(background='#121212',
                                              borderwidth='0',
                                              font='{Poppins} 28 {bold}',
                                              foreground='#ffffff')
        self.Register_Teacher_label.configure(text='Register Teacher')
        self.Register_Teacher_label.place(anchor='nw',
                                          x='274',
                                          y='28')

        self.Teacher_back_page_img_button = tk.Button(self)

        try:
            self.Teacer_img_BackPageIMG = tk.PhotoImage(file='BackPageIMG.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "BackPageIMG.png is missing")

        self.Teacher_back_page_img_button.configure(activebackground='#121212',
                                                    activeforeground='#121212',
                                                    background='#121212',
                                                    borderwidth='0',
                                                    command=self.goBackToTeacherHome)
        self.Teacher_back_page_img_button.configure(image=self.Teacer_img_BackPageIMG)
        self.Teacher_back_page_img_button.place(anchor='nw', x='15', y='15')

        self.Teacher_registation_theme_change_button = tk.Button(self)

        try:
            self.Teacher_img_DarkThemeimg = tk.PhotoImage(file='DarkThemeimg.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "DarkThemeimg.png is missing")

        self.Teacher_registation_theme_change_button.configure(activebackground='#121212',
                                                               activeforeground='#121212',
                                                               background='#121212',
                                                               borderwidth='0',
                                                               relief="flat",
                                                               overrelief="flat",
                                                               command=self.changeTeacherRegistationTheme)
        self.Teacher_registation_theme_change_button.configure(image=self.Teacher_img_DarkThemeimg,
                                                               text='button2')
        self.Teacher_registation_theme_change_button.place(anchor='nw',
                                                           x='60',
                                                           y='10')
        self.configure(background='#121212',
                       borderwidth='0',
                       height='515',
                       width='791')
        self.place(x="0", y="0")

    def changeTeacherRegistationTheme(self):
        self.master.switch_frame(LightTeacherRegistation)
        # try:
        #     self.Teacher_img_DarkThemeimg = tk.PhotoImage(file='DarkThemeimg.png')
        # except Exception as e:
        #     print(e)
        #     messagebox.showerror("File Missing", "DarkThemeimg.png IS Missing")

        # try:
        #     self.Teacher_img_lightThemeimg = tk.PhotoImage(file='LightThemeimg.png')
        # except Exception as e:
        #     print(e)
        #     messagebox.showerror("File Missing", "LightThemeimg.png IS Missing")

        # if self.Teacher_back_page_img_button["background"] == "#121212":
        #     self.TeacherRegistationBGColor = "#ffffff"
        #     self.TeacherRegistationFGColor = "#000000"
        #     self.configure(background=self.TeacherRegistationBGColor)
        #     self.Teacher_element_img_label.configure(background=self.TeacherRegistationBGColor,
        #                                              foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_First_name_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
        #                                                      foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_Last_name_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
        #                                                     foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_age_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
        #                                               foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_phone_number_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
        #                                                        foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_phone_number_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
        #                                                        foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_Admission_Number_label.configure(background=self.TeacherRegistationBGColor,
        #                                                   foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_subects_label.configure(background=self.TeacherRegistationBGColor,
        #                                          foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_first_name_entry.configure(background=self.TeacherRegistationBGColor,
        #                                             foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_Admission_Number_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
        #                                                            foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_First_name_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
        #                                                      foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_Last_name_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
        #                                                     foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_age_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
        #                                               foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_phone_number_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
        #                                                        foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_Subject_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
        #                                                   foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_first_name_label.configure(background=self.TeacherRegistationBGColor,
        #                                             foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_last_name_entry.configure(background=self.TeacherRegistationBGColor,
        #                                            foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_last_name_label.configure(background=self.TeacherRegistationBGColor,
        #                                            foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_phone_number_entry.configure(background=self.TeacherRegistationBGColor,
        #                                               foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_phone_number_label.configure(background=self.TeacherRegistationBGColor,
        #                                               foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_age_entry.configure(background=self.TeacherRegistationBGColor,
        #                                      foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_age_label.configure(background=self.TeacherRegistationBGColor,
        #                                      foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_Admission_Number_entry.configure(background=self.TeacherRegistationBGColor,
        #                                                   foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_Admission_Number_label.configure(background=self.TeacherRegistationBGColor,
        #                                                   foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_subject_entry.configure(background=self.TeacherRegistationBGColor,
        #                                          foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_subects_label.configure(background=self.TeacherRegistationBGColor,
        #                                          foreground=self.TeacherRegistationFGColor)
        #     self.add_Teacher_button.configure(background=self.TeacherRegistationBGColor,
        #                                       foreground=self.TeacherRegistationFGColor,
        #                                       activebackground=self.TeacherRegistationBGColor,
        #                                       activeforeground=self.TeacherRegistationBGColor)
        #     self.Teacher_Subject_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
        #                                                   foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_registation_close_button.configure(background=self.TeacherRegistationBGColor,
        #                                                     foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_phone_number_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
        #                                                        foreground=self.TeacherRegistationFGColor)
        #     self.Register_Teacher_label.configure(background=self.TeacherRegistationBGColor,
        #                                           foreground=self.TeacherRegistationFGColor)
        #     self.Teacher_back_page_img_button.configure(background=self.TeacherRegistationBGColor,
        #                                                 foreground=self.TeacherRegistationFGColor,
        #                                                 activebackground=self.TeacherRegistationBGColor,
        #                                                 activeforeground=self.TeacherRegistationBGColor)
        #     self.Teacher_registation_theme_change_button.configure(background=self.TeacherRegistationBGColor,
        #                                                            foreground=self.TeacherRegistationFGColor,
        #                                                            activebackground=self.TeacherRegistationBGColor,
        #                                                            activeforeground=self.TeacherRegistationBGColor,
        #                                                            image=self.Teacher_img_lightThemeimg)
        # else:
        #     self.DTeacherRegistationBGColor = "#121212"
        #     self.DTeacherRegistationFGColor = "#ffffff"
        #     self.configure(background=self.DTeacherRegistationBGColor)
        #     self.Teacher_element_img_label.configure(background=self.DTeacherRegistationBGColor,
        #                                              foreground=self.DTeacherRegistationFGColor)
        #     self.Teacher_First_name_Entry_bg_label.configure(background=self.DTeacherRegistationBGColor,
        #                                                      foreground=self.DTeacherRegistationFGColor)
        #     self.Teacher_Last_name_Entry_bg_label.configure(background=self.DTeacherRegistationBGColor,
        #                                                     foreground=self.DTeacherRegistationFGColor)
        #     self.Teacher_age_Entry_bg_label.configure(background=self.DTeacherRegistationBGColor,
        #                                               foreground=self.DTeacherRegistationFGColor)
        #     self.Teacher_phone_number_Entry_bg_label.configure(background=self.DTeacherRegistationBGColor,
        #                                                        foreground=self.DTeacherRegistationFGColor)
        #     self.Teacher_Subject_Entry_bg_label.configure(background=self.DTeacherRegistationBGColor,
        #                                                   foreground=self.DTeacherRegistationFGColor)
        #     self.Teacher_first_name_label.configure(background=self.DTeacherRegistationBGColor,
        #                                             foreground=self.DTeacherRegistationFGColor)
        #     self.Teacher_last_name_label.configure(background=self.DTeacherRegistationBGColor,
        #                                            foreground=self.DTeacherRegistationFGColor)
        #     self.Teacher_phone_number_label.configure(background=self.DTeacherRegistationBGColor,
        #                                               foreground=self.DTeacherRegistationFGColor)
        #     self.Teacher_age_label.configure(background=self.DTeacherRegistationBGColor,
        #                                      foreground=self.DTeacherRegistationFGColor)
        #     self.Teacher_Admission_Number_label.configure(background=self.DTeacherRegistationBGColor,
        #                                                   foreground=self.DTeacherRegistationFGColor)
        #     self.Teacher_subects_label.configure(background=self.DTeacherRegistationBGColor,
        #                                          foreground=self.DTeacherRegistationFGColor)
        #     self.add_Teacher_button.configure(background=self.DTeacherRegistationBGColor,
        #                                       foreground=self.DTeacherRegistationFGColor,
        #                                       activebackground=self.DTeacherRegistationBGColor,
        #                                       activeforeground=self.DTeacherRegistationBGColor)
        #     self.Teacher_registation_close_button.configure(background=self.DTeacherRegistationBGColor,
        #                                                     foreground=self.DTeacherRegistationFGColor)
        #     self.Register_Teacher_label.configure(background=self.DTeacherRegistationBGColor,
        #                                           foreground=self.DTeacherRegistationFGColor)
        #     self.Teacher_back_page_img_button.configure(background=self.DTeacherRegistationBGColor,
        #                                                 foreground=self.DTeacherRegistationFGColor)
        #     self.Teacher_Admission_Number_Entry_bg_label.configure(background=self.DTeacherRegistationBGColor,
        #                                                            foreground=self.DTeacherRegistationFGColor)
        #     self.Teacher_First_name_Entry_bg_label.configure(background=self.DTeacherRegistationBGColor,
        #                                                      foreground=self.DTeacherRegistationFGColor)
        #     self.Teacher_Last_name_Entry_bg_label.configure(background=self.DTeacherRegistationBGColor,
        #                                                     foreground=self.DTeacherRegistationFGColor)
        #     self.Teacher_age_Entry_bg_label.configure(background=self.DTeacherRegistationBGColor,
        #                                               foreground=self.DTeacherRegistationFGColor)
        #     self.Teacher_phone_number_Entry_bg_label.configure(background=self.DTeacherRegistationBGColor,
        #                                                        foreground=self.DTeacherRegistationFGColor)
        #     self.Teacher_Subject_Entry_bg_label.configure(background=self.DTeacherRegistationBGColor,
        #                                                   foreground=self.DTeacherRegistationFGColor)
        #     self.Teacher_registation_theme_change_button.configure(background=self.DTeacherRegistationBGColor,
        #                                                            foreground=self.DTeacherRegistationFGColor,
        #                                                            activebackground=self.DTeacherRegistationBGColor,
        #                                                            activeforeground=self.DTeacherRegistationBGColor,
        #                                                            image=self.Teacher_img_DarkThemeimg)

    def goBackToTeacherHome(self):
        self.master.switch_frame(DarkTeacherHome)


##################################################Click Add Button##########################################################################
    def clickAdd(self):
        ####################################################Clear###########################################################
        self.Clearerrors()
        self.ClearCommited()
        ######################################################################################################################
        #***********************************************************************************************************************#

        ##############################################Create variabals##########################################################
        global Teacher_first_name, Teacher_last_name, Teacher_phone_number, Teacher_age, Teacher_Admission_Number, Teacher_subjects
         #^^^^^^This is All variabels

        Teacher_first_name = self.Teacher_first_name_entry.get()

        Teacher_last_name = self.Teacher_last_name_entry.get()

        Teacher_phone_number = self.Teacher_phone_number_entry.get()

        Teacher_age = self.Teacher_age_entry.get()

        Teacher_Admission_Number = self.Teacher_Admission_Number_entry.get()

        Teacher_subjects = self.Teacher_subject_entry.get()

        Update_gender = Teacher_Admission_Number

        Update_subjects = Teacher_subjects


        #*******************************************************************************************************************

#*******************************************************************************************************************
###############################################Check All Fields Are Empty###########################################
        if Teacher_first_name == "" or Teacher_last_name == "" or Teacher_phone_number == "" or Teacher_age == "" or Update_gender == "" or Update_subjects == "":
            ##############################Clear All Erorr##################################
            try:
                self.Clearerrors()
            except:
                pass            
            #################################Distroy Student First Name########################
            #################################Place The Erorr###################################
            try:
                self.AllFildsRequiredErorr()
            except:
                pass
            
        else:
            ################################Distroy All Fields Erorr########################
            try:
                self.AllFildsRequiredErorrDestroy()
            except:
                pass
            if len(Teacher_first_name) > 50:
                #####################First Name Too long Error###########################
                self.FirstNameErorr()
            else:
                Teacher_first_name.capitalize()

                ############################Distroy First name Error##########################
                try:
                    self.Studetn_First_Name_error_label.destroy()
                except:
                    pass
                ##########################################Cehck Student Last name Lenth########################
                if len(Teacher_last_name) > 50:
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

                    Teacher_last_name.capitalize()                              
                    if Teacher_first_name.capitalize() == Teacher_last_name.capitalize():
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
                         ################################Numeber Lenth Check########################################
                        if len(Teacher_phone_number) != 10:
                            
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



#******************************************************************************************************************#
###################################################### place Studetn_Phone_Number_No_error_label####################
                            # self.PhoneNumberLenthNoErorr()

                                           ###############This  Place tick############## 
######################################################Check Phone Number Error##########################
#******************************************************************************************************#

                            try:
                                int(Teacher_phone_number)
                            except :
                                pass
                                # messagebox.showerror("Type Error", "You Can Only Type Numbers For Phone Number ")
                            if type(int(Teacher_phone_number)) != int:

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
                                if int(Teacher_phone_number[0]) != 0:
                                    #messagebox.showerror("Type Error", "This is Not Phone Number")
                                    #*************************************************************************************************************#
###############################################Distroy Phone Nimbers###########################################
                                    try:
                                        self.clearAllPhoneErors()
                                    except:
                                        pass
##############################################Place Error##############################################
                                    try:                                    
                                        self.PhoneNumberZeroError()
                                    except:
                                        pass
####################################################################################################### 
                                else:
                                    ##################Clear Zero Errors###############################
                                    try:
                                        self.ClearPhoneNumberZeroError()
                                    except:
                                        pass
                                    
                                    if len(Teacher_age) > 2:
                                        # messagebox.showerror("Age Error", "You Can Only Type Two Numbers For Age ")
                                        ################################NEW AGE #######################################
                                        self.AgeError()
                                        ###############################################################################
                                    else:
                                        #############################Clear Age Error#####################################
                                        try:
                                            self.ClearAgeError()
                                        except:
                                            pass
                                        #################################################################################
                                        genderIndex = ['male', "Male", "female", "Female", "m", "M", "F", "f"]
                                        if Update_gender not in genderIndex:
                                            # messagebox.showerror("Age Error", "You Can Add Only Type Male or Female ")
                                            self.GenderError()
                                        else:
                                            try:
                                                self.ClearGenderError()
                                            except:
                                                pass
                                            if Update_gender == "m" or Update_gender == "male":
                                                Update_gender = "Male"
                                            else:
                                                Update_gender = "Female"

                                            
                                            AllSubjects = ['Sinhala', 'SINHALA', 'Sin', 'sin',
                                                        'Tamil', 'tamil', 'tam', 'Tam',
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

                                            subject_list = Update_subjects.split(",")

                                            checkSubject = all(item in AllSubjects for item in Update_subjects.split(","))
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

                                                self.connetc = self.conn.cursor()
                                                self.connetc.execute(
                                                "CREATE TABLE IF NOT EXISTS teacher (id INT AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(50), LAstName VARCHAR(50), PhoneNumber INT(50), Age INT(2), Gender VARCHAR(10) ,Subjects VARCHAR(255) )")
                                                self.connetc.execute(
                                                    "INSERT INTO  teacher (FirstName, LAstName, PhoneNumber, Age, Gender, Subjects) VALUES (%s,%s,%s,%s,%s,%s)",
                                                    (str(Teacher_first_name.capitalize()), str(Teacher_last_name.capitalize()),
                                                    0 + int(Teacher_phone_number), int(Teacher_age),
                                                    str(Update_gender),
                                                    str(Update_subjects.capitalize())))
                                                # self.connetc.execute()
                                                self.conn.commit()
                                                self.clearTeacherRegistation()
                                                self.connetc.close()
                                                self.conn.close()
                                                # self.master.switch_frame(TeacherView)
                                                self.Commited()
#################################################################################################################                                

    def clearTeacherRegistation(self):
        self.Teacher_first_name_entry.delete(0, 'end')
        self.Teacher_subject_entry.delete(0, 'end')
        self.Teacher_last_name_entry.delete(0, 'end')
        self.Teacher_Admission_Number_entry.delete(0, 'end')
        self.Teacher_age_entry.delete(0, 'end')
        self.Teacher_phone_number_entry.delete(0, 'end')

    def Clearerrors(self):
        try:
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
            self.ClearGenderError()
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
        self.Studetn_All_Fields_Required_error_label.configure(background='#121212',
                                                    borderwidth='0',
                                                    font='{Poppins} 9 {}',
                                                    foreground='#ff0f15')
        self.Studetn_All_Fields_Required_error_label.configure(text='All Fields Are Required')
        self.Studetn_All_Fields_Required_error_label.place(anchor='nw',
                                                x='500',
                                                y='123')

    def AllFildsRequiredErorrDestroy(self):
        try:
            self.Studetn_All_Fields_Required_error_label.destroy()
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
        self.Studetn_First_Name_error_label.configure(background='#121212',
                                                    borderwidth='0',
                                                    font='{Poppins} 9 {}',
                                                    foreground='#ff0f15')
        self.Studetn_First_Name_error_label.configure(text='First Name Is Too Long')
        self.Studetn_First_Name_error_label.place(anchor='nw',
                                                x='500',
                                                y='123')
    
    def FirstNameNoErorr(self):
        try:
 ##############################Distroy Studetn_First_Name_error_label#######################
            self.Studetn_First_Name_error_label.destroy()
        except:
            pass

                ####################################Place Studetn_First_Name_No_error_label######################
            self.Studetn_First_Name_No_error_label = tk.Label(self)
            self.Studetn_First_Name_No_error_label.configure(background='#121212',
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
        self.Studetn_Last_Name_error_label.configure(background='#121212',
                                                        borderwidth='0',
                                                        font='{Poppins} 8 {}',
                                                        foreground='#ff0f15')
        self.Studetn_Last_Name_error_label.configure(text='Last Name Is Too Long')
        self.Studetn_Last_Name_error_label.place(anchor='nw',
                                                    x='500',
                                                    y='174')

    def ClearLastNameError(self):
        try:
            self.Studetn_Last_Name_error_label.destroy()

        except:
            pass

    def NoLastNameError(self):
        self.Studetn_Last_Name_No_error_label = tk.Label(self)
        self.Studetn_Last_Name_No_error_label.configure(background='#121212',
                                                        borderwidth='0',
                                                        font='{Poppins} 8 {}',
                                                        foreground='#09ff00')
        self.Studetn_Last_Name_No_error_label.configure(text=""+u'\u2713')
        self.Studetn_Last_Name_No_error_label.place(anchor='nw',
                                                    x='610',
                                                    y='174')

    def NoDuplicateNameError(self):
        self.Studetn_Duplicate_Name_No_error_label = tk.Label(self)
        self.Studetn_Duplicate_Name_No_error_label.configure(background='#121212',
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
        self.Studetn_Duplicate_Name_error_label.configure(background='#121212',
                                                            borderwidth='0',
                                                            font='{Poppins} 8 {}',
                                                            foreground='#ff0f15')
        self.Studetn_Duplicate_Name_error_label.configure(text='Name Duplicated')
        self.Studetn_Duplicate_Name_error_label.place(anchor='nw',
                                                        x='500',
                                                        y='174')
    
    def ClearNameDuplicatedErorr(self):

        try:
            self.Studetn_Duplicate_Name_error_label.destroy()

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
        self.Studetn_lenth_Phone_number_error_label.configure(background='#121212',
                                                                borderwidth='0',
                                                                font='{Poppins} 7 {}',
                                                                foreground='#ff0f15')
        self.Studetn_lenth_Phone_number_error_label.configure(text='Not Phone Number')
        self.Studetn_lenth_Phone_number_error_label.place(anchor='nw',
                                                            x='500',
                                                            y='274')
        #########################################################################

    def ClearPhoneNumberLenthErorr(self):

        ##################DISTROY PHONE NUMBER ERROR###################
        try:
            self.Studetn_lenth_Phone_number_error_label.destroy()
        except:
            pass
        ##############################################################

    def PhoneNumberLenthNoErorr(self):

        ####################NO ERROR PHONE NUMBER LENTH######################
        self.Studetn_lenth_Phone_Number_No_error_label = tk.Label(self)
        self.Studetn_lenth_Phone_Number_No_error_label.configure(background='#121212',
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
        self.Studetn_int_Phone_number_error_label.configure(background='#121212',
                                                                    borderwidth='0',
                                                                    font='{Poppins} 7 {}',
                                                                    foreground='#ff0f15')
        self.Studetn_int_Phone_number_error_label.configure(text='Type Number')
        self.Studetn_int_Phone_number_error_label.place(anchor='nw',
                                                                x='500',
                                                                y='274')
        ########################################################################


    def ClearPhoneNumberTypeErorr(self):
        ###############PHONE NUMBER CLEAR#################
        try:
            self.Studetn_int_Phone_number_error_label.destroy()
        except:
            pass
        ##################################################

    def PhoneNumberNoTypeErorr(self):

        #####################PHONE NUMBER TYPE ERROR##############
        self.Studetn_int_Phone_Number_No_error_label = tk.Label(self)
        self.Studetn_int_Phone_Number_No_error_label.configure(background='#121212',
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
        self.Studetn_0_Phone_number_error_label.configure(background='#121212',
                                                                        borderwidth='0',
                                                                        font='{Poppins} 7 {}',
                                                                        foreground='#ff0f15')
        self.Studetn_0_Phone_number_error_label.configure(text='Invalid Phone Number')
        self.Studetn_0_Phone_number_error_label.place(anchor='nw',
                                                                    x='500',
                                                                    y='274')
        ############################################################

    def ClearPhoneNumberZeroError(self):
        ##########CLEAR PHONE NUMBER###############################
        try:
            self.Studetn_0_Phone_number_error_label.configure(background='#121212',
                                                                        borderwidth='0',
                                                                        font='{Poppins} 0 {}',
                                                                        foreground='#121212')
            self.Studetn_0_Phone_number_error_label.destroy()
        except:
            pass
        ##########################################################

    def PhoneNumberNoZeroError(self):

        #################PHONE NUMBER ZERO NO ERROR################################
        self.Studetn_0_Phone_Number_No_error_label = tk.Label(self)
        self.Studetn_0_Phone_Number_No_error_label.configure(background='#121212',
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
            self.Studetn_Age_error_label.configure(background='#121212',
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
        except:
            pass
        ###############################################################

    def AgeNoError(self):

        #################PHONE NUMBER ZERO NO ERROR################################
        self.Studetn_Age_No_error_label = tk.Label(self)
        self.Studetn_Age_No_error_label.configure(background='#121212',
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
    

    def DatabaseNotConnectedError(self):
        ###############AGE Error##################################
        try:
            self.Database_not_Connected_error_label = tk.Label(self)
            self.Database_not_Connected_error_label.configure(background='#121212',
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
            self.Studetn_Subject_error_label.configure(background='#121212',
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

    def ClearSubjectError(self):
        try:
            self.Studetn_Subject_error_label.destroy()
        except:
            pass

    def Commited(self):
        ###############AGE Error##################################
        try:
            self.Comited_label = tk.Label(self)
            self.Comited_label.configure(background='#121212',
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

    def ClearCommited(self):
        try:
            self.Comited_label.destroy()
        except:
            pass
    
    def GenderError(self):
        ###############AGE Error##################################
        try:
            self.Gender_Error_label = tk.Label(self)
            self.Gender_Error_label.configure(background='#121212',
                                                                            borderwidth='0',
                                                                            font='{Poppins} 8 {}',
                                                                            foreground='#ff0f15')
            self.Gender_Error_label.configure(text='invalid gender')
            self.Gender_Error_label.place(anchor='nw',
                                                                        x='500',
                                                                        y='320')
        except:
            pass
        ####################################################################

    def ClearGenderError(self):
        try:
            self.Gender_Error_label.destroy()
        except:
            pass

