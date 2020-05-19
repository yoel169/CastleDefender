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


def update_window(win, time):
    win.fill((255, 255, 255))
    manager.draw_ui(win)
    manager.update(time)
    input.draw(win)
    pygame.display.update()


def main():
    run = True

    n = Connect()

    check = 'hello'

    if n.send(check) is None:
        online = False

    clock = pygame.time.Clock()

    while run:
        time = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.USEREVENT:
                if event.user_type == gui.UI_BUTTON_PRESSED:

                    if event.ui_element == input.exit_b:
                        run = False

                    if event.ui_element == input.enter_b:
                        player = {'name': input.name.text, 'username': input.user.text,
                                  'password': input.pswrd.text, 'class': input.class_selector.selected_option}
                        reply = n.send(player)

                        if reply is not None and reply['message'] == 'created':
                            helper.make_label(250, 500, 120, 40, 'Created', 'created', None)
                        else:
                            online = False

                    elif event.ui_element == input.create_b:
                        input.new_user()

                    elif event.ui_element == input.login_b:
                        reply = n.send({'username': input.user.text, 'password': input.pswrd.text})
                        if reply is not None:
                            helper.make_label(250, 360, 120, 40, reply['message'], 'loginM', None)
                        else:
                            online = False
                            helper.make_label(260, 360, 240, 40, 'Could not connect to server', 'title', None)

                    elif event.ui_element == input.back_login_b:
                        input.login_menu()

            input.handle_event(event)
            manager.process_events(event)

        input.update()

        update_window(win, time)


main()
