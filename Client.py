import pygame
import pygame_gui as gui
from Connector import Connect
from Server.InputBox import InputBox
from Server.GuiHelper import GuiHelper

pygame.init()

width = 500
height = 600
bg = 255, 255, 255
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

manager = gui.UIManager((500, 600))
helper = GuiHelper(500, 500, manager)
online = True


class ConnectMenu:
    def __init__(self):
        self.ip = InputBox(160, 185, 10, 30, '10.0.0.183')
        helper.make_label(250, 100, 120, 40, 'Connect', 'title', None)
        helper.make_label(80, 200, 120, 40, 'IP:', 'uname', None)

        self.enter_b = helper.make_button(250, 420, 80, 60, 'Enter', None)
        self.exit_b = helper.make_button(250, 550, 80, 60, 'Exit', None)

    def handle_event(self, event):
        self.ip.handle_event(event)

    def update(self):
        self.ip.update()

    def draw(self, win):
        self.ip.draw(win)


connect_menu = ConnectMenu()
server = Connect()


def update_window(win, time):
    win.fill((255, 255, 255))
    manager.draw_ui(win)
    manager.update(time)
    connect_menu.draw(win)
    pygame.display.update()


def main():
    run = True
    menu_flag = False
    Menus = None
    clock = pygame.time.Clock()

    while run:
        time = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.USEREVENT:
                if event.user_type == gui.UI_BUTTON_PRESSED:

                    if event.ui_element == connect_menu.enter_b:

                        ip = connect_menu.ip.text
                        response = server.connect(ip)

                        if response is None:
                            print('failed to connect')
                            helper.make_label(250, 240, 200, 40, 'failed to connect', 'uname', None)
                        else:
                            print('connected')
                            message = {'message': 'menu'}
                            Menus = server.send(message)
                            manager.clear_and_reset()
                            menu_flag = True
                            run = False

                    elif event.ui_element == connect_menu.exit_b:
                        run = False

            connect_menu.handle_event(event)
            manager.process_events(event)

        connect_menu.update()

        update_window(win, time)

    if menu_flag:
        run = True
        menu = Menus(manager)

    while run:
        time = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.USEREVENT:
                if event.user_type == gui.UI_BUTTON_PRESSED:

                    if event.ui_element == menu.exit_b:
                        run = False

                    if event.ui_element == menu.enter_b:
                        player = {'name': menu.name.text, 'username': menu.user.text,
                                  'password': menu.pswrd.text, 'class': menu.class_selector.selected_option}
                        reply = server.send(player)

                        if reply is not None and reply['message'] == 'created':
                            helper.make_label(250, 500, 120, 40, 'Created', 'created', None)
                        else:
                            online = False

                    elif event.ui_element == menu.create_b:
                        menu.new_user()

                    elif event.ui_element == menu.login_b:
                        reply = server.send({'username': menu.user.text, 'password': menu.pswrd.text})
                        if reply is not None:
                            helper.make_label(250, 360, 120, 40, reply['message'], 'loginM', None)
                        else:
                            online = False
                            helper.make_label(260, 360, 240, 40, 'Could not connect to server', 'title', None)

                    elif event.ui_element == menu.back_login_b:
                        menu.login_menu()

            menu.handle_event(event)
            manager.process_events(event)

        menu.update()

        win.fill((255, 255, 255))
        manager.draw_ui(win)
        manager.update(time)
        menu.draw(win)
        pygame.display.update()


main()
