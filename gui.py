import pygame
from settings import Colors

class GUI:
    def __init__(self):
        self.texts: list[Text] = []
        self.buttons: list[Button] = []



    def draw(self,screen):

        screen.fill(Colors.GRAY)

        for button in self.buttons:
            button.draw(screen)

        for text in self.texts:
            text.draw(screen)


    def check_buttons(self):
        mx, my = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()[0]

        for button in self.buttons:
            button.is_hovered = button.rect.collidepoint(mx, my)
            if pressed and button.is_hovered:
                button.on_click()

    def add_button(self, button):
        self.buttons.append(button)


class Button:
    def __init__(self, x, y, width=50, height=50, color=Colors.RED, hover_color=Colors.GREEN,
                 text='', font_size=30,selected_color = Colors.WHITE, callback=None, args=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.is_selected = False
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.callback = callback
        self.selected_color = selected_color
        self.args = args


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

        if self.is_selected:
            pygame.draw.rect(screen, self.selected_color, self.rect, width=3)


        if self.is_hovered:
            pygame.draw.rect(screen,self.hover_color, self.rect, width=3)



        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def on_click(self):
        if self.callback:
            if self.args is not None:
                self.callback(self.args)
            else:
                self.callback()


class Text:
    def __init__(self, x, y, text, font_size=30, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.color = color

    def draw(self, screen):
        text_surf = self.font.render(self.text, True, self.color)
        screen.blit(text_surf, (self.x, self.y))