import os
import py_cui
import logging

from dotenv import load_dotenv, set_key
from time import sleep

from views.tui_main import start_tui
from utils.facescan import FaceScan
from utils.database import create_db


load_dotenv()
DB_PATH = os.environ.get("DB_PATH")


class RegistrationTUI:
    def __init__(self, root: py_cui.PyCUI):
        self.root = root
        self.db_password = None

        ################ WELCOME TEXT BLOCK ################
        self.welcome_block = self.root.add_scroll_menu("Welcome!", 0, 0, 3)
        self.welcome_text = [
            "To start using TwoPasswords App you need to:",
            "",
            "1. Register your face for FaceAuth",
            "2. Create new Database with secure master password",
            "",
            "3. Restart App by hitting the Exit button",
        ]
        self.welcome_block.add_text_color_rule(
            "DONE", py_cui.CYAN_ON_BLACK, "startswith"
        )

        self.populate_welcome_text()

        ################ TAKE PICTURE BUTTON ################
        self.take_picture_button = self.root.add_button(
            "STEP 1 -- Register your face", 0, 1, command=self.take_new_user_picture
        )
        self.take_picture_button.set_color(py_cui.WHITE_ON_BLACK)

        ################ CREATE DATABASE BUTTON ################
        self.create_database_button = self.root.add_button(
            "STEP 2 -- Create new Database",
            1,
            1,
            command=self.show_create_database_popup,
        )
        self.create_database_button.set_color(py_cui.WHITE_ON_BLACK)

        ################ EXIT BUTTON ################
        self.next_button = self.root.add_button(
            "NEXT", 2, 1, command=self.proceed_to_app
        )
        self.next_button.set_color(py_cui.GREEN_ON_BLACK)

        self.root.set_selected_widget(1)

    def proceed_to_app(self):
        if self.db_password:
            self.root.forget_widget(self.welcome_block)
            self.root.forget_widget(self.take_picture_button)
            self.root.forget_widget(self.create_database_button)
            self.root.forget_widget(self.next_button)
            self.root.stop()
            start_tui(self.db_password)
        else:
            self.root.show_error_popup("ERROR", "Registration is not completed")

    def populate_welcome_text(self):
        self.welcome_block.clear()
        self.welcome_block.add_item_list(self.welcome_text)

    def take_new_user_picture(self):
        FaceScan("", "user_face.jpg").take_picture()
        sleep(1)
        self.root.show_message_popup("Done!", "Face registered successfully")

        self.welcome_text[2] = "DONE --> 1. Register your face for FaceAuth"
        self.populate_welcome_text()
        self.root.set_selected_widget(2)

    def show_create_database_popup(self):
        entry_fields = ["New Password", "Confirm new password"]
        self.root.show_form_popup(
            "Enter your Master password",
            entry_fields,
            entry_fields,
            required=entry_fields,
            callback=self.check_new_pragma,
        )

    def check_new_pragma(self, form_output):
        """
        form_output is a dictionary,
        hence the ugly implementation with different keys
        """
        entry1, entry2 = (
            form_output["New Password"],
            form_output["Confirm new password"],
        )

        if entry1 == entry2:
            set_key(
                ".env",
                key_to_set="DB_PASSWORD",
                value_to_set=entry1,
                quote_mode="never",
            )
            self.root.show_message_popup("OK!", f"{entry1}, {entry2}")
            create_db(DB_PATH, entry1, to_create=True)

            self.db_password = entry1

            self.welcome_text[
                3
            ] = "DONE --> 2. Create new Database with secure master password"
            self.populate_welcome_text()
            self.root.set_selected_widget(3)

        else:
            self.root.show_message_popup(
                "Warning!",
                "The confirm password does not match! Try again!",
            )


def start_registration():
    root = py_cui.PyCUI(3, 2)
    root.toggle_unicode_borders()
    root.enable_logging(logging_level=logging.DEBUG)
    frame = RegistrationTUI(root)
    root.start()


if __name__ == "__main__":
    start_registration()