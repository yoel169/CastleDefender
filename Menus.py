from Server.InputBox import InputBox
from Server.GuiHelper import GuiHelper

helper = GuiHelper


class Login:
    def __init__(self, manager):
        self.name = None
        self.user = InputBox(160, 185, 10, 30)
        self.pswrd = InputBox(160, 285, 10, 30)
        self.flag = False
        self.manager = manager

        helper.make_label(250, 100, 120, 40, 'Login', 'title', None)
        helper.make_label(80, 200, 120, 40, 'username:', 'uname', None)
        helper.make_label(80, 300, 120, 40, 'password:', 'pass', None)

        self.login_b = helper.make_button(250, 420, 80, 60, 'Login', None)
        self.exit_b = helper.make_button(180, 550, 80, 60, 'Exit', None)
        self.create_b = helper.make_button(320, 550, 120, 60, 'New Account', None)
        self.enter_b = None
        self.back_login_b = None
        self.class_selector = None

    def new_user(self):
        self.manager.clear_and_reset()
        self.name = InputBox(160, 125, 10, 30)
        self.user = InputBox(160, 225, 10, 30)
        self.pswrd = InputBox(160, 325, 10, 30)
        self.flag = True

        helper.make_label(250, 30, 120, 40, 'New Account', 'title', None)
        helper.make_label(80, 140, 120, 40, 'display name:', 'dname', None)
        helper.make_label(80, 240, 120, 40, 'username:', 'uname', None)
        helper.make_label(80, 340, 120, 40, 'password:', 'pass', None)
        helper.make_label(80, 440, 120, 40, 'class:', 'class', None)
        self.class_selector = helper.make_drop_down_menu(250, 440, 100, 50, 'classs', ['Melee', 'Range', 'Mage'])

        self.enter_b = helper.make_button(320, 550, 80, 60, 'Create', None)
        self.back_login_b = helper.make_button(180, 550, 80, 60, 'Back', None)

    def login_menu(self):
        self.manager.clear_and_reset()
        self.name = None
        self.user = InputBox(160, 185, 10, 30)
        self.pswrd = InputBox(160, 385, 10, 30)
        self.flag = False

        helper.make_label(250, 100, 120, 40, 'Login', 'title', None)
        helper.make_label(80, 200, 120, 40, 'username:', 'uname', None)
        helper.make_label(80, 300, 120, 40, 'password:', 'pass', None)

        self.login_b = helper.make_button(250, 420, 80, 60, 'Login', None)
        self.exit_b = helper.make_button(180, 550, 80, 60, 'Exit', None)
        self.create_b = helper.make_button(320, 550, 120, 60, 'New Account', None)
        self.enter_b = None
        self.back_login_b = None
        self.class_selector = None

    def handle_event(self, event):
        if self.flag:
            self.name.handle_event(event)
        self.user.handle_event(event)
        self.pswrd.handle_event(event)

    def update(self):
        if self.flag:
            self.name.update()
        self.user.update()
        self.pswrd.update()

    def draw(self, win):
        if self.flag:
            self.name.draw(win)
        self.user.draw(win)
        self.pswrd.draw(win)


class Connect:
    def __init__(self, manager):
        self.ip = InputBox(160, 185, 10, 30)
        self.manager = manager

        helper.make_label(250, 100, 120, 40, 'Connect', 'title', None)
        helper.make_label(80, 200, 120, 40, 'IP:', 'uname', None)

        self.login_b = helper.make_button(250, 420, 80, 60, 'Enter', None)
        self.exit_b = helper.make_button(180, 550, 80, 60, 'Exit', None)

    def handle_event(self, event):
        self.ip.handle_event(event)

    def update(self):
        self.ip.update()

    def draw(self, win):
        self.ip.draw(win)