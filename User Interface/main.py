import sqlite3
import random
import smtplib
from email.mime.text import MIMEText
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.modalview import ModalView
from kivymd.toast import toast
from pytube import YouTube
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.video import Video
import webbrowser
import shutil
import os

from kivymd.uix.button import MDIconButton

import re

# Load KV files
Builder.load_file("screen/sroot.kv")
Builder.load_file("screen/login.kv")
Builder.load_file("screen/password.kv")
Builder.load_file("screen/register.kv")
Builder.load_file("screen/shome.kv")
Builder.load_file("screen/navtologin.kv")
Builder.load_file("screen/card.kv")
Builder.load_file("screen/troot.kv")
Builder.load_file("screen/thome.kv")
Builder.load_file("screen/tlogin.kv")
Builder.load_file("screen/navtosignup.kv")
Builder.load_file("screen/scard.kv")
Builder.load_file('screen/leaderboard.kv')
Builder.load_file('screen/about.kv')

# Create a connection to the SQLite database
conn = sqlite3.connect('user_credentials.db')
c = conn.cursor()

# Create a table to store user credentials if it doesn't exist already
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT,email TEXT PRIMARY KEY, password TEXT,mobileno INT)''')

# Connect to the SQLite database
conn = sqlite3.connect('leaderboard.db')
c = conn.cursor()

# Create table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS scores
             (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, score INTEGER)''')
conn.commit()
# Close the connection
#conn.close()


class SignUpScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class TeacherLoginScreen(Screen):
    pass

class SetPasswordScreen(Screen):
    pass

class IconScreen(Screen):
    pass 

class StudentHome(Screen):
    pass 
class TeacherHome(Screen):
    pass 
class TeacherScreen(Screen):
    pass 
class YoutubeScreen(Screen):
    pass

class NavtoLoginScreen(Screen):
    pass 

class CardScreen(Screen):
    pass

class NavtoSignUpScreen(Screen):
    pass 

class SCardScreen(Screen):
    pass
class LeaderboardScreen(Screen):
    def on_pre_enter(self):
        # Fetch scores from the database in descending order
        c.execute('''SELECT username, score FROM scores ORDER BY score DESC''')
        rows = c.fetchall()

        # Get the layout for dynamically adding rows
        layout = self.ids.layout

        for index, (username, score) in enumerate(rows):
            row_layout = BoxLayout(orientation='horizontal', size_hint_y=None,  height=dp(70))

            # Add an image to the first row
            if index == 0:
               # You can change 'your_image.png' to the path of your image file
                image = Image(source='image/1st ranks.png',size_hint=(None,None), size=(120,90))
                row_layout.add_widget(image)
            elif index == 1:
                image = Image(source='image/2nd.png',size_hint=(None,None), size=(110,90))
                row_layout.add_widget(image)
            elif index == 2:
                image = Image(source='image/3rd.png',size_hint=(None,None), size=(120,90))
                row_layout.add_widget(image)
            else:
                # You can change 'your_image.png' to the path of your image file
                image = Image(source='image/other_row.png', size_hint=(None,None), size=(120,80))
                row_layout.add_widget(image)
            # Add labels for username and score to the row layout
            username_label = MDLabel(text=username, halign='center',           theme_text_color= "Custom",text_color= "#FFFFFF")

            score_label = MDLabel(text=str(score), halign='center',theme_text_color= "Custom",text_color= "#FFFFFF")

# Adjust vertical position of MDLabels
            username_label.pos_hint = {"center_y": 0.5}
            score_label.pos_hint = {"center_y": 0.5}

            # Add labels to the row layout
            row_layout.add_widget(username_label)
            row_layout.add_widget(score_label)

            # Add row layout to the main layout
            layout.add_widget(row_layout)
class AboutUs(Screen):
    pass

class NeuroNexApp(MDApp):
    def build(self):
        self.box_layout = BoxLayout(orientation='vertical')

         # Initialize video player
        self.video_player = Video(source='', state='play')
        self.box_layout.add_widget(self.video_player)  # Add video player to layout
        self.selected_file_path = ""  # Define selected_file_path attribute
        # Create screen manager
        self.modal_view = None  # Define modal_view attribute
        self.selected_file_label = None  # Initialize selected_file_label attribute

        self.screen_manager = ScreenManager()
        self.icon_screen = IconScreen(name='IconScreen')  # Add OtherScreen
        self.login_screen = LoginScreen(name='LoginScreen')
        self.teacher_login_screen = TeacherLoginScreen(name='TeacherLoginScreen')
        self.sign_up_screen = SignUpScreen(name='SignUpScreen')
        self.set_password_screen = SetPasswordScreen(name='SetPasswordScreen')
        self.student_home_screen = StudentHome(name='StudentHome')
        self.teacher_home_screen = TeacherHome(name='TeacherHome')

        self.teacher_icon_screen = TeacherScreen(name='TeacherScreen')
        self.navtologin_screen = NavtoLoginScreen(name='NavtoLoginScreen')
        self.card_screen = CardScreen(name='CardScreen')
        self.navtosignup_screen = NavtoSignUpScreen(name='NavtoSignUpScreen')
        self.scard_screen = SCardScreen(name='SCardScreen')
        self.about_screen = AboutUs(name='AboutUs')

        self.screen_manager.add_widget(self.icon_screen)
        self.leaderboard_screen = LeaderboardScreen(name='LeaderboardScreen')
        #Clock.schedule_once(self.force_layout_update)
        self.screen_manager.add_widget(self.teacher_icon_screen)

        self.screen_manager.add_widget(self.leaderboard_screen)
        self.screen_manager.add_widget(self.student_home_screen)
        self.screen_manager.add_widget(self.teacher_home_screen)

        self.screen_manager.add_widget(self.teacher_login_screen)
        self.screen_manager.add_widget(self.login_screen)
        self.screen_manager.add_widget(self.navtologin_screen)
        self.screen_manager.add_widget(self.navtosignup_screen)
        self.screen_manager.add_widget(self.sign_up_screen)
        self.screen_manager.add_widget(self.set_password_screen)   
        self.screen_manager.add_widget(self.card_screen)    
        self.screen_manager.add_widget(self.scard_screen)    
        self.screen_manager.add_widget(self.about_screen)    

        return self.screen_manager
        return self.video_player    

    def force_layout_update(self, dt):
        # Force a layout update
        self.screen_manager.current = 'IconScreen'
        self.screen_manager.current = 'LeaderboardScreen'
    # Inside NeuroNexApp class
    def on_hyperlink_press(self, text):
        if "Sign_in" in text:
            self.screen_manager.current = 'LoginScreen'
        elif "Sign_up" in text:
            self.screen_manager.current = 'SignUpScreen'

    def validate_passwords(self):
        new_password = self.root.ids.new_password_field.text
        confirm_password = self.root.ids.confirm_password_field.text
        
        if new_password == confirm_password:
            # Passwords match, do something (e.g., enable signup button)
            pass
        else:
            # Passwords do not match, show an error message or disable signup button
            pass

    def validate_email(self, email):
        # Regular expression pattern for validating email
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return True
        else:
            return False
        
    def validate_mobile(self, mobile):
        if len(mobile) == 10 and mobile.isdigit():
            return True
        else:
            return False

    def on_text_validate(self, email_input):
        if not self.validate_email(email_input.text):
            self.sign_up_screen.ids.invalid_email_label.text = "Invalid email format"
        else:
            self.sign_up_screen.ids.invalid_email_label.text = ""

    def send_otp(self):
        sender_email = 'shridharshininair@gmail.com'  # Replace with your email
        sender_password = 'zmrz ueir hodj ovzv'  # Replace with your email password
        sign_up_screen = self.sign_up_screen  # Access SignUpScreen instance
        receiver_email = sign_up_screen.ids.email_input.text

        # Check if the email already exists in the database
        if self.check_email_exists(receiver_email):
            self.sign_up_screen.ids.registration_message.text = "Email already registered"
            return

        # Generate and send OTP if the email is not registered
        self.otp = str(random.randint(100000, 999999))  # Generate a 6-digit OTP

        message = MIMEText(f'Your OTP is: {self.otp}')
        message['Subject'] = 'One-Time Password (OTP)'
        message['From'] = sender_email
        message['To'] = receiver_email

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            server.quit()
            self.sign_up_screen.ids.registration_message.text = "OTP sent successfully"
        except Exception as e:
            self.sign_up_screen.ids.registration_message.text = f"Failed to send OTP: {e}"
    
    def check_email_exists(self, email):
        conn = sqlite3.connect('user_credentials.db')
        c = conn.cursor()

        c.execute("SELECT * FROM users WHERE email=?", (email,))
        user = c.fetchone()

        conn.close()

        return True if user else False

    def verify_otp(self):
        if self.otp is None:
            self.sign_up_screen.ids.registration_message.text = "Please send OTP first"
            return
        
        sign_up_screen = self.sign_up_screen  # Access SignUpScreen instance
        user_input_otp = sign_up_screen.ids.otp_input.text
        if user_input_otp == self.otp:
            self.sign_up_screen.ids.registration_message.text = "OTP Verified Successfully!"
            # Reset OTP value after successful verification
            self.otp = None
            self.screen_manager.current = 'SetPasswordScreen'
        else:
            self.sign_up_screen.ids.registration_message.text = "OTP Verification Failed!"

    def set_password(self):
        username = self.sign_up_screen.ids.username_input.text
        email = self.sign_up_screen.ids.email_input.text
        new_password = self.root.get_screen('SetPasswordScreen').ids.new_password_input.text
        confirm_password = self.root.get_screen('SetPasswordScreen').ids.confirm_password_input.text
        mobileno = self.sign_up_screen.ids.mobile_input.text  # Get mobile number from input field

        if new_password == confirm_password:
            # Passwords match, perform the desired action (e.g., store password in database)
            self.register_user(username, email, new_password, mobileno)  # Pass mobileno to register_user
            # Navigate back to the signup screen
            self.screen_manager.current = 'LoginScreen'
            self.root.get_screen('IconScreen').ids.bottom_nav.switch_tab('signin')  # Switch to Home tab
        else:
            # Passwords do not match, display an error message
            self.set_password_screen.ids.registration_message.text = "Passwords do not match"

    def register_user(self, username, email, password, mobileno):
        conn = sqlite3.connect('user_credentials.db')
        c = conn.cursor()

        # Check if the email or username is empty
        if not email or not username:
            self.sign_up_screen.ids.registration_message.text = "Please fill in all required fields"
            conn.close()
            return False

        try:
            # Check if the email already exists in the database
            if self.check_email_exists(email):
                self.sign_up_screen.ids.registration_message.text = "Email already registered"
                conn.close()
                return False

            # Insert user credentials into the database
            c.execute("INSERT INTO users (username, email, password, mobileno) VALUES (?, ?, ?, ?)", (username, email, password, mobileno))
            conn.commit()
            self.sign_up_screen.ids.registration_message.text = "User registered successfully"
            return True
        except sqlite3.IntegrityError:
            self.sign_up_screen.ids.registration_message.text = "Email already registered"
            return False
        finally:
            conn.close()

    def login_student_user(self, email, password):
        conn = sqlite3.connect('user_credentials.db')
        c = conn.cursor()

        # Retrieve user credentials from the database
        c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = c.fetchone()

        if user:
            self.screen_manager.current = 'IconScreen'  # Move to another page
            # Display success message on IconScreen if needed
            self.screen_manager.get_screen('IconScreen').ids.bottom_nav.switch_tab('Home')

        else:
            self.login_screen.ids.registration_message.text = "Invalid email or password"  # Show error message on login screen

        conn.close()

    def login_teacher_user(self, email, password):
        conn = sqlite3.connect('user_credentials.db')
        c = conn.cursor()

        # Retrieve user credentials from the database
        c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = c.fetchone()

        if user:
            # Get the instance of the TeacherLoginScreen
            
            self.screen_manager.current = 'TeacherScreen'  # Move to another page
            self.root.get_screen('IconScreen').ids.bottom_nav.switch_tab('Home')  # Switch to Home tab

        else:
            self.login_screen.ids.registration_message.text = "Invalid email or password"  # Show error message on login screen

        conn.close()

    def goto_login_screen(self):
        self.screen_manager.current = 'LoginScreen'
        

    def goto_teacher_login_screen(self):
        self.screen_manager.current = 'TeacherLoginScreen'

    def goto_sign_up_screen(self):
        self.screen_manager.current = 'SignUpScreen'
    def show_leaderboard_screen(self):
        self.screen_manager.current = 'LeaderboardScreen'
    def choose_youtube_video(self, modal_view):
        modal_view.dismiss()

        youtube_modal_view = ModalView(size_hint=(None, None), size=(400, 200))

        youtube_input = TextInput(hint_text="Enter YouTube URL", multiline=False)
        confirm_button = MDIconButton(icon="check")

        def on_confirm_button(instance):
            youtube_url = youtube_input.text.strip()
            if youtube_url:
                self.open_youtube_video(youtube_url)
            else:
                print("Please enter a YouTube URL")

            youtube_modal_view.dismiss()

        confirm_button.bind(on_release=on_confirm_button)

        youtube_box_layout = BoxLayout(orientation="vertical")
        youtube_box_layout.add_widget(youtube_input)
        youtube_box_layout.add_widget(confirm_button)

        youtube_modal_view.add_widget(youtube_box_layout)
        youtube_modal_view.open()

    def open_youtube_video(self, youtube_url):
            # Split the URL by '/' and '=' characters
            url_parts = youtube_url.split('/')
            video_id = None

            # Find the part of the URL that contains the video ID
            for part in url_parts:
                if '=' in part:
                    video_id = part.split('=')[-1]
                elif 'youtu.be' in part:
                    video_id = part  # The video ID is directly after 'youtu.be/'
            
            if video_id:
                youtube_video_url = f"https://www.youtube.com/watch?v={video_id}"
                # Now you can use the youtube_video_url to open the video
                # For example, you can open it in a web browser or embed it in your application
                webbrowser.open(youtube_video_url)

            else:
                print("Invalid YouTube URL")
    def choose_local_file(self):
    # Dismiss the current modal view if it exists
        if self.modal_view:
            self.modal_view.dismiss()

        file_chooser = FileChooserListView()
        file_chooser.path = '.'

        selected_file_label = MDLabel(text="Selected File: ", halign="center", size_hint=(1, None))
        selected_file_label.height = "40dp"  # Adjust the height as needed

        def on_submit(instance, selection):
            if selection:
                selected_file_label.text = f"Selected File: {selection[0]}"
                self.selected_file_path = selection[0]

        file_chooser.bind(selection=on_submit)

        submit_button = MDIconButton(icon="check", pos_hint={"right": 1, "top": 0.5})
        submit_button.bind(on_release=lambda btn: self.upload_selected_file())

        close_button = MDIconButton(icon="close", pos_hint={"right": 1, "top": 1})
        close_button.bind(on_release=lambda btn: self.modal_view.dismiss())

        box_layout = BoxLayout(orientation='vertical')
        box_layout.add_widget(file_chooser)
        box_layout.add_widget(selected_file_label)
        box_layout.add_widget(submit_button)
        box_layout.add_widget(close_button)

        self.modal_view = ModalView(size_hint=(0.8, 0.8))
        self.modal_view.add_widget(box_layout)
        self.modal_view.open()
    def upload_selected_file(self):
        if self.selected_file_path:
            # Call the upload_video function with the selected file path
            self.upload_video(self.selected_file_path)
            self.modal_view.dismiss()  # Dismiss the modal view after uploading the file
        else:
            # No file selected, show error message or handle accordingly
            print("No file selected")
    def upload_video(self, selected_file_path):
        print(f"Selected file path: {selected_file_path}")  # Add this line to check if the method is being called
        print(f"Uploading video: {selected_file_path}")
        # Update the source of the video player with the selected video
        self.video_player.source = selected_file_path  
        self.video_player.state = 'play'  # Start playing the video

        # Create a BoxLayout to hold the buttons horizontally
        button_layout = BoxLayout(orientation="horizontal", spacing=20, size_hint=(None, None), size=(400, 100))

        # Button to choose YouTube video
        youtube_button = MDIconButton(icon="youtube")
        youtube_button.bind(on_release=lambda btn: self.choose_youtube_video(self.modal_view))

        # Button to choose local file
        file_button = MDIconButton(icon="file")
        file_button.bind(on_release=lambda btn: self.choose_local_file())

        # Button to close the modal view
        close_button = MDIconButton(icon="close")
        close_button.bind(on_release=lambda btn: self.modal_view.dismiss())

        # Add buttons to the button layout
        button_layout.add_widget(youtube_button)
        button_layout.add_widget(file_button)
        button_layout.add_widget(close_button)

        # Create a ModalView to contain the button layout
        self.modal_view = ModalView(size_hint=(None, None), size=(400, 100))
        self.modal_view.add_widget(button_layout)

        self.modal_view.open()
    def choose_file(self):
        file_chooser = FileChooserListView()
        file_chooser.path = '.'  # Set the default folder if needed

        modal_view = ModalView(size_hint=(0.9, 0.9))
        modal_view.add_widget(file_chooser)

        # Bind the selection event
        file_chooser.bind(on_submit=self.on_file_chosen)

        modal_view.open()

    def on_file_chosen(self, chooser, file_path, *args):
        # Store the selected file path
        self.selected_file_path = str(file_path[0])

        # Convert file_path to string
        file_path_str = str(file_path[0])

        # Create a submit button
        submit_button = MDIconButton(icon="check", pos_hint={"right": 1, "top": 0.5})
        submit_button.bind(on_release=lambda btn: self.upload_file(btn))

        # Create a layout to hold the file path and submit button
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(MDLabel(text=file_path_str))
        layout.add_widget(submit_button)

        # Open a modal view to display the selected file path and submit button
        modal_view = ModalView(size_hint=(0.9, 0.5))
        modal_view.add_widget(layout)
        modal_view.open()

    def upload_file(self, button):
        # Check if a file is selected
        if hasattr(self, 'selected_file_path'):
            # Specify the destination folder
            destination_folder = 'selected_file_path'
            
            # Create the destination folder if it doesn't exist
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            
            # Copy the file to the destination folder
            shutil.copy(self.selected_file_path, destination_folder)
            print("File uploaded to:", self.selected_file_path)
        else:
            print("No file selected")
            
    def on_stop(self):
        # Close the connection when the app stops
        conn.close()

if __name__ == '__main__':
    Window.size = (1400, 700)  # Set initial window size

    NeuroNexApp().run()
