from ast import Global
import sys
from tkinter import RIGHT, Y, Scrollbar, messagebox
import tkinter.ttk as ttk

if sys.version_info[0] == 2:
    import Tkinter as tk
else:
    import tkinter as tk
import mysql.connector

# This_is_the_back_ground_color_of_loging_page
# from ctypes import windll

background_color = '#1f1f1f'

TeacherRegistationTheme = "#121212"


class SchoolManegmentSystem(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(TeacherView)

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

    def minimize_window(self):
        if app.overrideredirect(True):
            app.overrideredirect(False)
            app.wm_state('iconic')


# this_is_the_Splash_Screen_of_this
# App
# I tried to create this as a normal lable
# but the self.after(miliseconds,and the funtion) is gave a error
class SplashScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # this_is_the_splash_button
        # it_will_return_you_to_log_in_page
        self.splash_button = tk.Button(self)
        try:
            self.img_splash = tk.PhotoImage(file='splash.png')
        except Exception as e:
            print(e)
            messagebox.showerror("Image Missing", "splash.png is missing")

        self.splash_button.configure(activebackground='#ffffff',
                                     activeforeground='#ffffff',
                                     background='#ffffff',
                                     borderwidth='0')
        self.splash_button.configure(cursor='wait',
                                     disabledforeground='#ffffff',
                                     foreground='#ffffff',
                                     highlightbackground='#ffffff')
        self.splash_button.configure(highlightcolor='#ffffff',
                                     highlightthickness='0',
                                     image=self.img_splash,
                                     overrelief='flat')
        ###################################################this_funtion_is_for_change_the_sopash_page_to_login_page
        self.splash_button.configure(relief='flat',
                                     text='button1',
                                     command=lambda: master.switch_frame(LogInPage))
        self.splash_button.pack(side='top')
        self.configure(height='200',
                       width='200')
        self.pack(side='top')


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
                                  background='#e7f4f9',
                                  compound='top',
                                  font='{Poppins} 23 {bold}')
        self.loginlabel.configure(foreground='#4f545c',
                                  justify='center',
                                  relief='flat',
                                  text='LOGIN')
        self.loginlabel.place(anchor='nw',
                              x='460',
                              y='70')

        # This_is_a_normal_lable_to_show_the_'"Username"'_in_the_log_in_window
        self.usernamelabel = tk.Label(self)
        self.usernamelabel.configure(background='#e7f4f9',
                                     font='{Poppins} 12 {bold}',
                                     foreground='#828282',
                                     relief='flat')
        self.usernamelabel.configure(text='USERNAME')
        self.usernamelabel.place(anchor='nw',
                                 x='380',
                                 y='160')

        ## This_is_a_normal_lable_to_show_the_background_of_Entry_box
        self.input_field_bg = tk.Label(self)

        try:
            self.img_img_textBox0 = tk.PhotoImage(file='img_textBox0.png')
        except Exception as e:
            print(e)
            messagebox.showerror("Image Missing", "img_textBox0.png is missing")

        self.input_field_bg.configure(background='#e7f4f9',
                                      image=self.img_img_textBox0,
                                      relief='flat')
        self.input_field_bg.place(anchor='nw',
                                  x='365',
                                  y='185')

        # This_is_a_normal_lable_to_show_the_'"PASSWORD"'_in_the_log_in_window
        self.password_label = tk.Label(self)
        self.password_label.configure(background='#e7f4f9',
                                      font='{Poppins} 12 {bold}',
                                      foreground='#828282',
                                      relief='flat')
        self.password_label.configure(text='PASSWORD')
        self.password_label.place(anchor='nw',
                                  x='380',
                                  y='240')

        ## This_is_a_normal_lable_to_show_the_background_of_Entry_box
        self.input_field_bg_2 = tk.Label(self)
        self.input_field_bg_2.configure(background='#e7f4f9',
                                        image=self.img_img_textBox0,
                                        relief='flat')
        self.input_field_bg_2.place(anchor='nw',
                                    x='365',
                                    y='265')

        # this_button_is_for_check_Usename&&Password_and return home_page
        self.login_button = tk.Button(self)

        try:
            self.img_img0 = tk.PhotoImage(file='img0.png')
        except Exception as e:
            print(e)
            messagebox.showerror("Image Missing", "img0.png is missing")

        self.login_button.configure(activebackground='#e7f4f9',
                                    activeforeground='#e7f4f9',
                                    background='#e7f4f9',
                                    borderwidth='0')
        self.login_button.configure(cursor='hand2',
                                    disabledforeground='#e7f4f9',
                                    foreground='#e7f4f9',
                                    highlightbackground='#e7f4f9',
                                    command=self.login_check)
        self.login_button.configure(highlightcolor='#e7f4f9',
                                    image=self.img_img0,
                                    relief='flat')
        self.login_button.place(anchor='nw',
                                x='405',
                                y='350')

        # Uuser_name_input_field
        self.username_input_field = tk.Entry(self)
        self.username_input_field.configure(background='#C7E4E0',
                                            font='{Poppins} 12 {bold}',
                                            insertbackground='#e7f4f9',
                                            insertborderwidth='3')
        self.username_input_field.configure(insertwidth='2',
                                            relief='flat',
                                            show='•')
        self.username_input_field.place(anchor='nw',
                                        height='40',
                                        x='380',
                                        y='269')

        # password_input_Field
        self.password_input_field = tk.Entry(self)
        self.password_input_field.configure(background='#C7E4E0',
                                            font='{Poppins} 12 {bold}',
                                            insertbackground='#e7f4f9',
                                            insertborderwidth='3')
        self.password_input_field.configure(insertwidth='2',
                                            relief='flat')
        self.password_input_field.place(anchor='nw',
                                        height='40',
                                        x='380',
                                        y='190')
        self.close_button = tk.Button(self)
        try:
            self.img_img4 = tk.PhotoImage(file='img4.png')
        except Exception as e:
            print(e)
            messagebox.showerror("Image Missing", "img4.png is missing")

        # this is the close button of login page
        self.close_button.configure(activebackground='#00FFD1',
                                    activeforeground='#00FFD1',
                                    background='#00FFD1',
                                    borderwidth='0')
        self.close_button.configure(compound='top',
                                    cursor='hand2',
                                    disabledforeground='#00FFD1',
                                    foreground='#00FFD1')
        self.close_button.configure(highlightbackground='#00FFD1',
                                    highlightcolor='#00FFD1',
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

        self.clear_btton.configure(activebackground='#E6F4F9',
                                   activeforeground='#E6F4F9',
                                   background='#E6F4F9',
                                   borderwidth='0')
        self.clear_btton.configure(compound='top', cursor='hand2',
                                   disabledforeground='#E6F4F9',
                                   foreground='#E6F4F9')
        self.clear_btton.configure(highlightbackground='#E6F4F9',
                                   highlightcolor='#E6F4F9',
                                   highlightthickness='0',
                                   image=self.img_img1)
        self.clear_btton.configure(overrelief='flat',
                                   relief='flat',
                                   command=self.clearLogin)
        self.clear_btton.place(anchor='nw',
                               x='600',
                               y='80')

        # this_Button_is for Change_the_color_Theme
        self.theme_change_button = tk.Button(self)
        try:
            self.img_img3 = tk.PhotoImage(file='LightThemeimg.png')
        except Exception as e:
            messagebox.showerror("Image Missing", "img3.png is missing")

        self.theme_change_button.configure(activebackground='#CDFF62',
                                           activeforeground='#CDFF62',
                                           background='#CDFF62',
                                           borderwidth='0',
                                           command=self.change_theme)
        self.theme_change_button.configure(cursor='hand2',
                                           disabledforeground='#CDFF62',
                                           foreground='#CDFF62',
                                           highlightbackground='#CDFF62')
        self.theme_change_button.configure(highlightcolor='#CDFF62',
                                           highlightthickness='0',
                                           image=self.img_img3,
                                           overrelief='flat')
        self.theme_change_button.configure(relief='flat')
        self.theme_change_button.place(anchor='nw',
                                       x='650',
                                       y='450')
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
        if usernamme != "Admin" and password != "Admin":
            self.username_error_label = tk.Label(self)
            self.username_error_label.configure(background='#E7F5FA',
                                                borderwidth='0',
                                                font='{Poppins} 9 {}',
                                                foreground='#ff0f15')
            self.username_error_label.configure(text='Invalid Username')
            self.username_error_label.place(anchor='nw',
                                            x='500',
                                            y='160')
            self.password_error_label = tk.Label(self)
            self.password_error_label.configure(background='#E7F5FA',
                                                borderwidth='0',
                                                font='{Poppins} 9 {}',
                                                foreground='#ff0f15')
            self.password_error_label.configure(text='invalid password')
            self.password_error_label.place(anchor='nw',
                                            x='500',
                                            y='240')
        else:
            self.master.switch_frame(Home)

    # This Function is for change the loght_theme_ to dark theme
    def change_theme(self):
        if self.backg["background"] == "#1f1f1f":
            self.backg.configure(background='#ffffff')
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


# This is a Template to create a new frame
# Copy this one fbefor use this

# class PageTwo(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         tk.Label(self, text="This is page two").pack(side="top", fill="x", pady=10)
#         tk.Button(self, text="Return to start page",
#                   command=lambda: master.switch_frame(StartPage)).pack()
# remember_ths

# this is the home page of SchoolManegment system
class Home(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # home_background_image_As_Lable
        self.home_backg = tk.Label(self)
        try:
            self.img_home_bg = tk.PhotoImage(file='home_bg.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "home_bg.png is missing")

        self.home_backg.configure(borderwidth='0',
                                  image=self.img_home_bg,
                                  text='label1')
        self.home_backg.pack(side='top')

        # home_button_to_return_ro_home_page
        self.home_button = tk.Button(self)

        try:
            self.img_home_button = tk.PhotoImage(file='home_button.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "home_button.png is missing")

        self.home_button.configure(activebackground='#000000',
                                   activeforeground='#000000',
                                   background="#000000",
                                   borderwidth='0',
                                   cursor='hand2')
        self.home_button.configure(default='normal',
                                   highlightcolor='#000000',
                                   highlightthickness='0',
                                   image=self.img_home_button)
        self.home_button.configure(overrelief='flat',
                                   relief='flat',
                                   takefocus=True,
                                   command=self.onClickHome)
        self.home_button.place(anchor='nw',
                               height='48',
                               width='220',
                               x='0', y='50')

        # search_button to return to search page
        self.search_button = tk.Button(self)

        try:
            self.img_search_button = tk.PhotoImage(file='search_button.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "search_button.png is missing")

        self.search_button.configure(activebackground='#000000',
                                     activeforeground='#000000',
                                     borderwidth='0',
                                     cursor='hand2')
        self.search_button.configure(default='normal',
                                     highlightcolor='#000000',
                                     highlightthickness='0',
                                     image=self.img_search_button,
                                     command=lambda: master.switch_frame(TeacherHome))
        self.search_button.configure(overrelief='flat',
                                     relief='flat',
                                     takefocus=True)
        self.search_button.place(anchor='nw',
                                 height='48',
                                 width='220',
                                 x='0',
                                 y='98')

        # setting_button to return to setting page
        self.student_button = tk.Button(self)
        self.student_button.configure(activebackground='#000000',
                                      activeforeground='#000000',
                                      borderwidth='0',
                                      cursor='hand2')
        self.student_button.configure(default='normal',
                                      highlightcolor='#000000',
                                      highlightthickness='0',
                                      image=self.img_search_button)
        self.student_button.configure(overrelief='flat',
                                      relief='flat',
                                      takefocus=True)
        self.student_button.place(anchor='nw',
                                  height='48',
                                  width='220',
                                  x='0',
                                  y='146')

        # home_image_button to show_about_NEWS_of_the_School
        # and_add_good_ui_and_ux
        # self.home_image_button = tk.Button(self)
        # self.img_news_poto = tk.PhotoImage(file='news_poto.png')
        # self.home_image_button.configure(activebackground='#000000', activeforeground='#000000', background='#000000',
        #                                  borderwidth='0')
        # self.home_image_button.configure(cursor='hand2', highlightcolor='#000000', highlightthickness='0',
        #                                  image=self.img_news_poto)
        # self.home_image_button.place(anchor='nw', height='220', width='220', y='295'
        try:
            self.img_img4 = tk.PhotoImage(file='img4.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "img_img4 is missing")

        # window_frame
        self.home_window_index_frame = tk.Frame(self)
        self.home_window_index_frame.configure(background='#121212',
                                               height='200',
                                               width='200')
        self.home_window_index_frame.place(anchor='nw',
                                           height='515',
                                           width='571',
                                           x='220')

        # home_page_close_button_vvvvv_v@
        self.home_close_button = tk.Button(self)
        self.home_close_button.configure(activebackground='#121212',
                                         activeforeground='#121212',
                                         background='#121212',
                                         borderwidth='0')
        self.home_close_button.configure(cursor='hand2', foreground='#121212',
                                         highlightbackground='#121212',
                                         highlightcolor='#121212')
        self.home_close_button.configure(highlightthickness='1',
                                         image=self.img_img4,
                                         relief='flat',
                                         command=self.master.on_close)
        self.home_close_button.place(anchor='nw',
                                     x='760',
                                     y='8')
        # self.home_close_button.lift()
        # @home_page_close_button^^^^_^
        self.onClickHome()

    # Todo_make_a_frame_to_bla_bla
    def onClickSearch(self):
        # this is the frame indide bla bla need to distry befor bla bla
        self.home_window_search_frame = tk.Frame(self)
        try:
            self.img_home_button = tk.PhotoImage(file='home_button_out.png')
            self.home_button.configure(image=self.img_home_button)
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "home_button_out.png is missing")

        self.test_btn_2 = tk.Button(self.home_window_search_frame)
        self.test_btn_2.configure(borderwidth='0',
                                  text='button6')
        self.test_btn_2.place(anchor='nw',
                              x='50',
                              y='0')
        self.home_window_search_frame.configure(background='#121212',
                                                borderwidth='0',
                                                height='200',
                                                width='200')
        self.home_window_search_frame.place(anchor='nw',
                                            height='515',
                                            width='571',
                                            x='220')

        # home_search_close_button
        self.home_search_close_button = tk.Button(self)
        self.home_search_close_button.configure(activebackground='#121212',
                                                activeforeground='#121212',
                                                background='#121212',
                                                borderwidth='0')
        self.home_search_close_button.configure(cursor='hand2',
                                                foreground='#121212',
                                                highlightbackground='#121212',
                                                highlightcolor='#121212')
        self.home_search_close_button.configure(highlightthickness='1',
                                                image=self.img_img4,
                                                relief='flat',
                                                command=self.master.on_close)
        self.home_search_close_button.place(anchor='nw',
                                            x='760',
                                            y='8')
        # self.home_image_button_news_2_img = tk.PhotoImage(file="news_poto_2.png")
        # self.home_image_button.configure(image=self.home_image_button_news_2_img)

        # if bool(self.home_window_index_frame.winfo_exists()):
        #     self.home_window_index_frame.destroy()
        # print(bool(self.home_window_index_frame.winfo_exists()))

    def onClickHome(self):
        self.home_window_index_frame = tk.Frame(self)
        self.test_btn_1 = tk.Button(self.home_window_index_frame)
        self.test_btn_1.configure(borderwidth='0',
                                  text='button6')
        self.test_btn_1.place(anchor='nw',
                              x='0', y='0')
        self.home_window_index_frame.configure(background='#121212',
                                               borderwidth='0',
                                               height='200',
                                               width='200')
        self.home_window_index_frame.place(anchor='nw',
                                           height='515',
                                           width='571',
                                           x='220')

        self.home__close_button = tk.Button(self)
        self.home__close_button.configure(activebackground='#121212',
                                          activeforeground='#121212',
                                          background='#121212',
                                          borderwidth='0')
        self.home__close_button.configure(cursor='hand2',
                                          foreground='#121212',
                                          highlightbackground='#121212',
                                          highlightcolor='#121212')
        self.home__close_button.configure(highlightthickness='1',
                                          image=self.img_img4,
                                          relief='flat',
                                          command=self.master.on_close)
        self.home__close_button.place(anchor='nw',
                                      x='760',
                                      y='8')
        self.configure(height='515',
                       width='791')
        self.pack(side='top')

        # app.overrideredirect(False)
        # app.wm_state('iconic')

        # try:
        #     self.home_image_button.configure(image=self.img_news_poto)
        # except Exception as e:
        #     print(e)

    #     try:
    #         if bool(self.home_window_search_frame.winfo_exists()):
    #             self.home_window_search_frame.destroy()
    #             # print(bool(self.home_window_search_frame.winfo_exists()))
    #             print("hoo")
    #     except Exception as e:
    #         print(e)

    # if bool(self.home_window_search_frame.winfo_exists()):
    #     self.home_window_search_frame.destroy()
    # print(bool(self.home_window_search_frame.winfo_exists()))

    # self.home_window_search_frame.pack_forget()

    def onClickSetting(self):
        pass


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
        self.Element_2_IMG_label.place(anchor='nw', y='296')

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
                                     image=self.img_TeacherHomeUpdateButton)
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
                                     background="#121212")
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


class TeacherRegistation(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.First_name_Entry_bg_label = tk.Label(self)
        self.element_img_label = tk.Label(self)

        try:
            self.img_Element_1_img_label = tk.PhotoImage(file='Element_1_img_label.png')
        except Exception as e:
            messagebox.showerror("Element_1_img_label.png' Missing")
            print(e)

        self.element_img_label.configure(background='#121212',
                                         image=self.img_Element_1_img_label)
        self.element_img_label.place(anchor='nw',
                                     x='431',
                                     y='322')

        try:
            self.img_TeacherRegiusterEntery = tk.PhotoImage(file='TeacherRegiusterEntery.png')
        except Exception as e:
            messagebox.showerror("TeacherAddButton.png Missing")
            print(e)

        self.First_name_Entry_bg_label.configure(background='#121212',
                                                 borderwidth='0',
                                                 image=self.img_TeacherRegiusterEntery)
        self.First_name_Entry_bg_label.place(anchor='nw',
                                             x='386',
                                             y='146')

        self.Last_name_Entry_bg_label = tk.Label(self)
        self.Last_name_Entry_bg_label.configure(background='#121212',
                                                borderwidth='0',
                                                image=self.img_TeacherRegiusterEntery)
        self.Last_name_Entry_bg_label.place(anchor='nw',
                                            x='386',
                                            y='196')

        self.age_Entry_bg_label = tk.Label(self)
        self.age_Entry_bg_label.configure(background='#121212',
                                          borderwidth='0',
                                          image=self.img_TeacherRegiusterEntery)
        self.age_Entry_bg_label.place(anchor='nw',
                                      x='386',
                                      y='246')

        self.phone_number_Entry_bg_label = tk.Label(self)
        self.phone_number_Entry_bg_label.configure(background='#121212',
                                                   borderwidth='0',
                                                   image=self.img_TeacherRegiusterEntery)
        self.phone_number_Entry_bg_label.place(anchor='nw',
                                               x='386',
                                               y='290')

        self.gender_Entry_bg_label = tk.Label(self)
        self.gender_Entry_bg_label.configure(background='#121212',
                                             borderwidth='0',
                                             image=self.img_TeacherRegiusterEntery)
        self.gender_Entry_bg_label.place(anchor='nw',
                                         x='386',
                                         y='340')

        self.subject_Entry_bg_label = tk.Label(self)
        self.subject_Entry_bg_label.configure(background='#121212',
                                              borderwidth='0',
                                              image=self.img_TeacherRegiusterEntery)
        self.subject_Entry_bg_label.place(anchor='nw',
                                          x='386',
                                          y='390')

        self.first_name_entry = tk.Entry(self)
        self.first_name_entry.configure(borderwidth='0')
        self.first_name_entry.configure(font='{Poppins} 10 {bold}',
                                        insertwidth='1',
                                        relief='flat')
        self.first_name_entry.place(anchor='nw',
                                    height='24',
                                    width='229',
                                    x='395',
                                    y='149')

        self.first_name_label = tk.Label(self)
        self.first_name_label.configure(background='#121212',
                                        font='{Poppins} 17 {bold}',
                                        foreground='#ffffff',
                                        text='First Name')
        self.first_name_label.place(anchor='nw',
                                    x='166',
                                    y='146')

        self.last_name_entry = tk.Entry(self)
        self.last_name_entry.configure(borderwidth='0')
        self.last_name_entry.configure(font='{Poppins} 10 {bold}',
                                       insertwidth='1',
                                       relief='flat')
        self.last_name_entry.place(anchor='nw',
                                   height='24',
                                   width='229',
                                   x='397',
                                   y='199')

        self.last_name_label = tk.Label(self)
        self.last_name_label.configure(background='#121212',
                                       font='{Poppins} 17 {bold}',
                                       foreground='#ffffff',
                                       text='Last Name')
        self.last_name_label.place(anchor='nw',
                                   x='166',
                                   y='198')

        self.phone_number_entry = tk.Entry(self)
        self.phone_number_entry.configure(borderwidth='0')
        self.phone_number_entry.configure(font='{Poppins} 10 {bold}',
                                          insertwidth='1',
                                          relief='flat')
        self.phone_number_entry.place(anchor='nw',
                                      height='24',
                                      width='229',
                                      x='397',
                                      y='293')

        self.phone_number_label = tk.Label(self)
        self.phone_number_label.configure(background='#121212',
                                          font='{Poppins} 17 {bold}',
                                          foreground='#ffffff',
                                          text='Phone number')
        self.phone_number_label.place(anchor='nw',
                                      x='166',
                                      y='289')

        self.age_entry = tk.Entry(self)
        self.age_entry.configure(borderwidth='0')
        self.age_entry.configure(font='{Poppins} 10 {bold}',
                                 insertwidth='1',
                                 relief='flat')
        self.age_entry.place(anchor='nw',
                             height='24',
                             width='229',
                             x='395',
                             y='249')

        self.age_label = tk.Label(self)
        self.age_label.configure(background='#121212',
                                 font='{Poppins} 17 {bold}',
                                 foreground='#ffffff',
                                 text='Age')
        self.age_label.place(anchor='nw',
                             x='166',
                             y='239')

        self.gender_label = tk.Label(self)
        self.gender_label.configure(background='#121212',
                                    font='{Poppins} 17 {bold}',
                                    foreground='#ffffff',
                                    text='Gender')
        self.gender_label.place(anchor='nw',
                                x='166',
                                y='331')

        self.gender_entry = tk.Entry(self)
        self.gender_entry.configure(borderwidth="0")
        self.gender_entry.configure(font='{Poppins} 10 {bold}',
                                    insertwidth='1',
                                    relief='flat')
        self.gender_entry.place(anchor='nw',
                                height='24',
                                width='229',
                                x='395',
                                y='343')

        self.subects_label = tk.Label(self)
        self.subects_label.configure(background='#121212',
                                     font='{Poppins} 17 {bold}',
                                     foreground='#ffffff',
                                     text='Subject')
        self.subects_label.place(anchor='nw',
                                 x='166',
                                 y='389')

        self.subject_entry = tk.Entry(self)
        self.subject_entry.configure(borderwidth="0")
        self.subject_entry.configure(font='{Poppins} 10 {bold}',
                                     insertwidth='1',
                                     relief='flat')
        self.subject_entry.place(anchor='nw',
                                 height='24',
                                 width='229',
                                 x='395',
                                 y='393')

        try:
            self.img_TeacherAddButton = tk.PhotoImage(file='TeacherAddButton.png')
        except Exception as e:
            messagebox.showerror("TeacherAddButton.png Missing")
            print(e)

        self.add_teachet_button = tk.Button(self)
        self.add_teachet_button.configure(background='#121212',
                                          activebackground='#121212',
                                          activeforeground='#121212',
                                          borderwidth='0',
                                          image=self.img_TeacherAddButton,
                                          relief='flat',
                                          command=self.clickAdd)
        self.add_teachet_button.place(anchor='nw',
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

        self.back_page_img_button = tk.Button(self)

        try:
            self.img_BackPageIMG = tk.PhotoImage(file='BackPageIMG.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "BackPageIMG.png is missing")

        self.back_page_img_button.configure(activebackground='#121212',
                                            activeforeground='#121212',
                                            background='#121212',
                                            borderwidth='0',
                                            command=self.goBackToTeacherHome)
        self.back_page_img_button.configure(image=self.img_BackPageIMG)
        self.back_page_img_button.place(anchor='nw', x='15', y='15')

        self.teacher_registation_theme_change_button = tk.Button(self)

        try:
            self.img_DarkThemeimg = tk.PhotoImage(file='DarkThemeimg.png')
        except Exception as e:
            print(e)
            messagebox.showerror("File Missing", "DarkThemeimg.png is missing")

        self.teacher_registation_theme_change_button.configure(activebackground='#121212',
                                                               activeforeground='#121212',
                                                               background='#121212',
                                                               borderwidth='0',
                                                               relief="flat",
                                                               overrelief="flat",
                                                               command=self.changeTeacherRegistationTheme)
        self.teacher_registation_theme_change_button.configure(image=self.img_DarkThemeimg,
                                                               text='button2')
        self.teacher_registation_theme_change_button.place(anchor='nw',
                                                           x='60',
                                                           y='10')
        self.configure(background='#121212',
                       borderwidth='0',
                       height='515',
                       width='791')
        self.pack(fill='both',
                  side='top')

    def changeTeacherRegistationTheme(self):
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

        if self.back_page_img_button["background"] == "#121212":
            self.teacherRegistationBGColor = "#ffffff"
            self.teacherRegistationFGColor = "#000000"
            self.configure(background=self.teacherRegistationBGColor)
            self.element_img_label.configure(background=self.teacherRegistationBGColor,
                                             foreground=self.teacherRegistationFGColor)
            self.First_name_Entry_bg_label.configure(background=self.teacherRegistationBGColor,
                                                     foreground=self.teacherRegistationFGColor)
            self.Last_name_Entry_bg_label.configure(background=self.teacherRegistationBGColor,
                                                    foreground=self.teacherRegistationFGColor)
            self.age_Entry_bg_label.configure(background=self.teacherRegistationBGColor,
                                              foreground=self.teacherRegistationFGColor)
            self.phone_number_Entry_bg_label.configure(background=self.teacherRegistationBGColor,
                                                       foreground=self.teacherRegistationFGColor)
            self.phone_number_Entry_bg_label.configure(background=self.teacherRegistationBGColor,
                                                       foreground=self.teacherRegistationFGColor)
            self.gender_Entry_bg_label.configure(background=self.teacherRegistationBGColor,
                                                 foreground=self.teacherRegistationFGColor)
            self.subject_Entry_bg_label.configure(background=self.teacherRegistationBGColor,
                                                  foreground=self.teacherRegistationFGColor)
            self.first_name_entry.configure(background=self.teacherRegistationBGColor,
                                            foreground=self.teacherRegistationFGColor)
            self.first_name_label.configure(background=self.teacherRegistationBGColor,
                                            foreground=self.teacherRegistationFGColor)
            self.last_name_entry.configure(background=self.teacherRegistationBGColor,
                                           foreground=self.teacherRegistationFGColor)
            self.last_name_label.configure(background=self.teacherRegistationBGColor,
                                           foreground=self.teacherRegistationFGColor)
            self.phone_number_entry.configure(background=self.teacherRegistationBGColor,
                                              foreground=self.teacherRegistationFGColor)
            self.phone_number_label.configure(background=self.teacherRegistationBGColor,
                                              foreground=self.teacherRegistationFGColor)
            self.age_entry.configure(background=self.teacherRegistationBGColor,
                                     foreground=self.teacherRegistationFGColor)
            self.age_label.configure(background=self.teacherRegistationBGColor,
                                     foreground=self.teacherRegistationFGColor)
            self.gender_entry.configure(background=self.teacherRegistationBGColor,
                                        foreground=self.teacherRegistationFGColor)
            self.gender_label.configure(background=self.teacherRegistationBGColor,
                                        foreground=self.teacherRegistationFGColor)
            self.subject_entry.configure(background=self.teacherRegistationBGColor,
                                         foreground=self.teacherRegistationFGColor)
            self.subects_label.configure(background=self.teacherRegistationBGColor,
                                         foreground=self.teacherRegistationFGColor)
            self.add_teachet_button.configure(background=self.teacherRegistationBGColor,
                                              foreground=self.teacherRegistationFGColor,
                                              activebackground=self.teacherRegistationBGColor,
                                              activeforeground=self.teacherRegistationBGColor)
            self.Teacher_registation_close_button.configure(background=self.teacherRegistationBGColor,
                                                            foreground=self.teacherRegistationFGColor)
            self.Register_Teacher_label.configure(background=self.teacherRegistationBGColor,
                                                  foreground=self.teacherRegistationFGColor)
            self.back_page_img_button.configure(background=self.teacherRegistationBGColor,
                                                foreground=self.teacherRegistationFGColor,
                                                activebackground=self.teacherRegistationBGColor,
                                                activeforeground=self.teacherRegistationBGColor)
            self.teacher_registation_theme_change_button.configure(background=self.teacherRegistationBGColor,
                                                                   foreground=self.teacherRegistationFGColor,
                                                                   activebackground=self.teacherRegistationBGColor,
                                                                   activeforeground=self.teacherRegistationBGColor,
                                                                   image=self.img_lightThemeimg)
        else:
            self.DteacherRegistationBGColor = "#121212"
            self.DteacherRegistationFGColor = "#ffffff"
            self.configure(background=self.DteacherRegistationBGColor)
            self.element_img_label.configure(background=self.DteacherRegistationBGColor,
                                             foreground=self.DteacherRegistationFGColor)
            self.First_name_Entry_bg_label.configure(background=self.DteacherRegistationBGColor,
                                                     foreground=self.DteacherRegistationFGColor)
            self.Last_name_Entry_bg_label.configure(background=self.DteacherRegistationBGColor,
                                                    foreground=self.DteacherRegistationFGColor)
            self.age_Entry_bg_label.configure(background=self.DteacherRegistationBGColor,
                                              foreground=self.DteacherRegistationFGColor)
            self.phone_number_Entry_bg_label.configure(background=self.DteacherRegistationBGColor,
                                                       foreground=self.DteacherRegistationFGColor)
            self.phone_number_Entry_bg_label.configure(background=self.DteacherRegistationBGColor,
                                                       foreground=self.DteacherRegistationFGColor)
            self.gender_Entry_bg_label.configure(background=self.DteacherRegistationBGColor,
                                                 foreground=self.DteacherRegistationFGColor)
            self.subject_Entry_bg_label.configure(background=self.DteacherRegistationBGColor,
                                                  foreground=self.DteacherRegistationFGColor)
            self.first_name_label.configure(background=self.DteacherRegistationBGColor,
                                            foreground=self.DteacherRegistationFGColor)
            self.last_name_label.configure(background=self.DteacherRegistationBGColor,
                                           foreground=self.DteacherRegistationFGColor)
            self.phone_number_label.configure(background=self.DteacherRegistationBGColor,
                                              foreground=self.DteacherRegistationFGColor)
            self.age_label.configure(background=self.DteacherRegistationBGColor,
                                     foreground=self.DteacherRegistationFGColor)
            self.gender_label.configure(background=self.DteacherRegistationBGColor,
                                        foreground=self.DteacherRegistationFGColor)
            self.subects_label.configure(background=self.DteacherRegistationBGColor,
                                         foreground=self.DteacherRegistationFGColor)
            self.add_teachet_button.configure(background=self.DteacherRegistationBGColor,
                                              foreground=self.DteacherRegistationFGColor,
                                              activebackground=self.DteacherRegistationBGColor,
                                              activeforeground=self.DteacherRegistationBGColor)
            self.Teacher_registation_close_button.configure(background=self.DteacherRegistationBGColor,
                                                            foreground=self.DteacherRegistationFGColor)
            self.Register_Teacher_label.configure(background=self.DteacherRegistationBGColor,
                                                  foreground=self.DteacherRegistationFGColor)
            self.back_page_img_button.configure(background=self.DteacherRegistationBGColor,
                                                foreground=self.DteacherRegistationFGColor)
            self.teacher_registation_theme_change_button.configure(background=self.DteacherRegistationBGColor,
                                                                   foreground=self.DteacherRegistationFGColor,
                                                                   activebackground=self.DteacherRegistationBGColor,
                                                                   activeforeground=self.DteacherRegistationBGColor,
                                                                   image=self.img_DarkThemeimg)

    def goBackToTeacherHome(self):
        self.master.switch_frame(TeacherHome)

    def clickAdd(self):
        global first_name, last_name, phone_number, age, gender, subjects
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        phone_number = self.phone_number_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        subjects = self.subject_entry.get()

        if first_name == "" or last_name == "" or phone_number == "" or age == "" or gender == "" or subjects == "":
            messagebox.showerror("insert status", "All Fields Are Required")
        else:
            if len(first_name) > 50:
                messagebox.showerror("First Name Error", "Your Name Is Too Long")
            else:
                first_name.capitalize()

                if len(last_name) > 50:
                    messagebox.showerror("Second Name Error", "Your Name Is Too Long")
                else:
                    last_name.capitalize()
                    if first_name == last_name:
                        messagebox.showerror("Copied Name Error", "Your First Name And Secont Name Is Duplicated")
                    else:
                        if len(phone_number) != 10:
                            messagebox.showerror("Phone Number Error", "You Can Add Only 10 Digit number")
                        else:
                            try:
                                int(phone_number)
                            except Exception as e:
                                messagebox.showerror("Type Error", "You Can Only Type Numbers For Phone Number ")
                                print(e)
                            if int(phone_number[0]) != 0:
                                messagebox.showerror("Type Error", "This is Not Phone Number")
                            else:
                                if len(age) > 2:
                                    messagebox.showerror("Age Error", "You Can Only Type Two Numbers For Age ")
                                else:
                                    genderIndex = ['male', "Male", "female", "Female", "m", "M", "F", "f"]
                                    if gender not in genderIndex:
                                        messagebox.showerror("Age Error", "You Can Add Only Type Male or Female ")
                                    else:
                                        if gender == "m" or gender == "male":
                                            gender = "Male"
                                        else:
                                            gender = "Female"

                                        self.conn = mysql.connector.connect(host="localhost", user="root",
                                                                            password="",
                                                                            database="eduway_test_1")
                                        int(phone_number)
                                        int(age)
                                        self.connetc = self.conn.cursor()

                                        self.connetc.execute(
                                            "CREATE TABLE IF NOT EXISTS teacher (id INT AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(50), LAstName VARCHAR(50), PhoneNumber INT(50), Age INT(2), Gender VARCHAR(50) ,Subjects VARCHAR(255) )")
                                        self.connetc.execute(
                                            "INSERT INTO  teacher (FirstName, LAstName, PhoneNumber, Age, Gender, Subjects) VALUES (%s,%s,%s,%s,%s,%s)",
                                            (str(first_name.capitalize()), str(last_name.capitalize()),
                                             0 + int(phone_number), int(age), str(gender.capitalize()),
                                             str(subjects.capitalize())))
                                        self.conn.commit()

                                        self.clearTeacherRegistation()
                                        self.connetc.close()
                                        self.conn.close()
                                        # self.master.switch_frame(TeacherView)

    def clearTeacherRegistation(self):
        self.first_name_entry.delete(0, 'end')
        self.subject_entry.delete(0, 'end')
        self.last_name_entry.delete(0, 'end')
        self.gender_entry.delete(0, 'end')
        self.age_entry.delete(0, 'end')
        self.phone_number_entry.delete(0, 'end')

        # ============================================Need to return the view page===============================================#


class TeacherView(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.sty = ttk.Style()
        self.sty.configure('Treeview', rowheight=46)
        self.sty.map('Treeview', background=[('selected', '#3B3B3B'), ('focus', '#212121')])
        self.sty.configure("Vertical.TScrollbar",
                           background="#000000", darkcolor="#000000", lightcolor="#000000",
                           troughcolor="gray", bordercolor="gray", arrowcolor="white")
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
        self.conn = mysql.connector.connect(host="localhost", user="root",
                                            password="",
                                            database="eduway_test_1")

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
                    record[6], record[0], record[1], record[3], "0" + str(record[2]), record[4], record[5]),
                                            tags=("oneColor"))
            else:
                self.teacher_recodes.insert(parent="", index='end', iid=count, values=(
                    record[6], record[0], record[1], record[3], "0" + str(record[2]), record[4], record[5]),
                                            tags=("secondColor"))
            count += 1

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
                                               foreground="c2c2c2")
            self.teacher_recodes.tag_configure("oneColor", background="#0a0a0a",
                                               font='{Poppins} 8 {bold}',
                                               foreground="c2c2c2")
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


                                                            
# run_the_app_in_Hr_____VVVVVVVVVVV@
if __name__ == "__main__":
    app = SchoolManegmentSystem()
    app.title("EDUWAY")
    app.eval('tk::PlaceWindow . center')
    app.attributes('-topmost', True)
    app.resizable(False, False)
    app.overrideredirect(True)
    app.mainloop()
# @^^^^^^^  ^o^
