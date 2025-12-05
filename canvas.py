import pygame
from settings import *

class Canvas:
    def __init__(self, settings:Settings):
        self.x = 50
        self.y = 50
        self.settings = settings

        self.windows_size = 600
        while True:
            try:
                self.size = int(input("Size of matrix from 10 to 50 - "))
                if self.size >= 10 and self.size <= 50:
                    break
            except:
                print("try again please")

        self.canvas: list[list] = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.block_size = self.windows_size // self.size


    def draw(self,screen):
        pygame.draw.rect(screen, Colors.BLACK, (self.x,self.y, self.windows_size, self.windows_size))

        for y,row in enumerate(self.canvas):
            for x, el in enumerate(row):
                pygame.draw.rect(screen, Colors.get_color(self.canvas[y][x]), (x*self.block_size + self.x, y*self.block_size+self.y, self.block_size, self.block_size))



    def update(self,screen):
        mx, my = pygame.mouse.get_pos()


        rel_x = mx - self.x
        rel_y = my - self.y


        if 0 <= rel_x < self.windows_size and 0 <= rel_y < self.windows_size:
            cx = int(rel_x // self.block_size)
            cy = int(rel_y // self.block_size)
            pygame.draw.rect(screen, Colors.DARK_GRAY, (cx*self.block_size + self.x,cy * self.block_size + self.y , self.block_size, self.block_size ))

            pressed = pygame.mouse.get_pressed()[0]

            if pressed and self.settings.METHOD == StateMent.PENCIL:
                print(self.settings.selected_color)
                self.canvas[cy][cx] = self.settings.selected_color
                print(self.canvas)

            elif pressed and self.settings.METHOD == StateMent.BUCKET:
                target_color = self.canvas[cy][cx]
                replacement_color = self.settings.selected_color
                self.flood_fill(cx, cy, target_color, replacement_color)

    def flood_fill(self, cx, cy, target_color, replacement_color):
        if target_color == replacement_color:
            return

        if self.canvas[cy][cx] != target_color:
            return

        stack = [(cx, cy)]

        while stack:
            x, y = stack.pop()
            if self.canvas[y][x] == target_color:
                self.canvas[y][x] = replacement_color

                # Перевіряємо суміжні клітинки
                if x > 0:
                    stack.append((x - 1, y))
                if x < self.size - 1:
                    stack.append((x + 1, y))
                if y > 0:
                    stack.append((x, y - 1))
                if y < self.size - 1:
                    stack.append((x, y + 1))

