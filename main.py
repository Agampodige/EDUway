#**********************************************************************************#
#################Copyrigh@Rashith Senishka De Silva#################################

##########################################Import Sys##################################
import sys

###################################Import Time For Splash Screen#############
import time

##################Import ttk for Treeview##############################
import tkinter.ttk as ttk

##################Import massage for errors
from tkinter import messagebox

###################Cheking Python vertion for import tkinter######################
if sys.version_info[0] == 2:
#####################import tkinter if python vertion is old###########################
    import Tkinter as tk
else:
    import tkinter as tk
############################Import mysql for connect db###################################

import mysql.connector
##############################




            #############################
            ################################
            ##################################
            ########               ############
            ########               ############
            ########               ###########
            ########              ###########
            ########            ############
            ########          ###########
            ########        ##########
            ###################
            ########    #########      
            ########     #########
            ########         ########
            ########            #######
            ########            ######





################################## This_is_the_back_ground_color_of_loging_page####################
background_color = '#1f1f1f'

TeacherRegistationTheme = "#121212"

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
###############################this is the app#####################################################################
class SchoolManegmentSystem(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None

####################################### this is the page first load#################################################
        self.switch_frame(StudentRegistation)



####################################################This is the funtion for switch##################################

    # this_funtion_is_for_change
    # the frame == window of the app
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def on_close(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.quit()
            app.quit()
            app.destroy()
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
########################################## This is the splash screen###############################################
####################################### this_is_the_Splash_Screen_of_this##########################################
################################################# App #############################################################
class SplashScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # this_is_the_splash_button
        # it_will_return_you_to_log_in_page

        # self.splash_button = tk.Button(self)

        try:
            self.img_splash = tk.PhotoImage(file='splash.png')
        except Exception as e:
            print(e)
            messagebox.showerror("Image Missing", "splash.png is missing")

        # self.splash_button.configure(activebackground='#ffffff',
        #                              activeforeground='#ffffff',
        #                              background='#ffffff',
        #                              borderwidth='0')
        # self.splash_button.configure(cursor='wait',
        #                              disabledforeground='#ffffff',
        #                              foreground='#ffffff',
        #                              highlightbackground='#ffffff')
        # self.splash_button.configure(highlightcolor='#ffffff',
        #                              highlightthickness='0',
        #                              image=self.img_splash,
        #                              overrelief='flat')
        # ###################################################this_funtion_is_for_change_the_sopash_page_to_login_page
        # self.splash_button.configure(relief='flat',
        #                              text='button1',
        #                              command=lambda: master.switch_frame(LogInPage))
        # self.splash_button.pack(side='top')

        self.configure(height='515',
                       width='791',
                       background="#090D10")
        self.Splash_Bg_img = tk.Label()

        self.Splash_Bg_img.configure(image=self.img_splash, borderwidth='0', relief='flat')
        self.Splash_Bg_img.place(x='0', y='0')

        self.after(3000, lambda: master.switch_frame(LogInPage))

        self.place(x='0', y='0')
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#





#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
#######################################################This is the login page######################################
class LogInPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # this_is_the_background_of_the_login_page
        # it_will_can_change_the_theme_and_theme_change_button
        self.backg = tk.Label(self)

        try:
            self.img_background = tk.PhotoImage(file='background.png')
        except Exception as e:
            print(e)
            messagebox.showerror("Image Missing", "backfround.png is missing")

        self.backg.configure(background=background_color,
                             borderwidth='0',
                             cursor='arrow',
                             font='TkDefaultFont',
                             image=self.img_background)
        self.backg.configure(relief='flat')
        self.backg.place(x='0',
                         y='0')

        # This_is_a_normal_lable_to_show_the_Lable_in_the_log_in_window
        # some_time_the_font(POPPINS)_Work_like_unecpected_ !!!!WORNING!!
        # Will_nees_to_fix_it
        self.loginlabel = tk.Label(self)
        self.loginlabel.configure(anchor='n',
                                  background='#0F0F0F',
                                  compound='top',
                                  font='{Poppins} 23 {bold}')
        self.loginlabel.configure(foreground='#ffffff',
                                  justify='center',
                                  relief='flat',
                                  text='LOGIN')
        self.loginlabel.place(anchor='nw',
                              x='460',
                              y='70')

        # This_is_a_normal_lable_to_show_the_'"Username"'_in_the_log_in_window
        self.usernamelabel = tk.Label(self)
        self.usernamelabel.configure(background='#0F0F0F',
                                     font='{Poppins} 12 {bold}',
                                     foreground='#EFEFEF',
                                     relief='flat')
        self.usernamelabel.configure(text='USERNAME')
        self.usernamelabel.place(anchor='nw',
                                 x='390',
                                 y='150')

        ## This_is_a_normal_lable_to_show_the_background_of_Entry_box
        self.input_field_bg = tk.Label(self)

        try:
            self.img_img_textBox0 = tk.PhotoImage(file='img_textBox0.png')
        except Exception as e:
            print(e)
            messagebox.showerror("Image Missing", "img_textBox0.png is missing")

        self.input_field_bg.configure(background='#0F0F0F',
                                      image=self.img_img_textBox0,
                                      relief='flat')
        self.input_field_bg.place(anchor='nw',
                                  x='373',
                                  y='177')

        # This_is_a_normal_lable_to_show_the_'"PASSWORD"'_in_the_log_in_window
        self.password_label = tk.Label(self)
        self.password_label.configure(background='#0F0F0F',
                                      font='{Poppins} 12 {bold}',
                                      foreground='#EFEFEF',
                                      relief='flat')
        self.password_label.configure(text='PASSWORD')
        self.password_label.place(anchor='nw',
                                  x='380',
                                  y='240')

        ## This_is_a_normal_lable_to_show_the_background_of_Entry_box
        self.input_field_bg_2 = tk.Label(self)
        self.input_field_bg_2.configure(background='#0F0F0F',
                                        image=self.img_img_textBox0,
                                        relief='flat')
        self.input_field_bg_2.place(anchor='nw',
                                    x='373',
                                    y='265')

        # this_button_is_for_check_Usename&&Password_and return home_page
        self.login_button = tk.Button(self)

        try:
            self.img_img0 = tk.PhotoImage(file='img0.png')
        except Exception as e:
            print(e)
            messagebox.showerror("Image Missing", "img0.png is missing")

        self.login_button.configure(activebackground='#0F0F0F',
                                    activeforeground='#0F0F0F',
                                    background='#0F0F0F',
                                    borderwidth='0')
        self.login_button.configure(cursor='hand2',
                                    disabledforeground='#0F0F0F',
                                    foreground='#0F0F0F',
                                    highlightbackground='#0F0F0F',
                                    command=self.login_check)
        self.login_button.configure(highlightcolor='#0F0F0F',
                                    image=self.img_img0,
                                    relief='flat')
        self.login_button.place(anchor='nw',
                                x='405',
                                y='365')

        # Uuser_name_input_field
        self.username_input_field = tk.Entry(self)
        self.username_input_field.configure(background='#9BFFED',
                                            font='{Poppins} 12 {bold}',
                                            insertbackground='#0F0F0F',
                                            insertborderwidth='3')
        self.username_input_field.configure(insertwidth='2',
                                            relief='flat')
        self.username_input_field.place(anchor='nw',
                                        height='40',
                                        x='389',
                                        y='180')

        # password_input_Field
        self.password_input_field = tk.Entry(self)
        self.password_input_field.configure(background='#9BFFED',
                                            font='{Poppins} 12 {bold}',
                                            insertbackground='#0F0F0F',
                                            insertborderwidth='3')
        self.password_input_field.configure(insertwidth='2',
                                            relief='flat',
                                            show='•')
        self.password_input_field.place(anchor='nw',
                                        height='40',
                                        x='389',
                                        y='268')
        self.close_button = tk.Button(self)
        try:
            self.img_img4 = tk.PhotoImage(file='img4.png')
        except Exception as e:
            print(e)
            messagebox.showerror("Image Missing", "img4.png is missing")

        # this is the close button of login page
        self.close_button.configure(activebackground='#000000',
                                    activeforeground='#000000',
                                    background='#000000',
                                    borderwidth='0')
        self.close_button.configure(compound='top',
                                    cursor='hand2',
                                    disabledforeground='#000000',
                                    foreground='#000000')
        self.close_button.configure(highlightbackground='#000000',
                                    highlightcolor='#000000',
                                    highlightthickness='0',
                                    image=self.img_img4)
        self.close_button.configure(overrelief='flat',
                                    relief='flat',
                                    command=self.master.on_close)
        self.close_button.place(anchor='nw',
                                x='730',
                                y='15')

        # this_clear_button_is_for_clear_All_input_fields
        self.clear_btton = tk.Button(self)
        try:
            self.img_img1 = tk.PhotoImage(file='img1.png')
        except Exception as e:
            print(e)
            messagebox.showerror("Image Missing", "img1.png is missing")

        self.clear_btton.configure(activebackground='#0F0F0F',
                                   activeforeground='#0F0F0F',
                                   background='#0F0F0F',
                                   borderwidth='0')
        self.clear_btton.configure(compound='top', cursor='hand2',
                                   disabledforeground='#0F0F0F',
                                   foreground='#0F0F0F')
        self.clear_btton.configure(highlightbackground='#0F0F0F',
                                   highlightcolor='#0F0F0F',
                                   highlightthickness='0',
                                   image=self.img_img1)
        self.clear_btton.configure(overrelief='flat',
                                   relief='flat',
                                   command=self.clearLogin)
        self.clear_btton.place(anchor='nw',
                               x='600',
                               y='80')

        # this_Button_is for Change_the_color_Theme
        # self.theme_change_button = tk.Button(self)
        # try:
        #     self.img_img3 = tk.PhotoImage(file='DarkThemeimg.png')
        # except Exception as e:
        #     messagebox.showerror("Image Missing", "img3.png is missing")

        # self.theme_change_button.configure(activebackground='#000000',
        #                                    activeforeground='#000000',
        #                                    background='#000000',
        #                                    borderwidth='0',
        #                                    command=self.change_theme)
        # self.theme_change_button.configure(cursor='hand2',
        #                                    disabledforeground='#000000',
        #                                    foreground='#000000',
        #                                    highlightbackground='#000000')
        # self.theme_change_button.configure(highlightcolor='#000000',
        #                                    highlightthickness='0',
        #                                    image=self.img_img3,
        #                                    overrelief='flat')
        # self.theme_change_button.configure(relief='flat')
        # self.theme_change_button.place(anchor='nw',
        #                                x='735',
        #                                y='469')
        self.configure(borderwidth='0',
                       height='515',
                       relief='flat',
                       width='791')
        self.place(relx='0.0',
                   x='0',
                   y='0')
        self.grid_propagate(0)
        self.grid_anchor('center')

    def clearLogin(self):
        self.username_input_field.delete(0, 'end')
        self.password_input_field.delete(0, 'end')
        try:
            self.password_error_label.configure(foreground="#121212")
            self.username_error_label.configure(foreground="#121212")
        except:
            pass

        try:
            self.password_empty_error_label.configure(foreground="#121212")
            self.username_empty_error_label.configure(foreground="#121212")
        except:
            pass

    # This Function is succesed
    # this funtion is for check login username and password
    # change page
    def login_check(self):
        usernamme = self.username_input_field.get()
        password = self.password_input_field.get()

        # check_the_password_and_name
        # if usernamme == 'Admin' and password == 'Admin':
        #     self.master.switch_frame(Home)
        # else:
        #
        if usernamme != "" and password != "":

            if usernamme != "Admin":
                self.username_error_label = tk.Label(self)
                self.username_error_label.configure(background='#0F0F0F',
                                                    borderwidth='0',
                                                    font='{Poppins} 9 {}',
                                                    foreground='#ff0f15')
                self.username_error_label.configure(text='Invalid Username')
                self.username_error_label.place(anchor='nw',
                                                x='500',
                                                y='150')
                self.password_error_label = tk.Label(self)

                self.password_error_label.configure(background='#0F0F0F',
                                                    borderwidth='0',
                                                    font='{Poppins} 9 {}',
                                                    foreground='#ff0f15')
                self.password_error_label.configure(text='invalid password')
                self.password_error_label.place(anchor='nw',
                                                x='500',
                                                y='232')
            else:
                if password == "Admin":
                    self.master.switch_frame(Home)
        else:
            try:
                self.password_error_label.configure(foreground="#121212")
                self.username_error_label.configure(foreground="#121212")
            except:
                pass
            self.username_empty_error_label = tk.Label(self)
            self.username_empty_error_label.configure(background='#0F0F0F',
                                                      borderwidth='0',
                                                      font='{Poppins} 9 {}',
                                                      foreground='#ff0f15')
            self.username_empty_error_label.configure(text='Enter Username')
            self.username_empty_error_label.place(anchor='nw',
                                                  x='500',
                                                  y='150')
            self.password_empty_error_label = tk.Label(self)

            self.password_empty_error_label.configure(background='#0F0F0F',
                                                      borderwidth='0',
                                                      font='{Poppins} 9 {}',
                                                      foreground='#ff0f15')
            self.password_empty_error_label.configure(text='Enter password')
            self.password_empty_error_label.place(anchor='nw',
                                                  x='500',
                                                  y='232')

    # This Function is for change the loght_theme_ to dark theme
    def change_theme(self):
        if self.backg["background"] == "#1f1f1f":
            try:
                self.img_backgroundLight = tk.PhotoImage(file="backgroundLight.png")
            except Exception as e:
                print(e)
                messagebox.showerror("Image Missing", "backgroundLight.png is missing")

            self.backg.configure(background='#ffffff', image=self.img_backgroundLight)
            try:
                self.img_img3 = tk.PhotoImage(file="LightThemeimg.png")
            except Exception as e:
                print(e)
                messagebox.showerror("Image Missing", "LightThemeimg.png is missing")
            try:
                self.theme_change_button.configure(image=self.img_img3)
            except Exception as e:
                print(e)
                messagebox.showerror("Image Missing", "img_img_3.png is missing")
        elif self.backg["background"] == "#ffffff":
            self.backg.configure(background='#1f1f1f')

            try:
                self.img_img3 = tk.PhotoImage(file="DarkThemeimg.png")
            except Exception as e:
                print(e)
                messagebox.showerror("Image Missing", "DarkThemeimg.png is missing")

            self.theme_change_button.configure(image=self.img_img3)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#


# This is a Template to create a new frame
# Copy this one fbefor use this

# class PageTwo(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
# remember_ths

# this is the home page of 
# this window is return after the Splash Screen
class Home(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        try:
            self.img_Home_Banner = tk.PhotoImage(file='HomeBanner.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "HomeBanner.png")

        self.home_banner_label = tk.Label(self)
        self.home_banner_label.configure(image=self.img_Home_Banner, background="#121212")
        self.home_banner_label.place(x="0",
                                     y="0")

        try:
            self.img_Home_Teacher = tk.PhotoImage(file='HomeTeacher.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "HomeTeacher.png")

        self.home_teacher_button = tk.Button(self)
        self.home_teacher_button.configure(image=self.img_Home_Teacher,
                                           background="#121212",
                                           borderwidth="0",
                                           relief="flat",
                                           activebackground="#121212",
                                           activeforeground="#121212",
                                           command=lambda: master.switch_frame(TeacherHome))
        self.home_teacher_button.place(x="130",
                                       y="280")

        try:
            self.img_Home_Student = tk.PhotoImage(file='HomeStudent.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "HomeStudent.png is missing")

        self.home_Student_button = tk.Button(self)
        self.home_Student_button.configure(image=self.img_Home_Student,
                                           background="#121212",
                                           borderwidth="0",
                                           relief="flat",
                                           activebackground="#121212",
                                           activeforeground="#121212",
                                           command=lambda: master.switch_frame(StudentHome))
        self.home_Student_button.place(x="319",
                                       y="280")

        try:
            self.img_Home_About_Us = tk.PhotoImage(file='HomeAboutUs.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "HomeAboutUs.png is missing")

        self.home_About_Us_button = tk.Button(self)
        self.home_About_Us_button.configure(image=self.img_Home_About_Us,
                                            background="#121212",
                                            borderwidth="0",
                                            relief="flat",
                                            activebackground="#121212",
                                            activeforeground="#121212",
                                            command=lambda: master.switch_frame(AboutMe))
        self.home_About_Us_button.place(x="508",
                                        y="280")

        self.configure(background='#121212',
                       height='515',
                       takefocus=False,
                       width='791')
        self.place(x="0",
                   y="0")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

# this is the student home
# you can do all crud operations in this Student Home
class StudentHome(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.Student_Element_2_IMG_label = tk.Label(self)

        try:
            self.img_ElementIMG2Label = tk.PhotoImage(file='ElementIMG2Label.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "ElementIMG2Label.png is missing")

        self.Student_Element_2_IMG_label.configure(activebackground='#121212',
                                                   activeforeground='#121212',
                                                   background='#121212',
                                                   borderwidth='0')
        self.Student_Element_2_IMG_label.configure(image=self.img_ElementIMG2Label, text='label1')
        self.Student_Element_2_IMG_label.place(x='0', y='0')

        try:
            self.img_TeacherHomeAddButton = tk.PhotoImage(file='TeacherHomeAddButton.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "TeacherHomeAddButton.png is missing")

        self.Student_register_button = tk.Button(self)
        self.Student_register_button.configure(borderwidth='0',
                                               background="#121212",
                                               activeforeground="#121212",
                                               activebackground="#121212",
                                               image=self.img_TeacherHomeAddButton,
                                               command=lambda: master.switch_frame(StudentRegistation))
        self.Student_register_button.place(anchor='nw',
                                           x='196',
                                           y='111')

        try:
            self.img_TeacherHomeUpdateButton = tk.PhotoImage(file='TeacherHomeUpdateButton.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "TeacherHomeView Button.png is missing")

        self.Student_update_button = tk.Button(self)
        self.Student_update_button.configure(borderwidth='0',
                                             background="#121212",
                                             activeforeground="#121212",
                                             activebackground="#121212",
                                             image=self.img_TeacherHomeUpdateButton,
                                             command=lambda: master.switch_frame(StudentUpdate))
        self.Student_update_button.place(anchor='nw',
                                         x='441',
                                         y='111')

        try:
            self.img_TeacherHomeViewButton = tk.PhotoImage(file='TeacherHomeView Button.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "TeacherHomeView Button.png is missing")

        self.Student_view_button = tk.Button(self)
        self.Student_view_button.configure(borderwidth='0',
                                           activebackground="#121212",
                                           activeforeground="#121212",
                                           background="#121212",
                                           image=self.img_TeacherHomeViewButton,
                                           command=lambda: master.switch_frame(StudentView))
        self.Student_view_button.place(anchor='nw',
                                       x='196',
                                       y='317')

        try:
            self.img_TeacherHomeRemoveButton = tk.PhotoImage(file='TeacherHomeRemoveButton.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "TeacherHomeRemoveButton.png is missing")

        self.Student_Delete_button = tk.Button(self)
        self.Student_Delete_button.configure(borderwidth='0',
                                             image=self.img_TeacherHomeRemoveButton,
                                             activeforeground="#121212",
                                             activebackground="#121212",
                                             background="#121212",
                                             command=lambda: master.switch_frame(StudentDelete))
        self.Student_Delete_button.place(anchor='nw',
                                         x='441',
                                         y='317')

        self.Manege_Student_label = tk.Label(self)
        self.Manege_Student_label.configure(background='#121212',
                                            borderwidth='0',
                                            font='{Poppins} 28 {bold}',
                                            foreground='#ffffff')
        self.Manege_Student_label.configure(text='Manage Student')
        self.Manege_Student_label.place(anchor='nw',
                                        x='267',
                                        y='28')
        try:
            self.img_img4 = tk.PhotoImage(file='img4.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "img_img4.png is missing")

        self.Student_Manege_close_button = tk.Button(self)
        self.Student_Manege_close_button.configure(activebackground='#121212',
                                                   activeforeground='#121212',
                                                   background='#121212',
                                                   borderwidth='0')
        self.Student_Manege_close_button.configure(cursor='hand2',
                                                   foreground='#121212',
                                                   highlightbackground='#121212',
                                                   highlightcolor='#121212')
        self.Student_Manege_close_button.configure(highlightthickness='1',
                                                   image=self.img_img4,
                                                   relief='flat',
                                                   command=self.master.on_close)

        self.Student_Manege_close_button.place(anchor='nw',
                                               x='760',
                                               y='8')

        self.Student_Manege_theme_change_button = tk.Button(self)

        try:
            self.img_DarkThemeimg = tk.PhotoImage(file='DarkThemeimg.png')
        except Exception as e:
            messagebox.showerror("DarkThemeimg.png Missing")
            print(e)

        self.Student_Manege_theme_change_button.configure(activebackground='#121212',
                                                          activeforeground='#121212',
                                                          background='#121212',
                                                          borderwidth='0',
                                                          command=self.changeTeacherHomeTheme)
        self.Student_Manege_theme_change_button.configure(image=self.img_DarkThemeimg)
        self.Student_Manege_theme_change_button.place(anchor='nw',
                                                      x='60',
                                                      y='10')

        self.Student_home_back_page_img_button = tk.Button(self)

        try:
            self.img_BackPageIMG = tk.PhotoImage(file='BackPageIMG.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "BackPageIMG.png is missing")

        self.Student_home_back_page_img_button.configure(activebackground='#121212',
                                                         activeforeground='#121212',
                                                         background='#121212',
                                                         borderwidth='0',
                                                         command=self.goHome)
        self.Student_home_back_page_img_button.configure(image=self.img_BackPageIMG)
        self.Student_home_back_page_img_button.place(anchor='nw',
                                                     x='15',
                                                     y='15')

        self.configure(background='#121212',
                       height='515',
                       takefocus=False,
                       width='791')
        self.place(anchor='nw',
                   x='0',
                   y='0')

    def changeTeacherHomeTheme(self):
        if self["background"] == "#121212":
            TeacherHomeBGColor = "#ffffff"
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
            self.Student_register_button.configure(background=TeacherHomeBGColor,
                                                   foreground=TeacherHomeBGColor,
                                                   activebackground=TeacherHomeBGColor,
                                                   activeforeground=TeacherHomeBGColor)
            self.Student_Element_2_IMG_label.configure(background=TeacherHomeBGColor,
                                                       foreground=TeacherHomeFGColor)
            self.Student_update_button.configure(background=TeacherHomeBGColor,
                                                 foreground=TeacherHomeBGColor,
                                                 activebackground=TeacherHomeBGColor,
                                                 activeforeground=TeacherHomeBGColor)
            self.Student_view_button.configure(background=TeacherHomeBGColor,
                                               foreground=TeacherHomeBGColor,
                                               activebackground=TeacherHomeBGColor,
                                               activeforeground=TeacherHomeBGColor)
            self.Student_Delete_button.configure(background=TeacherHomeBGColor,
                                                 foreground=TeacherHomeBGColor,
                                                 activebackground=TeacherHomeBGColor,
                                                 activeforeground=TeacherHomeBGColor)
            self.Manege_Student_label.configure(background=TeacherHomeBGColor,
                                                foreground=TeacherHomeFGColor,
                                                activebackground=TeacherHomeBGColor,
                                                activeforeground=TeacherHomeBGColor)
            self.Student_Manege_close_button.configure(background=TeacherHomeBGColor,
                                                       foreground=TeacherHomeBGColor,
                                                       activebackground=TeacherHomeBGColor,
                                                       activeforeground=TeacherHomeBGColor)
            self.Student_Manege_theme_change_button.configure(background=TeacherHomeBGColor,
                                                              foreground=TeacherHomeBGColor,
                                                              activebackground=TeacherHomeBGColor,
                                                              activeforeground=TeacherHomeBGColor,
                                                              image=self.img_lightThemeimg)
            self.Student_home_back_page_img_button.configure(background=TeacherHomeBGColor,
                                                             foreground=TeacherHomeBGColor,
                                                             activebackground=TeacherHomeBGColor,
                                                             activeforeground=TeacherHomeBGColor, )
        else:
            DTeacherHomeBGColor = "#121212"
            DTeacherHomeFGColor = "#ffffff"

            self.configure(background=DTeacherHomeBGColor)
            self.Student_register_button.configure(background=DTeacherHomeBGColor,
                                                   foreground=DTeacherHomeBGColor,
                                                   activebackground=DTeacherHomeBGColor,
                                                   activeforeground=DTeacherHomeBGColor)
            self.Student_Element_2_IMG_label.configure(background=DTeacherHomeBGColor,
                                                       foreground=DTeacherHomeFGColor)
            self.Student_update_button.configure(background=DTeacherHomeBGColor,
                                                 foreground=DTeacherHomeBGColor,
                                                 activebackground=DTeacherHomeBGColor,
                                                 activeforeground=DTeacherHomeBGColor)
            self.Student_view_button.configure(background=DTeacherHomeBGColor,
                                               foreground=DTeacherHomeBGColor,
                                               activebackground=DTeacherHomeBGColor,
                                               activeforeground=DTeacherHomeBGColor)
            self.Student_Delete_button.configure(background=DTeacherHomeBGColor,
                                                 foreground=DTeacherHomeBGColor,
                                                 activebackground=DTeacherHomeBGColor,
                                                 activeforeground=DTeacherHomeBGColor)
            self.Manege_Student_label.configure(background=DTeacherHomeBGColor,
                                                foreground=DTeacherHomeFGColor,
                                                activebackground=DTeacherHomeBGColor,
                                                activeforeground=DTeacherHomeBGColor)
            self.Student_Manege_close_button.configure(background=DTeacherHomeBGColor,
                                                       foreground=DTeacherHomeBGColor,
                                                       activebackground=DTeacherHomeBGColor,
                                                       activeforeground=DTeacherHomeBGColor)
            self.Student_Manege_theme_change_button.configure(background=DTeacherHomeBGColor,
                                                              foreground=DTeacherHomeBGColor,
                                                              activebackground=DTeacherHomeBGColor,
                                                              activeforeground=DTeacherHomeBGColor,
                                                              image=self.img_DarkThemeimg)
            self.Student_home_back_page_img_button.configure(background=DTeacherHomeBGColor,
                                                             foreground=DTeacherHomeBGColor,
                                                             activebackground=DTeacherHomeBGColor,
                                                             activeforeground=DTeacherHomeBGColor, )

    def goHome(self):
        self.master.switch_frame(Home)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

class TeacherDelete(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        try:
            self.img_DarkThemeimg = tk.PhotoImage(file='DarkThemeimg.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "DarkThemeimg.png is missing")
        self.teacher_Delete_theme_change_button = tk.Button(self)
        self.teacher_Delete_theme_change_button.configure(activebackground='#121212',
                                                          activeforeground='#121212',
                                                          background='#121212',
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
        self.Delete_Teacher_label.configure(background='#121212',
                                            borderwidth='0',
                                            font='{Poppins} 28 {bold}',
                                            foreground='#ffffff')
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

        self.Delete_Teacher_back_page_img_button.configure(activebackground='#121212',
                                                           activeforeground='#121212',
                                                           background='#121212',
                                                           borderwidth='0',
                                                           command=lambda: master.switch_frame(TeacherHome))
        self.Delete_Teacher_back_page_img_button.configure(image=self.img_BackPageIMG)
        self.Delete_Teacher_back_page_img_button.place(anchor='nw', x='15', y='15')
        self.Delete_Id_label = tk.Label(self)
        self.Delete_Id_label.configure(background='#121212',
                                       font='{Poppins} 17 {bold}',
                                       foreground='#ffffff',
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
        self.Delete_Go_button.configure(background='#121212',
                                        activebackground='#121212',
                                        activeforeground='#121212',
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

        self.Delete_Id_bg_label.configure(background='#121212',
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

        self.configure(background='#121212',
                       height='515',
                       takefocus=False,
                       width='791')
        self.place(anchor='nw',
                   x='0',
                   y='0')

    def DeleteGo(self):
        global DeleteId

        DeleteId = self.Delete_Id_entry.get()

        try:
            int(DeleteId)
        except:
            messagebox.showerror("Type Error", "You Can Only Type Numbers For ID ")

        if DeleteId == "":
            messagebox.showerror("Type Error", "You Need To Type ID ")
        else:
            try:
                int(DeleteId)
            except:
                messagebox.showerror("Type Error", "You Can Only Type Numbers For ID ")
                self.Delete_Id_entry.delete(0, 'end')
                self.Delete_Teacher_recodes.configure(height=0)
                DeleteId = ""
            self.conn = mysql.connector.connect(user="root",
                                                password="",
                                                database="eduway")
            self.connetc = self.conn.cursor()

            self.connetc.execute(f"SELECT * FROM teacher WHERE id = {DeleteId}")
            self.deleteRecode = self.connetc.fetchall()

            self.conn.commit()

            self.Delete_Teacher_ID_label = tk.Label(self)
            self.Delete_Teacher_ID_label.configure(background='#121212',
                                                   borderwidth='0',
                                                   font='{Poppins} 10 {bold}',
                                                   foreground='#ffffff')
            self.Delete_Teacher_ID_label.configure(text='ID')
            self.Delete_Teacher_ID_label.place(anchor='nw',
                                               x='16',
                                               y='265')

            self.Delete_Teacher_First_Name_label = tk.Label(self)
            self.Delete_Teacher_First_Name_label.configure(background='#121212',
                                                           borderwidth='0',
                                                           font='{Poppins} 10 {bold}',
                                                           foreground='#ffffff')
            self.Delete_Teacher_First_Name_label.configure(text='First Name')
            self.Delete_Teacher_First_Name_label.place(anchor='nw',
                                                       x='55',
                                                       y='265')

            self.Delete_Teacher_Second_Name_label = tk.Label(self)
            self.Delete_Teacher_Second_Name_label.configure(background='#121212',
                                                            borderwidth='0',
                                                            font='{Poppins} 10 {bold}',
                                                            foreground='#ffffff')
            self.Delete_Teacher_Second_Name_label.configure(text='Second Name')
            self.Delete_Teacher_Second_Name_label.place(anchor='nw',
                                                        x='180',
                                                        y='265')

            self.Delete_Teacher_Age_label = tk.Label(self)
            self.Delete_Teacher_Age_label.configure(background='#121212',
                                                    borderwidth='0',
                                                    font='{Poppins} 10 {bold}',
                                                    foreground='#ffffff')
            self.Delete_Teacher_Age_label.configure(text='Age')
            self.Delete_Teacher_Age_label.place(anchor='nw',
                                                x='340',
                                                y='265')

            self.Delete_Teacher_Phone_Number_label = tk.Label(self)
            self.Delete_Teacher_Phone_Number_label.configure(background='#121212',
                                                             borderwidth='0',
                                                             font='{Poppins} 10 {bold}',
                                                             foreground='#ffffff')
            self.Delete_Teacher_Phone_Number_label.configure(text='Phone Number')
            self.Delete_Teacher_Phone_Number_label.place(anchor='nw',
                                                         x='390',
                                                         y='265')

            self.Delete_Teacher_Gender_label = tk.Label(self)
            self.Delete_Teacher_Gender_label.configure(background='#121212',
                                                       borderwidth='0',
                                                       font='{Poppins} 10 {bold}',
                                                       foreground='#ffffff')
            self.Delete_Teacher_Gender_label.configure(text='Gender')
            self.Delete_Teacher_Gender_label.place(anchor='nw',
                                                   x='520',
                                                   y='265')

            self.Delete_Teacher_Main_Subject_label = tk.Label(self)
            self.Delete_Teacher_Main_Subject_label.configure(background='#121212',
                                                             borderwidth='0',
                                                             font='{Poppins} 10 {bold}',
                                                             foreground='#ffffff')
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
            self.Delete_teachet_button.configure(background='#121212',
                                                 activebackground='#121212',
                                                 activeforeground='#121212',
                                                 borderwidth='0',
                                                 image=self.img_TeacherAddButton,
                                                 relief='flat',
                                                 command=self.onClickDeleteRecodes)

            self.Delete_teachet_button.place(anchor='nw',
                                             x='412',
                                             y='448')
            if self.deleteRecode == []:
                messagebox.showerror("Search Error", "ID You Entered is Already Deleted or Cannot Find That Id ")

            self.Delete_Teacher_recodes.tag_configure("oneColorStudent", background="#121212",
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

        if self["background"] == "#121212":
            self.TeacherDeleteBGColor = "#ffffff"
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

            self.Delete_Teacher_recodes.tag_configure("oneColorStudent", background="#ffffff",
                                                      font='{Poppins} 8 {bold}',
                                                      foreground="#000000")
        else:
            self.DTeacherDeleteBGColor = "#121212"
            self.DTeacherDeleteFGColor = "#ffffff"
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

            self.Delete_Teacher_recodes.tag_configure("oneColorStudent", background="#121212",
                                                      font='{Poppins} 8 {bold}',
                                                      foreground="#ffffff")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

class StudentDelete(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        try:
            self.img_DarkThemeimg = tk.PhotoImage(file='DarkThemeimg.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "DarkThemeimg.png is missing")
        self.Student_Delete_theme_change_button = tk.Button(self)
        self.Student_Delete_theme_change_button.configure(activebackground='#121212',
                                                          activeforeground='#121212',
                                                          background='#121212',
                                                          borderwidth='0',
                                                          relief="flat",
                                                          overrelief="flat",
                                                          command=self.changeTeacherDeleteTheme)
        self.Student_Delete_theme_change_button.configure(image=self.img_DarkThemeimg,
                                                          text='button2')
        self.Student_Delete_theme_change_button.place(anchor='nw',
                                                      x='60',
                                                      y='10')
        self.Delete_Student_label = tk.Label(self)
        self.Delete_Student_label.configure(background='#121212',
                                            borderwidth='0',
                                            font='{Poppins} 28 {bold}',
                                            foreground='#ffffff')
        self.Delete_Student_label.configure(text='Delete Student')
        self.Delete_Student_label.place(anchor='nw',
                                        x='274',
                                        y='28')
        self.Delete_Student_back_page_img_button = tk.Button(self)

        try:
            self.img_BackPageIMG = tk.PhotoImage(file='BackPageIMG.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "BackPageIMG.png is missing")

        self.Delete_Student_back_page_img_button.configure(activebackground='#121212',
                                                           activeforeground='#121212',
                                                           background='#121212',
                                                           borderwidth='0',
                                                           command=lambda: master.switch_frame(StudentHome))
        self.Delete_Student_back_page_img_button.configure(image=self.img_BackPageIMG)
        self.Delete_Student_back_page_img_button.place(anchor='nw', x='15', y='15')
        self.Student_Delete_Id_label = tk.Label(self)
        self.Student_Delete_Id_label.configure(background='#121212',
                                               font='{Poppins} 17 {bold}',
                                               foreground='#ffffff',
                                               text='Delete ID')
        self.Student_Delete_Id_label.place(anchor='nw',
                                           x='166',
                                           y='306')

        try:
            self.img_TeacherGoButton = tk.PhotoImage(file='Update_Go_button_img.png')
        except Exception as e:
            messagebox.showerror("Update_Go_button_img.png Missing")
            print(e)

        self.Student_Delete_Go_button = tk.Button(self)
        self.Student_Delete_Go_button.configure(background='#121212',
                                                activebackground='#121212',
                                                activeforeground='#121212',
                                                borderwidth='0',
                                                image=self.img_TeacherGoButton,
                                                relief='flat',
                                                command=self.DeleteGo)
        self.Student_Delete_Go_button.place(anchor='nw',
                                            x='527',
                                            y='305')

        self.Student_Delete_Id_bg_label = tk.Label(self)

        try:
            self.img_TeacheridbgEntery = tk.PhotoImage(file='Update_id_bg_IMG.png')
        except Exception as e:
            messagebox.showerror("TeacherAddButton.png Missing")
            print(e)

        self.Student_Delete_Id_bg_label.configure(background='#121212',
                                                  borderwidth='0',
                                                  image=self.img_TeacheridbgEntery)
        self.Student_Delete_Id_bg_label.place(anchor='nw',
                                              x='386',
                                              y='310')

        self.Student_Delete_Id_entry = tk.Entry(self)
        self.Student_Delete_Id_entry.configure(borderwidth='0')
        self.Student_Delete_Id_entry.configure(font='{Poppins} 10 {bold}',
                                               insertwidth='1',
                                               relief='flat')
        self.Student_Delete_Id_entry.place(anchor='nw',
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

        self.Delete_Student_recodes = ttk.Treeview(height=1, columns=self.columns, show="tree")
        self.Delete_Student_recodes.configure(height=0)

        self.Delete_Student_recodes.column("ID", width=50)
        self.Delete_Student_recodes.column("First name", width=150)
        self.Delete_Student_recodes.column("Last name", width=130)
        self.Delete_Student_recodes.column("Age", width=50)
        self.Delete_Student_recodes.column("Phone Number", width=130)
        self.Delete_Student_recodes.column("AdmissionNo", width=100)
        self.Delete_Student_recodes.column("Subjects", width=220)

        self.configure(background='#121212',
                       height='515',
                       takefocus=False,
                       width='791')
        self.place(anchor='nw',
                   x='0',
                   y='0')

    def DeleteGo(self):
        global StudentDeleteId

        StudentDeleteId = self.Student_Delete_Id_entry.get()

        try:
            int(StudentDeleteId)
        except:
            messagebox.showerror("Type Error", "You Can Only Type Numbers For ID ")

        if StudentDeleteId == "":
            messagebox.showerror("Type Error", "You Need To Type ID ")
        else:
            try:
                int(StudentDeleteId)
            except:
                messagebox.showerror("Type Error", "You Can Only Type Numbers For ID ")
                self.Student_Delete_Id_entry.delete(0, 'end')
                self.Delete_Student_recodes.configure(height=0)
                StudentDeleteId = ""
            self.conn = mysql.connector.connect(user="root",
                                                password="",
                                                database="eduway")
            self.connetc = self.conn.cursor()

            self.connetc.execute(f"SELECT * FROM student WHERE id = {StudentDeleteId}")
            self.deleteRecode = self.connetc.fetchall()

            self.conn.commit()

            self.Delete_Teacher_ID_label = tk.Label(self)
            self.Delete_Teacher_ID_label.configure(background='#121212',
                                                   borderwidth='0',
                                                   font='{Poppins} 10 {bold}',
                                                   foreground='#ffffff')
            self.Delete_Teacher_ID_label.configure(text='ID')
            self.Delete_Teacher_ID_label.place(anchor='nw',
                                               x='16',
                                               y='265')

            self.Delete_Teacher_First_Name_label = tk.Label(self)
            self.Delete_Teacher_First_Name_label.configure(background='#121212',
                                                           borderwidth='0',
                                                           font='{Poppins} 10 {bold}',
                                                           foreground='#ffffff')
            self.Delete_Teacher_First_Name_label.configure(text='First Name')
            self.Delete_Teacher_First_Name_label.place(anchor='nw',
                                                       x='55',
                                                       y='265')

            self.Delete_Teacher_Second_Name_label = tk.Label(self)
            self.Delete_Teacher_Second_Name_label.configure(background='#121212',
                                                            borderwidth='0',
                                                            font='{Poppins} 10 {bold}',
                                                            foreground='#ffffff')
            self.Delete_Teacher_Second_Name_label.configure(text='Second Name')
            self.Delete_Teacher_Second_Name_label.place(anchor='nw',
                                                        x='180',
                                                        y='265')

            self.Delete_Teacher_Age_label = tk.Label(self)
            self.Delete_Teacher_Age_label.configure(background='#121212',
                                                    borderwidth='0',
                                                    font='{Poppins} 10 {bold}',
                                                    foreground='#ffffff')
            self.Delete_Teacher_Age_label.configure(text='Age')
            self.Delete_Teacher_Age_label.place(anchor='nw',
                                                x='340',
                                                y='265')

            self.Delete_Teacher_Phone_Number_label = tk.Label(self)
            self.Delete_Teacher_Phone_Number_label.configure(background='#121212',
                                                             borderwidth='0',
                                                             font='{Poppins} 10 {bold}',
                                                             foreground='#ffffff')
            self.Delete_Teacher_Phone_Number_label.configure(text='Phone Number')
            self.Delete_Teacher_Phone_Number_label.place(anchor='nw',
                                                         x='390',
                                                         y='265')

            self.Delete_Teacher_Gender_label = tk.Label(self)
            self.Delete_Teacher_Gender_label.configure(background='#121212',
                                                       borderwidth='0',
                                                       font='{Poppins} 10 {bold}',
                                                       foreground='#ffffff')
            self.Delete_Teacher_Gender_label.configure(text='Gender')
            self.Delete_Teacher_Gender_label.place(anchor='nw',
                                                   x='520',
                                                   y='265')

            self.Delete_Teacher_Main_Subject_label = tk.Label(self)
            self.Delete_Teacher_Main_Subject_label.configure(background='#121212',
                                                             borderwidth='0',
                                                             font='{Poppins} 10 {bold}',
                                                             foreground='#ffffff')
            self.Delete_Teacher_Main_Subject_label.configure(text='Main Subject')
            self.Delete_Teacher_Main_Subject_label.place(anchor='nw',
                                                         x='600',
                                                         y='265')
            try:
                self.img_TeacherAddButton = tk.PhotoImage(file='Student_Delete.png')
            except Exception as e:
                messagebox.showerror("Student_Delete.png Missing")
                print(e)

            self.Delete_teachet_button = tk.Button(self)
            self.Delete_teachet_button.configure(background='#121212',
                                                 activebackground='#121212',
                                                 activeforeground='#121212',
                                                 borderwidth='0',
                                                 image=self.img_TeacherAddButton,
                                                 relief='flat',
                                                 command=self.onClickDeleteRecodes)

            self.Delete_teachet_button.place(anchor='nw',
                                             x='412',
                                             y='448')
            if self.deleteRecode == []:
                messagebox.showerror("Search Error", "ID You Entered is Already Deleted or Cannot Find That Id ")

            self.Delete_Student_recodes.tag_configure("oneColorStudent", background="#121212",
                                                      font='{Poppins} 8 {bold}',
                                                      foreground="#c2c2c2")
            self.Delete_Student_recodes.configure(height=1)
            global count
            self.deleteRecodes()
            for record in self.deleteRecode:
                self.Delete_Student_recodes.insert(parent="", index='end', iid=0, values=(
                    record[0], record[1], record[2], record[4], "0" + str(record[3]), record[5], record[6]),
                                                   tags=("oneColorStudent"))

            self.Student_Delete_Id_label.place(anchor='nw',
                                               x='166',
                                               y='156')
            self.Student_Delete_Go_button.place(anchor='nw',
                                                x='527',
                                                y='155')
            self.Student_Delete_Id_bg_label.place(anchor='nw',
                                                  x='386',
                                                  y='160')
            self.Student_Delete_Id_entry.place(anchor='nw',
                                               height='24',
                                               width='120',
                                               x='395',
                                               y='163')
            self.Delete_Student_recodes.place(anchor='nw', x='0', y='300', relx="-0.24", bordermode='ignore')
            self.Student_Delete_Id_entry.delete(0, "end")
            self.connetc.close()
            self.conn.close()

    def deleteRecodes(self):
        for item in self.Delete_Student_recodes.get_children():
            self.Delete_Student_recodes.delete(item)

    def onClickDeleteRecodes(self):
        self.conn = mysql.connector.connect(user="root",
                                            password="",
                                            database="eduway")
        self.connetc = self.conn.cursor()
        self.connetc.execute(f"DELETE FROM student WHERE id = {StudentDeleteId}")
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

        if self["background"] == "#121212":
            self.TeacherDeleteBGColor = "#ffffff"
            self.TeacherDeleteFGColor = "#000000"
            self.configure(background=self.TeacherDeleteBGColor)
            self.Student_Delete_theme_change_button.configure(background=self.TeacherDeleteBGColor,
                                                              foreground=self.TeacherDeleteFGColor,
                                                              activeforeground=self.TeacherDeleteBGColor,
                                                              activebackground=self.TeacherDeleteBGColor,
                                                              image=self.img_lightThemeimg)

            self.Delete_Student_label.configure(background=self.TeacherDeleteBGColor,
                                                foreground=self.TeacherDeleteFGColor)
            self.Delete_Student_back_page_img_button.configure(background=self.TeacherDeleteBGColor,
                                                               foreground=self.TeacherDeleteFGColor,
                                                               activeforeground=self.TeacherDeleteBGColor,
                                                               activebackground=self.TeacherDeleteBGColor)
            self.Student_Delete_Id_label.configure(background=self.TeacherDeleteBGColor,
                                                   foreground=self.TeacherDeleteFGColor)

            self.Student_Delete_Go_button.configure(background=self.TeacherDeleteBGColor,
                                                    foreground=self.TeacherDeleteFGColor,
                                                    activeforeground=self.TeacherDeleteBGColor,
                                                    activebackground=self.TeacherDeleteBGColor)
            self.Student_Delete_Id_bg_label.configure(background=self.TeacherDeleteBGColor,
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

            self.Delete_Student_recodes.tag_configure("oneColorStudent", background="#ffffff",
                                                      font='{Poppins} 8 {bold}',
                                                      foreground="#000000")
        else:
            self.DTeacherDeleteBGColor = "#121212"
            self.DTeacherDeleteFGColor = "#ffffff"
            self.configure(background=self.DTeacherDeleteBGColor)
            self.Student_Delete_theme_change_button.configure(background=self.DTeacherDeleteBGColor,
                                                              foreground=self.DTeacherDeleteFGColor,
                                                              activeforeground=self.DTeacherDeleteBGColor,
                                                              activebackground=self.DTeacherDeleteBGColor,
                                                              image=self.img_DarkThemeimg)

            self.Delete_Student_label.configure(background=self.DTeacherDeleteBGColor,
                                                foreground=self.DTeacherDeleteFGColor)
            self.Delete_Student_back_page_img_button.configure(background=self.DTeacherDeleteBGColor,
                                                               foreground=self.DTeacherDeleteFGColor,
                                                               activeforeground=self.DTeacherDeleteBGColor,
                                                               activebackground=self.DTeacherDeleteBGColor)
            self.Student_Delete_Id_label.configure(background=self.DTeacherDeleteBGColor,
                                                   foreground=self.DTeacherDeleteFGColor)

            self.Student_Delete_Go_button.configure(background=self.DTeacherDeleteBGColor,
                                                    foreground=self.DTeacherDeleteFGColor,
                                                    activeforeground=self.DTeacherDeleteBGColor,
                                                    activebackground=self.DTeacherDeleteBGColor)
            self.Student_Delete_Id_bg_label.configure(background=self.DTeacherDeleteBGColor,
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

            self.Delete_Student_recodes.tag_configure("oneColorStudent", background="#121212",
                                                      font='{Poppins} 8 {bold}',
                                                      foreground="#ffffff")


# this is the student register Window
# you can register student in hear
# need to repair
class StudentRegistation(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.Student_element_img_label = tk.Label(self)

        try:
            self.img_Element_1_img_label = tk.PhotoImage(file='Element_1_img_label.png')
        except Exception as e:
            messagebox.showerror("Element_1_img_label.png' Missing")
            print(e)

        self.Student_element_img_label.configure(background='#121212',
                                                 image=self.img_Element_1_img_label)
        self.Student_element_img_label.place(anchor='nw',
                                             x='0',
                                             y='0')

        try:
            self.img_TeacherRegiusterEntery = tk.PhotoImage(file='TeacherRegiusterEntery.png')
        except Exception as e:
            messagebox.showerror("TeacherAddButton.png Missing")
            print(e)

        self.Student_Admission_Number_Entry_bg_label = tk.Label(self)
        self.Student_Admission_Number_Entry_bg_label.configure(background='#121212',
                                                               borderwidth='0',
                                                               image=self.img_TeacherRegiusterEntery)
        self.Student_Admission_Number_Entry_bg_label.place(anchor='nw',
                                                           x='386',
                                                           y='340')
        self.Student_First_name_Entry_bg_label = tk.Label(self)
        self.Student_First_name_Entry_bg_label.configure(background='#121212',
                                                         borderwidth='0',
                                                         image=self.img_TeacherRegiusterEntery)
        self.Student_First_name_Entry_bg_label.place(anchor='nw',
                                                     x='386',
                                                     y='146')

        self.Student_Last_name_Entry_bg_label = tk.Label(self)
        self.Student_Last_name_Entry_bg_label.configure(background='#121212',
                                                        borderwidth='0',
                                                        image=self.img_TeacherRegiusterEntery)
        self.Student_Last_name_Entry_bg_label.place(anchor='nw',
                                                    x='386',
                                                    y='196')

        self.Student_age_Entry_bg_label = tk.Label(self)
        self.Student_age_Entry_bg_label.configure(background='#121212',
                                                  borderwidth='0',
                                                  image=self.img_TeacherRegiusterEntery)
        self.Student_age_Entry_bg_label.place(anchor='nw',
                                              x='386',
                                              y='246')

        self.Student_phone_number_Entry_bg_label = tk.Label(self)
        self.Student_phone_number_Entry_bg_label.configure(background='#121212',
                                                           borderwidth='0',
                                                           image=self.img_TeacherRegiusterEntery)
        self.Student_phone_number_Entry_bg_label.place(anchor='nw',
                                                       x='386',
                                                       y='290')

        self.Student_Subject_Entry_bg_label = tk.Label(self)
        self.Student_Subject_Entry_bg_label.configure(background='#121212',
                                                      borderwidth='0',
                                                      image=self.img_TeacherRegiusterEntery)
        self.Student_Subject_Entry_bg_label.place(anchor='nw',
                                                  x='386',
                                                  y='390')

        self.Student_first_name_entry = tk.Entry(self)
        self.Student_first_name_entry.configure(borderwidth='0')
        self.Student_first_name_entry.configure(font='{Poppins} 10 {bold}',
                                                insertwidth='1',
                                                relief='flat')
        self.Student_first_name_entry.place(anchor='nw',
                                            height='24',
                                            width='229',
                                            x='395',
                                            y='149')

        self.Student_first_name_label = tk.Label(self)
        self.Student_first_name_label.configure(background='#121212',
                                                font='{Poppins} 17 {bold}',
                                                foreground='#ffffff',
                                                text='First Name')
        self.Student_first_name_label.place(anchor='nw',
                                            x='166',
                                            y='146')

        self.Student_last_name_entry = tk.Entry(self)
        self.Student_last_name_entry.configure(borderwidth='0')
        self.Student_last_name_entry.configure(font='{Poppins} 10 {bold}',
                                               insertwidth='1',
                                               relief='flat')
        self.Student_last_name_entry.place(anchor='nw',
                                           height='24',
                                           width='229',
                                           x='397',
                                           y='199')

        self.Student_last_name_label = tk.Label(self)
        self.Student_last_name_label.configure(background='#121212',
                                               font='{Poppins} 17 {bold}',
                                               foreground='#ffffff',
                                               text='Last Name')
        self.Student_last_name_label.place(anchor='nw',
                                           x='166',
                                           y='198')

        self.Student_phone_number_entry = tk.Entry(self)
        self.Student_phone_number_entry.configure(borderwidth='0')
        self.Student_phone_number_entry.configure(font='{Poppins} 10 {bold}',
                                                  insertwidth='1',
                                                  relief='flat')
        self.Student_phone_number_entry.place(anchor='nw',
                                              height='24',
                                              width='229',
                                              x='397',
                                              y='293')

        self.Student_phone_number_label = tk.Label(self)
        self.Student_phone_number_label.configure(background='#121212',
                                                  font='{Poppins} 17 {bold}',
                                                  foreground='#ffffff',
                                                  text='Phone number')
        self.Student_phone_number_label.place(anchor='nw',
                                              x='166',
                                              y='289')

        self.Student_age_entry = tk.Entry(self)
        self.Student_age_entry.configure(borderwidth='0')
        self.Student_age_entry.configure(font='{Poppins} 10 {bold}',
                                         insertwidth='1',
                                         relief='flat')
        self.Student_age_entry.place(anchor='nw',
                                     height='24',
                                     width='229',
                                     x='395',
                                     y='249')

        self.Student_age_label = tk.Label(self)
        self.Student_age_label.configure(background='#121212',
                                         font='{Poppins} 17 {bold}',
                                         foreground='#ffffff',
                                         text='Age')
        self.Student_age_label.place(anchor='nw',
                                     x='166',
                                     y='239')

        self.Student_Admission_Number_label = tk.Label(self)
        self.Student_Admission_Number_label.configure(background='#121212',
                                                      font='{Poppins} 17 {bold}',
                                                      foreground='#ffffff',
                                                      text='AdmissionNo')
        self.Student_Admission_Number_label.place(anchor='nw',
                                                  x='166',
                                                  y='331')

        self.Student_Admission_Number_entry = tk.Entry(self)
        self.Student_Admission_Number_entry.configure(borderwidth="0")
        self.Student_Admission_Number_entry.configure(font='{Poppins} 10 {bold}',
                                                      insertwidth='1',
                                                      relief='flat')
        self.Student_Admission_Number_entry.place(anchor='nw',
                                                  height='24',
                                                  width='229',
                                                  x='395',
                                                  y='343')

        self.Student_subects_label = tk.Label(self)
        self.Student_subects_label.configure(background='#121212',
                                             font='{Poppins} 17 {bold}',
                                             foreground='#ffffff',
                                             text='Main Subject')
        self.Student_subects_label.place(anchor='nw',
                                         x='166',
                                         y='389')

        self.Student_subject_entry = tk.Entry(self)
        self.Student_subject_entry.configure(borderwidth="0")
        self.Student_subject_entry.configure(font='{Poppins} 10 {bold}',
                                             insertwidth='1',
                                             relief='flat')
        self.Student_subject_entry.place(anchor='nw',
                                         height='24',
                                         width='229',
                                         x='395',
                                         y='393')

        try:
            self.img_TeacherAddButton = tk.PhotoImage(file='Student_Add.png')
        except Exception as e:
            messagebox.showerror("TeacherAddButton.png Missing")
            print(e)

        self.add_Student_button = tk.Button(self)
        self.add_Student_button.configure(background='#121212',
                                          activebackground='#121212',
                                          activeforeground='#121212',
                                          borderwidth='0',
                                          image=self.img_TeacherAddButton,
                                          relief='flat',
                                          command=self.clickAdd)
        self.add_Student_button.place(anchor='nw',
                                      x='412',
                                      y='448')

        try:
            self.img_img4 = tk.PhotoImage(file='img4.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "img_img4.png is missing")
        self.Student_registation_close_button = tk.Button(self)
        self.Student_registation_close_button.configure(activebackground='#121212',
                                                        activeforeground='#121212',
                                                        background='#121212',
                                                        borderwidth='0')
        self.Student_registation_close_button.configure(cursor='hand2',
                                                        foreground='#121212',
                                                        highlightbackground='#121212',
                                                        highlightcolor='#121212')
        self.Student_registation_close_button.configure(highlightthickness='1',
                                                        image=self.img_img4,
                                                        relief='flat',
                                                        command=self.master.on_close)
        self.Student_registation_close_button.place(anchor='nw',
                                                    x='760',
                                                    y='8')

        self.Register_Student_label = tk.Label(self)
        self.Register_Student_label.configure(background='#121212',
                                              borderwidth='0',
                                              font='{Poppins} 28 {bold}',
                                              foreground='#ffffff')
        self.Register_Student_label.configure(text='Register Student')
        self.Register_Student_label.place(anchor='nw',
                                          x='274',
                                          y='28')

        self.Student_back_page_img_button = tk.Button(self)

        try:
            self.img_BackPageIMG = tk.PhotoImage(file='BackPageIMG.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "BackPageIMG.png is missing")

        self.Student_back_page_img_button.configure(activebackground='#121212',
                                                    activeforeground='#121212',
                                                    background='#121212',
                                                    borderwidth='0',
                                                    command=self.goBackToStudentHome)
        self.Student_back_page_img_button.configure(image=self.img_BackPageIMG)
        self.Student_back_page_img_button.place(anchor='nw', x='15', y='15')

        self.Student_registation_theme_change_button = tk.Button(self)

        try:
            self.img_DarkThemeimg = tk.PhotoImage(file='DarkThemeimg.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "DarkThemeimg.png is missing")

        self.Student_registation_theme_change_button.configure(activebackground='#121212',
                                                               activeforeground='#121212',
                                                               background='#121212',
                                                               borderwidth='0',
                                                               relief="flat",
                                                               overrelief="flat",
                                                               command=self.changeStudentRegistationTheme)
        self.Student_registation_theme_change_button.configure(image=self.img_DarkThemeimg,
                                                               text='button2')
        self.Student_registation_theme_change_button.place(anchor='nw',
                                                           x='60',
                                                           y='10')
        self.configure(background='#121212',
                       borderwidth='0',
                       height='515',
                       width='791')
        self.place(x="0", y="0")

    def changeStudentRegistationTheme(self):
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

        if self.Student_back_page_img_button["background"] == "#121212":
            self.StudentRegistationBGColor = "#ffffff"
            self.StudentRegistationFGColor = "#000000"
            self.configure(background=self.StudentRegistationBGColor)
            self.Student_element_img_label.configure(background=self.StudentRegistationBGColor,
                                                     foreground=self.StudentRegistationFGColor)
            self.Student_First_name_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
                                                             foreground=self.StudentRegistationFGColor)
            self.Student_Last_name_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
                                                            foreground=self.StudentRegistationFGColor)
            self.Student_age_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
                                                      foreground=self.StudentRegistationFGColor)
            self.Student_phone_number_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
                                                               foreground=self.StudentRegistationFGColor)
            self.Student_phone_number_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
                                                               foreground=self.StudentRegistationFGColor)
            self.Student_Admission_Number_label.configure(background=self.StudentRegistationBGColor,
                                                          foreground=self.StudentRegistationFGColor)
            self.Student_subects_label.configure(background=self.StudentRegistationBGColor,
                                                 foreground=self.StudentRegistationFGColor)
            self.Student_first_name_entry.configure(background=self.StudentRegistationBGColor,
                                                    foreground=self.StudentRegistationFGColor)
            self.Student_Admission_Number_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
                                                                   foreground=self.StudentRegistationFGColor)
            self.Student_First_name_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
                                                             foreground=self.StudentRegistationFGColor)
            self.Student_Last_name_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
                                                            foreground=self.StudentRegistationFGColor)
            self.Student_age_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
                                                      foreground=self.StudentRegistationFGColor)
            self.Student_phone_number_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
                                                               foreground=self.StudentRegistationFGColor)
            self.Student_Subject_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
                                                          foreground=self.StudentRegistationFGColor)
            self.Student_first_name_label.configure(background=self.StudentRegistationBGColor,
                                                    foreground=self.StudentRegistationFGColor)
            self.Student_last_name_entry.configure(background=self.StudentRegistationBGColor,
                                                   foreground=self.StudentRegistationFGColor)
            self.Student_last_name_label.configure(background=self.StudentRegistationBGColor,
                                                   foreground=self.StudentRegistationFGColor)
            self.Student_phone_number_entry.configure(background=self.StudentRegistationBGColor,
                                                      foreground=self.StudentRegistationFGColor)
            self.Student_phone_number_label.configure(background=self.StudentRegistationBGColor,
                                                      foreground=self.StudentRegistationFGColor)
            self.Student_age_entry.configure(background=self.StudentRegistationBGColor,
                                             foreground=self.StudentRegistationFGColor)
            self.Student_age_label.configure(background=self.StudentRegistationBGColor,
                                             foreground=self.StudentRegistationFGColor)
            self.Student_Admission_Number_entry.configure(background=self.StudentRegistationBGColor,
                                                          foreground=self.StudentRegistationFGColor)
            self.Student_Admission_Number_label.configure(background=self.StudentRegistationBGColor,
                                                          foreground=self.StudentRegistationFGColor)
            self.Student_subject_entry.configure(background=self.StudentRegistationBGColor,
                                                 foreground=self.StudentRegistationFGColor)
            self.Student_subects_label.configure(background=self.StudentRegistationBGColor,
                                                 foreground=self.StudentRegistationFGColor)
            self.add_Student_button.configure(background=self.StudentRegistationBGColor,
                                              foreground=self.StudentRegistationFGColor,
                                              activebackground=self.StudentRegistationBGColor,
                                              activeforeground=self.StudentRegistationBGColor)
            self.Student_Subject_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
                                                          foreground=self.StudentRegistationFGColor)
            self.Student_registation_close_button.configure(background=self.StudentRegistationBGColor,
                                                            foreground=self.StudentRegistationFGColor)
            self.Student_phone_number_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
                                                               foreground=self.StudentRegistationFGColor)
            self.Register_Student_label.configure(background=self.StudentRegistationBGColor,
                                                  foreground=self.StudentRegistationFGColor)
            self.Student_back_page_img_button.configure(background=self.StudentRegistationBGColor,
                                                        foreground=self.StudentRegistationFGColor,
                                                        activebackground=self.StudentRegistationBGColor,
                                                        activeforeground=self.StudentRegistationBGColor)
            self.Student_registation_theme_change_button.configure(background=self.StudentRegistationBGColor,
                                                                   foreground=self.StudentRegistationFGColor,
                                                                   activebackground=self.StudentRegistationBGColor,
                                                                   activeforeground=self.StudentRegistationBGColor,
                                                                   image=self.img_lightThemeimg)
        else:
            self.DStudentRegistationBGColor = "#121212"
            self.DStudentRegistationFGColor = "#ffffff"
            self.configure(background=self.DStudentRegistationBGColor)
            self.Student_element_img_label.configure(background=self.DStudentRegistationBGColor,
                                                     foreground=self.DStudentRegistationFGColor)
            self.Student_First_name_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
                                                             foreground=self.DStudentRegistationFGColor)
            self.Student_Last_name_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
                                                            foreground=self.DStudentRegistationFGColor)
            self.Student_age_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
                                                      foreground=self.DStudentRegistationFGColor)
            self.Student_phone_number_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
                                                               foreground=self.DStudentRegistationFGColor)
            self.Student_Subject_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
                                                          foreground=self.DStudentRegistationFGColor)
            self.Student_first_name_label.configure(background=self.DStudentRegistationBGColor,
                                                    foreground=self.DStudentRegistationFGColor)
            self.Student_last_name_label.configure(background=self.DStudentRegistationBGColor,
                                                   foreground=self.DStudentRegistationFGColor)
            self.Student_phone_number_label.configure(background=self.DStudentRegistationBGColor,
                                                      foreground=self.DStudentRegistationFGColor)
            self.Student_age_label.configure(background=self.DStudentRegistationBGColor,
                                             foreground=self.DStudentRegistationFGColor)
            self.Student_Admission_Number_label.configure(background=self.DStudentRegistationBGColor,
                                                          foreground=self.DStudentRegistationFGColor)
            self.Student_subects_label.configure(background=self.DStudentRegistationBGColor,
                                                 foreground=self.DStudentRegistationFGColor)
            self.add_Student_button.configure(background=self.DStudentRegistationBGColor,
                                              foreground=self.DStudentRegistationFGColor,
                                              activebackground=self.DStudentRegistationBGColor,
                                              activeforeground=self.DStudentRegistationBGColor)
            self.Student_registation_close_button.configure(background=self.DStudentRegistationBGColor,
                                                            foreground=self.DStudentRegistationFGColor)
            self.Register_Student_label.configure(background=self.DStudentRegistationBGColor,
                                                  foreground=self.DStudentRegistationFGColor)
            self.Student_back_page_img_button.configure(background=self.DStudentRegistationBGColor,
                                                        foreground=self.DStudentRegistationFGColor)
            self.Student_Admission_Number_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
                                                                   foreground=self.DStudentRegistationFGColor)
            self.Student_First_name_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
                                                             foreground=self.DStudentRegistationFGColor)
            self.Student_Last_name_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
                                                            foreground=self.DStudentRegistationFGColor)
            self.Student_age_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
                                                      foreground=self.DStudentRegistationFGColor)
            self.Student_phone_number_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
                                                               foreground=self.DStudentRegistationFGColor)
            self.Student_Subject_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
                                                          foreground=self.DStudentRegistationFGColor)
            self.Student_registation_theme_change_button.configure(background=self.DStudentRegistationBGColor,
                                                                   foreground=self.DStudentRegistationFGColor,
                                                                   activebackground=self.DStudentRegistationBGColor,
                                                                   activeforeground=self.DStudentRegistationBGColor,
                                                                   image=self.img_DarkThemeimg)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
###########################################################Go Back To Student Home#################################
    def goBackToStudentHome(self):
        self.master.switch_frame(StudentHome)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
#########################################On CLick Add Button ######################################################
    def clickAdd(self):

#####################################################Clear#######################################################
        self.Clearerrors()
####################################################Clear########################################################

#*******************************************************************************************************************
#########################################Create variabels###########################################################
        global Student_first_name, Student_last_name, Student_phone_number, Student_age, Student_Admission_Number, Student_subjects
        #^^^^^^This is All variabels

        Student_first_name = self.Student_first_name_entry.get() #This Is Student First Name

        Student_last_name = self.Student_last_name_entry.get() #This is student last name

        Student_phone_number = self.Student_phone_number_entry.get() #this is student phone number
        
        Student_age = self.Student_age_entry.get() #This is the Student error

        Student_Admission_Number = self.Student_Admission_Number_entry.get() #this is the student Admission number

        Student_subjects = self.Student_subject_entry.get() #this is the student Subjects

#*******************************************************************************************************************

#*******************************************************************************************************************
###############################################Check All Fields Are Empty###########################################
        if Student_first_name == "" or Student_last_name == "" or Student_phone_number == "" or Student_age == "" or Student_Admission_Number == "" or Student_subjects == "":
            
            
            #################################Distroy Student First Name########################            
            self.AllFildsRequiredErorr()
        else:
            ################################Distroy All Fields Erore#####################
            self.AllFildsRequiredErorrDestroy()
            
            ##################################Student First Name Lenth Check#############
            if len(Student_first_name) > 50:
                ###################################Distroy Studetn_First_Name_No_error_label#####################
                self.FirstNameErorr()
            else:
                Student_first_name.capitalize()

                # self.FirstNameNoErorr()

                ##########################################Cehck Student Last name Lenth########################
                if len(Student_last_name) > 50:
                    #####################################Distroy Studetn_Last_Name_No_error_label###############
                    self.LastNameError()
                else:
                    self.ClearLastNameError()

                    # self.NoLastNameError()


                    Student_last_name.capitalize()
                    if Student_first_name.capitalize() == Student_last_name.capitalize():

                        self.ClearNoLastNameError()

                        self.NameDuplicatedErorr()
                    else:

                        self.ClearNameDuplicatedErorr()

                        # self.NoDuplicateNameError()

                              ################################Numeber Lenth Check########################################
                        if len(Student_phone_number) != 10:

                            ##################################Distroy Number No Eror#################                          
                            self.clearAllPhoneErors()


                            ##################################PHONE NUMBER LENTH ERROR#####################
                            self.PhoneNumberLenthErorr()


###################################################Distroy Studetn_lenth_Phone_number_error_label############
                        else:
                            self.ClearPhoneNumberLenthErorr()



#******************************************************************************************************************#
###################################################### place Studetn_Phone_Number_No_error_label####################
                            # self.PhoneNumberLenthNoErorr()

                                           ###############This  Place tick############## 
######################################################Check Phone Number Error##########################
#******************************************************************************************************#
                            try:
                                int(Student_phone_number)
                            except:
                                pass
                            if type(int(Student_phone_number)) != int:

######################################################Distroy All Error##################################
                                self.clearAllPhoneErors()

#####################################################Place Studetn_int_Phone_number_error_label####################
                                self.PhoneNumberTypeErorr()
                            else:
####################################################Distroy Studetn_int_Phone_number_error_label ##################
                                try:
                                    self.clearAllPhoneErors()
                                except:
                                    pass
##################################################Place  Studetn_int_Phone_Number_No_error_label####################
                                # self.PhoneNumberNoTypeErorr()
################################
                                if int(Student_phone_number[0]) != 0:
#*************************************************************************************************************#
###############################################Distroy Phone Nimbers###########################################
                                    try:
                                        self.clearAllPhoneErors()
                                    except:
                                        pass
##############################################Place Error##############################################                                    
                                    self.PhoneNumberZeroError()
#######################################################################################################                                    
                                else:
                                    try:
                                        self.ClearPhoneNumberZeroError()
                                    except:
                                        pass

                                    
                                    if len(Student_age) > 2:
                                        self.AgeError()
                                    else:
                                        
                                        try:
                                            self.ClearAgeError()
                                        except:
                                            pass
                                        
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

                                        checkSubject = all(item in AllSubjects for item in Update_subjects.split(","))
                                        if checkSubject is False:
                                            messagebox.showerror("Subject Error", "You Can Add Only Subjects ")
                                        else:
                                            # try:
                                            #     self.AgeNoError()
                                            # except:
                                            #     pass  
                                            self.conn = mysql.connector.connect(user="root",
                                                                                password="",
                                                                                database="eduway")
                                            int(Student_phone_number)
                                            int(Student_age)
                                            self.connetc = self.conn.cursor()

                                            self.connetc.execute(
                                                "CREATE TABLE IF NOT EXISTS Student (id INT AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(50), LAstName VARCHAR(50), PhoneNumber INT(50), Age INT(2), Student_Admission_Number INT(255) ,Subjects VARCHAR(255) )")
                                            self.connetc.execute(
                                                "INSERT INTO  Student (FirstName, LAstName, PhoneNumber, Age, StudentAdmissionNumber, Subjects) VALUES (%s,%s,%s,%s,%s,%s)",
                                                (str(Student_first_name.capitalize()), str(Student_last_name.capitalize()),
                                                0 + int(Student_phone_number), int(Student_age),
                                                str(Student_Admission_Number),
                                                str(Student_subjects.capitalize())))
                                            self.conn.commit()

                                            self.clearTeacherRegistation()
                                            self.Clearerrors()
                                            self.connetc.close()
                                            self.conn.close()
                                            # self.master.switch_frame(TeacherView)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#


    def clearTeacherRegistation(self):
        self.Student_first_name_entry.delete(0, 'end')
        self.Student_subject_entry.delete(0, 'end')
        self.Student_last_name_entry.delete(0, 'end')
        self.Student_Admission_Number_entry.delete(0, 'end')
        self.Student_age_entry.delete(0, 'end')
        self.Student_phone_number_entry.delete(0, 'end')

##############################################################Clear error labales###################################

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
                   
# this is the update window
# You can update all data in this fields
class TeacherUpdate(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.Update_element_img_label = tk.Label(self)

        try:
            self.img_Element_1_img_label = tk.PhotoImage(file='Element_1_img_label.png')
        except Exception as e:
            messagebox.showerror("Element_1_img_label.png' Missing")
            print(e)

        self.Update_element_img_label.configure(background='#121212',
                                                image=self.img_Element_1_img_label)
        self.Update_element_img_label.place(anchor='nw',
                                            x='0',
                                            y='0')

        try:
            self.img_TeacherRegiusterEntery = tk.PhotoImage(file='TeacherRegiusterEntery.png')
        except Exception as e:
            messagebox.showerror("TeacherAddButton.png Missing")
            print(e)

        self.img_TeacheridbgEntery = tk.PhotoImage(file='Update_id_bg_IMG.png')

        self.Update_Id_bg_label = tk.Label(self)
        self.Update_Id_bg_label.configure(background='#121212',
                                          borderwidth='0',
                                          image=self.img_TeacheridbgEntery)
        self.Update_Id_bg_label.place(anchor='nw',
                                      x='386',
                                      y="100")

        self.Update_First_name_Entry_bg_label = tk.Label(self)
        self.Update_First_name_Entry_bg_label.configure(background='#121212',
                                                        borderwidth='0',
                                                        image=self.img_TeacherRegiusterEntery)
        self.Update_First_name_Entry_bg_label.place(anchor='nw',
                                                    x='386',
                                                    y='146')

        self.Update_Last_name_Entry_bg_label = tk.Label(self)
        self.Update_Last_name_Entry_bg_label.configure(background='#121212',
                                                       borderwidth='0',
                                                       image=self.img_TeacherRegiusterEntery)
        self.Update_Last_name_Entry_bg_label.place(anchor='nw',
                                                   x='386',
                                                   y='196')

        self.Update_age_Entry_bg_label = tk.Label(self)
        self.Update_age_Entry_bg_label.configure(background='#121212',
                                                 borderwidth='0',
                                                 image=self.img_TeacherRegiusterEntery)
        self.Update_age_Entry_bg_label.place(anchor='nw',
                                             x='386',
                                             y='246')

        self.Update_phone_number_Entry_bg_label = tk.Label(self)
        self.Update_phone_number_Entry_bg_label.configure(background='#121212',
                                                          borderwidth='0',
                                                          image=self.img_TeacherRegiusterEntery)
        self.Update_phone_number_Entry_bg_label.place(anchor='nw',
                                                      x='386',
                                                      y='290')

        self.Update_gender_Entry_bg_label = tk.Label(self)
        self.Update_gender_Entry_bg_label.configure(background='#121212',
                                                    borderwidth='0',
                                                    image=self.img_TeacherRegiusterEntery)
        self.Update_gender_Entry_bg_label.place(anchor='nw',
                                                x='386',
                                                y='340')

        self.Update_subject_Entry_bg_label = tk.Label(self)
        self.Update_subject_Entry_bg_label.configure(background='#121212',
                                                     borderwidth='0',
                                                     image=self.img_TeacherRegiusterEntery)
        self.Update_subject_Entry_bg_label.place(anchor='nw',
                                                 x='386',
                                                 y='390')

        self.Update_Id_entry = tk.Entry(self)
        self.Update_Id_entry.configure(borderwidth='0')
        self.Update_Id_entry.configure(font='{Poppins} 10 {bold}',
                                       insertwidth='1',
                                       relief='flat')
        self.Update_Id_entry.place(anchor='nw',
                                   height='24',
                                   width='120',
                                   x='395',
                                   y='103  ')

        self.Update_Id_label = tk.Label(self)
        self.Update_Id_label.configure(background='#121212',
                                       font='{Poppins} 17 {bold}',
                                       foreground='#ffffff',
                                       text='ChangeID')
        self.Update_Id_label.place(anchor='nw',
                                   x='166',
                                   y='96')

        self.Update_first_name_entry = tk.Entry(self)
        self.Update_first_name_entry.configure(borderwidth='0')
        self.Update_first_name_entry.configure(font='{Poppins} 10 {bold}',
                                               insertwidth='1',
                                               relief='flat')
        self.Update_first_name_entry.place(anchor='nw',
                                           height='24',
                                           width='229',
                                           x='395',
                                           y='149')

        self.Update_first_name_label = tk.Label(self)
        self.Update_first_name_label.configure(background='#121212',
                                               font='{Poppins} 17 {bold}',
                                               foreground='#ffffff',
                                               text='First Name')
        self.Update_first_name_label.place(anchor='nw',
                                           x='166',
                                           y='146')

        self.Update_last_name_entry = tk.Entry(self)
        self.Update_last_name_entry.configure(borderwidth='0')
        self.Update_last_name_entry.configure(font='{Poppins} 10 {bold}',
                                              insertwidth='1',
                                              relief='flat')
        self.Update_last_name_entry.place(anchor='nw',
                                          height='24',
                                          width='229',
                                          x='397',
                                          y='199')

        self.Update_last_name_label = tk.Label(self)
        self.Update_last_name_label.configure(background='#121212',
                                              font='{Poppins} 17 {bold}',
                                              foreground='#ffffff',
                                              text='Last Name')
        self.Update_last_name_label.place(anchor='nw',
                                          x='166',
                                          y='198')

        self.Update_phone_number_entry = tk.Entry(self)
        self.Update_phone_number_entry.configure(borderwidth='0')
        self.Update_phone_number_entry.configure(font='{Poppins} 10 {bold}',
                                                 insertwidth='1',
                                                 relief='flat')
        self.Update_phone_number_entry.place(anchor='nw',
                                             height='24',
                                             width='229',
                                             x='397',
                                             y='293')

        self.Update_phone_number_label = tk.Label(self)
        self.Update_phone_number_label.configure(background='#121212',
                                                 font='{Poppins} 17 {bold}',
                                                 foreground='#ffffff',
                                                 text='Phone number')
        self.Update_phone_number_label.place(anchor='nw',
                                             x='166',
                                             y='289')

        self.Update_age_entry = tk.Entry(self)
        self.Update_age_entry.configure(borderwidth='0')
        self.Update_age_entry.configure(font='{Poppins} 10 {bold}',
                                        insertwidth='1',
                                        relief='flat')
        self.Update_age_entry.place(anchor='nw',
                                    height='24',
                                    width='229',
                                    x='395',
                                    y='249')

        self.Update_age_label = tk.Label(self)
        self.Update_age_label.configure(background='#121212',
                                        font='{Poppins} 17 {bold}',
                                        foreground='#ffffff',
                                        text='Age')
        self.Update_age_label.place(anchor='nw',
                                    x='166',
                                    y='239')

        self.Update_gender_label = tk.Label(self)
        self.Update_gender_label.configure(background='#121212',
                                           font='{Poppins} 17 {bold}',
                                           foreground='#ffffff',
                                           text='Gender')
        self.Update_gender_label.place(anchor='nw',
                                       x='166',
                                       y='331')

        self.Update_gender_entry = tk.Entry(self)
        self.Update_gender_entry.configure(borderwidth="0")
        self.Update_gender_entry.configure(font='{Poppins} 10 {bold}',
                                           insertwidth='1',
                                           relief='flat')
        self.Update_gender_entry.place(anchor='nw',
                                       height='24',
                                       width='229',
                                       x='395',
                                       y='343')

        self.Update_subects_label = tk.Label(self)
        self.Update_subects_label.configure(background='#121212',
                                            font='{Poppins} 17 {bold}',
                                            foreground='#ffffff',
                                            text='MaIn Subject')
        self.Update_subects_label.place(anchor='nw',
                                        x='166',
                                        y='389')

        self.Update_subject_entry = tk.Entry(self)
        self.Update_subject_entry.configure(borderwidth="0")
        self.Update_subject_entry.configure(font='{Poppins} 10 {bold}',
                                            insertwidth='1',
                                            relief='flat')
        self.Update_subject_entry.place(anchor='nw',
                                        height='24',
                                        width='229',
                                        x='395',
                                        y='393')

        try:
            self.img_TeacherUpdateButton = tk.PhotoImage(file='Update_Teacher_Btn_img.png')
        except Exception as e:
            messagebox.showerror("Update_Teacher_Btn_img.png Missing")
            print(e)

        self.Update_Update_teachet_button = tk.Button(self)
        self.Update_Update_teachet_button.configure(background='#121212',
                                                    activebackground='#121212',
                                                    activeforeground='#121212',
                                                    borderwidth='0',
                                                    image=self.img_TeacherUpdateButton,
                                                    relief='flat',
                                                    command=self.clickUpdate)
        self.Update_Update_teachet_button.place(anchor='nw',
                                                x='412',
                                                y='448')

        try:
            self.img_TeacherGoButton = tk.PhotoImage(file='Update_Go_button_img.png')
        except Exception as e:
            messagebox.showerror("Update_Go_button_img.png Missing")
            print(e)

        self.Update_Update_Go_button = tk.Button(self)
        self.Update_Update_Go_button.configure(background='#121212',
                                               activebackground='#121212',
                                               activeforeground='#121212',
                                               borderwidth='0',
                                               image=self.img_TeacherGoButton,
                                               relief='flat',
                                               command=self.clickGo)
        self.Update_Update_Go_button.place(anchor='nw',
                                           x='527',
                                           y='95')

        try:
            self.img_img4 = tk.PhotoImage(file='img4.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "img_img4.png is missing")
        self.Update_Teacher_registation_close_button = tk.Button(self)
        self.Update_Teacher_registation_close_button.configure(activebackground='#121212',
                                                               activeforeground='#121212',
                                                               background='#121212',
                                                               borderwidth='0')
        self.Update_Teacher_registation_close_button.configure(cursor='hand2',
                                                               foreground='#121212',
                                                               highlightbackground='#121212',
                                                               highlightcolor='#121212')
        self.Update_Teacher_registation_close_button.configure(highlightthickness='1',
                                                               image=self.img_img4,
                                                               relief='flat',
                                                               command=self.master.on_close)
        self.Update_Teacher_registation_close_button.place(anchor='nw',
                                                           x='760',
                                                           y='8')

        self.Update_Teacher_label = tk.Label(self)
        self.Update_Teacher_label.configure(background='#121212',
                                            borderwidth='0',
                                            font='{Poppins} 28 {bold}',
                                            foreground='#ffffff')
        self.Update_Teacher_label.configure(text='Update Teacher')
        self.Update_Teacher_label.place(anchor='nw',
                                        x='274',
                                        y='28')

        self.Update_back_page_img_button = tk.Button(self)

        try:
            self.img_BackPageIMG = tk.PhotoImage(file='BackPageIMG.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "BackPageIMG.png is missing")

        self.Update_back_page_img_button.configure(activebackground='#121212',
                                                   activeforeground='#121212',
                                                   background='#121212',
                                                   borderwidth='0',
                                                   command=self.goBackToTeacherHome)
        self.Update_back_page_img_button.configure(image=self.img_BackPageIMG)
        self.Update_back_page_img_button.place(anchor='nw', x='15', y='15')

        self.Update_teacher_registation_theme_change_button = tk.Button(self)

        try:
            self.img_DarkThemeimg = tk.PhotoImage(file='DarkThemeimg.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "DarkThemeimg.png is missing")

        self.Update_teacher_registation_theme_change_button.configure(activebackground='#121212',
                                                                      activeforeground='#121212',
                                                                      background='#121212',
                                                                      borderwidth='0',
                                                                      relief="flat",
                                                                      overrelief="flat",
                                                                      command=self.changeTeacherUpdateTheme)
        self.Update_teacher_registation_theme_change_button.configure(image=self.img_DarkThemeimg,
                                                                      text='button2')
        self.Update_teacher_registation_theme_change_button.place(anchor='nw',
                                                                  x='60',
                                                                  y='10')
        self.configure(background='#121212',
                       borderwidth='0',
                       height='515',
                       width='791')
        self.pack(fill='both',
                  side='top')

    def clickGo(self):
        global changeId
        changeId = self.Update_Id_entry.get()

        if changeId == "":
            messagebox.showerror("ID Name Error", "ID Need To Enter ID")
        else:
            try:
                int(changeId)
            except:
                messagebox.showerror("ID Name Error", "ID Need To Enter Numbers")

            self.conn = mysql.connector.connect(
                user="root",
                password="",
                database="eduway")
            self.connetc = self.conn.cursor()
            try:
                self.connetc.execute(
                    "SELECT * FROM teacher WHERE id = {}".format(changeId))
                self.IdRecode = self.connetc.fetchone()
                self.Update_first_name_entry.delete(0, 'end')
                self.Update_first_name_entry.insert(0, self.IdRecode[1])
                self.Update_last_name_entry.delete(0, 'end')
                self.Update_last_name_entry.insert(0, self.IdRecode[2])
                self.Update_age_entry.delete(0, 'end')
                self.Update_age_entry.insert(0, self.IdRecode[4])
                self.Update_phone_number_entry.delete(0, 'end')
                Update_phone_number_add_o = '0' + str(self.IdRecode[3])
                self.Update_phone_number_entry.insert(0, Update_phone_number_add_o)
                self.Update_gender_entry.delete(0, 'end')
                self.Update_gender_entry.insert(0, self.IdRecode[5])
                self.Update_subject_entry.delete(0, 'end')
                self.Update_subject_entry.insert(0, self.IdRecode[6])
            except:
                messagebox.showerror("ID Name Error", "Invalid Id number Or No Id Number Finded")

            self.connetc.close()
            self.conn.close()

    def changeTeacherUpdateTheme(self):
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

        if self.Update_back_page_img_button["background"] == "#121212":
            self.Update_teacherRegistationBGColor = "#ffffff"
            self.Update_teacherRegistationFGColor = "#000000"
            self.configure(background=self.Update_teacherRegistationBGColor)
            self.Update_Id_bg_label.configure(background=self.Update_teacherRegistationBGColor,
                                              foreground=self.Update_teacherRegistationFGColor)
            self.Update_Id_label.configure(background=self.Update_teacherRegistationBGColor,
                                           foreground=self.Update_teacherRegistationFGColor)

            self.Update_Update_Go_button.configure(background=self.Update_teacherRegistationBGColor,
                                                   foreground=self.Update_teacherRegistationFGColor,
                                                   activebackground=self.Update_teacherRegistationBGColor,
                                                   activeforeground=self.Update_teacherRegistationBGColor)
            self.Update_element_img_label.configure(background=self.Update_teacherRegistationBGColor,
                                                    foreground=self.Update_teacherRegistationFGColor)
            self.Update_First_name_Entry_bg_label.configure(background=self.Update_teacherRegistationBGColor,
                                                            foreground=self.Update_teacherRegistationFGColor)
            self.Update_Last_name_Entry_bg_label.configure(background=self.Update_teacherRegistationBGColor,
                                                           foreground=self.Update_teacherRegistationFGColor)
            self.Update_age_Entry_bg_label.configure(background=self.Update_teacherRegistationBGColor,
                                                     foreground=self.Update_teacherRegistationFGColor)
            self.Update_phone_number_Entry_bg_label.configure(background=self.Update_teacherRegistationBGColor,
                                                              foreground=self.Update_teacherRegistationFGColor)
            self.Update_phone_number_Entry_bg_label.configure(background=self.Update_teacherRegistationBGColor,
                                                              foreground=self.Update_teacherRegistationFGColor)
            self.Update_gender_Entry_bg_label.configure(background=self.Update_teacherRegistationBGColor,
                                                        foreground=self.Update_teacherRegistationFGColor)
            self.Update_subject_Entry_bg_label.configure(background=self.Update_teacherRegistationBGColor,
                                                         foreground=self.Update_teacherRegistationFGColor)
            self.Update_first_name_entry.configure(background=self.Update_teacherRegistationBGColor,
                                                   foreground=self.Update_teacherRegistationFGColor)
            self.Update_first_name_label.configure(background=self.Update_teacherRegistationBGColor,
                                                   foreground=self.Update_teacherRegistationFGColor)
            self.Update_last_name_entry.configure(background=self.Update_teacherRegistationBGColor,
                                                  foreground=self.Update_teacherRegistationFGColor)
            self.Update_last_name_label.configure(background=self.Update_teacherRegistationBGColor,
                                                  foreground=self.Update_teacherRegistationFGColor)
            self.Update_phone_number_entry.configure(background=self.Update_teacherRegistationBGColor,
                                                     foreground=self.Update_teacherRegistationFGColor)
            self.Update_phone_number_label.configure(background=self.Update_teacherRegistationBGColor,
                                                     foreground=self.Update_teacherRegistationFGColor)
            self.Update_age_entry.configure(background=self.Update_teacherRegistationBGColor,
                                            foreground=self.Update_teacherRegistationFGColor)
            self.Update_age_label.configure(background=self.Update_teacherRegistationBGColor,
                                            foreground=self.Update_teacherRegistationFGColor)
            self.Update_gender_entry.configure(background=self.Update_teacherRegistationBGColor,
                                               foreground=self.Update_teacherRegistationFGColor)
            self.Update_gender_label.configure(background=self.Update_teacherRegistationBGColor,
                                               foreground=self.Update_teacherRegistationFGColor)
            self.Update_subject_entry.configure(background=self.Update_teacherRegistationBGColor,
                                                foreground=self.Update_teacherRegistationFGColor)
            self.Update_subects_label.configure(background=self.Update_teacherRegistationBGColor,
                                                foreground=self.Update_teacherRegistationFGColor)
            self.Update_Update_teachet_button.configure(background=self.Update_teacherRegistationBGColor,
                                                        foreground=self.Update_teacherRegistationFGColor,
                                                        activebackground=self.Update_teacherRegistationBGColor,
                                                        activeforeground=self.Update_teacherRegistationBGColor)
            self.Update_Teacher_registation_close_button.configure(background=self.Update_teacherRegistationBGColor,
                                                                   foreground=self.Update_teacherRegistationFGColor)
            self.Update_Teacher_label.configure(background=self.Update_teacherRegistationBGColor,
                                                foreground=self.Update_teacherRegistationFGColor)
            self.Update_back_page_img_button.configure(background=self.Update_teacherRegistationBGColor,
                                                       foreground=self.Update_teacherRegistationFGColor,
                                                       activebackground=self.Update_teacherRegistationBGColor,
                                                       activeforeground=self.Update_teacherRegistationBGColor)
            self.Update_teacher_registation_theme_change_button.configure(
                background=self.Update_teacherRegistationBGColor,
                foreground=self.Update_teacherRegistationFGColor,
                activebackground=self.Update_teacherRegistationBGColor,
                activeforeground=self.Update_teacherRegistationBGColor,
                image=self.img_lightThemeimg)
        else:
            self.Update_DteacherRegistationBGColor = "#121212"
            self.Update_DteacherRegistationFGColor = "#ffffff"
            self.configure(background=self.Update_DteacherRegistationBGColor)
            self.Update_Id_bg_label.configure(background=self.Update_DteacherRegistationBGColor,
                                              foreground=self.Update_DteacherRegistationFGColor)
            self.Update_Id_label.configure(background=self.Update_DteacherRegistationBGColor,
                                           foreground=self.Update_DteacherRegistationFGColor)
            self.Update_Update_Go_button.configure(background=self.Update_DteacherRegistationBGColor,
                                                   foreground=self.Update_DteacherRegistationFGColor,
                                                   activebackground=self.Update_DteacherRegistationBGColor,
                                                   activeforeground=self.Update_DteacherRegistationBGColor)
            self.Update_element_img_label.configure(background=self.Update_DteacherRegistationBGColor,
                                                    foreground=self.Update_DteacherRegistationFGColor)
            self.Update_First_name_Entry_bg_label.configure(background=self.Update_DteacherRegistationBGColor,
                                                            foreground=self.Update_DteacherRegistationFGColor)
            self.Update_Last_name_Entry_bg_label.configure(background=self.Update_DteacherRegistationBGColor,
                                                           foreground=self.Update_DteacherRegistationFGColor)
            self.Update_age_Entry_bg_label.configure(background=self.Update_DteacherRegistationBGColor,
                                                     foreground=self.Update_DteacherRegistationFGColor)
            self.Update_phone_number_Entry_bg_label.configure(background=self.Update_DteacherRegistationBGColor,
                                                              foreground=self.Update_DteacherRegistationFGColor)
            self.Update_phone_number_Entry_bg_label.configure(background=self.Update_DteacherRegistationBGColor,
                                                              foreground=self.Update_DteacherRegistationFGColor)
            self.Update_gender_Entry_bg_label.configure(background=self.Update_DteacherRegistationBGColor,
                                                        foreground=self.Update_DteacherRegistationFGColor)
            self.Update_subject_Entry_bg_label.configure(background=self.Update_DteacherRegistationBGColor,
                                                         foreground=self.Update_DteacherRegistationFGColor)
            self.Update_first_name_label.configure(background=self.Update_DteacherRegistationBGColor,
                                                   foreground=self.Update_DteacherRegistationFGColor)
            self.Update_last_name_label.configure(background=self.Update_DteacherRegistationBGColor,
                                                  foreground=self.Update_DteacherRegistationFGColor)
            self.Update_phone_number_label.configure(background=self.Update_DteacherRegistationBGColor,
                                                     foreground=self.Update_DteacherRegistationFGColor)
            self.Update_age_label.configure(background=self.Update_DteacherRegistationBGColor,
                                            foreground=self.Update_DteacherRegistationFGColor)
            self.Update_gender_label.configure(background=self.Update_DteacherRegistationBGColor,
                                               foreground=self.Update_DteacherRegistationFGColor)
            self.Update_subects_label.configure(background=self.Update_DteacherRegistationBGColor,
                                                foreground=self.Update_DteacherRegistationFGColor)
            self.Update_Update_teachet_button.configure(background=self.Update_DteacherRegistationBGColor,
                                                        foreground=self.Update_DteacherRegistationFGColor,
                                                        activebackground=self.Update_DteacherRegistationBGColor,
                                                        activeforeground=self.Update_DteacherRegistationBGColor)
            self.Update_Teacher_registation_close_button.configure(background=self.Update_DteacherRegistationBGColor,
                                                                   foreground=self.Update_DteacherRegistationFGColor)
            self.Update_Teacher_label.configure(background=self.Update_DteacherRegistationBGColor,
                                                foreground=self.Update_DteacherRegistationFGColor)
            self.Update_back_page_img_button.configure(background=self.Update_DteacherRegistationBGColor,
                                                       foreground=self.Update_DteacherRegistationFGColor)
            self.Update_teacher_registation_theme_change_button.configure(
                background=self.Update_DteacherRegistationBGColor,
                foreground=self.Update_DteacherRegistationFGColor,
                activebackground=self.Update_DteacherRegistationBGColor,
                activeforeground=self.Update_DteacherRegistationBGColor,
                image=self.img_DarkThemeimg)

    def goBackToTeacherHome(self):
        self.master.switch_frame(TeacherHome)

    def clickUpdate(self):
        global Update_first_name, Update_last_name, Update_phone_number, Update_age, Update_gender, Update_subjects
        Update_first_name = self.Update_first_name_entry.get()
        Update_last_name = self.Update_last_name_entry.get()
        Update_phone_number = self.Update_phone_number_entry.get()
        Update_age = self.Update_age_entry.get()
        Update_gender = self.Update_gender_entry.get()
        Update_subjects = self.Update_subject_entry.get()

        if Update_first_name == "" or Update_last_name == "" or Update_phone_number == "" or Update_age == "" or Update_gender == "" or Update_subjects == "":
            messagebox.showerror("insert status", "All Fields Are Required")
        else:
            if len(Update_first_name) > 50:
                messagebox.showerror("First Name Error", "Your Name Is Too Long")
            else:
                Update_first_name.capitalize()

                if len(Update_last_name) > 50:
                    messagebox.showerror("Second Name Error", "Your Name Is Too Long")
                else:
                    Update_last_name.capitalize()
                    if Update_first_name == Update_last_name:
                        messagebox.showerror("Copied Name Error", "Your First Name And Secont Name Is Duplicated")
                    else:
                        if len(Update_phone_number) != 10:
                            messagebox.showerror("Phone Number Error", "You Can Add Only 10 Digit number")
                        else:
                            try:
                                int(Update_phone_number)
                            except Exception as e:
                                messagebox.showerror("Type Error", "You Can Only Type Numbers For Phone Number ")
                                print(e)
                            if int(Update_phone_number[0]) != 0:
                                messagebox.showerror("Type Error", "This is Not Phone Number")
                            else:
                                if len(Update_age) > 2:
                                    messagebox.showerror("Age Error", "You Can Only Type Two Numbers For Age ")
                                else:
                                    genderIndex = ['male', "Male", "female", "Female", "m", "M", "F", "f"]
                                    if Update_gender not in genderIndex:
                                        messagebox.showerror("Age Error", "You Can Add Only Type Male or Female ")
                                    else:
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
                                        if checkSubject is False:
                                            messagebox.showerror("Subject Error", "You Can Add Only Subjects ")
                                        else:

                                            self.conn = mysql.connector.connect(
                                                user="root",
                                                password="",
                                                database="eduway")
                                            int(Update_phone_number)
                                            int(Update_age)
                                            self.connetc = self.conn.cursor()
                                            self.connetc.execute(
                                                f"UPDATE teacher SET FirstName='{Update_first_name}',LAstName='{Update_last_name}',PhoneNumber='{Update_phone_number}',Age='{Update_age}',Gender='{Update_gender}',Subjects='{Update_subjects}' WHERE id={changeId}")
                                            # self.connetc.execute()
                                            self.conn.commit()
                                            self.clearTeacherUpdate()
                                            self.connetc.close()
                                            self.conn.close()
                                            # self.master.switch_frame(TeacherView)

    def clearTeacherUpdate(self):
        self.Update_first_name_entry.delete(0, 'end')
        self.Update_subject_entry.delete(0, 'end')
        self.Update_last_name_entry.delete(0, 'end')
        self.Update_gender_entry.delete(0, 'end')
        self.Update_age_entry.delete(0, 'end')
        self.Update_phone_number_entry.delete(0, 'end')


# this is the Teacher Home
# You can do all crud operations in hear
class TeacherHome(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.Element_2_IMG_label = tk.Label(self)

        try:
            self.img_ElementIMG2Label = tk.PhotoImage(file='ElementIMG2Label.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "ElementIMG2Label.png is missing")

        self.Element_2_IMG_label.configure(activebackground='#121212',
                                           activeforeground='#121212',
                                           background='#121212',
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
                                       background="#121212",
                                       activeforeground="#121212",
                                       activebackground="#121212",
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
                                     background="#121212",
                                     activeforeground="#121212",
                                     activebackground="#121212",
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
                                   activebackground="#121212",
                                   activeforeground="#121212",
                                   background="#121212",
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
                                     activeforeground="#121212",
                                     activebackground="#121212",
                                     background="#121212",
                                     command=lambda: master.switch_frame(TeacherDelete))
        self.Delete_button.place(anchor='nw',
                                 x='441',
                                 y='317')

        self.Manege_Teacher_label = tk.Label(self)
        self.Manege_Teacher_label.configure(background='#121212',
                                            borderwidth='0',
                                            font='{Poppins} 28 {bold}',
                                            foreground='#ffffff')
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
        self.Teacher_Manege_close_button.configure(activebackground='#121212',
                                                   activeforeground='#121212',
                                                   background='#121212',
                                                   borderwidth='0')
        self.Teacher_Manege_close_button.configure(cursor='hand2',
                                                   foreground='#121212',
                                                   highlightbackground='#121212',
                                                   highlightcolor='#121212')
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

        self.teacher_Manege_theme_change_button.configure(activebackground='#121212',
                                                          activeforeground='#121212',
                                                          background='#121212',
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

        self.Teacher_home_back_page_img_button.configure(activebackground='#121212',
                                                         activeforeground='#121212',
                                                         background='#121212',
                                                         borderwidth='0',
                                                         command=self.goHome)
        self.Teacher_home_back_page_img_button.configure(image=self.img_BackPageIMG)
        self.Teacher_home_back_page_img_button.place(anchor='nw',
                                                     x='15',
                                                     y='15')

        self.configure(background='#121212',
                       height='515',
                       takefocus=False,
                       width='791')
        self.place(anchor='nw',
                   x='0',
                   y='0')

    def changeTeacherHomeTheme(self):
        if self["background"] == "#121212":
            TeacherHomeBGColor = "#ffffff"
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
            DTeacherHomeBGColor = "#121212"
            DTeacherHomeFGColor = "#ffffff"

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


# This is the Teacher RegisTation 
# You Can Add Data To Database Frome This Frame 
class TeacherRegistation(tk.Frame):
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
        try:
            self.Teacher_img_DarkThemeimg = tk.PhotoImage(file='DarkThemeimg.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "DarkThemeimg.png IS Missing")

        try:
            self.Teacher_img_lightThemeimg = tk.PhotoImage(file='LightThemeimg.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "LightThemeimg.png IS Missing")

        if self.Teacher_back_page_img_button["background"] == "#121212":
            self.TeacherRegistationBGColor = "#ffffff"
            self.TeacherRegistationFGColor = "#000000"
            self.configure(background=self.TeacherRegistationBGColor)
            self.Teacher_element_img_label.configure(background=self.TeacherRegistationBGColor,
                                                     foreground=self.TeacherRegistationFGColor)
            self.Teacher_First_name_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
                                                             foreground=self.TeacherRegistationFGColor)
            self.Teacher_Last_name_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
                                                            foreground=self.TeacherRegistationFGColor)
            self.Teacher_age_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
                                                      foreground=self.TeacherRegistationFGColor)
            self.Teacher_phone_number_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
                                                               foreground=self.TeacherRegistationFGColor)
            self.Teacher_phone_number_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
                                                               foreground=self.TeacherRegistationFGColor)
            self.Teacher_Admission_Number_label.configure(background=self.TeacherRegistationBGColor,
                                                          foreground=self.TeacherRegistationFGColor)
            self.Teacher_subects_label.configure(background=self.TeacherRegistationBGColor,
                                                 foreground=self.TeacherRegistationFGColor)
            self.Teacher_first_name_entry.configure(background=self.TeacherRegistationBGColor,
                                                    foreground=self.TeacherRegistationFGColor)
            self.Teacher_Admission_Number_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
                                                                   foreground=self.TeacherRegistationFGColor)
            self.Teacher_First_name_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
                                                             foreground=self.TeacherRegistationFGColor)
            self.Teacher_Last_name_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
                                                            foreground=self.TeacherRegistationFGColor)
            self.Teacher_age_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
                                                      foreground=self.TeacherRegistationFGColor)
            self.Teacher_phone_number_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
                                                               foreground=self.TeacherRegistationFGColor)
            self.Teacher_Subject_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
                                                          foreground=self.TeacherRegistationFGColor)
            self.Teacher_first_name_label.configure(background=self.TeacherRegistationBGColor,
                                                    foreground=self.TeacherRegistationFGColor)
            self.Teacher_last_name_entry.configure(background=self.TeacherRegistationBGColor,
                                                   foreground=self.TeacherRegistationFGColor)
            self.Teacher_last_name_label.configure(background=self.TeacherRegistationBGColor,
                                                   foreground=self.TeacherRegistationFGColor)
            self.Teacher_phone_number_entry.configure(background=self.TeacherRegistationBGColor,
                                                      foreground=self.TeacherRegistationFGColor)
            self.Teacher_phone_number_label.configure(background=self.TeacherRegistationBGColor,
                                                      foreground=self.TeacherRegistationFGColor)
            self.Teacher_age_entry.configure(background=self.TeacherRegistationBGColor,
                                             foreground=self.TeacherRegistationFGColor)
            self.Teacher_age_label.configure(background=self.TeacherRegistationBGColor,
                                             foreground=self.TeacherRegistationFGColor)
            self.Teacher_Admission_Number_entry.configure(background=self.TeacherRegistationBGColor,
                                                          foreground=self.TeacherRegistationFGColor)
            self.Teacher_Admission_Number_label.configure(background=self.TeacherRegistationBGColor,
                                                          foreground=self.TeacherRegistationFGColor)
            self.Teacher_subject_entry.configure(background=self.TeacherRegistationBGColor,
                                                 foreground=self.TeacherRegistationFGColor)
            self.Teacher_subects_label.configure(background=self.TeacherRegistationBGColor,
                                                 foreground=self.TeacherRegistationFGColor)
            self.add_Teacher_button.configure(background=self.TeacherRegistationBGColor,
                                              foreground=self.TeacherRegistationFGColor,
                                              activebackground=self.TeacherRegistationBGColor,
                                              activeforeground=self.TeacherRegistationBGColor)
            self.Teacher_Subject_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
                                                          foreground=self.TeacherRegistationFGColor)
            self.Teacher_registation_close_button.configure(background=self.TeacherRegistationBGColor,
                                                            foreground=self.TeacherRegistationFGColor)
            self.Teacher_phone_number_Entry_bg_label.configure(background=self.TeacherRegistationBGColor,
                                                               foreground=self.TeacherRegistationFGColor)
            self.Register_Teacher_label.configure(background=self.TeacherRegistationBGColor,
                                                  foreground=self.TeacherRegistationFGColor)
            self.Teacher_back_page_img_button.configure(background=self.TeacherRegistationBGColor,
                                                        foreground=self.TeacherRegistationFGColor,
                                                        activebackground=self.TeacherRegistationBGColor,
                                                        activeforeground=self.TeacherRegistationBGColor)
            self.Teacher_registation_theme_change_button.configure(background=self.TeacherRegistationBGColor,
                                                                   foreground=self.TeacherRegistationFGColor,
                                                                   activebackground=self.TeacherRegistationBGColor,
                                                                   activeforeground=self.TeacherRegistationBGColor,
                                                                   image=self.Teacher_img_lightThemeimg)
        else:
            self.DTeacherRegistationBGColor = "#121212"
            self.DTeacherRegistationFGColor = "#ffffff"
            self.configure(background=self.DTeacherRegistationBGColor)
            self.Teacher_element_img_label.configure(background=self.DTeacherRegistationBGColor,
                                                     foreground=self.DTeacherRegistationFGColor)
            self.Teacher_First_name_Entry_bg_label.configure(background=self.DTeacherRegistationBGColor,
                                                             foreground=self.DTeacherRegistationFGColor)
            self.Teacher_Last_name_Entry_bg_label.configure(background=self.DTeacherRegistationBGColor,
                                                            foreground=self.DTeacherRegistationFGColor)
            self.Teacher_age_Entry_bg_label.configure(background=self.DTeacherRegistationBGColor,
                                                      foreground=self.DTeacherRegistationFGColor)
            self.Teacher_phone_number_Entry_bg_label.configure(background=self.DTeacherRegistationBGColor,
                                                               foreground=self.DTeacherRegistationFGColor)
            self.Teacher_Subject_Entry_bg_label.configure(background=self.DTeacherRegistationBGColor,
                                                          foreground=self.DTeacherRegistationFGColor)
            self.Teacher_first_name_label.configure(background=self.DTeacherRegistationBGColor,
                                                    foreground=self.DTeacherRegistationFGColor)
            self.Teacher_last_name_label.configure(background=self.DTeacherRegistationBGColor,
                                                   foreground=self.DTeacherRegistationFGColor)
            self.Teacher_phone_number_label.configure(background=self.DTeacherRegistationBGColor,
                                                      foreground=self.DTeacherRegistationFGColor)
            self.Teacher_age_label.configure(background=self.DTeacherRegistationBGColor,
                                             foreground=self.DTeacherRegistationFGColor)
            self.Teacher_Admission_Number_label.configure(background=self.DTeacherRegistationBGColor,
                                                          foreground=self.DTeacherRegistationFGColor)
            self.Teacher_subects_label.configure(background=self.DTeacherRegistationBGColor,
                                                 foreground=self.DTeacherRegistationFGColor)
            self.add_Teacher_button.configure(background=self.DTeacherRegistationBGColor,
                                              foreground=self.DTeacherRegistationFGColor,
                                              activebackground=self.DTeacherRegistationBGColor,
                                              activeforeground=self.DTeacherRegistationBGColor)
            self.Teacher_registation_close_button.configure(background=self.DTeacherRegistationBGColor,
                                                            foreground=self.DTeacherRegistationFGColor)
            self.Register_Teacher_label.configure(background=self.DTeacherRegistationBGColor,
                                                  foreground=self.DTeacherRegistationFGColor)
            self.Teacher_back_page_img_button.configure(background=self.DTeacherRegistationBGColor,
                                                        foreground=self.DTeacherRegistationFGColor)
            self.Teacher_Admission_Number_Entry_bg_label.configure(background=self.DTeacherRegistationBGColor,
                                                                   foreground=self.DTeacherRegistationFGColor)
            self.Teacher_First_name_Entry_bg_label.configure(background=self.DTeacherRegistationBGColor,
                                                             foreground=self.DTeacherRegistationFGColor)
            self.Teacher_Last_name_Entry_bg_label.configure(background=self.DTeacherRegistationBGColor,
                                                            foreground=self.DTeacherRegistationFGColor)
            self.Teacher_age_Entry_bg_label.configure(background=self.DTeacherRegistationBGColor,
                                                      foreground=self.DTeacherRegistationFGColor)
            self.Teacher_phone_number_Entry_bg_label.configure(background=self.DTeacherRegistationBGColor,
                                                               foreground=self.DTeacherRegistationFGColor)
            self.Teacher_Subject_Entry_bg_label.configure(background=self.DTeacherRegistationBGColor,
                                                          foreground=self.DTeacherRegistationFGColor)
            self.Teacher_registation_theme_change_button.configure(background=self.DTeacherRegistationBGColor,
                                                                   foreground=self.DTeacherRegistationFGColor,
                                                                   activebackground=self.DTeacherRegistationBGColor,
                                                                   activeforeground=self.DTeacherRegistationBGColor,
                                                                   image=self.Teacher_img_DarkThemeimg)

    def goBackToTeacherHome(self):
        self.master.switch_frame(TeacherHome)

    def clickAdd(self):
        global Teacher_first_name, Teacher_last_name, Teacher_phone_number, Teacher_age, Teacher_Admission_Number, Teacher_subjects
        Teacher_first_name = self.Teacher_first_name_entry.get()
        Teacher_last_name = self.Teacher_last_name_entry.get()
        Teacher_phone_number = self.Teacher_phone_number_entry.get()
        Teacher_age = self.Teacher_age_entry.get()
        Teacher_Admission_Number = self.Teacher_Admission_Number_entry.get()
        Teacher_subjects = self.Teacher_subject_entry.get()
        Update_gender = Teacher_Admission_Number
        Update_subjects = Teacher_subjects
        if Teacher_first_name == "" or Teacher_last_name == "" or Teacher_phone_number == "" or Teacher_age == "" or Update_gender == "" or Update_subjects == "":
            
            try:
                self.Studetn_First_Name_error_label.destroy()
            except:
                pass
            
            self.Teacher_All_Fields_Required_error_label = tk.Label(self)
            self.Teacher_All_Fields_Required_error_label.configure(background='#121212',
                                                    borderwidth='0',
                                                    font='{Poppins} 9 {}',
                                                    foreground='#ff0f15')
            self.Teacher_All_Fields_Required_error_label.configure(text='All Fields Are Required')
            self.Teacher_All_Fields_Required_error_label.place(anchor='nw',
                                                x='500',
                                                y='123')
        else:
            try:
                self.Teacher_All_Fields_Required_error_label.configure(background='#121212',
                                                    borderwidth='0',
                                                    font='{Poppins} 0 {}',
                                                    foreground='#121212')
                self.Teacher_All_Fields_Required_error_label.destroy()
            except:
                pass
            if len(Teacher_first_name) > 50:
                self.Studetn_First_Name_error_label = tk.Label(self)
                self.Studetn_First_Name_error_label.configure(background='#121212',
                                                    borderwidth='0',
                                                    font='{Poppins} 9 {}',
                                                    foreground='#ff0f15')
                self.Studetn_First_Name_error_label.configure(text='First Name Is Too Long')
                self.Studetn_First_Name_error_label.place(anchor='nw',
                                                x='500',
                                                y='123')
            else:
                Teacher_first_name.capitalize()
                try:
                    self.Studetn_First_Name_error_label.configure(background='#121212',
                                                    borderwidth='0',
                                                    font='{Poppins} 9 {}',
                                                    foreground='#121212')
                    self.Studetn_First_Name_error_label.destroy()
                except:
                    pass
                self.Studetn_First_Name_No_error_label = tk.Label(self)
                self.Studetn_First_Name_No_error_label.configure(background='#121212',
                                                    borderwidth='0',
                                                    font='{Poppins} 9 {}',
                                                    foreground='#09ff00')
                self.Studetn_First_Name_No_error_label.configure(text=""+u'\u2713')
                self.Studetn_First_Name_No_error_label.place(anchor='nw',
                                                x='610',
                                                y='123')
                if len(Teacher_last_name) > 50:
                    self.Studetn_Last_Name_error_label = tk.Label(self)
                    self.Studetn_Last_Name_error_label.configure(background='#121212',
                                                        borderwidth='0',
                                                        font='{Poppins} 8 {}',
                                                        foreground='#ff0f15')
                    self.Studetn_Last_Name_error_label.configure(text='Last Name Is Too Long')
                    self.Studetn_Last_Name_error_label.place(anchor='nw',
                                                    x='500',
                                                    y='174')
                else:
                    Teacher_last_name.capitalize()
                    try:
                        self.Studetn_Last_Name_error_label.configure(background='#121212',
                                                        borderwidth='0',
                                                        font='{Poppins} 8 {}',
                                                        foreground='#121212')
                        self.Studetn_Last_Name_error_label.destroy()
                    except:
                        pass

                    self.Studetn_Last_Name_No_error_label = tk.Label(self)
                    self.Studetn_Last_Name_No_error_label.configure(background='#121212',
                                                        borderwidth='0',
                                                        font='{Poppins} 8 {}',
                                                        foreground='#09ff00')
                    self.Studetn_Last_Name_No_error_label.configure(text=""+u'\u2713')
                    self.Studetn_Last_Name_No_error_label.place(anchor='nw',
                                                    x='610',
                                                    y='174')

                                                    
                    if Teacher_first_name.capitalize() == Teacher_last_name.capitalize():
                        messagebox.showerror("Copied Name Error", "Your First Name And Secont Name Is Duplicated")
                    else:
                        if len(Teacher_phone_number) != 10:
                            messagebox.showerror("Phone Number Error", "You Can Add Only 10 Digit number")
                        else:
                            try:
                                int(Teacher_phone_number)
                            except Exception as e:
                                messagebox.showerror("Type Error", "You Can Only Type Numbers For Phone Number ")
                                print(e)
                            if int(Teacher_phone_number[0]) != 0:
                                messagebox.showerror("Type Error", "This is Not Phone Number")
                            else:
                                if len(Teacher_age) > 2:
                                    messagebox.showerror("Age Error", "You Can Only Type Two Numbers For Age ")
                                else:
                                    genderIndex = ['male', "Male", "female", "Female", "m", "M", "F", "f"]
                                    if Update_gender not in genderIndex:
                                        messagebox.showerror("Age Error", "You Can Add Only Type Male or Female ")
                                    else:
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
                                        if checkSubject is False:
                                            messagebox.showerror("Subject Error", "You Can Add Only Subjects ")
                                        else:

                                            self.conn = mysql.connector.connect(
                                                user="root",
                                                password="",
                                                database="eduway")
                                            self.connetc = self.conn.cursor()
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

    def clearTeacherRegistation(self):
        self.Teacher_first_name_entry.delete(0, 'end')
        self.Teacher_subject_entry.delete(0, 'end')
        self.Teacher_last_name_entry.delete(0, 'end')
        self.Teacher_Admission_Number_entry.delete(0, 'end')
        self.Teacher_age_entry.delete(0, 'end')
        self.Teacher_phone_number_entry.delete(0, 'end')


class StudentUpdate(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.Update_Student__element_img_label = tk.Label(self)

        try:
            self.img_Element_1_img_label = tk.PhotoImage(file='Element_1_img_label.png')
        except Exception as e:
            messagebox.showerror("Element_1_img_label.png' Missing")
            print(e)

        self.Update_Student__element_img_label.configure(background='#121212',
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
        self.Update_Student__Id_bg_label.configure(background='#121212',
                                                   borderwidth='0',
                                                   image=self.img_StudentidbgEntery)
        self.Update_Student__Id_bg_label.place(anchor='nw',
                                               x='386',
                                               y='100')

        self.Update_Student_First_name_Entry_bg_label = tk.Label(self)

        self.Update_Student_First_name_Entry_bg_label.configure(background='#121212',
                                                                borderwidth='0',
                                                                image=self.img_StudentRegiusterEntery)
        self.Update_Student_First_name_Entry_bg_label.place(anchor='nw',
                                                            x='386',
                                                            y='146')

        self.Update_Student_Last_name_Entry_bg_label = tk.Label(self)
        self.Update_Student_Last_name_Entry_bg_label.configure(background='#121212',
                                                               borderwidth='0',
                                                               image=self.img_StudentRegiusterEntery)
        self.Update_Student_Last_name_Entry_bg_label.place(anchor='nw',
                                                           x='386',
                                                           y='196')

        self.Update_Student_age_Entry_bg_label = tk.Label(self)
        self.Update_Student_age_Entry_bg_label.configure(background='#121212',
                                                         borderwidth='0',
                                                         image=self.img_StudentRegiusterEntery)
        self.Update_Student_age_Entry_bg_label.place(anchor='nw',
                                                     x='386',
                                                     y='246')

        self.Update_Student_phone_number_Entry_bg_label = tk.Label(self)
        self.Update_Student_phone_number_Entry_bg_label.configure(background='#121212',
                                                                  borderwidth='0',
                                                                  image=self.img_StudentRegiusterEntery)
        self.Update_Student_phone_number_Entry_bg_label.place(anchor='nw',
                                                              x='386',
                                                              y='290')

        self.Update_Student_gender_Entry_bg_label = tk.Label(self)
        self.Update_Student_gender_Entry_bg_label.configure(background='#121212',
                                                            borderwidth='0',
                                                            image=self.img_StudentRegiusterEntery)
        self.Update_Student_gender_Entry_bg_label.place(anchor='nw',
                                                        x='386',
                                                        y='340')

        self.Update_Student_subject_Entry_bg_label = tk.Label(self)
        self.Update_Student_subject_Entry_bg_label.configure(background='#121212',
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
        self.Student_Update_Id_label.configure(background='#121212',
                                               font='{Poppins} 17 {bold}',
                                               foreground='#ffffff',
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
        self.Student_Update_first_name_label.configure(background='#121212',
                                                       font='{Poppins} 17 {bold}',
                                                       foreground='#ffffff',
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
        self.Student_Update_last_name_label.configure(background='#121212',
                                                      font='{Poppins} 17 {bold}',
                                                      foreground='#ffffff',
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
        self.Student_Update_phone_number_label.configure(background='#121212',
                                                         font='{Poppins} 17 {bold}',
                                                         foreground='#ffffff',
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
        self.Student_Update_age_label.configure(background='#121212',
                                                font='{Poppins} 17 {bold}',
                                                foreground='#ffffff',
                                                text='Age')
        self.Student_Update_age_label.place(anchor='nw',
                                            x='166',
                                            y='239')

        self.Student_Update_gender_label = tk.Label(self)
        self.Student_Update_gender_label.configure(background='#121212',
                                                   font='{Poppins} 17 {bold}',
                                                   foreground='#ffffff',
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
        self.Student_Update_subects_label.configure(background='#121212',
                                                    font='{Poppins} 17 {bold}',
                                                    foreground='#ffffff',
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
        self.Student_Update_Update_teachet_button.configure(background='#121212',
                                                            activebackground='#121212',
                                                            activeforeground='#121212',
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
        self.Student_Update_Update_Go_button.configure(background='#121212',
                                                       activebackground='#121212',
                                                       activeforeground='#121212',
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
        self.Student_Update_Student_registation_close_button.configure(activebackground='#121212',
                                                                       activeforeground='#121212',
                                                                       background='#121212',
                                                                       borderwidth='0')
        self.Student_Update_Student_registation_close_button.configure(cursor='hand2',
                                                                       foreground='#121212',
                                                                       highlightbackground='#121212',
                                                                       highlightcolor='#121212')
        self.Student_Update_Student_registation_close_button.configure(highlightthickness='1',
                                                                       image=self.img_img4,
                                                                       relief='flat',
                                                                       command=self.master.on_close)
        self.Student_Update_Student_registation_close_button.place(anchor='nw',
                                                                   x='760',
                                                                   y='8')

        self.Update_Student_label = tk.Label(self)
        self.Update_Student_label.configure(background='#121212',
                                            borderwidth='0',
                                            font='{Poppins} 28 {bold}',
                                            foreground='#ffffff')
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

        self.Student_Update_back_page_img_button.configure(activebackground='#121212',
                                                           activeforeground='#121212',
                                                           background='#121212',
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

        self.Student_Update_Student_registation_theme_change_button.configure(activebackground='#121212',
                                                                              activeforeground='#121212',
                                                                              background='#121212',
                                                                              borderwidth='0',
                                                                              relief="flat",
                                                                              overrelief="flat",
                                                                              command=self.changeStudentUpdateTheme)
        self.Student_Update_Student_registation_theme_change_button.configure(image=self.img_DarkThemeimg,
                                                                              text='button2')
        self.Student_Update_Student_registation_theme_change_button.place(anchor='nw',
                                                                          x='60',
                                                                          y='10')
        self.configure(background='#121212',
                       borderwidth='0',
                       height='515',
                       width='791')
        self.pack(fill='both',
                  side='top')

    def clickGo(self):
        global Student_changeId

        Student_changeId = self.Student_Update_Id_entry.get()

        if Student_changeId == "":
            messagebox.showerror("ID Name Error", "ID Need To Enter ID")
        else:
            try:
                int(Student_changeId)
            except:
                messagebox.showerror("ID Name Error", "ID Need To Enter Numbers")

            self.conn = mysql.connector.connect(
                user="root",
                password="",
                database="eduway")
            self.connetc = self.conn.cursor()
            try:
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
                messagebox.showerror("ID Name Error", "Invalid Id number Or No Id Number Finded")

            self.connetc.close()
            self.conn.close()

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
            self.Update_StudentRegistationBGColor = "#ffffff"
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
        else:
            self.Update_DStudentRegistationBGColor = "#121212"
            self.Update_DStudentRegistationFGColor = "#ffffff"
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

    def goBackToStudentHome(self):
        self.master.switch_frame(StudentHome)

    def clickUpdate(self):
        global Student_Update_first_name, Student_Update_last_name, Student_Update_phone_number, Student_Update_age, Student_Update_gender, Student_Update_subjects
        Student_Update_first_name = self.Student_Update_first_name_entry.get()
        Student_Update_last_name = self.Student_Update_last_name_entry.get()
        Student_Update_phone_number = self.Student_Update_phone_number_entry.get()
        Student_Update_age = self.Student_Update_age_entry.get()
        Student_Update_gender = self.Student_Update_gender_entry.get()
        Student_Update_subjects = self.Student_Update_subject_entry.get()

        if Student_Update_first_name == "" or Student_Update_last_name == "" or Student_Update_phone_number == "" or Student_Update_age == "" or Student_Update_gender == "" or Student_Update_subjects == "":
            messagebox.showerror("insert status", "All Fields Are Required")
        else:
            if len(Student_Update_first_name) > 50:
                messagebox.showerror("First Name Error", "Your Name Is Too Long")
            else:
                Student_Update_first_name.capitalize()

                if len(Student_Update_last_name) > 50:
                    messagebox.showerror("Second Name Error", "Your Name Is Too Long")
                else:
                    Student_Update_last_name.capitalize()
                    if Student_Update_first_name == Student_Update_last_name:
                        messagebox.showerror("Copied Name Error", "Your First Name And Secont Name Is Duplicated")
                    else:
                        if len(Student_Update_phone_number) != 10:
                            messagebox.showerror("Phone Number Error", "You Can Add Only 10 Digit number")
                        else:
                            try:
                                int(Student_Update_phone_number)
                            except Exception as e:
                                messagebox.showerror("Type Error", "You Can Only Type Numbers For Phone Number ")
                                print(e)
                            if int(Student_Update_phone_number[0]) != 0:
                                messagebox.showerror("Type Error", "This is Not Phone Number")
                            else:
                                try:
                                    self.Student_Admission_Number = int(Student_Update_gender)
                                except:
                                    messagebox.showerror("AdmissionNumber Error",
                                                         "You Can Only Type  Numbers For AdmissionNumber ")

                                if len(Student_Update_age) > 2:
                                    messagebox.showerror("Age Error", "You Can Only Type Two Numbers For Age ")
                                else:
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

                                        checkSubject = all(
                                            item in AllSubjects for item in Student_Update_subjects.split(","))
                                        if checkSubject is False:
                                            messagebox.showerror("Subject Error", "You Can Add Only Subjects ")
                                        else:

                                            self.conn = mysql.connector.connect(
                                                user="root",
                                                password="",
                                                database="eduway")
                                            int(Student_Update_phone_number)
                                            int(Student_Update_age)
                                            self.connetc = self.conn.cursor()
                                            self.connetc.execute(
                                                f"UPDATE Student SET FirstName='{Student_Update_first_name}',LAstName='{Student_Update_last_name}',PhoneNumber='{Student_Update_phone_number}',Age='{Student_Update_age}',StudentAdmissionNumber='{(Student_Update_gender)}',Subjects='{Student_Update_subjects}' WHERE id={Student_changeId}")
                                            # self.connetc.execute()
                                            self.conn.commit()
                                            self.clearStudentUpdate()
                                            self.connetc.close()
                                            self.conn.close()
                                            # self.master.switch_frame(StudentView)
                                    else:
                                        messagebox.showerror("AdmissionNumber Error",
                                                             "You Can Only Type  Numbers For AdmissionNumber ")

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


# this is the Student View
# You can watch all Deatail About All Student
class StudentView(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.sty = ttk.Style()
        self.sty.configure('Treeview', rowheight=46, fieldbackground="#000000")
        self.sty.map('Treeview', background=[('selected', '#3B3B3B'), ('focus', '#212121')])
        self.sty.configure("Vertical.TScrollbar",
                           background="#000000", darkcolor="#000000", lightcolor="#000000",
                           troughcolor="gray", bordercolor="gray", arrowcolor="#000000")
        self.Student_recodes_scroll = ttk.Scrollbar(self)
        self.columns = ('ID',
                        'First name',
                        'Last name',
                        'Age',
                        'Phone Number',
                        'AdmissionNo',
                        'Subjects')
        self.Student_recodes = ttk.Treeview(height=8, columns=self.columns, show="tree",
                                            yscrollcommand=self.Student_recodes_scroll.set)

        # self.Student_recodes.heading("ID", text="ID")
        # self.Student_recodes.heading("First name", text="First name")
        # self.Student_recodes.heading("Last name", text="Last name")
        # self.Student_recodes.heading("Age", text="Age")
        # self.Student_recodes.heading("Phone Number", text="Phone Number")
        # self.Student_recodes.heading("Gender", text="Gender")
        # self.Student_recodes.heading("Subjects", text="Subjects")

        self.Student_recodes.column("ID", width=50)
        self.Student_recodes.column("First name", width=150)
        self.Student_recodes.column("Last name", width=130)
        self.Student_recodes.column("Age", width=50)
        self.Student_recodes.column("Phone Number", width=130)
        self.Student_recodes.column("AdmissionNo", width=100)
        self.Student_recodes.column("Subjects", width=220)

        # Add data
        self.conn = mysql.connector.connect(user="root",
                                            password="",
                                            database="eduway")

        self.connetc = self.conn.cursor()
        self.connetc.execute("SELECT * FROM student")
        self.recodes = self.connetc.fetchall()
        global count

        count = 0
        self.Student_recodes.tag_configure("oneColorStudent", background="#121212",
                                           font='{Poppins} 8 {bold}',
                                           foreground="#c2c2c2")

        self.Student_recodes.tag_configure("secondColorStudent", background="#0a0a0a",
                                           font='{Poppins} 8 {bold}',
                                           foreground="#c2c2c2")

        for record in self.recodes:
            if count % 2 == 0:
                self.Student_recodes.insert(parent="", index='end', iid=count, values=(
                    record[0], record[1], record[2], record[4], "0" + str(record[3]), record[5], record[6]),
                                            tags=("oneColorStudent"))
                if count <=7:
                    self.Student_recodes.configure(height=int(count))
                else:
                    self.Student_recodes.configure(height="8")
                    print("hi")
            else:
                self.Student_recodes.insert(parent="", index='end', iid=count, values=(
                    record[0], record[1], record[2], record[4], "0" + str(record[3]), record[5], record[6]),
                                            tags=("secondColorStudent"))
                if count <=7:
                    self.Student_recodes.configure(height=int(count))
                else:
                    self.Student_recodes.configure(height="8")
                    print("hi")
            count += 1
            print(count)
        
        self.connetc.close()
        self.conn.close()

        # self.Student_recodes.insert()

        self.Student_recodes.place(anchor='nw', x='0', y='146', relx="-0.24", bordermode='ignore')
        self.Student_recodes_scroll.configure(command=self.Student_recodes.yview)
        self.Student_recodes_scroll.configure(orient='vertical', )
        self.Student_recodes_scroll.place(anchor='nw', height='0', x='0', y='0')

        self.Student_view_theme_change_button = tk.Button(self)

        try:
            self.img_DarkThemeimg = tk.PhotoImage(file='DarkThemeimg.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "DarkThemeimg.png is missing")

        self.Student_view_theme_change_button.configure(activebackground='#121212',
                                                        activeforeground='#121212',
                                                        background='#121212',
                                                        borderwidth='0',
                                                        relief="flat",
                                                        overrelief="flat")
        self.Student_view_theme_change_button.configure(image=self.img_DarkThemeimg,
                                                        text='button2',
                                                        command=self.changeStudentViewTheme)
        self.Student_view_theme_change_button.place(anchor='nw',
                                                    x='60',
                                                    y='10')

        self.Student_home_back_page_img_button = tk.Button(self)

        try:
            self.img_BackPageIMG = tk.PhotoImage(file='BackPageIMG.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "BackPageIMG.png is missing")

        self.Student_home_back_page_img_button.configure(activebackground='#121212',
                                                         activeforeground='#121212',
                                                         background='#121212',
                                                         borderwidth='0',
                                                         command=self.goBackToStudentHome)
        self.Student_home_back_page_img_button.configure(image=self.img_BackPageIMG)
        self.Student_home_back_page_img_button.place(anchor='nw', x='15', y='15')

        try:
            self.img_img4 = tk.PhotoImage(file='img4.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "img_img4.png is missing")
        self.Student_view_close_button = tk.Button(self)
        self.Student_view_close_button.configure(activebackground='#121212',
                                                 activeforeground='#121212',
                                                 background='#121212',
                                                 borderwidth='0')
        self.Student_view_close_button.configure(cursor='hand2',
                                                 foreground='#121212',
                                                 highlightbackground='#121212',
                                                 highlightcolor='#121212')
        self.Student_view_close_button.configure(highlightthickness='1',
                                                 image=self.img_img4,
                                                 relief='flat',
                                                 command=self.master.on_close)
        self.Student_view_close_button.place(anchor='nw',
                                             x='760',
                                             y='8')
        self.View_Student_label = tk.Label(self)
        self.View_Student_label.configure(background='#121212',
                                          borderwidth='0',
                                          font='{Poppins} 28 {bold}',
                                          foreground='#ffffff')
        self.View_Student_label.configure(text='View Student')
        self.View_Student_label.place(anchor='nw',
                                      x='274',
                                      y='28')

        self.Student_ID_label = tk.Label(self)
        self.Student_ID_label.configure(background='#121212',
                                        borderwidth='0',
                                        font='{Poppins} 10 {bold}',
                                        foreground='#ffffff')
        self.Student_ID_label.configure(text='ID')
        self.Student_ID_label.place(anchor='nw',
                                    x='16',
                                    y='115')

        self.Student_First_Name_label = tk.Label(self)
        self.Student_First_Name_label.configure(background='#121212',
                                                borderwidth='0',
                                                font='{Poppins} 10 {bold}',
                                                foreground='#ffffff')
        self.Student_First_Name_label.configure(text='First Name')
        self.Student_First_Name_label.place(anchor='nw',
                                            x='55',
                                            y='115')

        self.Student_Second_Name_label = tk.Label(self)
        self.Student_Second_Name_label.configure(background='#121212',
                                                 borderwidth='0',
                                                 font='{Poppins} 10 {bold}',
                                                 foreground='#ffffff')
        self.Student_Second_Name_label.configure(text='Last Name')
        self.Student_Second_Name_label.place(anchor='nw',
                                             x='210',
                                             y='115')

        self.Student_Age_label = tk.Label(self)
        self.Student_Age_label.configure(background='#121212',
                                         borderwidth='0',
                                         font='{Poppins} 10 {bold}',
                                         foreground='#ffffff')
        self.Student_Age_label.configure(text='Age')
        self.Student_Age_label.place(anchor='nw',
                                     x='340',
                                     y='115')

        self.Student_Phone_Number_label = tk.Label(self)
        self.Student_Phone_Number_label.configure(background='#121212',
                                                  borderwidth='0',
                                                  font='{Poppins} 10 {bold}',
                                                  foreground='#ffffff')
        self.Student_Phone_Number_label.configure(text='Phone Number')
        self.Student_Phone_Number_label.place(anchor='nw',
                                              x='390',
                                              y='115')

        self.Student_Admission_Number_label = tk.Label(self)
        self.Student_Admission_Number_label.configure(background='#121212',
                                                      borderwidth='0',
                                                      font='{Poppins} 10 {bold}',
                                                      foreground='#ffffff')
        self.Student_Admission_Number_label.configure(text='AdmissionNO')
        self.Student_Admission_Number_label.place(anchor='nw',
                                                  x='520',
                                                  y='115')

        self.Student_Main_Subject_label = tk.Label(self)
        self.Student_Main_Subject_label.configure(background='#121212',
                                                  borderwidth='0',
                                                  font='{Poppins} 10 {bold}',
                                                  foreground='#ffffff')
        self.Student_Main_Subject_label.configure(text='Main Subject')
        self.Student_Main_Subject_label.place(anchor='nw',
                                              x='625',
                                              y='115')

        self.configure(background='#121212',
                       height='515',
                       width='791')

        self.place(anchor='nw',
                   x='0',
                   y='0')

    def goBackToStudentHome(self):
        self.master.switch_frame(StudentHome)

    def changeStudentViewTheme(self):

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
            StudentViewBackgroundColor = "#ffffff"
            StudentViewForegroundColor = "#000000"

            self.configure(background=StudentViewBackgroundColor)
            self.sty.map('Treeview', background=[('selected', '#4d4d4d'), ('focus', '#212121')])
            self.Student_recodes.tag_configure("secondColorStudent", background=StudentViewBackgroundColor,
                                               font='{Poppins} 8 {bold}',
                                               foreground=StudentViewForegroundColor)
            self.Student_recodes.tag_configure("oneColorStudent", background="#e6e6e6",
                                               font='{Poppins} 8 {bold}',
                                               foreground=StudentViewForegroundColor)
            # self.Student_view_theme_change_button  
            self.Student_home_back_page_img_button.configure(background=StudentViewBackgroundColor,
                                                             foreground=StudentViewForegroundColor)
            self.Student_view_close_button.configure(background=StudentViewBackgroundColor,
                                                     foreground=StudentViewForegroundColor)
            self.View_Student_label.configure(background=StudentViewBackgroundColor,
                                              foreground=StudentViewForegroundColor)
            self.Student_ID_label.configure(background=StudentViewBackgroundColor,
                                            foreground=StudentViewForegroundColor)
            self.Student_First_Name_label.configure(background=StudentViewBackgroundColor,
                                                    foreground=StudentViewForegroundColor)
            self.Student_Second_Name_label.configure(background=StudentViewBackgroundColor,
                                                     foreground=StudentViewForegroundColor)
            self.Student_Age_label.configure(background=StudentViewBackgroundColor,
                                             foreground=StudentViewForegroundColor)
            self.Student_Phone_Number_label.configure(background=StudentViewBackgroundColor,
                                                      foreground=StudentViewForegroundColor)
            self.Student_Admission_Number_label.configure(background=StudentViewBackgroundColor,
                                                          foreground=StudentViewForegroundColor)
            self.Student_Main_Subject_label.configure(background=StudentViewBackgroundColor,
                                                      foreground=StudentViewForegroundColor)
            self.Student_view_theme_change_button.configure(background=StudentViewBackgroundColor,
                                                            foreground=StudentViewForegroundColor,
                                                            image=self.img_lightThemeimg)
        else:
            DStudentViewBackgroundColor = "#121212"
            DStudentViewForegroundColor = "#ffffff"

            self.configure(background=DStudentViewBackgroundColor)
            self.sty.map('Treeview', background=[('selected', '#3B3B3B'), ('focus', '#212121')])
            self.Student_recodes.tag_configure("secondColorStudent", background=DStudentViewBackgroundColor,
                                               font='{Poppins} 8 {bold}',
                                               foreground="#c2c2c2")
            self.Student_recodes.tag_configure("oneColorStudent", background="#0a0a0a",
                                               font='{Poppins} 8 {bold}',
                                               foreground="#c2c2c2")
            # self.Student_view_theme_change_button
            self.Student_home_back_page_img_button.configure(background=DStudentViewBackgroundColor,
                                                             foreground=DStudentViewForegroundColor)
            self.Student_view_close_button.configure(background=DStudentViewBackgroundColor,
                                                     foreground=DStudentViewForegroundColor)
            self.View_Student_label.configure(background=DStudentViewBackgroundColor,
                                              foreground=DStudentViewForegroundColor)
            self.Student_ID_label.configure(background=DStudentViewBackgroundColor,
                                            foreground=DStudentViewForegroundColor)
            self.Student_First_Name_label.configure(background=DStudentViewBackgroundColor,
                                                    foreground=DStudentViewForegroundColor)
            self.Student_Second_Name_label.configure(background=DStudentViewBackgroundColor,
                                                     foreground=DStudentViewForegroundColor)
            self.Student_Age_label.configure(background=DStudentViewBackgroundColor,
                                             foreground=DStudentViewForegroundColor)
            self.Student_Phone_Number_label.configure(background=DStudentViewBackgroundColor,
                                                      foreground=DStudentViewForegroundColor)
            self.Student_Admission_Number_label.configure(background=DStudentViewBackgroundColor,
                                                          foreground=DStudentViewForegroundColor)
            self.Student_Main_Subject_label.configure(background=DStudentViewBackgroundColor,
                                                      foreground=DStudentViewForegroundColor)
            self.Student_view_theme_change_button.configure(background=DStudentViewBackgroundColor,
                                                            foreground=DStudentViewForegroundColor,
                                                            image=self.img_DarkThemeimg)


# This Is The Teacher View
# You Can Watch All Deatail About All Teachers
# need to repair
class TeacherView(tk.Frame):
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
            else:
                self.teacher_recodes.insert(parent="", index='end', iid=count, values=(
                    record[0], record[1], record[2], record[4], "0" + str(record[3]), record[5], record[6]),
                                            tags=("secondColor"))
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


# Abiout me
class AboutMe(tk.Frame):
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
        self.configure(background='#121212',
                       height='515',
                       width='791')
        self.place(x='0', y="0")

    def goAboutMeHome(self):
        self.master.switch_frame(Home)


# this is the About page this page have option watch about me
# run_the_app_in_Hr_____VVVVVVVVVVV@
if __name__ == "__main__":
    app = SchoolManegmentSystem()
    app.title("EDUWAY")
    app.eval('tk::PlaceWindow . center')
    app.attributes('-topmost', True)
    app.resizable(False, False)
    app.overrideredirect(False)
    app.mainloop()
# @^^^^^^^  ^o^
