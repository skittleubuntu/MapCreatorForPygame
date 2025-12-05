import sys
from gui import *
import pygame

from canvas import *

from settings import *
pygame.init()




class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((1000,700))
        self.clock = pygame.time.Clock()
        self.GUI = GUI()
        self.settings = Settings()
        self.canvas = Canvas(self.settings)
        print(self.settings)


        #buttons
        color_size = 40
        padding = 5
        color = 0
        for y in range(3):
            for x in range(3):
                button_x = 700 + x * (color_size + padding)
                button_y = 100 + y * (color_size + padding)
                button_color = Colors.get_color(color)

                button = Button(
                    button_x,
                    button_y,
                    width=color_size,
                    height=color_size,
                    color=button_color,
                    hover_color=Colors.WHITE,
                    callback=lambda b=None: self.select_color(b, self.GUI)

                )

                button.callback = lambda b=button: self.select_color(b, self.GUI)
                if self.settings.selected_color == color:
                    button.is_selected = True
                self.GUI.add_button(button)
                color += 1


        b = Button(700, 500, color=Colors.DARK_GRAY, text="B", callback=self.change_to_bucket)
        b.args = b
        print(b)
        self.GUI.add_button(b)

        b = Button(760, 500, color=Colors.DARK_GRAY, text="P", callback=self.change_to_pencil)
        b.args = b
        b.is_selected = True
        print(b)
        self.GUI.add_button(b)



    def change_to_bucket(self,button):
        button.is_selected = True
        print(button)
        print(button.is_selected)
        self.settings.METHOD = StateMent.BUCKET
        print(self.settings.METHOD)

        self.GUI.buttons[-1].is_selected = False



    def change_to_pencil(self,button):
        button.is_selected = True
        print(button)
        print(button.is_selected)
        self.settings.METHOD = StateMent.PENCIL
        print(self.settings.METHOD)
        self.GUI.buttons[-2].is_selected = False



    def select_color(self,button: Button, gui: GUI):

        for b in gui.buttons[0:9]:
            b.is_selected = False

        button.is_selected = True
        self.settings.selected_color = Colors.get_index(Colors.get_name(button.color))
        print(self.settings.selected_color)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()


            self.screen.fill((0,0,0))
            self.GUI.draw(self.screen)
            self.GUI.check_buttons()

            self.canvas.draw(self.screen)
            self.canvas.update(self.screen)

            pygame.display.flip()
            self.clock.tick(60)


    def quit(self):
        sys.exit()
        pygame.quit()




if __name__ == '__main__':
    App().run()