import pygame

class Button:
    def __init__(self, x, y, width, height, color, text, font_size, text_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.font_size = font_size
        self.text_color = text_color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.Font(None, self.font_size)
        text = font.render(self.text, 1, self.text_color)
        textpos = text.get_rect(centerx=self.x+(self.width/2), centery=self.y+(self.height/2))
        surface.blit(text, textpos)

    def is_clicked(self, mouse_pos):
        if self.x < mouse_pos[0] < self.x + self.width and self.y < mouse_pos[1] < self.y + self.height:
            return True
        else:
            return False


class ButtonManager:
    def __init__(self, screen_width, screen_height):
        self.buttons = []
        self.screen_width = screen_width
        self.screen_height = screen_height

    def draw(self, surface):
        for button in self.buttons:
            button.draw(surface)    

    def get_clicked(self, mouse_pos):
        for button in self.buttons:
            if button.is_clicked(mouse_pos):
                return button

        return None
    
    def add_button(self, percentageX, percentageY, width, height, color, text, font_size, text_color):
        x = int(self.screen_width * percentageX / 100)
        y = int(self.screen_height * percentageY / 100)
        button = Button(x, y, width, height, color, text, font_size, text_color)
        self.buttons.append(button)
