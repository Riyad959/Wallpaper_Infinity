from color_palettes import Palette

from random import randint
import pygame as pg
import pygame.gfxdraw
import pygame.freetype
import pygame_gui as pgui
from tkinter import *
from tkinter.filedialog import asksaveasfilename

pg.init()
pg.freetype.init()

SW,SH = 1280,720
window= pg.display.set_mode((SW,SH))
# app name
pg.display.set_caption("Wallpaper_Infinity")
# logo - pore
logo = pg.image.load("assets/Logo.png")
pg.display.set_icon(logo)
# backgroud colr
background_color = pg.Color("#91e7eb")

# font design
xs_font = pg.freetype.Font("Poppins-Regular.ttf", 12)
small_font = pg.freetype.Font("Poppins-Regular.ttf", 14)
medium_font = pg.freetype.Font("Poppins-Regular.ttf", 18)
large_font = pg.freetype.Font("Poppins-Regular.ttf", 24)
xl_font = pg.freetype.Font("Poppins-Regular.ttf", 30)
xxl_font = pg.freetype.Font("Poppins-Regular.ttf", 40)

fonts = [xs_font, small_font, medium_font, large_font, xl_font, xxl_font]
font_sizes = [12, 14, 18, 24, 30, 40]

def text_to_screen(window, text, color, pos, font_size):
    font_used = fonts[font_sizes.index(font_size)]
    font_used.render_to(window, pos, text, color)
    
    
# style shaps (*change of plan| using 1,2,3,4)
art_styles_list = [
    "Chaotic",
    "Horizontal",
    "Vertical",
    "Mosaic",
    "Cornered",
    "Centered",
    "Empty"
]

art_shapes_list = [
    "Lines",
    "Circles",
    "Squares",
    "Hollow Polygons",
    "Filled Polygons",
    "Dots",
    "Curves",
    "Rings"
]

resolutions_list = [
    "4K: 3840x2160",
    "Full HD: 1920x1080",
    "HD: 1280x720"
]


# main page (idea1- one page, idea2- two page->main & download)
class Canvas:
    def __init__(self, size, display_size):
        self.width = size[0]
        self.height = size[1]
        self.display_size = display_size
        self.sPos = ((SW - self.width) // 2, (SH - self.height) // 2)
        self.dsPos = ((SW - self.display_size[0])//2 + 10, (SH-self.display_size[1])//2)
        self.canvas = pg.Surface((self.width, self.height))
        self.canvas.fill((255, 255, 255))
        self.display_canvas = pg.Surface(self.display_size)

        self.bg_layer = pg.Surface((self.width, self.height))
        self.bg_layer.fill((255, 255, 255))
        self.layer_one = pg.Surface((self.width, self.height), pg.SRCALPHA)
        self.layer_two = pg.Surface((self.width, self.height), pg.SRCALPHA)
        self.fg_layer = pg.Surface((self.width, self.height), pg.SRCALPHA)

    def export_art(self):
        tkinter_window = Tk()
        tkinter_window.withdraw()

        available_formats = [("some name", "*.png")]
        filename = asksaveasfilename(title="Export File", filetypes=available_formats)

        if filename:
            name = filename[:]
            return name
        
    # layar idea (idea1- add 2 layer for eatch, idea2- add saparate and marge them)
    def clean_all_layers(self):
        self.layer_one.fill((0, 0, 0, 0))
        self.layer_two.fill((0, 0, 0, 0))

    def clean_layer(self, layer):
        layer.fill((0, 0, 0, 0))
        
        
    # Shapes (idea- line,square,circle,polygon,sin or cos curv,dot)
    # style for eatch shaps will be here
    
    def generate_lines(self, complexity, cp, style, layer, magnitude):
        
        # Chaotic
        if style == art_styles_list[0]:     
            for i in range(complexity):
                posX = (randint(-200, self.width+200), randint(0, self.width))
                posY = (randint(-200, self.height+200), randint(0, self.height))
                current_color = cp[randint(0, len(cp) - 1)]
                size = randint(magnitude[0], magnitude[1])
                pg.draw.line(layer, pg.Color(current_color), (posX[0], posY[0]), (posX[1], posY[1]), size//4)
        
         # horizontal
        elif style == art_styles_list[1]:  
            interval = self.height // complexity
            for i in range(complexity):
                posX = 0, self.width
                posY = i * interval + randint(0, self.height//10), i * interval + randint(0, self.height//10)
                current_color = cp[randint(0, len(cp) - 1)]
                size = randint(magnitude[0], magnitude[1])
                pg.draw.line(layer, pg.Color(current_color), (posX[0], posY[0]), (posX[1], posY[1]), size // 4)
        
        # vertical
        elif style == art_styles_list[2]:
            interval = self.width // complexity
            for i in range(complexity):
                posY = 0, self.height
                posX = i * interval + randint(0, self.width//10), i * interval + randint(0, self.width//10)
                current_color = cp[randint(0, len(cp) - 1)]
                size = randint(magnitude[0], magnitude[1])
                pg.draw.line(layer, pg.Color(current_color), (posX[0], posY[0]), (posX[1], posY[1]), size // 4)
        
        # mosaic
        elif style == art_styles_list[3]:   
            row_line_count = complexity // 3 + 1
            row_count = complexity // 4 + 1
            x_interval = self.width // (row_line_count - 1)
            y_interval = self.height // (row_count - 1)
            color_one = cp[randint(0, len(cp) - 1)]
            color_two = cp[randint(0, len(cp) - 1)]
            while color_two == color_one:
                color_two = cp[randint(0, len(cp) - 1)]
            for i in range(row_count):
                for j in range(row_line_count):
                    current_color = color_one if (i+j) % 2 == 0 else color_two
                    size = randint(magnitude[0], magnitude[1]) // 4
                    posX = ((x_interval*j), (x_interval*(j+1)))
                    posY_u = ((y_interval*i), (y_interval*(i+1)))
                    posY_d = ((y_interval*(i+1)), (y_interval*i))
                    if randint(0,1) == 0:
                        pg.draw.line(layer, pg.Color(current_color), (posX[0], posY_u[0]), (posX[1], posY_u[1]), size)
                    else:
                        pg.draw.line(layer, pg.Color(current_color), (posX[0], posY_d[0]), (posX[1], posY_d[1]), size)

        # corner
        elif style == art_styles_list[4]:   
            for i in range(complexity*2):
                current_color = cp[randint(0, len(cp) - 1)]
                size = randint(magnitude[0], magnitude[1]) // 4
                corner = randint(0, 3)
                first_x_area, second_x_area = 0, 0
                first_y_area, second_y_area = 0, 0
                if corner == 0:
                    first_x_area, second_x_area = (-50, 100), (0, self.width//2)
                    first_y_area, second_y_area = (-50, 100), (0, self.height//2)
                elif corner == 1:
                    first_x_area, second_x_area = (self.width-100, self.width+50), (self.width//2, self.width)
                    first_y_area, second_y_area = (-50, 100), (0, self.height // 2)
                elif corner == 2:
                    first_x_area, second_x_area = (self.width-100, self.width+50), (self.width//2, self.width)
                    first_y_area, second_y_area = (self.height-100, self.height+50), (self.height//2, self.height)
                elif corner == 3:
                    first_x_area, second_x_area = (-50, 100), (0, self.width // 2)
                    first_y_area, second_y_area = (self.height-100, self.height+50), (self.height//2, self.height)

                posX = (randint(first_x_area[0], first_x_area[1]), randint(second_x_area[0], second_x_area[1]))
                posY = (randint(first_y_area[0], first_y_area[1]), randint(second_y_area[0], second_y_area[1]))

                pg.draw.line(layer, pg.Color(current_color), (posX[0], posY[0]), (posX[1], posY[1]), size)
        
        # center
        elif style == art_styles_list[5]:   
            for i in range(complexity//2):
                current_color = cp[randint(0, len(cp)-1)]
                posX = (randint(2*self.width//5, 3*self.width//5), randint(0, self.width))
                posY = (randint(2*self.height//5, 3*self.height//5), randint(0, self.height))
                size = randint(magnitude[0], magnitude[1]) // 4
                pg.draw.line(layer, pg.Color(current_color), (posX[0], posY[0]), (posX[1], posY[1]), size)
        
        # Empty
        elif style == art_styles_list[6]:
            pass