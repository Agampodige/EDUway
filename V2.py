#**********************************************************************************#
#################Copyrigh@Rashith Senishka De Silva#################################

##########################################Import Sys##################################
from ast import Pass
import sys

###################################Import Time For Splash Screen#############
import time

##################Import ttk for Treeview##############################
import tkinter.ttk as ttk

##################Import massage for errors
from tkinter import messagebox
from turtle import home
# from urllib.parse import parse_qs


###################Cheking Python vertion for import tkinter######################
if sys.version_info[0] == 2:
#####################import tkinter if python vertion is old###########################
    import Tkinter as tk
else:
    import tkinter as tk
############################Import mysql for connect db###################################

import mysql.connector
##########################################################################################

            #############################
            ################################
            ##################################
            ########              ############
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
            ########           #######
            ########            ######

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
###############################this is the app#####################################################################
class SchoolManegmentSystem(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
####################################### this is the page first load#################################################
        self.switch_frame(SplashScreen)
####################################################This is the funtion for switch##################################
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
class SplashScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        try:
            self.img_splash = tk.PhotoImage(file='splash.png')
        except Exception as e:
            print(e)
            messagebox.showerror("Image Missing", "splash.png is missing")

        self.configure(height='515',
                       width='791',
                       background="#090D10")
        self.Splash_Bg_img = tk.Label()

        self.Splash_Bg_img.configure(image=self.img_splash, borderwidth='0', relief='flat')
        self.Splash_Bg_img.place(x='0', y='0')

        self.after(3000, lambda: master.switch_frame(DarkHome))

        self.place(x='0', y='0')
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
#######################################################This is the login page######################################
class LogInPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.bgcolor = "#121212"
        self.fgcolor = "#000000"
        self.backg = tk.Label(self)

        try:
            self.img_background = tk.PhotoImage(file='background.png')
        except Exception as e:
            print(e)
            messagebox.showerror("Image Missing", "backfround.png is missing")

        self.backg.configure(background=self.bgcolor,
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
                                  background=self.bgcolor,
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
            self.password_error_label.configure(foreground=self.bgcolor)
            self.username_error_label.configure(foreground=self.bgcolor)
        except:
            pass

        try:
            self.password_empty_error_label.configure(foreground=self.bgcolor)
            self.username_empty_error_label.configure(foreground=self.bgcolor)
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
class DarkHome(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.fgcolor = "#ffffff"
        self.bgcolor = "#121212"
        try:
            self.img_Home_Banner = tk.PhotoImage(file='HomeBanner.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "HomeBanner.png")

        self.home_banner_label = tk.Label(self)
        self.home_banner_label.configure(image=self.img_Home_Banner, background=self.bgcolor , borderwidth="0")
        self.home_banner_label.place(x="0",
                                     y="0")

        try:
            self.img_Home_Teacher = tk.PhotoImage(file='HomeTeacher.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "HomeTeacher.png")

        self.home_teacher_button = tk.Button(self)
        self.home_teacher_button.configure(image=self.img_Home_Teacher,
                                           background=self.bgcolor,
                                           borderwidth="0",
                                           relief="flat",
                                           activebackground=self.bgcolor,
                                           activeforeground=self.bgcolor,
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
                                           background=self.bgcolor,
                                           borderwidth="0",
                                           relief="flat",
                                           activebackground=self.bgcolor,
                                           activeforeground=self.bgcolor,
                                           command=lambda: master.switch_frame(DarkStudentHome))
        self.home_Student_button.place(x="319",
                                       y="280")

        try:
            self.img_Home_About_Us = tk.PhotoImage(file='HomeAboutUs.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "HomeAboutUs.png is missing")

        self.home_About_Us_button = tk.Button(self)
        self.home_About_Us_button.configure(image=self.img_Home_About_Us,
                                            background=self.bgcolor,
                                            borderwidth="0",
                                            relief="flat",
                                            activebackground=self.bgcolor,
                                            activeforeground=self.bgcolor,
                                            command=lambda: master.switch_frame(AboutMe))
        self.home_About_Us_button.place(x="508",
                                        y="280")

        self.configure(background=self.bgcolor,
                       height='515',
                       takefocus=False,
                       width='791')
        self.place(x="0",
                   y="0")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
class LightHome(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.fgcolor = "#121212"
        self.bgcolor = "#ffffff"
        try:
            self.img_Home_Banner = tk.PhotoImage(file='HomeBanner.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "HomeBanner.png")

        self.home_banner_label = tk.Label(self)
        self.home_banner_label.configure(image=self.img_Home_Banner, background=self.bgcolor,borderwidth="0")
        self.home_banner_label.place(x="0",
                                     y="0")

        try:
            self.img_Home_Teacher = tk.PhotoImage(file='HomeTeacher.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "HomeTeacher.png")

        self.home_teacher_button = tk.Button(self)
        self.home_teacher_button.configure(image=self.img_Home_Teacher,
                                           background=self.bgcolor,
                                           borderwidth="0",
                                           relief="flat",
                                           activebackground=self.bgcolor,
                                           activeforeground=self.bgcolor,
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
                                           background=self.bgcolor,
                                           borderwidth="0",
                                           relief="flat",
                                           activebackground=self.bgcolor,
                                           activeforeground=self.bgcolor,
                                           command=lambda: master.switch_frame(LightStudentHome))
        self.home_Student_button.place(x="319",
                                       y="280")

        try:
            self.img_Home_About_Us = tk.PhotoImage(file='HomeAboutUs.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "HomeAboutUs.png is missing")

        self.home_About_Us_button = tk.Button(self)
        self.home_About_Us_button.configure(image=self.img_Home_About_Us,
                                            background=self.bgcolor,
                                            borderwidth="0",
                                            relief="flat",
                                            activebackground=self.bgcolor,
                                            activeforeground=self.bgcolor,
                                            command=lambda: master.switch_frame(AboutMe))
        self.home_About_Us_button.place(x="508",
                                        y="280")

        self.configure(background=self.bgcolor,
                       height='515',
                       takefocus=False,
                       width='791')
        self.place(x="0",
                   y="0")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

class DarkStudentHome(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.bgcolor = "#121212"
        self.fgcolor = "#ffffff"
        self.Student_Element_2_IMG_label = tk.Label(self)

        try:
            self.img_ElementIMG2Label = tk.PhotoImage(file='ElementIMG2Label.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "ElementIMG2Label.png is missing")

        self.Student_Element_2_IMG_label.configure(activebackground=self.bgcolor,
                                                   activeforeground=self.bgcolor,
                                                   background=self.bgcolor,
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
                                               background=self.bgcolor,
                                               activeforeground=self.bgcolor,
                                               activebackground=self.bgcolor,
                                               image=self.img_TeacherHomeAddButton,
                                               command=lambda: master.switch_frame(DarkStudentRegistation))
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
                                             background=self.bgcolor,
                                             activeforeground=self.bgcolor,
                                             activebackground=self.bgcolor,
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
                                           activebackground=self.bgcolor,
                                           activeforeground=self.bgcolor,
                                           background=self.bgcolor,
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
                                             activeforeground=self.bgcolor,
                                             activebackground=self.bgcolor,
                                             background=self.bgcolor,
                                             command=lambda: master.switch_frame(StudentDelete))
        self.Student_Delete_button.place(anchor='nw',
                                         x='441',
                                         y='317')

        self.Manege_Student_label = tk.Label(self)
        self.Manege_Student_label.configure(background=self.bgcolor,
                                            borderwidth='0',
                                            font='{Poppins} 28 {bold}',
                                            foreground=self.fgcolor)
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
        self.Student_Manege_close_button.configure(activebackground=self.bgcolor,
                                                   activeforeground=self.bgcolor,
                                                   background=self.bgcolor,
                                                   borderwidth='0')
        self.Student_Manege_close_button.configure(cursor='hand2',
                                                   foreground=self.bgcolor,
                                                   highlightbackground=self.bgcolor,
                                                   highlightcolor=self.bgcolor)
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

        self.Student_Manege_theme_change_button.configure(activebackground=self.bgcolor,
                                                          activeforeground=self.bgcolor,
                                                          background=self.bgcolor,
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

        self.Student_home_back_page_img_button.configure(activebackground=self.bgcolor,
                                                         activeforeground=self.bgcolor,
                                                         background=self.bgcolor,
                                                         borderwidth='0',
                                                         command=self.goHome)
        self.Student_home_back_page_img_button.configure(image=self.img_BackPageIMG)
        self.Student_home_back_page_img_button.place(anchor='nw',
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
        self.master.switch_frame(LightStudentHome)
        # if self["background"] == "#121212":
        #     TeacherHomeBGColor = "#ffffff"
        #     TeacherHomeFGColor = "#000000"

        #     try:
        #         self.img_DarkThemeimg = tk.PhotoImage(file='DarkThemeimg.png')
        #     except Exception as e:
        #         print(e)
        #         messagebox.showerror("File Missing", "DarkThemeimg.png IS Missing")

        #     try:
        #         self.img_lightThemeimg = tk.PhotoImage(file='LightThemeimg.png')
        #     except Exception as e:
        #         print(e)
        #         messagebox.showerror("File Missing", "LightThemeimg.png IS Missing")

        #     self.configure(background=TeacherHomeBGColor)
        #     self.Student_register_button.configure(background=TeacherHomeBGColor,
        #                                            foreground=TeacherHomeBGColor,
        #                                            activebackground=TeacherHomeBGColor,
        #                                            activeforeground=TeacherHomeBGColor)
        #     self.Student_Element_2_IMG_label.configure(background=TeacherHomeBGColor,
        #                                                foreground=TeacherHomeFGColor)
        #     self.Student_update_button.configure(background=TeacherHomeBGColor,
        #                                          foreground=TeacherHomeBGColor,
        #                                          activebackground=TeacherHomeBGColor,
        #                                          activeforeground=TeacherHomeBGColor)
        #     self.Student_view_button.configure(background=TeacherHomeBGColor,
        #                                        foreground=TeacherHomeBGColor,
        #                                        activebackground=TeacherHomeBGColor,
        #                                        activeforeground=TeacherHomeBGColor)
        #     self.Student_Delete_button.configure(background=TeacherHomeBGColor,
        #                                          foreground=TeacherHomeBGColor,
        #                                          activebackground=TeacherHomeBGColor,
        #                                          activeforeground=TeacherHomeBGColor)
        #     self.Manege_Student_label.configure(background=TeacherHomeBGColor,
        #                                         foreground=TeacherHomeFGColor,
        #                                         activebackground=TeacherHomeBGColor,
        #                                         activeforeground=TeacherHomeBGColor)
        #     self.Student_Manege_close_button.configure(background=TeacherHomeBGColor,
        #                                                foreground=TeacherHomeBGColor,
        #                                                activebackground=TeacherHomeBGColor,
        #                                                activeforeground=TeacherHomeBGColor)
        #     self.Student_Manege_theme_change_button.configure(background=TeacherHomeBGColor,
        #                                                       foreground=TeacherHomeBGColor,
        #                                                       activebackground=TeacherHomeBGColor,
        #                                                       activeforeground=TeacherHomeBGColor,
        #                                                       image=self.img_lightThemeimg)
        #     self.Student_home_back_page_img_button.configure(background=TeacherHomeBGColor,
        #                                                      foreground=TeacherHomeBGColor,
        #                                                      activebackground=TeacherHomeBGColor,
        #                                                      activeforeground=TeacherHomeBGColor, )
        # else:
        #     DTeacherHomeBGColor = "#121212"
        #     DTeacherHomeFGColor = "#ffffff"

        #     self.configure(background=DTeacherHomeBGColor)
        #     self.Student_register_button.configure(background=DTeacherHomeBGColor,
        #                                            foreground=DTeacherHomeBGColor,
        #                                            activebackground=DTeacherHomeBGColor,
        #                                            activeforeground=DTeacherHomeBGColor)
        #     self.Student_Element_2_IMG_label.configure(background=DTeacherHomeBGColor,
        #                                                foreground=DTeacherHomeFGColor)
        #     self.Student_update_button.configure(background=DTeacherHomeBGColor,
        #                                          foreground=DTeacherHomeBGColor,
        #                                          activebackground=DTeacherHomeBGColor,
        #                                          activeforeground=DTeacherHomeBGColor)
        #     self.Student_view_button.configure(background=DTeacherHomeBGColor,
        #                                        foreground=DTeacherHomeBGColor,
        #                                        activebackground=DTeacherHomeBGColor,
        #                                        activeforeground=DTeacherHomeBGColor)
        #     self.Student_Delete_button.configure(background=DTeacherHomeBGColor,
        #                                          foreground=DTeacherHomeBGColor,
        #                                          activebackground=DTeacherHomeBGColor,
        #                                          activeforeground=DTeacherHomeBGColor)
        #     self.Manege_Student_label.configure(background=DTeacherHomeBGColor,
        #                                         foreground=DTeacherHomeFGColor,
        #                                         activebackground=DTeacherHomeBGColor,
        #                                         activeforeground=DTeacherHomeBGColor)
        #     self.Student_Manege_close_button.configure(background=DTeacherHomeBGColor,
        #                                                foreground=DTeacherHomeBGColor,
        #                                                activebackground=DTeacherHomeBGColor,
        #                                                activeforeground=DTeacherHomeBGColor)
        #     self.Student_Manege_theme_change_button.configure(background=DTeacherHomeBGColor,
        #                                                       foreground=DTeacherHomeBGColor,
        #                                                       activebackground=DTeacherHomeBGColor,
        #                                                       activeforeground=DTeacherHomeBGColor,
        #                                                       image=self.img_DarkThemeimg)
        #     self.Student_home_back_page_img_button.configure(background=DTeacherHomeBGColor,
        #                                                      foreground=DTeacherHomeBGColor,
        #                                                      activebackground=DTeacherHomeBGColor,
        #                                                      activeforeground=DTeacherHomeBGColor, )

    def goHome(self):
        self.master.switch_frame(DarkHome)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

class LightStudentHome(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.bgcolor = "#ffffff"
        self.fgcolor = "#121212"
        self.Student_Element_2_IMG_label = tk.Label(self)

        try:
            self.img_ElementIMG2Label = tk.PhotoImage(file='ElementIMG2Label.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "ElementIMG2Label.png is missing")

        self.Student_Element_2_IMG_label.configure(activebackground=self.bgcolor,
                                                   activeforeground=self.bgcolor,
                                                   background=self.bgcolor,
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
                                               background=self.bgcolor,
                                               activeforeground=self.bgcolor,
                                               activebackground=self.bgcolor,
                                               image=self.img_TeacherHomeAddButton,
                                               command=lambda: master.switch_frame(LightStudentRegistation))
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
                                             background=self.bgcolor,
                                             activeforeground=self.bgcolor,
                                             activebackground=self.bgcolor,
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
                                           activebackground=self.bgcolor,
                                           activeforeground=self.bgcolor,
                                           background=self.bgcolor,
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
                                             activeforeground=self.bgcolor,
                                             activebackground=self.bgcolor,
                                             background=self.bgcolor,
                                             command=lambda: master.switch_frame(StudentDelete))
        self.Student_Delete_button.place(anchor='nw',
                                         x='441',
                                         y='317')

        self.Manege_Student_label = tk.Label(self)
        self.Manege_Student_label.configure(background=self.bgcolor,
                                            borderwidth='0',
                                            font='{Poppins} 28 {bold}',
                                            foreground=self.fgcolor)
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
        self.Student_Manege_close_button.configure(activebackground=self.bgcolor,
                                                   activeforeground=self.bgcolor,
                                                   background=self.bgcolor,
                                                   borderwidth='0')
        self.Student_Manege_close_button.configure(cursor='hand2',
                                                   foreground=self.bgcolor,
                                                   highlightbackground=self.bgcolor,
                                                   highlightcolor=self.bgcolor)
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

        self.Student_Manege_theme_change_button.configure(activebackground=self.bgcolor,
                                                          activeforeground=self.bgcolor,
                                                          background=self.bgcolor,
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

        self.Student_home_back_page_img_button.configure(activebackground=self.bgcolor,
                                                         activeforeground=self.bgcolor,
                                                         background=self.bgcolor,
                                                         borderwidth='0',
                                                         command=self.goHome)
        self.Student_home_back_page_img_button.configure(image=self.img_BackPageIMG)
        self.Student_home_back_page_img_button.place(anchor='nw',
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
        self.master.switch_frame(DarkStudentHome)
        # if self["background"] == "#121212":
        #     TeacherHomeBGColor = "#ffffff"
        #     TeacherHomeFGColor = "#000000"

        #     try:
        #         self.img_DarkThemeimg = tk.PhotoImage(file='DarkThemeimg.png')
        #     except Exception as e:
        #         print(e)
        #         messagebox.showerror("File Missing", "DarkThemeimg.png IS Missing")

        #     try:
        #         self.img_lightThemeimg = tk.PhotoImage(file='LightThemeimg.png')
        #     except Exception as e:
        #         print(e)
        #         messagebox.showerror("File Missing", "LightThemeimg.png IS Missing")

        #     self.configure(background=TeacherHomeBGColor)
        #     self.Student_register_button.configure(background=TeacherHomeBGColor,
        #                                            foreground=TeacherHomeBGColor,
        #                                            activebackground=TeacherHomeBGColor,
        #                                            activeforeground=TeacherHomeBGColor)
        #     self.Student_Element_2_IMG_label.configure(background=TeacherHomeBGColor,
        #                                                foreground=TeacherHomeFGColor)
        #     self.Student_update_button.configure(background=TeacherHomeBGColor,
        #                                          foreground=TeacherHomeBGColor,
        #                                          activebackground=TeacherHomeBGColor,
        #                                          activeforeground=TeacherHomeBGColor)
        #     self.Student_view_button.configure(background=TeacherHomeBGColor,
        #                                        foreground=TeacherHomeBGColor,
        #                                        activebackground=TeacherHomeBGColor,
        #                                        activeforeground=TeacherHomeBGColor)
        #     self.Student_Delete_button.configure(background=TeacherHomeBGColor,
        #                                          foreground=TeacherHomeBGColor,
        #                                          activebackground=TeacherHomeBGColor,
        #                                          activeforeground=TeacherHomeBGColor)
        #     self.Manege_Student_label.configure(background=TeacherHomeBGColor,
        #                                         foreground=TeacherHomeFGColor,
        #                                         activebackground=TeacherHomeBGColor,
        #                                         activeforeground=TeacherHomeBGColor)
        #     self.Student_Manege_close_button.configure(background=TeacherHomeBGColor,
        #                                                foreground=TeacherHomeBGColor,
        #                                                activebackground=TeacherHomeBGColor,
        #                                                activeforeground=TeacherHomeBGColor)
        #     self.Student_Manege_theme_change_button.configure(background=TeacherHomeBGColor,
        #                                                       foreground=TeacherHomeBGColor,
        #                                                       activebackground=TeacherHomeBGColor,
        #                                                       activeforeground=TeacherHomeBGColor,
        #                                                       image=self.img_lightThemeimg)
        #     self.Student_home_back_page_img_button.configure(background=TeacherHomeBGColor,
        #                                                      foreground=TeacherHomeBGColor,
        #                                                      activebackground=TeacherHomeBGColor,
        #                                                      activeforeground=TeacherHomeBGColor, )
        # else:
        #     DTeacherHomeBGColor = "#121212"
        #     DTeacherHomeFGColor = "#ffffff"

        #     self.configure(background=DTeacherHomeBGColor)
        #     self.Student_register_button.configure(background=DTeacherHomeBGColor,
        #                                            foreground=DTeacherHomeBGColor,
        #                                            activebackground=DTeacherHomeBGColor,
        #                                            activeforeground=DTeacherHomeBGColor)
        #     self.Student_Element_2_IMG_label.configure(background=DTeacherHomeBGColor,
        #                                                foreground=DTeacherHomeFGColor)
        #     self.Student_update_button.configure(background=DTeacherHomeBGColor,
        #                                          foreground=DTeacherHomeBGColor,
        #                                          activebackground=DTeacherHomeBGColor,
        #                                          activeforeground=DTeacherHomeBGColor)
        #     self.Student_view_button.configure(background=DTeacherHomeBGColor,
        #                                        foreground=DTeacherHomeBGColor,
        #                                        activebackground=DTeacherHomeBGColor,
        #                                        activeforeground=DTeacherHomeBGColor)
        #     self.Student_Delete_button.configure(background=DTeacherHomeBGColor,
        #                                          foreground=DTeacherHomeBGColor,
        #                                          activebackground=DTeacherHomeBGColor,
        #                                          activeforeground=DTeacherHomeBGColor)
        #     self.Manege_Student_label.configure(background=DTeacherHomeBGColor,
        #                                         foreground=DTeacherHomeFGColor,
        #                                         activebackground=DTeacherHomeBGColor,
        #                                         activeforeground=DTeacherHomeBGColor)
        #     self.Student_Manege_close_button.configure(background=DTeacherHomeBGColor,
        #                                                foreground=DTeacherHomeBGColor,
        #                                                activebackground=DTeacherHomeBGColor,
        #                                                activeforeground=DTeacherHomeBGColor)
        #     self.Student_Manege_theme_change_button.configure(background=DTeacherHomeBGColor,
        #                                                       foreground=DTeacherHomeBGColor,
        #                                                       activebackground=DTeacherHomeBGColor,
        #                                                       activeforeground=DTeacherHomeBGColor,
        #                                                       image=self.img_DarkThemeimg)
        #     self.Student_home_back_page_img_button.configure(background=DTeacherHomeBGColor,
        #                                                      foreground=DTeacherHomeBGColor,
        #                                                      activebackground=DTeacherHomeBGColor,
        #                                                      activeforeground=DTeacherHomeBGColor, )

    def goHome(self):
        self.master.switch_frame(LightHome)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

class DarkStudentRegistation(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.bgcolor = "#121212"
        self.fgcolor = "#ffffff"
        self.Student_element_img_label = tk.Label(self)

        try:
            self.img_Element_1_img_label = tk.PhotoImage(file='Element_1_img_label.png')
        except Exception as e:
            messagebox.showerror("Element_1_img_label.png' Missing")
            print(e)

        self.Student_element_img_label.configure(background=self.bgcolor,
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
        self.Student_Admission_Number_Entry_bg_label.configure(background=self.bgcolor,
                                                               borderwidth='0',
                                                               image=self.img_TeacherRegiusterEntery)
        self.Student_Admission_Number_Entry_bg_label.place(anchor='nw',
                                                           x='386',
                                                           y='340')
        self.Student_First_name_Entry_bg_label = tk.Label(self)
        self.Student_First_name_Entry_bg_label.configure(background=self.bgcolor,
                                                         borderwidth='0',
                                                         image=self.img_TeacherRegiusterEntery)
        self.Student_First_name_Entry_bg_label.place(anchor='nw',
                                                     x='386',
                                                     y='146')

        self.Student_Last_name_Entry_bg_label = tk.Label(self)
        self.Student_Last_name_Entry_bg_label.configure(background=self.bgcolor,
                                                        borderwidth='0',
                                                        image=self.img_TeacherRegiusterEntery)
        self.Student_Last_name_Entry_bg_label.place(anchor='nw',
                                                    x='386',
                                                    y='196')

        self.Student_age_Entry_bg_label = tk.Label(self)
        self.Student_age_Entry_bg_label.configure(background=self.bgcolor,
                                                  borderwidth='0',
                                                  image=self.img_TeacherRegiusterEntery)
        self.Student_age_Entry_bg_label.place(anchor='nw',
                                              x='386',
                                              y='246')

        self.Student_phone_number_Entry_bg_label = tk.Label(self)
        self.Student_phone_number_Entry_bg_label.configure(background=self.bgcolor,
                                                           borderwidth='0',
                                                           image=self.img_TeacherRegiusterEntery)
        self.Student_phone_number_Entry_bg_label.place(anchor='nw',
                                                       x='386',
                                                       y='290')

        self.Student_Subject_Entry_bg_label = tk.Label(self)
        self.Student_Subject_Entry_bg_label.configure(background=self.bgcolor,
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
        self.Student_first_name_label.configure(background=self.bgcolor,
                                                font='{Poppins} 17 {bold}',
                                                foreground=self.fgcolor,
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
        self.Student_last_name_label.configure(background=self.bgcolor,
                                               font='{Poppins} 17 {bold}',
                                               foreground=self.fgcolor,
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
        self.Student_phone_number_label.configure(background=self.bgcolor,
                                                  font='{Poppins} 17 {bold}',
                                                  foreground=self.fgcolor,
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
        self.Student_age_label.configure(background=self.bgcolor,
                                         font='{Poppins} 17 {bold}',
                                         foreground=self.fgcolor,
                                         text='Age')
        self.Student_age_label.place(anchor='nw',
                                     x='166',
                                     y='239')

        self.Student_Admission_Number_label = tk.Label(self)
        self.Student_Admission_Number_label.configure(background=self.bgcolor,
                                                      font='{Poppins} 17 {bold}',
                                                      foreground=self.fgcolor,
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
        self.Student_subects_label.configure(background=self.bgcolor,
                                             font='{Poppins} 17 {bold}',
                                             foreground=self.fgcolor,
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
        self.add_Student_button.configure(background=self.bgcolor,
                                          activebackground=self.bgcolor,
                                          activeforeground=self.bgcolor,
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
        self.Student_registation_close_button.configure(activebackground=self.bgcolor,
                                                        activeforeground=self.bgcolor,
                                                        background=self.bgcolor,
                                                        borderwidth='0')
        self.Student_registation_close_button.configure(cursor='hand2',
                                                        foreground=self.bgcolor,
                                                        highlightbackground=self.bgcolor,
                                                        highlightcolor=self.bgcolor)
        self.Student_registation_close_button.configure(highlightthickness='1',
                                                        image=self.img_img4,
                                                        relief='flat',
                                                        command=self.master.on_close)
        self.Student_registation_close_button.place(anchor='nw',
                                                    x='760',
                                                    y='8')

        self.Register_Student_label = tk.Label(self)
        self.Register_Student_label.configure(background=self.bgcolor,
                                              borderwidth='0',
                                              font='{Poppins} 28 {bold}',
                                              foreground=self.fgcolor)
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

        self.Student_back_page_img_button.configure(activebackground=self.bgcolor,
                                                    activeforeground=self.bgcolor,
                                                    background=self.bgcolor,
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

        self.Student_registation_theme_change_button.configure(activebackground=self.bgcolor,
                                                               activeforeground=self.bgcolor,
                                                               background=self.bgcolor,
                                                               borderwidth='0',
                                                               relief="flat",
                                                               overrelief="flat",
                                                               command=self.changeStudentRegistationTheme)
        self.Student_registation_theme_change_button.configure(image=self.img_DarkThemeimg,
                                                               text='button2')
        self.Student_registation_theme_change_button.place(anchor='nw',
                                                           x='60',
                                                           y='10')
        self.configure(background=self.bgcolor,
                       borderwidth='0',
                       height='515',
                       width='791')
        self.place(x="0", y="0")

    def changeStudentRegistationTheme(self):
        self.master.switch_frame(LightStudentRegistation)
        # try:
        #     self.img_DarkThemeimg = tk.PhotoImage(file='DarkThemeimg.png')
        # except Exception as e:
        #     print(e)
        #     messagebox.showerror("File Missing", "DarkThemeimg.png IS Missing")

        # try:
        #     self.img_lightThemeimg = tk.PhotoImage(file='LightThemeimg.png')
        # except Exception as e:
        #     print(e)
        #     messagebox.showerror("File Missing", "LightThemeimg.png IS Missing")

        # if self.Student_back_page_img_button["background"] == self.fgcolor:
        #     self.StudentRegistationBGColor = self.fgcolor
        #     self.StudentRegistationFGColor = "#000000"
        #     try:
        #         self.configure(background=self.StudentRegistationBGColor)
        #         self.Student_element_img_label.configure(background=self.StudentRegistationBGColor,
        #                                                 foreground=self.StudentRegistationFGColor)
        #         self.Student_First_name_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                         foreground=self.StudentRegistationFGColor)
        #         self.Student_Last_name_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                         foreground=self.StudentRegistationFGColor)
        #         self.Student_age_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                 foreground=self.StudentRegistationFGColor)
        #         self.Student_phone_number_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                         foreground=self.StudentRegistationFGColor)
        #         self.Student_phone_number_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                         foreground=self.StudentRegistationFGColor)
        #         self.Student_Admission_Number_label.configure(background=self.StudentRegistationBGColor,
        #                                                     foreground=self.StudentRegistationFGColor)
        #         self.Student_subects_label.configure(background=self.StudentRegistationBGColor,
        #                                             foreground=self.StudentRegistationFGColor)
        #         self.Student_first_name_entry.configure(background=self.StudentRegistationBGColor,
        #                                                 foreground=self.StudentRegistationFGColor)
        #         self.Student_Admission_Number_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                             foreground=self.StudentRegistationFGColor)
        #         self.Student_First_name_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                         foreground=self.StudentRegistationFGColor)
        #         self.Student_Last_name_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                         foreground=self.StudentRegistationFGColor)
        #         self.Student_age_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                 foreground=self.StudentRegistationFGColor)
        #         self.Student_phone_number_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                         foreground=self.StudentRegistationFGColor)
        #         self.Student_Subject_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                     foreground=self.StudentRegistationFGColor)
        #         self.Student_first_name_label.configure(background=self.StudentRegistationBGColor,
        #                                                 foreground=self.StudentRegistationFGColor)
        #         self.Student_last_name_entry.configure(background=self.StudentRegistationBGColor,
        #                                             foreground=self.StudentRegistationFGColor)
        #         self.Student_last_name_label.configure(background=self.StudentRegistationBGColor,
        #                                             foreground=self.StudentRegistationFGColor)
        #         self.Student_phone_number_entry.configure(background=self.StudentRegistationBGColor,
        #                                                 foreground=self.StudentRegistationFGColor)
        #         self.Student_phone_number_label.configure(background=self.StudentRegistationBGColor,
        #                                                 foreground=self.StudentRegistationFGColor)
        #         self.Student_age_entry.configure(background=self.StudentRegistationBGColor,
        #                                         foreground=self.StudentRegistationFGColor)
        #         self.Student_age_label.configure(background=self.StudentRegistationBGColor,
        #                                         foreground=self.StudentRegistationFGColor)
        #         self.Student_Admission_Number_entry.configure(background=self.StudentRegistationBGColor,
        #                                                     foreground=self.StudentRegistationFGColor)
        #         self.Student_Admission_Number_label.configure(background=self.StudentRegistationBGColor,
        #                                                     foreground=self.StudentRegistationFGColor)
        #         self.Student_subject_entry.configure(background=self.StudentRegistationBGColor,
        #                                             foreground=self.StudentRegistationFGColor)
        #         self.Student_subects_label.configure(background=self.StudentRegistationBGColor,
        #                                             foreground=self.StudentRegistationFGColor)
        #         self.add_Student_button.configure(background=self.StudentRegistationBGColor,
        #                                         foreground=self.StudentRegistationFGColor,
        #                                         activebackground=self.StudentRegistationBGColor,
        #                                         activeforeground=self.StudentRegistationBGColor)
        #         self.Student_Subject_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                     foreground=self.StudentRegistationFGColor)
        #         self.Student_registation_close_button.configure(background=self.StudentRegistationBGColor,
        #                                                         foreground=self.StudentRegistationFGColor)
        #         self.Student_phone_number_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                         foreground=self.StudentRegistationFGColor)
        #         self.Register_Student_label.configure(background=self.StudentRegistationBGColor,
        #                                             foreground=self.StudentRegistationFGColor)
        #         self.Student_back_page_img_button.configure(background=self.StudentRegistationBGColor,
        #                                                     foreground=self.StudentRegistationFGColor,
        #                                                     activebackground=self.StudentRegistationBGColor,
        #                                                     activeforeground=self.StudentRegistationBGColor)
        #         self.Student_registation_theme_change_button.configure(background=self.StudentRegistationBGColor,
        #                                                             foreground=self.StudentRegistationFGColor,
        #                                                             activebackground=self.StudentRegistationBGColor,
        #                                                             activeforeground=self.StudentRegistationBGColor,
        #                                                             image=self.img_lightThemeimg)


        #         ####################################Errors ######################################################
        #         self.Studetn_All_Fields_Required_error_label.configure(background=self.StudentRegistationBGColor)
        #         self.Studetn_First_Name_error_label.configure(background=self.StudentRegistationBGColor)
        #         self.Studetn_Last_Name_error_label.configure(background=self.StudentRegistationBGColor)
        #         self.Studetn_Duplicate_Name_error_label.configure(background=self.StudentRegistationBGColor)
        #         self.Studetn_lenth_Phone_number_error_label.configure(background=self.StudentRegistationBGColor)
        #         self.Studetn_int_Phone_number_error_label.configure(background=self.StudentRegistationBGColor)
        #         self.Studetn_0_Phone_number_error_label.configure(background=self.StudentRegistationBGColor)
        #         Student_age = self.Student_age_entry.get() #This is the Student error

                
        #         self.Studetn_Subject_error_label.configure(background=self.StudentRegistationBGColor)
        #         self.Database_not_Connected_error_label.configure(background=self.StudentRegistationBGColor)
        #         ###################################Commited #################################################
        #         self.Comited_label.configure(background=self.StudentRegistationBGColor)
        #     except:
        #         pass
            #*******************************************************************************************************************
    #########################################Create variabels###########################################################
            #^^^^^^This is All variabels

            # Student_first_name = self.Student_first_name_entry.get() #This Is Student First Name

            # Student_last_name = self.Student_last_name_entry.get() #This is student last name

            # Student_phone_number = self.Student_phone_number_entry.get() #this is student phone number
            
            # Student_age = self.Student_age_entry.get() #This is the Student error

            # Student_Admission_Number = self.Student_Admission_Number_entry.get() #this is the student Admission number

            # Student_subjects = self.Student_subject_entry.get() #this is the student Subjects

    #*******************************************************************************************************************

            #*******************************************************************************************************************
###############################################Check All Fields Are Empty###########################################
    #         if Student_first_name == "" or Student_last_name == "" or Student_phone_number == "" or Student_age == "" or Student_Admission_Number == "" or Student_subjects == "":
                
    #             ##############################Clear All Erorr##################################
    #             try:
    #                 self.Clearerrors()
    #             except:
    #                 pass
    #             try:
    #                 self.AllFildsRequiredErorrDestroy()
    #             except:
    #                 pass
    #             #################################Distroy Student First Name########################
    #             #################################Place The Erorr###################################  
    #             try:          
    #                 self.WAllFildsRequiredErorr()
    #             except:
    #                 pass

    #         else:
    #             ################################Distroy All Fields Erore#####################
    #             try:
    #                 self.AllFildsRequiredErorrDestroy()
    #                 self.WStudetn_First_Name_error_label.destroy()
    #                 self.Studetn_First_Name_error_label.destroy()
    #             except:
    #                 pass 
    #                 ##################################Student First Name Lenth Check#############
    #             if len(Student_first_name) > 50:
    #                 ###################################Distroy Studetn_First_Name_No_error_label#####################
    #                 self.WFirstNameErorr()
    #             else:
    #                 Student_first_name.capitalize()
    #                 # self.FirstNameNoErorr()
                    
    #                 ############################Distroy First name Error##################################
    #                 try:
    #                     self.WStudetn_First_Name_error_label.destroy()
    #                 except:
    #                     pass
    #                 ##########################################Cehck Student Last name Lenth########################
    #                 if len(Student_last_name) > 50:
    #                     #####################################Distroy Studetn_Last_Name_No_error_label###############
    #                     try:
    #                         self.WLastNameError()
    #                     except:
    #                         pass
    #                 else:
    #                     ####################################Distroy Last Name Error#################################
    #                     try:
    #                         self.ClearLastNameError()
    #                     except:
    #                         pass
    #                     # self.NoLastNameError()


    #                     Student_last_name.capitalize()
    #                     if Student_first_name.capitalize() == Student_last_name.capitalize():
    #                         ###############################Clear LAST NAME#######################
    #                         try:
    #                             self.ClearNoLastNameError()
    #                             self.ClearNameDuplicatedErorr
    #                         except:
    #                             pass
    #                         ################################Add Duplicated Error#################
    #                         try:
    #                             self.WNameDuplicatedErorr()
    #                         except:
    #                             pass

    #                     else:
    #                         #############################Clear Duplicate error########################
    #                         try: 
    #                             self.ClearNameDuplicatedErorr()
    #                         except:
    #                             pass
    #                         # self.NoDuplicateNameError()

    #                             ################################Numeber Lenth Check########################################
    #                         if len(Student_phone_number) != 10:

    #                             ##################################Distroy Number No Eror################# 
    #                             try:                         
    #                                 self.clearAllPhoneErors()
    #                             except:
    #                                 pass

    #                             ##################################PHONE NUMBER LENTH ERROR#####################
    #                             try:
    #                                 self.WPhoneNumberLenthErorr()
    #                             except:
    #                                 pass

    # ###################################################Distroy Studetn_lenth_Phone_number_error_label############
    #                         else:
    #                             ###############################Clear phone number lenth erorr####################
    #                             try:
    #                                 self.ClearPhoneNumberLenthErorr()
    #                             except:
    #                                 pass



    # #******************************************************************************************************************#
    # ###################################################### place Studetn_Phone_Number_No_error_label####################
    #                             # self.PhoneNumberLenthNoErorr()

    #                                         ###############This  Place tick############## 
    # ######################################################Check Phone Number Error##########################
    # #******************************************************************************************************#
    #                             try:
    #                                 int(Student_phone_number)
    #                             except:
    #                                 pass
    #                             if type(int(Student_phone_number)) != int:

    # ######################################################Distroy All Error##################################
    #                                 try:
    #                                     self.clearAllPhoneErors()
    #                                 except:
    #                                     pass
    # #####################################################Place Studetn_int_Phone_number_error_label####################
    #                                 try:
    #                                     self.WPhoneNumberTypeErorr()
    #                                 except:
    #                                     pass
    #                             else:
    # ####################################################Distroy Studetn_int_Phone_number_error_label ##################
    #                                 try:
    #                                     self.clearAllPhoneErors()
    #                                 except:
    #                                     pass
    # ##################################################Place  Studetn_int_Phone_Number_No_error_label####################
    #                                 # self.PhoneNumberNoTypeErorr()
    # ################################
    #                                 if int(Student_phone_number[0]) != 0:
    # #*************************************************************************************************************#
    # ###############################################Distroy Phone Nimbers###########################################
    #                                     try:
    #                                         self.clearAllPhoneErors()
    #                                     except:
    #                                         pass
    # ##############################################Place Error##############################################
    #                                     try:                                    
    #                                         self.WPhoneNumberZeroError()
    #                                     except:
    #                                         pass
    # #######################################################################################################                                    
    #                                 else:
    #                                     ##################Clear Zero Errors###############################
    #                                     try:
    #                                         self.ClearPhoneNumberZeroError()
    #                                     except:
    #                                         pass

                                        
    #                                     if len(Student_age) > 2:
    #                                         self.ClearAgeError()
    #                                         self.WAgeError()
    #                                     else:
                                            
    #                                         try:
    #                                             self.ClearAgeError()
    #                                         except:
    #                                             pass
                                            
    #                                         AllSubjects = ['Sinhala','sinhala', 'SINHALA', 'Sin', 'sin',
    #                                                     'Tamil', 'tamil', 'tam', 'Tam',
    #                                                     'English', 'english', "En", 'en',
    #                                                     'Mathematics', 'mathematics', "MATHEMATICS", "math", 'Math',
    #                                                     'MATH',
    #                                                     "Health", 'HEALTH', "HEAL", "health",
    #                                                     "Geography", 'geography', 'GEOGRAPHY', 'geo', "Geo", "GEO",
    #                                                     'French', "french", 'FRENCH',
    #                                                     'Spanish', 'SPANISH', "spanish",
    #                                                     'Computer Science', 'computer science', 'COMPUTER SCIENCE',
    #                                                     'Art', 'ART', 'art',
    #                                                     'Band', 'band', 'BAND',
    #                                                     'Choir', "choir", 'CHOIR',
    #                                                     'Drama', "drama", "DRAMA",
    #                                                     "Sports", "SPORTS", "sports",
    #                                                     'Science', 'science', "SCIENCE",
    #                                                     'History', 'history', 'HISTORY',
    #                                                     'Chess', 'CHESS', 'chess',
    #                                                     "music", 'Music', 'MUSIC',
    #                                                     "ict", 'ICT', "Ict",
    #                                                     'Japan', 'japan', 'JAPAN',
    #                                                     'China', 'china', 'CHINA',
    #                                                     'Accounting', 'accounting', 'ACCOUNTING',
    #                                                     'Latin', 'latin', 'LATIN',
    #                                                     'Greek', 'greek', "GREEK",
    #                                                     'Hebrew', 'HEBREW', "hebrew",
    #                                                     'Zoology', "ZOOLOGY", "zoology",
    #                                                     ]
                                            
    #                                         checkSubject = all(item in AllSubjects for item in Student_subjects.split(","))
    #                                         ##########################Clear Error###############################
    #                                         self.ClearSubjectError()
    #                                         ###################################################################
    #                                         if checkSubject is False:
    #                                             ########################Subject Error############################
    #                                             self.WSubjectError()
    #                                             ################################################################
    #                                         else:
    #                                             self.ClearSubjectError()
    #                                             # try:
    #                                             #     self.AgeNoError()
    #                                             # except:
    #                                             #     pass
    #                                             self.ClearDarabaseNotConnectedError()
    #                                             try: 
    #                                                 ##################Chekc db######################### 
    #                                                 self.connectDB()
    #                                                 ###################################################
    #                                             except:
    #                                                 #AddDB ERROR
    #                                                 self.ClearDarabaseNotConnectedError()
    #                                                 self.DatabaseNotConnectedError()
#         else:
#             self.DStudentRegistationBGColor = self.fgcolor
#             self.DStudentRegistationFGColor = self.fgcolor
#             self.configure(background=self.DStudentRegistationBGColor)
#             self.Student_element_img_label.configure(background=self.DStudentRegistationBGColor,
#                                                      foreground=self.DStudentRegistationFGColor)
#             self.Student_First_name_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
#                                                              foreground=self.DStudentRegistationFGColor)
#             self.Student_Last_name_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
#                                                             foreground=self.DStudentRegistationFGColor)
#             self.Student_age_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
#                                                       foreground=self.DStudentRegistationFGColor)
#             self.Student_phone_number_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
#                                                                foreground=self.DStudentRegistationFGColor)
#             self.Student_Subject_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
#                                                           foreground=self.DStudentRegistationFGColor)
#             self.Student_first_name_label.configure(background=self.DStudentRegistationBGColor,
#                                                     foreground=self.DStudentRegistationFGColor)
#             self.Student_last_name_label.configure(background=self.DStudentRegistationBGColor,
#                                                    foreground=self.DStudentRegistationFGColor)
#             self.Student_phone_number_label.configure(background=self.DStudentRegistationBGColor,
#                                                       foreground=self.DStudentRegistationFGColor)
#             self.Student_age_label.configure(background=self.DStudentRegistationBGColor,
#                                              foreground=self.DStudentRegistationFGColor)
#             self.Student_Admission_Number_label.configure(background=self.DStudentRegistationBGColor,
#                                                           foreground=self.DStudentRegistationFGColor)
#             self.Student_subects_label.configure(background=self.DStudentRegistationBGColor,
#                                                  foreground=self.DStudentRegistationFGColor)
#             self.add_Student_button.configure(background=self.DStudentRegistationBGColor,
#                                               foreground=self.DStudentRegistationFGColor,
#                                               activebackground=self.DStudentRegistationBGColor,
#                                               activeforeground=self.DStudentRegistationBGColor)
#             self.Student_registation_close_button.configure(background=self.DStudentRegistationBGColor,
#                                                             foreground=self.DStudentRegistationFGColor)
#             self.Register_Student_label.configure(background=self.DStudentRegistationBGColor,
#                                                   foreground=self.DStudentRegistationFGColor)
#             self.Student_back_page_img_button.configure(background=self.DStudentRegistationBGColor,
#                                                         foreground=self.DStudentRegistationFGColor)
#             self.Student_Admission_Number_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
#                                                                    foreground=self.DStudentRegistationFGColor)
#             self.Student_First_name_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
#                                                              foreground=self.DStudentRegistationFGColor)
#             self.Student_Last_name_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
#                                                             foreground=self.DStudentRegistationFGColor)
#             self.Student_age_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
#                                                       foreground=self.DStudentRegistationFGColor)
#             self.Student_phone_number_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
#                                                                foreground=self.DStudentRegistationFGColor)
#             self.Student_Subject_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
#                                                           foreground=self.DStudentRegistationFGColor)
#             self.Student_registation_theme_change_button.configure(background=self.DStudentRegistationBGColor,
#                                                                    foreground=self.DStudentRegistationFGColor,
#                                                                    activebackground=self.DStudentRegistationBGColor,
#                                                                    activeforeground=self.DStudentRegistationBGColor,
#                                                                    image=self.img_DarkThemeimg)
# ############################Age Error#################################################
#             Student_age = self.Student_age_entry.get() #This is the Student error

#             Student_first_name = self.Student_first_name_entry.get() #This Is Student First Name

#             Student_last_name = self.Student_last_name_entry.get() #This is student last name

#             Student_phone_number = self.Student_phone_number_entry.get() #this is student phone number
            
#             Student_age = self.Student_age_entry.get() #This is the Student error

#             Student_Admission_Number = self.Student_Admission_Number_entry.get() #this is the student Admission number

#             Student_subjects = self.Student_subject_entry.get() #this is the student Subjects

    #*******************************************************************************************************************

    #*******************************************************************************************************************
    ###############################################Check All Fields Are Empty###########################################
    #         if Student_first_name == "" or Student_last_name == "" or Student_phone_number == "" or Student_age == "" or Student_Admission_Number == "" or Student_subjects == "":
                
    #             ##############################Clear All Erorr##################################
    #             try:
    #                 self.Clearerrors()
    #             except:
    #                 pass
    #             #################################Distroy Student First Name########################
    #             #################################Place The Erorr###################################  
    #             try:          
    #                 self.AllFildsRequiredErorr()
    #             except:
    #                 pass

    #         else:
    #             ################################Distroy All Fields Erore#####################
    #             self.AllFildsRequiredErorrDestroy()
                
    #             ##################################Student First Name Lenth Check#############
    #             if len(Student_first_name) > 50:
    #                 ###################################Distroy Studetn_First_Name_No_error_label#####################
    #                 self.FirstNameErorr()
    #             else:
    #                 Student_first_name.capitalize()
    #                 # self.FirstNameNoErorr()
                    
    #                 ############################Distroy First name Error##################################
    #                 try:
    #                     self.Studetn_First_Name_error_label.destroy()
    #                 except:
    #                     pass
    #                 ##########################################Cehck Student Last name Lenth########################
    #                 if len(Student_last_name) > 50:
    #                     #####################################Distroy Studetn_Last_Name_No_error_label###############
    #                     try:
    #                         self.LastNameError()
    #                     except:
    #                         pass
    #                 else:
    #                     ####################################Distroy Last Name Error#################################
    #                     try:
    #                         self.ClearLastNameError()
    #                     except:
    #                         pass
    #                     # self.NoLastNameError()


    #                     Student_last_name.capitalize()
    #                     if Student_first_name.capitalize() == Student_last_name.capitalize():
    #                         ###############################Clear LAST NAME#######################
    #                         try:
    #                             self.ClearNoLastNameError()
    #                         except:
    #                             pass
    #                         ################################Add Duplicated Error#################
    #                         try:
    #                             self.NameDuplicatedErorr()
    #                         except:
    #                             pass

    #                     else:
    #                         #############################Clear Duplicate error########################
    #                         try: 
    #                             self.ClearNameDuplicatedErorr()
    #                         except:
    #                             pass
    #                         # self.NoDuplicateNameError()

    #                             ################################Numeber Lenth Check########################################
    #                         if len(Student_phone_number) != 10:

    #                             ##################################Distroy Number No Eror################# 
    #                             try:                         
    #                                 self.clearAllPhoneErors()
    #                             except:
    #                                 pass

    #                             ##################################PHONE NUMBER LENTH ERROR#####################
    #                             try:
    #                                 self.PhoneNumberLenthErorr()
    #                             except:
    #                                 pass

    # ###################################################Distroy Studetn_lenth_Phone_number_error_label############
    #                         else:
    #                             ###############################Clear phone number lenth erorr####################
    #                             try:
    #                                 self.ClearPhoneNumberLenthErorr()
    #                             except:
    #                                 pass



    # #******************************************************************************************************************#
    # ###################################################### place Studetn_Phone_Number_No_error_label####################
    #                             # self.PhoneNumberLenthNoErorr()

    #                                         ###############This  Place tick############## 
    # ######################################################Check Phone Number Error##########################
    # #******************************************************************************************************#
    #                             try:
    #                                 int(Student_phone_number)
    #                             except:
    #                                 pass
    #                             if type(int(Student_phone_number)) != int:

    # ######################################################Distroy All Error##################################
    #                                 try:
    #                                     self.clearAllPhoneErors()
    #                                 except:
    #                                     pass
    # #####################################################Place Studetn_int_Phone_number_error_label####################
    #                                 try:
    #                                     self.PhoneNumberTypeErorr()
    #                                 except:
    #                                     pass
    #                             else:
    # ####################################################Distroy Studetn_int_Phone_number_error_label ##################
    #                                 try:
    #                                     self.clearAllPhoneErors()
    #                                 except:
    #                                     pass
    # ##################################################Place  Studetn_int_Phone_Number_No_error_label####################
    #                                 # self.PhoneNumberNoTypeErorr()
    # ################################
    #                                 if int(Student_phone_number[0]) != 0:
    # #*************************************************************************************************************#
    # ###############################################Distroy Phone Nimbers###########################################
    #                                     try:
    #                                         self.clearAllPhoneErors()
    #                                     except:
    #                                         pass
    # ##############################################Place Error##############################################
    #                                     try:                                    
    #                                         self.PhoneNumberZeroError()
    #                                     except:
    #                                         pass
    # #######################################################################################################                                    
    #                                 else:
    #                                     ##################Clear Zero Errors###############################
    #                                     try:
    #                                         self.ClearPhoneNumberZeroError()
    #                                     except:
    #                                         pass

                                        
    #                                     if len(Student_age) > 2:
    #                                         self.ClearAgeError()
    #                                         self.AgeError()
    #                                     else:  
                                            
    #                                         try:
    #                                             self.ClearAgeError()
    #                                         except:
    #                                             pass
                                            
    #                                         AllSubjects = ['Sinhala','sinhala', 'SINHALA', 'Sin', 'sin',
    #                                                     'Tamil', 'tamil', 'tam', 'Tam',
    #                                                     'English', 'english', "En", 'en',
    #                                                     'Mathematics', 'mathematics', "MATHEMATICS", "math", 'Math',
    #                                                     'MATH',
    #                                                     "Health", 'HEALTH', "HEAL", "health",
    #                                                     "Geography", 'geography', 'GEOGRAPHY', 'geo', "Geo", "GEO",
    #                                                     'French', "french", 'FRENCH',
    #                                                     'Spanish', 'SPANISH', "spanish",
    #                                                     'Computer Science', 'computer science', 'COMPUTER SCIENCE',
    #                                                     'Art', 'ART', 'art',
    #                                                     'Band', 'band', 'BAND',
    #                                                     'Choir', "choir", 'CHOIR',
    #                                                     'Drama', "drama", "DRAMA",
    #                                                     "Sports", "SPORTS", "sports",
    #                                                     'Science', 'science', "SCIENCE",
    #                                                     'History', 'history', 'HISTORY',
    #                                                     'Chess', 'CHESS', 'chess',
    #                                                     "music", 'Music', 'MUSIC',
    #                                                     "ict", 'ICT', "Ict",
    #                                                     'Japan', 'japan', 'JAPAN',
    #                                                     'China', 'china', 'CHINA',
    #                                                     'Accounting', 'accounting', 'ACCOUNTING',
    #                                                     'Latin', 'latin', 'LATIN',
    #                                                     'Greek', 'greek', "GREEK",
    #                                                     'Hebrew', 'HEBREW', "hebrew",
    #                                                     'Zoology', "ZOOLOGY", "zoology",
    #                                                     ]
                                            
    #                                         checkSubject = all(item in AllSubjects for item in Student_subjects.split(","))
    #                                         ##########################Clear Error###############################
    #                                         self.ClearSubjectError()
    #                                         ###################################################################
    #                                         if checkSubject is False:
    #                                             ########################Subject Error############################
    #                                             self.SubjectError()
    #                                             ################################################################
    #                                         else:
    #                                             # try:
    #                                             #     self.AgeNoError()
    #                                             # except:
    #                                             #     pass
    #                                             try: 
    #                                                 ##################Chekc db######################### 
    #                                                 self.connectDB()
    #                                                 ###################################################
    #                                             except:
    #                                                 #AddDB ERROR
    #                                                 self.DatabaseNotConnectedError()
                

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
###########################################################Go Back To Student Home#################################
    def goBackToStudentHome(self):
        self.master.switch_frame(DarkStudentHome)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
#########################################On CLick Add Button ######################################################
    def clickAdd(self):

#####################################################Clear#######################################################
        self.Clearerrors()
        self.ClearCommited()
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
            
            ##############################Clear All Erorr##################################
            try:
                self.Clearerrors()
            except:
                pass
            try:
                self.AllFildsRequiredErorrDestroy()
            except:
                pass
            #################################Distroy Student First Name########################
            #################################Place The Erorr###################################  
            try:          
                self.AllFildsRequiredErorr()
            except:
                pass

        else:
            ################################Distroy All Fields Erore#####################
            try:
                self.AllFildsRequiredErorrDestroy()
                self.WStudetn_First_Name_error_label.destroy()
                self.Studetn_First_Name_error_label.destroy()
            except:
                pass 
            ##################################Student First Name Lenth Check#############
            if len(Student_first_name) > 50:
                ###################################Distroy Studetn_First_Name_No_error_label#####################
                self.FirstNameErorr()
            else:
                Student_first_name.capitalize()
                # self.FirstNameNoErorr()
                
                ############################Distroy First name Error##################################
                try:
                    self.Studetn_First_Name_error_label.destroy()
                    self.WStudetn_First_Name_error_label.destroy
                except:
                    pass
                ##########################################Cehck Student Last name Lenth########################
                if len(Student_last_name) > 50:
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


                    Student_last_name.capitalize()
                    if Student_first_name.capitalize() == Student_last_name.capitalize():
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
                        if len(Student_phone_number) != 10:

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
                                int(Student_phone_number)
                            except:
                                pass
                            if type(int(Student_phone_number)) != int:

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
                                if int(Student_phone_number[0]) != 0:
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

                                    
                                    if len(Student_age) > 2:
                                        self.ClearAgeError()
                                        self.AgeError()
                                    else:
                                        
                                        try:
                                            self.ClearAgeError()
                                        except:
                                            pass
                                        
                                        AllSubjects = ['Sinhala','sinhala', 'SINHALA', 'Sin', 'sin',
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
                                        
                                        checkSubject = all(item in AllSubjects for item in Student_subjects.split(","))
                                        ##########################Clear Error###############################
                                        self.ClearSubjectError()
                                        ###################################################################
                                        if checkSubject is False:
                                            ########################Subject Error############################
                                            self.SubjectError()
                                            ################################################################
                                        else:
                                            self.ClearSubjectError()
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

                                            int(Student_phone_number)
                                            int(Student_age)
                                            self.connetc = self.conn.cursor()

                                            self.connetc.execute(
                                                "CREATE TABLE IF NOT EXISTS Student (id INT AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(50), LAstName VARCHAR(50), PhoneNumber INT(50), Age INT(2), Student_Admission_Number VARCHAR(255) ,Subjects VARCHAR(255) )")
                                            self.connetc.execute(
                                                "INSERT INTO  Student (FirstName, LAstName, PhoneNumber, Age, Student_Admission_Number, Subjects) VALUES (%s,%s,%s,%s,%s,%s)",
                                                (str(Student_first_name.capitalize()), str(Student_last_name.capitalize()),
                                                0 + int(Student_phone_number), int(Student_age),
                                                str(Student_Admission_Number),
                                                str(Student_subjects.capitalize())))
                                            self.conn.commit()

                                            self.clearTeacherRegistation()
                                            self.Clearerrors()
                                            self.connetc.close()
                                            self.conn.close()
                                            self.Commited()
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
            self.ClearAgeError()
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
                                                    font='{Poppins} 9 {}',
                                                    foreground='#ff0f15')
        self.Studetn_All_Fields_Required_error_label.configure(text='All Fields Are Required')
        self.Studetn_All_Fields_Required_error_label.place(anchor='nw',
                                                x='500',
                                                y='121')
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
                                                    font='{Poppins} 9 {}',
                                                    foreground='#ff0f15')
        self.WStudetn_All_Fields_Required_error_label.configure(text='All Fields Are Required')
        self.WStudetn_All_Fields_Required_error_label.place(anchor='nw',
                                                x='500',
                                                y='121')

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
            self.WStudetn_First_Name_error_label.destroy()
            self.WStudetn_First_Name_No_error_label.destroy()
        except:
            pass
                
###################################################place Studetn_First_Name_error_label############################
        self.Studetn_First_Name_error_label = tk.Label(self)
        self.Studetn_First_Name_error_label.configure(background=self.bgcolor,
                                                    borderwidth='0',
                                                    font='{Poppins} 9 {}',
                                                    foreground='#ff0f15')
        self.Studetn_First_Name_error_label.configure(text='First Name Is Too Long')
        self.Studetn_First_Name_error_label.place(anchor='nw',
                                                x='500',
                                                y='123')
    def WFirstNameErorr(self):
        try:
            self.Studetn_First_Name_error_label.destroy()
            self.WStudetn_First_Name_error_label.destroy()
        except:
            pass
                
###################################################place Studetn_First_Name_error_label############################
        self.WStudetn_First_Name_error_label = tk.Label(self)
        self.WStudetn_First_Name_error_label.configure(background=self.fgcolor,
                                                    borderwidth='0',
                                                    font='{Poppins} 9 {}',
                                                    foreground='#ff0f15')
        self.WStudetn_First_Name_error_label.configure(text='First Name Is Too Long')
        self.WStudetn_First_Name_error_label.place(anchor='nw',
                                                x='500',
                                                y='123')


############################################################Last Name################################################
    def LastNameError(self):
        try:
            self.Studetn_First_Name_error_label.destroy()
            self.WStudetn_First_Name_error_label.destroy()
            self.WStudetn_Last_Name_error_label.destroy()
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

    def ClearPhoneNumberZeroError(self):
        ##########CLEAR PHONE NUMBER###############################
        try:
            self.WStudetn_0_Phone_number_error_label.destroy()
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
                                                                        y='227')
        except:
            pass
        ####################################################################

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
    def ClearAgeError(self):

        ################CLEAR AGE ERROR#############
        try:
            self.Studetn_Age_error_label.destroy()
            self.WStudetn_Age_error_label.destroy()
        except:
            pass
        ###############################################################

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

    def ClearDarabaseNotConnectedError(self):
        try:
            self.Database_not_Connected_error_label.destroy()
            self.WDatabase_not_Connected_error_label.destroy()
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

    def ClearCommited(self):
        try:
            self.Comited_label.destroy()
        except:
            pass
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

class LightStudentRegistation(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.bgcolor = "#ffffff"
        self.fgcolor = "#121212"
        self.Student_element_img_label = tk.Label(self)

        try:
            self.img_Element_1_img_label = tk.PhotoImage(file='Element_1_img_label.png')
        except Exception as e:
            messagebox.showerror("Element_1_img_label.png' Missing")
            print(e)

        self.Student_element_img_label.configure(background=self.bgcolor,
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
        self.Student_Admission_Number_Entry_bg_label.configure(background=self.bgcolor,
                                                               borderwidth='0',
                                                               image=self.img_TeacherRegiusterEntery)
        self.Student_Admission_Number_Entry_bg_label.place(anchor='nw',
                                                           x='386',
                                                           y='340')
        self.Student_First_name_Entry_bg_label = tk.Label(self)
        self.Student_First_name_Entry_bg_label.configure(background=self.bgcolor,
                                                         borderwidth='0',
                                                         image=self.img_TeacherRegiusterEntery)
        self.Student_First_name_Entry_bg_label.place(anchor='nw',
                                                     x='386',
                                                     y='146')

        self.Student_Last_name_Entry_bg_label = tk.Label(self)
        self.Student_Last_name_Entry_bg_label.configure(background=self.bgcolor,
                                                        borderwidth='0',
                                                        image=self.img_TeacherRegiusterEntery)
        self.Student_Last_name_Entry_bg_label.place(anchor='nw',
                                                    x='386',
                                                    y='196')

        self.Student_age_Entry_bg_label = tk.Label(self)
        self.Student_age_Entry_bg_label.configure(background=self.bgcolor,
                                                  borderwidth='0',
                                                  image=self.img_TeacherRegiusterEntery)
        self.Student_age_Entry_bg_label.place(anchor='nw',
                                              x='386',
                                              y='246')

        self.Student_phone_number_Entry_bg_label = tk.Label(self)
        self.Student_phone_number_Entry_bg_label.configure(background=self.bgcolor,
                                                           borderwidth='0',
                                                           image=self.img_TeacherRegiusterEntery)
        self.Student_phone_number_Entry_bg_label.place(anchor='nw',
                                                       x='386',
                                                       y='290')

        self.Student_Subject_Entry_bg_label = tk.Label(self)
        self.Student_Subject_Entry_bg_label.configure(background=self.bgcolor,
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
        self.Student_first_name_label.configure(background=self.bgcolor,
                                                font='{Poppins} 17 {bold}',
                                                foreground=self.fgcolor,
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
        self.Student_last_name_label.configure(background=self.bgcolor,
                                               font='{Poppins} 17 {bold}',
                                               foreground=self.fgcolor,
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
        self.Student_phone_number_label.configure(background=self.bgcolor,
                                                  font='{Poppins} 17 {bold}',
                                                  foreground=self.fgcolor,
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
        self.Student_age_label.configure(background=self.bgcolor,
                                         font='{Poppins} 17 {bold}',
                                         foreground=self.fgcolor,
                                         text='Age')
        self.Student_age_label.place(anchor='nw',
                                     x='166',
                                     y='239')

        self.Student_Admission_Number_label = tk.Label(self)
        self.Student_Admission_Number_label.configure(background=self.bgcolor,
                                                      font='{Poppins} 17 {bold}',
                                                      foreground=self.fgcolor,
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
        self.Student_subects_label.configure(background=self.bgcolor,
                                             font='{Poppins} 17 {bold}',
                                             foreground=self.fgcolor,
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
        self.add_Student_button.configure(background=self.bgcolor,
                                          activebackground=self.bgcolor,
                                          activeforeground=self.bgcolor,
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
        self.Student_registation_close_button.configure(activebackground=self.bgcolor,
                                                        activeforeground=self.bgcolor,
                                                        background=self.bgcolor,
                                                        borderwidth='0')
        self.Student_registation_close_button.configure(cursor='hand2',
                                                        foreground=self.bgcolor,
                                                        highlightbackground=self.bgcolor,
                                                        highlightcolor=self.bgcolor)
        self.Student_registation_close_button.configure(highlightthickness='1',
                                                        image=self.img_img4,
                                                        relief='flat',
                                                        command=self.master.on_close)
        self.Student_registation_close_button.place(anchor='nw',
                                                    x='760',
                                                    y='8')

        self.Register_Student_label = tk.Label(self)
        self.Register_Student_label.configure(background=self.bgcolor,
                                              borderwidth='0',
                                              font='{Poppins} 28 {bold}',
                                              foreground=self.fgcolor)
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

        self.Student_back_page_img_button.configure(activebackground=self.bgcolor,
                                                    activeforeground=self.bgcolor,
                                                    background=self.bgcolor,
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

        self.Student_registation_theme_change_button.configure(activebackground=self.bgcolor,
                                                               activeforeground=self.bgcolor,
                                                               background=self.bgcolor,
                                                               borderwidth='0',
                                                               relief="flat",
                                                               overrelief="flat",
                                                               command=self.changeStudentRegistationTheme)
        self.Student_registation_theme_change_button.configure(image=self.img_DarkThemeimg,
                                                               text='button2')
        self.Student_registation_theme_change_button.place(anchor='nw',
                                                           x='60',
                                                           y='10')
        self.configure(background=self.bgcolor,
                       borderwidth='0',
                       height='515',
                       width='791')
        self.place(x="0", y="0")

    def changeStudentRegistationTheme(self):
        self.master.switch_frame(DarkStudentRegistation)
        # try:
        #     self.img_DarkThemeimg = tk.PhotoImage(file='DarkThemeimg.png')
        # except Exception as e:
        #     print(e)
        #     messagebox.showerror("File Missing", "DarkThemeimg.png IS Missing")

        # try:
        #     self.img_lightThemeimg = tk.PhotoImage(file='LightThemeimg.png')
        # except Exception as e:
        #     print(e)
        #     messagebox.showerror("File Missing", "LightThemeimg.png IS Missing")

        # if self.Student_back_page_img_button["background"] == self.fgcolor:
        #     self.StudentRegistationBGColor = self.fgcolor
        #     self.StudentRegistationFGColor = "#000000"
        #     try:
        #         self.configure(background=self.StudentRegistationBGColor)
        #         self.Student_element_img_label.configure(background=self.StudentRegistationBGColor,
        #                                                 foreground=self.StudentRegistationFGColor)
        #         self.Student_First_name_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                         foreground=self.StudentRegistationFGColor)
        #         self.Student_Last_name_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                         foreground=self.StudentRegistationFGColor)
        #         self.Student_age_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                 foreground=self.StudentRegistationFGColor)
        #         self.Student_phone_number_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                         foreground=self.StudentRegistationFGColor)
        #         self.Student_phone_number_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                         foreground=self.StudentRegistationFGColor)
        #         self.Student_Admission_Number_label.configure(background=self.StudentRegistationBGColor,
        #                                                     foreground=self.StudentRegistationFGColor)
        #         self.Student_subects_label.configure(background=self.StudentRegistationBGColor,
        #                                             foreground=self.StudentRegistationFGColor)
        #         self.Student_first_name_entry.configure(background=self.StudentRegistationBGColor,
        #                                                 foreground=self.StudentRegistationFGColor)
        #         self.Student_Admission_Number_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                             foreground=self.StudentRegistationFGColor)
        #         self.Student_First_name_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                         foreground=self.StudentRegistationFGColor)
        #         self.Student_Last_name_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                         foreground=self.StudentRegistationFGColor)
        #         self.Student_age_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                 foreground=self.StudentRegistationFGColor)
        #         self.Student_phone_number_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                         foreground=self.StudentRegistationFGColor)
        #         self.Student_Subject_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                     foreground=self.StudentRegistationFGColor)
        #         self.Student_first_name_label.configure(background=self.StudentRegistationBGColor,
        #                                                 foreground=self.StudentRegistationFGColor)
        #         self.Student_last_name_entry.configure(background=self.StudentRegistationBGColor,
        #                                             foreground=self.StudentRegistationFGColor)
        #         self.Student_last_name_label.configure(background=self.StudentRegistationBGColor,
        #                                             foreground=self.StudentRegistationFGColor)
        #         self.Student_phone_number_entry.configure(background=self.StudentRegistationBGColor,
        #                                                 foreground=self.StudentRegistationFGColor)
        #         self.Student_phone_number_label.configure(background=self.StudentRegistationBGColor,
        #                                                 foreground=self.StudentRegistationFGColor)
        #         self.Student_age_entry.configure(background=self.StudentRegistationBGColor,
        #                                         foreground=self.StudentRegistationFGColor)
        #         self.Student_age_label.configure(background=self.StudentRegistationBGColor,
        #                                         foreground=self.StudentRegistationFGColor)
        #         self.Student_Admission_Number_entry.configure(background=self.StudentRegistationBGColor,
        #                                                     foreground=self.StudentRegistationFGColor)
        #         self.Student_Admission_Number_label.configure(background=self.StudentRegistationBGColor,
        #                                                     foreground=self.StudentRegistationFGColor)
        #         self.Student_subject_entry.configure(background=self.StudentRegistationBGColor,
        #                                             foreground=self.StudentRegistationFGColor)
        #         self.Student_subects_label.configure(background=self.StudentRegistationBGColor,
        #                                             foreground=self.StudentRegistationFGColor)
        #         self.add_Student_button.configure(background=self.StudentRegistationBGColor,
        #                                         foreground=self.StudentRegistationFGColor,
        #                                         activebackground=self.StudentRegistationBGColor,
        #                                         activeforeground=self.StudentRegistationBGColor)
        #         self.Student_Subject_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                     foreground=self.StudentRegistationFGColor)
        #         self.Student_registation_close_button.configure(background=self.StudentRegistationBGColor,
        #                                                         foreground=self.StudentRegistationFGColor)
        #         self.Student_phone_number_Entry_bg_label.configure(background=self.StudentRegistationBGColor,
        #                                                         foreground=self.StudentRegistationFGColor)
        #         self.Register_Student_label.configure(background=self.StudentRegistationBGColor,
        #                                             foreground=self.StudentRegistationFGColor)
        #         self.Student_back_page_img_button.configure(background=self.StudentRegistationBGColor,
        #                                                     foreground=self.StudentRegistationFGColor,
        #                                                     activebackground=self.StudentRegistationBGColor,
        #                                                     activeforeground=self.StudentRegistationBGColor)
        #         self.Student_registation_theme_change_button.configure(background=self.StudentRegistationBGColor,
        #                                                             foreground=self.StudentRegistationFGColor,
        #                                                             activebackground=self.StudentRegistationBGColor,
        #                                                             activeforeground=self.StudentRegistationBGColor,
        #                                                             image=self.img_lightThemeimg)


        #         ####################################Errors ######################################################
        #         self.Studetn_All_Fields_Required_error_label.configure(background=self.StudentRegistationBGColor)
        #         self.Studetn_First_Name_error_label.configure(background=self.StudentRegistationBGColor)
        #         self.Studetn_Last_Name_error_label.configure(background=self.StudentRegistationBGColor)
        #         self.Studetn_Duplicate_Name_error_label.configure(background=self.StudentRegistationBGColor)
        #         self.Studetn_lenth_Phone_number_error_label.configure(background=self.StudentRegistationBGColor)
        #         self.Studetn_int_Phone_number_error_label.configure(background=self.StudentRegistationBGColor)
        #         self.Studetn_0_Phone_number_error_label.configure(background=self.StudentRegistationBGColor)
        #         Student_age = self.Student_age_entry.get() #This is the Student error

                
        #         self.Studetn_Subject_error_label.configure(background=self.StudentRegistationBGColor)
        #         self.Database_not_Connected_error_label.configure(background=self.StudentRegistationBGColor)
        #         ###################################Commited #################################################
        #         self.Comited_label.configure(background=self.StudentRegistationBGColor)
        #     except:
        #         pass
            #*******************************************************************************************************************
    #########################################Create variabels###########################################################
            #^^^^^^This is All variabels

            # Student_first_name = self.Student_first_name_entry.get() #This Is Student First Name

            # Student_last_name = self.Student_last_name_entry.get() #This is student last name

            # Student_phone_number = self.Student_phone_number_entry.get() #this is student phone number
            
            # Student_age = self.Student_age_entry.get() #This is the Student error

            # Student_Admission_Number = self.Student_Admission_Number_entry.get() #this is the student Admission number

            # Student_subjects = self.Student_subject_entry.get() #this is the student Subjects

    #*******************************************************************************************************************

            #*******************************************************************************************************************
###############################################Check All Fields Are Empty###########################################
    #         if Student_first_name == "" or Student_last_name == "" or Student_phone_number == "" or Student_age == "" or Student_Admission_Number == "" or Student_subjects == "":
                
    #             ##############################Clear All Erorr##################################
    #             try:
    #                 self.Clearerrors()
    #             except:
    #                 pass
    #             try:
    #                 self.AllFildsRequiredErorrDestroy()
    #             except:
    #                 pass
    #             #################################Distroy Student First Name########################
    #             #################################Place The Erorr###################################  
    #             try:          
    #                 self.WAllFildsRequiredErorr()
    #             except:
    #                 pass

    #         else:
    #             ################################Distroy All Fields Erore#####################
    #             try:
    #                 self.AllFildsRequiredErorrDestroy()
    #                 self.WStudetn_First_Name_error_label.destroy()
    #                 self.Studetn_First_Name_error_label.destroy()
    #             except:
    #                 pass 
    #                 ##################################Student First Name Lenth Check#############
    #             if len(Student_first_name) > 50:
    #                 ###################################Distroy Studetn_First_Name_No_error_label#####################
    #                 self.WFirstNameErorr()
    #             else:
    #                 Student_first_name.capitalize()
    #                 # self.FirstNameNoErorr()
                    
    #                 ############################Distroy First name Error##################################
    #                 try:
    #                     self.WStudetn_First_Name_error_label.destroy()
    #                 except:
    #                     pass
    #                 ##########################################Cehck Student Last name Lenth########################
    #                 if len(Student_last_name) > 50:
    #                     #####################################Distroy Studetn_Last_Name_No_error_label###############
    #                     try:
    #                         self.WLastNameError()
    #                     except:
    #                         pass
    #                 else:
    #                     ####################################Distroy Last Name Error#################################
    #                     try:
    #                         self.ClearLastNameError()
    #                     except:
    #                         pass
    #                     # self.NoLastNameError()


    #                     Student_last_name.capitalize()
    #                     if Student_first_name.capitalize() == Student_last_name.capitalize():
    #                         ###############################Clear LAST NAME#######################
    #                         try:
    #                             self.ClearNoLastNameError()
    #                             self.ClearNameDuplicatedErorr
    #                         except:
    #                             pass
    #                         ################################Add Duplicated Error#################
    #                         try:
    #                             self.WNameDuplicatedErorr()
    #                         except:
    #                             pass

    #                     else:
    #                         #############################Clear Duplicate error########################
    #                         try: 
    #                             self.ClearNameDuplicatedErorr()
    #                         except:
    #                             pass
    #                         # self.NoDuplicateNameError()

    #                             ################################Numeber Lenth Check########################################
    #                         if len(Student_phone_number) != 10:

    #                             ##################################Distroy Number No Eror################# 
    #                             try:                         
    #                                 self.clearAllPhoneErors()
    #                             except:
    #                                 pass

    #                             ##################################PHONE NUMBER LENTH ERROR#####################
    #                             try:
    #                                 self.WPhoneNumberLenthErorr()
    #                             except:
    #                                 pass

    # ###################################################Distroy Studetn_lenth_Phone_number_error_label############
    #                         else:
    #                             ###############################Clear phone number lenth erorr####################
    #                             try:
    #                                 self.ClearPhoneNumberLenthErorr()
    #                             except:
    #                                 pass



    # #******************************************************************************************************************#
    # ###################################################### place Studetn_Phone_Number_No_error_label####################
    #                             # self.PhoneNumberLenthNoErorr()

    #                                         ###############This  Place tick############## 
    # ######################################################Check Phone Number Error##########################
    # #******************************************************************************************************#
    #                             try:
    #                                 int(Student_phone_number)
    #                             except:
    #                                 pass
    #                             if type(int(Student_phone_number)) != int:

    # ######################################################Distroy All Error##################################
    #                                 try:
    #                                     self.clearAllPhoneErors()
    #                                 except:
    #                                     pass
    # #####################################################Place Studetn_int_Phone_number_error_label####################
    #                                 try:
    #                                     self.WPhoneNumberTypeErorr()
    #                                 except:
    #                                     pass
    #                             else:
    # ####################################################Distroy Studetn_int_Phone_number_error_label ##################
    #                                 try:
    #                                     self.clearAllPhoneErors()
    #                                 except:
    #                                     pass
    # ##################################################Place  Studetn_int_Phone_Number_No_error_label####################
    #                                 # self.PhoneNumberNoTypeErorr()
    # ################################
    #                                 if int(Student_phone_number[0]) != 0:
    # #*************************************************************************************************************#
    # ###############################################Distroy Phone Nimbers###########################################
    #                                     try:
    #                                         self.clearAllPhoneErors()
    #                                     except:
    #                                         pass
    # ##############################################Place Error##############################################
    #                                     try:                                    
    #                                         self.WPhoneNumberZeroError()
    #                                     except:
    #                                         pass
    # #######################################################################################################                                    
    #                                 else:
    #                                     ##################Clear Zero Errors###############################
    #                                     try:
    #                                         self.ClearPhoneNumberZeroError()
    #                                     except:
    #                                         pass

                                        
    #                                     if len(Student_age) > 2:
    #                                         self.ClearAgeError()
    #                                         self.WAgeError()
    #                                     else:
                                            
    #                                         try:
    #                                             self.ClearAgeError()
    #                                         except:
    #                                             pass
                                            
    #                                         AllSubjects = ['Sinhala','sinhala', 'SINHALA', 'Sin', 'sin',
    #                                                     'Tamil', 'tamil', 'tam', 'Tam',
    #                                                     'English', 'english', "En", 'en',
    #                                                     'Mathematics', 'mathematics', "MATHEMATICS", "math", 'Math',
    #                                                     'MATH',
    #                                                     "Health", 'HEALTH', "HEAL", "health",
    #                                                     "Geography", 'geography', 'GEOGRAPHY', 'geo', "Geo", "GEO",
    #                                                     'French', "french", 'FRENCH',
    #                                                     'Spanish', 'SPANISH', "spanish",
    #                                                     'Computer Science', 'computer science', 'COMPUTER SCIENCE',
    #                                                     'Art', 'ART', 'art',
    #                                                     'Band', 'band', 'BAND',
    #                                                     'Choir', "choir", 'CHOIR',
    #                                                     'Drama', "drama", "DRAMA",
    #                                                     "Sports", "SPORTS", "sports",
    #                                                     'Science', 'science', "SCIENCE",
    #                                                     'History', 'history', 'HISTORY',
    #                                                     'Chess', 'CHESS', 'chess',
    #                                                     "music", 'Music', 'MUSIC',
    #                                                     "ict", 'ICT', "Ict",
    #                                                     'Japan', 'japan', 'JAPAN',
    #                                                     'China', 'china', 'CHINA',
    #                                                     'Accounting', 'accounting', 'ACCOUNTING',
    #                                                     'Latin', 'latin', 'LATIN',
    #                                                     'Greek', 'greek', "GREEK",
    #                                                     'Hebrew', 'HEBREW', "hebrew",
    #                                                     'Zoology', "ZOOLOGY", "zoology",
    #                                                     ]
                                            
    #                                         checkSubject = all(item in AllSubjects for item in Student_subjects.split(","))
    #                                         ##########################Clear Error###############################
    #                                         self.ClearSubjectError()
    #                                         ###################################################################
    #                                         if checkSubject is False:
    #                                             ########################Subject Error############################
    #                                             self.WSubjectError()
    #                                             ################################################################
    #                                         else:
    #                                             self.ClearSubjectError()
    #                                             # try:
    #                                             #     self.AgeNoError()
    #                                             # except:
    #                                             #     pass
    #                                             self.ClearDarabaseNotConnectedError()
    #                                             try: 
    #                                                 ##################Chekc db######################### 
    #                                                 self.connectDB()
    #                                                 ###################################################
    #                                             except:
    #                                                 #AddDB ERROR
    #                                                 self.ClearDarabaseNotConnectedError()
    #                                                 self.DatabaseNotConnectedError()
#         else:
#             self.DStudentRegistationBGColor = self.fgcolor
#             self.DStudentRegistationFGColor = self.fgcolor
#             self.configure(background=self.DStudentRegistationBGColor)
#             self.Student_element_img_label.configure(background=self.DStudentRegistationBGColor,
#                                                      foreground=self.DStudentRegistationFGColor)
#             self.Student_First_name_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
#                                                              foreground=self.DStudentRegistationFGColor)
#             self.Student_Last_name_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
#                                                             foreground=self.DStudentRegistationFGColor)
#             self.Student_age_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
#                                                       foreground=self.DStudentRegistationFGColor)
#             self.Student_phone_number_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
#                                                                foreground=self.DStudentRegistationFGColor)
#             self.Student_Subject_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
#                                                           foreground=self.DStudentRegistationFGColor)
#             self.Student_first_name_label.configure(background=self.DStudentRegistationBGColor,
#                                                     foreground=self.DStudentRegistationFGColor)
#             self.Student_last_name_label.configure(background=self.DStudentRegistationBGColor,
#                                                    foreground=self.DStudentRegistationFGColor)
#             self.Student_phone_number_label.configure(background=self.DStudentRegistationBGColor,
#                                                       foreground=self.DStudentRegistationFGColor)
#             self.Student_age_label.configure(background=self.DStudentRegistationBGColor,
#                                              foreground=self.DStudentRegistationFGColor)
#             self.Student_Admission_Number_label.configure(background=self.DStudentRegistationBGColor,
#                                                           foreground=self.DStudentRegistationFGColor)
#             self.Student_subects_label.configure(background=self.DStudentRegistationBGColor,
#                                                  foreground=self.DStudentRegistationFGColor)
#             self.add_Student_button.configure(background=self.DStudentRegistationBGColor,
#                                               foreground=self.DStudentRegistationFGColor,
#                                               activebackground=self.DStudentRegistationBGColor,
#                                               activeforeground=self.DStudentRegistationBGColor)
#             self.Student_registation_close_button.configure(background=self.DStudentRegistationBGColor,
#                                                             foreground=self.DStudentRegistationFGColor)
#             self.Register_Student_label.configure(background=self.DStudentRegistationBGColor,
#                                                   foreground=self.DStudentRegistationFGColor)
#             self.Student_back_page_img_button.configure(background=self.DStudentRegistationBGColor,
#                                                         foreground=self.DStudentRegistationFGColor)
#             self.Student_Admission_Number_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
#                                                                    foreground=self.DStudentRegistationFGColor)
#             self.Student_First_name_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
#                                                              foreground=self.DStudentRegistationFGColor)
#             self.Student_Last_name_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
#                                                             foreground=self.DStudentRegistationFGColor)
#             self.Student_age_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
#                                                       foreground=self.DStudentRegistationFGColor)
#             self.Student_phone_number_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
#                                                                foreground=self.DStudentRegistationFGColor)
#             self.Student_Subject_Entry_bg_label.configure(background=self.DStudentRegistationBGColor,
#                                                           foreground=self.DStudentRegistationFGColor)
#             self.Student_registation_theme_change_button.configure(background=self.DStudentRegistationBGColor,
#                                                                    foreground=self.DStudentRegistationFGColor,
#                                                                    activebackground=self.DStudentRegistationBGColor,
#                                                                    activeforeground=self.DStudentRegistationBGColor,
#                                                                    image=self.img_DarkThemeimg)
# ############################Age Error#################################################
#             Student_age = self.Student_age_entry.get() #This is the Student error

#             Student_first_name = self.Student_first_name_entry.get() #This Is Student First Name

#             Student_last_name = self.Student_last_name_entry.get() #This is student last name

#             Student_phone_number = self.Student_phone_number_entry.get() #this is student phone number
            
#             Student_age = self.Student_age_entry.get() #This is the Student error

#             Student_Admission_Number = self.Student_Admission_Number_entry.get() #this is the student Admission number

#             Student_subjects = self.Student_subject_entry.get() #this is the student Subjects

    #*******************************************************************************************************************

    #*******************************************************************************************************************
    ###############################################Check All Fields Are Empty###########################################
    #         if Student_first_name == "" or Student_last_name == "" or Student_phone_number == "" or Student_age == "" or Student_Admission_Number == "" or Student_subjects == "":
                
    #             ##############################Clear All Erorr##################################
    #             try:
    #                 self.Clearerrors()
    #             except:
    #                 pass
    #             #################################Distroy Student First Name########################
    #             #################################Place The Erorr###################################  
    #             try:          
    #                 self.AllFildsRequiredErorr()
    #             except:
    #                 pass

    #         else:
    #             ################################Distroy All Fields Erore#####################
    #             self.AllFildsRequiredErorrDestroy()
                
    #             ##################################Student First Name Lenth Check#############
    #             if len(Student_first_name) > 50:
    #                 ###################################Distroy Studetn_First_Name_No_error_label#####################
    #                 self.FirstNameErorr()
    #             else:
    #                 Student_first_name.capitalize()
    #                 # self.FirstNameNoErorr()
                    
    #                 ############################Distroy First name Error##################################
    #                 try:
    #                     self.Studetn_First_Name_error_label.destroy()
    #                 except:
    #                     pass
    #                 ##########################################Cehck Student Last name Lenth########################
    #                 if len(Student_last_name) > 50:
    #                     #####################################Distroy Studetn_Last_Name_No_error_label###############
    #                     try:
    #                         self.LastNameError()
    #                     except:
    #                         pass
    #                 else:
    #                     ####################################Distroy Last Name Error#################################
    #                     try:
    #                         self.ClearLastNameError()
    #                     except:
    #                         pass
    #                     # self.NoLastNameError()


    #                     Student_last_name.capitalize()
    #                     if Student_first_name.capitalize() == Student_last_name.capitalize():
    #                         ###############################Clear LAST NAME#######################
    #                         try:
    #                             self.ClearNoLastNameError()
    #                         except:
    #                             pass
    #                         ################################Add Duplicated Error#################
    #                         try:
    #                             self.NameDuplicatedErorr()
    #                         except:
    #                             pass

    #                     else:
    #                         #############################Clear Duplicate error########################
    #                         try: 
    #                             self.ClearNameDuplicatedErorr()
    #                         except:
    #                             pass
    #                         # self.NoDuplicateNameError()

    #                             ################################Numeber Lenth Check########################################
    #                         if len(Student_phone_number) != 10:

    #                             ##################################Distroy Number No Eror################# 
    #                             try:                         
    #                                 self.clearAllPhoneErors()
    #                             except:
    #                                 pass

    #                             ##################################PHONE NUMBER LENTH ERROR#####################
    #                             try:
    #                                 self.PhoneNumberLenthErorr()
    #                             except:
    #                                 pass

    # ###################################################Distroy Studetn_lenth_Phone_number_error_label############
    #                         else:
    #                             ###############################Clear phone number lenth erorr####################
    #                             try:
    #                                 self.ClearPhoneNumberLenthErorr()
    #                             except:
    #                                 pass



    # #******************************************************************************************************************#
    # ###################################################### place Studetn_Phone_Number_No_error_label####################
    #                             # self.PhoneNumberLenthNoErorr()

    #                                         ###############This  Place tick############## 
    # ######################################################Check Phone Number Error##########################
    # #******************************************************************************************************#
    #                             try:
    #                                 int(Student_phone_number)
    #                             except:
    #                                 pass
    #                             if type(int(Student_phone_number)) != int:

    # ######################################################Distroy All Error##################################
    #                                 try:
    #                                     self.clearAllPhoneErors()
    #                                 except:
    #                                     pass
    # #####################################################Place Studetn_int_Phone_number_error_label####################
    #                                 try:
    #                                     self.PhoneNumberTypeErorr()
    #                                 except:
    #                                     pass
    #                             else:
    # ####################################################Distroy Studetn_int_Phone_number_error_label ##################
    #                                 try:
    #                                     self.clearAllPhoneErors()
    #                                 except:
    #                                     pass
    # ##################################################Place  Studetn_int_Phone_Number_No_error_label####################
    #                                 # self.PhoneNumberNoTypeErorr()
    # ################################
    #                                 if int(Student_phone_number[0]) != 0:
    # #*************************************************************************************************************#
    # ###############################################Distroy Phone Nimbers###########################################
    #                                     try:
    #                                         self.clearAllPhoneErors()
    #                                     except:
    #                                         pass
    # ##############################################Place Error##############################################
    #                                     try:                                    
    #                                         self.PhoneNumberZeroError()
    #                                     except:
    #                                         pass
    # #######################################################################################################                                    
    #                                 else:
    #                                     ##################Clear Zero Errors###############################
    #                                     try:
    #                                         self.ClearPhoneNumberZeroError()
    #                                     except:
    #                                         pass

                                        
    #                                     if len(Student_age) > 2:
    #                                         self.ClearAgeError()
    #                                         self.AgeError()
    #                                     else:  
                                            
    #                                         try:
    #                                             self.ClearAgeError()
    #                                         except:
    #                                             pass
                                            
    #                                         AllSubjects = ['Sinhala','sinhala', 'SINHALA', 'Sin', 'sin',
    #                                                     'Tamil', 'tamil', 'tam', 'Tam',
    #                                                     'English', 'english', "En", 'en',
    #                                                     'Mathematics', 'mathematics', "MATHEMATICS", "math", 'Math',
    #                                                     'MATH',
    #                                                     "Health", 'HEALTH', "HEAL", "health",
    #                                                     "Geography", 'geography', 'GEOGRAPHY', 'geo', "Geo", "GEO",
    #                                                     'French', "french", 'FRENCH',
    #                                                     'Spanish', 'SPANISH', "spanish",
    #                                                     'Computer Science', 'computer science', 'COMPUTER SCIENCE',
    #                                                     'Art', 'ART', 'art',
    #                                                     'Band', 'band', 'BAND',
    #                                                     'Choir', "choir", 'CHOIR',
    #                                                     'Drama', "drama", "DRAMA",
    #                                                     "Sports", "SPORTS", "sports",
    #                                                     'Science', 'science', "SCIENCE",
    #                                                     'History', 'history', 'HISTORY',
    #                                                     'Chess', 'CHESS', 'chess',
    #                                                     "music", 'Music', 'MUSIC',
    #                                                     "ict", 'ICT', "Ict",
    #                                                     'Japan', 'japan', 'JAPAN',
    #                                                     'China', 'china', 'CHINA',
    #                                                     'Accounting', 'accounting', 'ACCOUNTING',
    #                                                     'Latin', 'latin', 'LATIN',
    #                                                     'Greek', 'greek', "GREEK",
    #                                                     'Hebrew', 'HEBREW', "hebrew",
    #                                                     'Zoology', "ZOOLOGY", "zoology",
    #                                                     ]
                                            
    #                                         checkSubject = all(item in AllSubjects for item in Student_subjects.split(","))
    #                                         ##########################Clear Error###############################
    #                                         self.ClearSubjectError()
    #                                         ###################################################################
    #                                         if checkSubject is False:
    #                                             ########################Subject Error############################
    #                                             self.SubjectError()
    #                                             ################################################################
    #                                         else:
    #                                             # try:
    #                                             #     self.AgeNoError()
    #                                             # except:
    #                                             #     pass
    #                                             try: 
    #                                                 ##################Chekc db######################### 
    #                                                 self.connectDB()
    #                                                 ###################################################
    #                                             except:
    #                                                 #AddDB ERROR
    #                                                 self.DatabaseNotConnectedError()
                

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
###########################################################Go Back To Student Home#################################
    def goBackToStudentHome(self):
        self.master.switch_frame(LightStudentHome)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
#########################################On CLick Add Button ######################################################
    def clickAdd(self):

#####################################################Clear#######################################################
        self.Clearerrors()
        self.ClearCommited()
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
            
            ##############################Clear All Erorr##################################
            try:
                self.Clearerrors()
            except:
                pass
            try:
                self.AllFildsRequiredErorrDestroy()
            except:
                pass
            #################################Distroy Student First Name########################
            #################################Place The Erorr###################################  
            try:          
                self.AllFildsRequiredErorr()
            except:
                pass

        else:
            ################################Distroy All Fields Erore#####################
            try:
                self.AllFildsRequiredErorrDestroy()
                self.WStudetn_First_Name_error_label.destroy()
                self.Studetn_First_Name_error_label.destroy()
            except:
                pass 
            ##################################Student First Name Lenth Check#############
            if len(Student_first_name) > 50:
                ###################################Distroy Studetn_First_Name_No_error_label#####################
                self.FirstNameErorr()
            else:
                Student_first_name.capitalize()
                # self.FirstNameNoErorr()
                
                ############################Distroy First name Error##################################
                try:
                    self.Studetn_First_Name_error_label.destroy()
                    self.WStudetn_First_Name_error_label.destroy
                except:
                    pass
                ##########################################Cehck Student Last name Lenth########################
                if len(Student_last_name) > 50:
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


                    Student_last_name.capitalize()
                    if Student_first_name.capitalize() == Student_last_name.capitalize():
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
                        if len(Student_phone_number) != 10:

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
                                int(Student_phone_number)
                            except:
                                pass
                            if type(int(Student_phone_number)) != int:

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
                                if int(Student_phone_number[0]) != 0:
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

                                    
                                    if len(Student_age) > 2:
                                        self.ClearAgeError()
                                        self.AgeError()
                                    else:
                                        
                                        try:
                                            self.ClearAgeError()
                                        except:
                                            pass
                                        
                                        AllSubjects = ['Sinhala','sinhala', 'SINHALA', 'Sin', 'sin',
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
                                        
                                        checkSubject = all(item in AllSubjects for item in Student_subjects.split(","))
                                        ##########################Clear Error###############################
                                        self.ClearSubjectError()
                                        ###################################################################
                                        if checkSubject is False:
                                            ########################Subject Error############################
                                            self.SubjectError()
                                            ################################################################
                                        else:
                                            self.ClearSubjectError()
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

                                            int(Student_phone_number)
                                            int(Student_age)
                                            self.connetc = self.conn.cursor()

                                            self.connetc.execute(
                                                "CREATE TABLE IF NOT EXISTS Student (id INT AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(50), LAstName VARCHAR(50), PhoneNumber INT(50), Age INT(2), Student_Admission_Number VARCHAR(255) ,Subjects VARCHAR(255) )")
                                            self.connetc.execute(
                                                "INSERT INTO  Student (FirstName, LAstName, PhoneNumber, Age, Student_Admission_Number, Subjects) VALUES (%s,%s,%s,%s,%s,%s)",
                                                (str(Student_first_name.capitalize()), str(Student_last_name.capitalize()),
                                                0 + int(Student_phone_number), int(Student_age),
                                                str(Student_Admission_Number),
                                                str(Student_subjects.capitalize())))
                                            self.conn.commit()

                                            self.clearTeacherRegistation()
                                            self.Clearerrors()
                                            self.connetc.close()
                                            self.conn.close()
                                            self.Commited()
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
            self.ClearAgeError()
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
                                                    font='{Poppins} 9 {}',
                                                    foreground='#ff0f15')
        self.Studetn_All_Fields_Required_error_label.configure(text='All Fields Are Required')
        self.Studetn_All_Fields_Required_error_label.place(anchor='nw',
                                                x='500',
                                                y='121')
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
                                                    font='{Poppins} 9 {}',
                                                    foreground='#ff0f15')
        self.WStudetn_All_Fields_Required_error_label.configure(text='All Fields Are Required')
        self.WStudetn_All_Fields_Required_error_label.place(anchor='nw',
                                                x='500',
                                                y='121')

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
            self.WStudetn_First_Name_error_label.destroy()
            self.WStudetn_First_Name_No_error_label.destroy()
        except:
            pass
                
###################################################place Studetn_First_Name_error_label############################
        self.Studetn_First_Name_error_label = tk.Label(self)
        self.Studetn_First_Name_error_label.configure(background=self.bgcolor,
                                                    borderwidth='0',
                                                    font='{Poppins} 9 {}',
                                                    foreground='#ff0f15')
        self.Studetn_First_Name_error_label.configure(text='First Name Is Too Long')
        self.Studetn_First_Name_error_label.place(anchor='nw',
                                                x='500',
                                                y='123')
    def WFirstNameErorr(self):
        try:
            self.Studetn_First_Name_error_label.destroy()
            self.WStudetn_First_Name_error_label.destroy()
        except:
            pass
                
###################################################place Studetn_First_Name_error_label############################
        self.WStudetn_First_Name_error_label = tk.Label(self)
        self.WStudetn_First_Name_error_label.configure(background=self.fgcolor,
                                                    borderwidth='0',
                                                    font='{Poppins} 9 {}',
                                                    foreground='#ff0f15')
        self.WStudetn_First_Name_error_label.configure(text='First Name Is Too Long')
        self.WStudetn_First_Name_error_label.place(anchor='nw',
                                                x='500',
                                                y='123')


############################################################Last Name################################################
    def LastNameError(self):
        try:
            self.Studetn_First_Name_error_label.destroy()
            self.WStudetn_First_Name_error_label.destroy()
            self.WStudetn_Last_Name_error_label.destroy()
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

    def ClearPhoneNumberZeroError(self):
        ##########CLEAR PHONE NUMBER###############################
        try:
            self.WStudetn_0_Phone_number_error_label.destroy()
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
                                                                        y='227')
        except:
            pass
        ####################################################################

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
    def ClearAgeError(self):

        ################CLEAR AGE ERROR#############
        try:
            self.Studetn_Age_error_label.destroy()
            self.WStudetn_Age_error_label.destroy()
        except:
            pass
        ###############################################################

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

    def ClearDarabaseNotConnectedError(self):
        try:
            self.Database_not_Connected_error_label.destroy()
            self.WDatabase_not_Connected_error_label.destroy()
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

    def ClearCommited(self):
        try:
            self.Comited_label.destroy()
        except:
            pass
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

class DarkStudentDelete(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.bgcolor = ""
        try:
            self.img_DarkThemeimg = tk.PhotoImage(file='DarkThemeimg.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "DarkThemeimg.png is missing")
        self.Student_Delete_theme_change_button = tk.Button(self)
        self.Student_Delete_theme_change_button.configure(activebackground=self.bgcolor,
                                                          activeforeground=self.bgcolor,
                                                          background=self.bgcolor,
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
        self.Delete_Student_label.configure(background=self.bgcolor,
                                            borderwidth='0',
                                            font='{Poppins} 28 {bold}',
                                            foreground=self.fgcolor)
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

        self.Delete_Student_back_page_img_button.configure(activebackground=self.bgcolor,
                                                           activeforeground=self.bgcolor,
                                                           background=self.bgcolor,
                                                           borderwidth='0',
                                                           command=lambda: master.switch_frame(StudentHome))
        self.Delete_Student_back_page_img_button.configure(image=self.img_BackPageIMG)
        self.Delete_Student_back_page_img_button.place(anchor='nw', x='15', y='15')
        self.Student_Delete_Id_label = tk.Label(self)
        self.Student_Delete_Id_label.configure(background=self.bgcolor,
                                               font='{Poppins} 17 {bold}',
                                               foreground=self.fgcolor,
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
        self.Student_Delete_Go_button.configure(background=self.bgcolor,
                                                activebackground=self.bgcolor,
                                                activeforeground=self.bgcolor,
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

        self.Student_Delete_Id_bg_label.configure(background=self.bgcolor,
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

        self.configure(background=self.bgcolor,
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
                self.img_TeacherAddButton = tk.PhotoImage(file='Student_Delete.png')
            except Exception as e:
                messagebox.showerror("Student_Delete.png Missing")
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
                messagebox.showerror("Search Error", "ID You Entered is Already Deleted or Cannot Find That Id ")

            self.Delete_Student_recodes.tag_configure("oneColorStudent", background=self.bgcolor,
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

        if self["background"] == self.bgcolor:
            self.TeacherDeleteBGColor = self.fgcolor
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

            self.Delete_Student_recodes.tag_configure("oneColorStudent", background=self.fgcolor,
                                                      font='{Poppins} 8 {bold}',
                                                      foreground="#000000")
        else:
            self.DTeacherDeleteBGColor = self.bgcolor
            self.DTeacherDeleteFGColor = self.fgcolor
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

            self.Delete_Student_recodes.tag_configure("oneColorStudent", background=self.bgcolor,
                                                      font='{Poppins} 8 {bold}',
                                                      foreground=self.fgcolor)



if __name__ == "__main__":
    app = SchoolManegmentSystem()
    app.title("EDUWAY     ")
    app.eval('tk::PlaceWindow . center')
    app.attributes('-topmost', True)
    app.resizable(False, False)
    app.overrideredirect(False)
    app.mainloop()
# @^^^^^^^  ^o^
