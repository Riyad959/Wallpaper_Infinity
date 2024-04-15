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
    
    
# style shaps 
art_styles_list = [
    "Chaotic",
    "Striped Horizontal",
    "Striped Vertical",
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
    