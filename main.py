import sys
from tkinter import messagebox
import tkinter.ttk as ttk

if sys.version_info[0] == 2:
    import Tkinter as tk
else:
    import tkinter as tk
import mysql.connector

# This_is_the_back_ground_color_of_loging_page
# from ctypes import windll

background_color = '#1f1f1f'


class SchoolManegmentSystem(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(SplashScreen)

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
            self.img_img3 = tk.PhotoImage(file='img3.png')
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
                self.img_img3 = tk.PhotoImage(file="icons8-sun-31.png")
            except Exception as e:
                print(e)
                messagebox.showerror("Image Missing", "icons8-sun-31.png is missing")
            try:
                self.theme_change_button.configure(image=self.img_img3)
            except Exception as e:
                print(e)
                messagebox.showerror("Image Missing", "img_img_3.png is missing")
        elif self.backg["background"] == "#ffffff":
            self.backg.configure(background='#1f1f1f')

            self.img_img3 = tk.PhotoImage(file="img3.png")
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
        self.setting_button = tk.Button(self)
        self.setting_button.configure(activebackground='#000000',
                                      activeforeground='#000000',
                                      borderwidth='0',
                                      cursor='hand2')
        self.setting_button.configure(default='normal',
                                      highlightcolor='#000000',
                                      highlightthickness='0',
                                      image=self.img_search_button)
        self.setting_button.configure(overrelief='flat',
                                      relief='flat',
                                      takefocus=True)
        self.setting_button.place(anchor='nw',
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

        if bool(self.home_window_index_frame.winfo_exists()):
            self.home_window_index_frame.destroy()
        print(bool(self.home_window_index_frame.winfo_exists()))

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

        try:
            if bool(self.home_window_search_frame.winfo_exists()):
                self.home_window_search_frame.destroy()
                # print(bool(self.home_window_search_frame.winfo_exists()))
                print("hoo")
        except Exception as e:
            print(e)

        # if bool(self.home_window_search_frame.winfo_exists()):
        #     self.home_window_search_frame.destroy()
        # print(bool(self.home_window_search_frame.winfo_exists()))

    # self.home_window_search_frame.pack_forget()

    def onClickSetting(self):
        pass


class TeacherHome(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.register = tk.Button(self)
        self.register.configure(borderwidth='0',
                                text='register',
                                command=lambda: master.switch_frame(TeacherRegistation))
        self.register.place(anchor='nw',
                            height='150',
                            width='150',
                            x='15',
                            y='15')
        self.update = tk.Button(self)
        self.update.configure(borderwidth='0',
                              text='Update')
        self.update.place(anchor='nw',
                          height='150',
                          width='150',
                          x='315',
                          y='15')
        self.view = tk.Button(self)
        self.view.configure(borderwidth='0',
                            text='viwe',
                            command=lambda: master.switch_frame(TeacherView))
        self.view.place(anchor='nw',
                        height='150',
                        width='150',
                        x='315',
                        y='312')
        self.Delete = tk.Button(self)
        self.Delete.configure(borderwidth='0',
                              text='Delete')
        self.Delete.place(anchor='nw',
                          height='150',
                          width='150',
                          x='15',
                          y='315')
        self.configure(background='#121212',
                       height='515',
                       takefocus=False,
                       width='791')
        self.place(anchor='nw',
                   x='0',
                   y='0')


class TeacherRegistation(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.first_name_entry = tk.Entry(self)
        self.first_name_entry.place(anchor='nw',
                                    x='250',
                                    y='50')
        self.first_name_label = tk.Label(self)
        self.first_name_label.configure(text='First name')
        self.first_name_label.place(anchor='nw',
                                    x='175',
                                    y='50')
        self.second_name_entry = tk.Entry(self)
        self.second_name_entry.place(anchor='nw',
                                     x='260',
                                     y='100')
        self.second_name_label = tk.Label(self)
        self.second_name_label.configure(text='Second name')
        self.second_name_label.place(anchor='nw',
                                     x='175',
                                     y='100')
        self.phone_number_entry = tk.Entry(self)
        self.phone_number_entry.place(anchor='nw',
                                      x='260',
                                      y='150')
        self.phone_number_label = tk.Label(self)
        self.phone_number_label.configure(text='phone number')
        self.phone_number_label.place(anchor='nw',
                                      x='150',
                                      y='150')
        self.age_entry = tk.Entry(self)
        self.age_entry.place(anchor='nw',
                             x='260',
                             y='200')
        self.age_label = tk.Label(self)
        self.age_label.configure(text='age')
        self.age_label.place(anchor='nw',
                             x='150',
                             y='200')
        self.gender_label = tk.Label(self)
        self.gender_label.configure(text='gender')
        self.gender_label.place(anchor='nw',
                                x='150',
                                y='250')
        self.gender_entry = tk.Entry(self)
        self.gender_entry.place(anchor='nw',
                                x='260',
                                y='250')
        self.subects_label = tk.Label(self)
        self.subects_label.configure(text='Subject')
        self.subects_label.place(anchor='nw',
                                 x='150',
                                 y='300')
        self.subject_entry = tk.Entry(self)
        self.subject_entry.place(anchor='nw',
                                 x='260',
                                 y='300')
        self.add_teachet_button = tk.Button(self)
        self.add_teachet_button.configure(text='Add teacher',
                                          command=self.clickAdd)
        self.add_teachet_button.place(anchor='nw',
                                      x='200',
                                      y='400')

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
        self.configure(background='#121212',
                       borderwidth='0',
                       height='515',
                       width='791')
        self.pack(fill='both',
                  side='top')

    def clickAdd(self):
        global first_name, second_name, phone_number, age, gender, subjects
        first_name = self.first_name_entry.get()
        second_name = self.second_name_entry.get()
        phone_number = self.phone_number_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        subjects = self.subject_entry.get()

        if first_name == "" or second_name == "" or phone_number == "" or age == "" or gender == "" or subjects == "":
            messagebox.showerror("insert status", "All Fields Are Required")
        else:
            if len(first_name) > 50:
                messagebox.showerror("First Name Error", "Your Name Is Too Long")
            else:
                first_name.capitalize()

                if len(second_name) > 50:
                    messagebox.showerror("Second Name Error", "Your Name Is Too Long")
                else:

                    second_name.capitalize()
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
                                        (str(first_name.capitalize()), str(second_name.capitalize()),
                                         0 + int(phone_number), int(age), str(gender.capitalize()),
                                         str(subjects.capitalize())))
                                    self.conn.commit()

                                    self.clearTeacherRegistation()
                                    self.connetc.close()
                                    self.conn.close()
                                    self.master.switch_frame(TeacherView)

    def clearTeacherRegistation(self):
        self.first_name_entry.delete(0, 'end')
        self.subject_entry.delete(0, 'end')
        self.second_name_entry.delete(0, 'end')
        self.gender_entry.delete(0, 'end')
        self.age_entry.delete(0, 'end')
        self.phone_number_entry.delete(0, 'end')

        # ============================================Need to return the view page===============================================#


class TeacherView(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.columns = ('ID',
                        'First name',
                        'Last name',
                        'Age',
                        'Phone Number',
                        'Gender',
                        'Subjects')
        self.teacher_recodes = ttk.Treeview(height=75, columns=self.columns)

        self.teacher_recodes.heading("ID", text="ID")
        self.teacher_recodes.heading("First name", text="First name")
        self.teacher_recodes.heading("Last name", text="Last name")
        self.teacher_recodes.heading("Age", text="Age")
        self.teacher_recodes.heading("Phone Number", text="Phone Number")
        self.teacher_recodes.heading("Gender", text="Gender")
        self.teacher_recodes.heading("Subjects", text="Subjects")

        self.teacher_recodes['show'] = 'headings'

        self.teacher_recodes.column("ID", width=50)
        self.teacher_recodes.column("First name", width=150)
        self.teacher_recodes.column("Last name", width=130)
        self.teacher_recodes.column("Age", width=50)
        self.teacher_recodes.column("Phone Number", width=150)
        self.teacher_recodes.column("Gender", width=50)
        self.teacher_recodes.column("Subjects", width=200)

        # Add data
        self.conn = mysql.connector.connect(host="localhost", user="root",
                                            password="",
                                            database="eduway_test_1")

        self.connetc = self.conn.cursor()
        self.connetc.execute("SELECT * FROM teacher")
        self.recodes = self.connetc.fetchall()
        global count

        count = 0

        for record in self.recodes:
            self.teacher_recodes.insert(parent="", index='end', iid=count, values=(
                record[6], record[0], record[1], record[3], "0" + str(record[2]), record[4], record[5]))
            count += 1

        self.connetc.close()
        self.conn.close()

        # self.teacher_recodes.insert()

        self.teacher_recodes.place(anchor='nw', x='0', y='0')

        self.configure(background='#121212',
                       height='515',
                       width='791')
        self.place(anchor='nw',
                   x='0',
                   y='0')


# run_the_app_in_Hr_____VVVVVVVVVVV@
if __name__ == "__main__":
    app = SchoolManegmentSystem()
    app.title("EDUWAY")
    app.eval('tk::PlaceWindow . center')
    app.attributes('-topmost', True)
    app.resizable(False, False)
    # app.overrideredirect(True)
    app.mainloop()
# @^^^^^^^  ^o^
