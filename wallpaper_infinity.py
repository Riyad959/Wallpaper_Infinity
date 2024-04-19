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
ui_manager = pgui.UIManager((SW, SH))
# app name
pg.display.set_caption("Wallpaper_Infinity")
# logo - pore
logo = pg.image.load("assets/Logo.png")
pg.display.set_icon(logo)
# backgroud colr
background_color = pg.Color("#F9F7F7")

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

        available_formats = [("Portable Network Graphics", "*.png")]
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
    
    
    
    # line all
    
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
        
        
        
        
        
        
        
    # square all
    
    def generate_squares(self, complexity, cp, style, layer, magnitude):
        
        
        # chaotic
        if style == art_styles_list[0]:     
            for i in range(complexity*2):
                size = randint(magnitude[0], magnitude[1])
                posX = randint(-size, self.width)
                posY = randint(-size, self.height)
                current_color = cp[randint(0, len(cp)-1)]
                pg.draw.rect(layer, pg.Color(current_color), (posX, posY, size, size))
        
        
        # horizontal
        if style == art_styles_list[1]:     
            row_square_count = complexity // 2 + 2
            point = self.width // (row_square_count - 2)
            row_count = self.height // point + 2
            color_one = cp[randint(0, len(cp) - 1)]
            color_two = cp[randint(0, len(cp) - 1)]
            current_color = color_one
            while color_two == color_one:
                color_two = cp[randint(0, len(cp) - 1)]

            for i in range(row_count):
                if i % 2 == 0:
                    current_color = color_one if current_color == color_two else color_two
                for j in range(row_square_count):
                    posX = j * point
                    posY = i * point
                    size = randint(magnitude[0], magnitude[1])
                    if i % 2 == 0:
                        pg.draw.rect(layer, pg.Color(current_color),(posX, posY, size, size))
        
        
        # vertical
        if style == art_styles_list[2]:     
            row_square_count = complexity // 2 + 2
            point = self.width // (row_square_count - 2)
            row_count = self.height // point + 2
            color_one = cp[randint(0, len(cp) - 1)]
            color_two = cp[randint(0, len(cp) - 1)]
            current_color = color_one
            while color_two == color_one:
                color_two = cp[randint(0, len(cp) - 1)]

            for i in range(row_count):
                for j in range(row_square_count):
                    if j % 1 == 0:
                        current_color = color_one if current_color == color_two else color_two
                    posX = j * point
                    posY = i * point
                    size = randint(magnitude[0], magnitude[1])
                    if j % 2 == 0:
                        pg.draw.rect(layer, pg.Color(current_color), (posX-size//2, posY-size//2, size, size))
        
        
        # mosaic
        if style == art_styles_list[3]:     
            row_square_count = complexity//2 + 2
            size = self.width // (row_square_count-2)
            row_count = self.height // size + 2
            color_one = cp[randint(0, len(cp)-1)]
            color_two = cp[randint(0, len(cp)-1)]
            while color_two == color_one:
                color_two = cp[randint(0, len(cp) - 1)]

            for i in range(row_count):
                for j in range(row_square_count):
                    current_color = color_one if (i + j) % 2 == 0 else color_two
                    posX = j * size
                    posY = i * size
                    pg.draw.rect(layer, pg.Color(current_color), (posX+size//20, posY+size//20, size-size//10, size-size//10))


        # corner
        if style == art_styles_list[4]:     
            for corner in range(4):
                corner_color = cp[randint(0, len(cp)-1)]
                if corner == 0:
                    pg.draw.rect(layer, pg.Color(corner_color), (0, 0, magnitude[1], magnitude[1]))
                if corner == 1:
                    pg.draw.rect(layer, pg.Color(corner_color), (self.width-magnitude[1], 0, magnitude[1], magnitude[1]))
                if corner == 2:
                    pg.draw.rect(layer, pg.Color(corner_color), (self.width-magnitude[1], self.height-magnitude[1], magnitude[1], magnitude[1]))
                if corner == 3:
                    pg.draw.rect(layer, pg.Color(corner_color), (0, self.height-magnitude[1], magnitude[1], magnitude[1]))
            for i in range(complexity*3):
                current_color = cp[randint(0, len(cp)-1)]
                corner = randint(0, 3)
                x_area, y_area = (0, 0), (0, 0)
                if corner == 0:
                    x_area, y_area = (-magnitude[1]//2, self.width//3), (-magnitude[1]//2, self.height//2-magnitude[1])
                if corner == 1:
                    x_area, y_area = (2*self.width//3-magnitude[1], self.width), (-magnitude[1]//2, self.height//2-magnitude[1])
                if corner == 2:
                    x_area, y_area = (2*self.width//3-magnitude[1], self.width), (self.height//2, self.height)
                if corner == 3:
                    x_area, y_area = (-magnitude[1], self.width//3), (self.height//2, self.height)

                posX = randint(x_area[0], x_area[1])
                posY = randint(y_area[0], y_area[1])
                size = randint(magnitude[0], magnitude[1])

                pg.draw.rect(layer, pg.Color(current_color), (posX, posY, size, size))

        
         # center
        if style == art_styles_list[5]:    
            in_x_area, in_y_area = (self.width // 4, 3 * self.width // 4), (self.height // 4, 3 * self.height // 4)
            out_x_area, out_y_area = (self.width // 6, 5 * self.width // 6), (self.height // 6, 5 * self.height // 6)

            for i in range(complexity):
                random_number = randint(0, 5)
                if random_number < 4:
                    center_x = randint(in_x_area[0], in_x_area[1])
                    center_y = randint(in_y_area[0], in_y_area[1])
                else:
                    center_x = randint(out_x_area[0], out_x_area[1])
                    center_y = randint(out_y_area[0], out_y_area[1])

                size = randint(magnitude[0], magnitude[1])
                current_color = cp[randint(0, len(cp) - 1)]

                pg.draw.rect(layer, pg.Color(current_color), (center_x-size//2, center_y-size//2, size, size))
        
        # empty
        if style == art_styles_list[6]:     
            pass
        
   
   
   
   # circle all
        
    def generate_circles(self, complexity, cp, style, layer, magnitude, fill):
        
        
         # chaotic
        if style == art_styles_list[0]:    
            for i in range(complexity):
                rad = randint(magnitude[0], magnitude[1])
                if fill == 1:
                    fill_type = randint(5, rad//2)
                else:
                    fill_type = 0
                centerX = randint(-25, self.width + 25)
                centerY = randint(-25, self.height + 25)
                current_color = cp[randint(0, len(cp) - 1)]
                alpha_surface = pg.Surface((rad*2, rad*2))
                alpha_surface.fill((0, 0, 0))
                pg.draw.circle(alpha_surface, pg.Color(current_color), (rad, rad), rad, fill_type)
                alpha_surface.set_colorkey((0, 0, 0))
                alpha_surface.set_alpha(randint(150, 255))
                layer.blit(alpha_surface, (centerX-rad, centerY-rad))

        
        
        # horizontal
        if style == art_styles_list[1]:     
            row_circle_count = complexity // 2 + 2
            point = self.width // (row_circle_count - 2)
            row_count = self.height // point + 2
            color_one = cp[randint(0, len(cp) - 1)]
            color_two = cp[randint(0, len(cp) - 1)]
            current_color = color_one
            while color_two == color_one:
                color_two = cp[randint(0, len(cp) - 1)]

            for i in range(row_count):
                if i % 2 == 0:
                    current_color = color_one if current_color == color_two else color_two
                for j in range(row_circle_count):
                    posX = j * point
                    posY = i * point
                    rad = randint(magnitude[0], magnitude[1])
                    if fill == 1:
                        fill_type = randint(5, rad // 2)
                    else:
                        fill_type = 0
                    if i % 2 == 0:
                        alpha_surface = pg.Surface((rad * 2, rad * 2))
                        alpha_surface.fill((0, 0, 0))
                        pg.draw.circle(alpha_surface, pg.Color(current_color), (rad, rad), rad, fill_type)
                        alpha_surface.set_colorkey((0, 0, 0))
                        alpha_surface.set_alpha(randint(150, 255))
                        layer.blit(alpha_surface, (posX - rad, posY - rad))

        
        
        # vertical
        if style == art_styles_list[2]:  
            row_circle_count = complexity // 2 + 2
            point = self.width // (row_circle_count - 2)
            row_count = self.height // point + 2
            color_one = cp[randint(0, len(cp) - 1)]
            color_two = cp[randint(0, len(cp) - 1)]
            current_color = color_one
            while color_two == color_one:
                color_two = cp[randint(0, len(cp) - 1)]

            for i in range(row_count):
                for j in range(row_circle_count):
                    if (j+1) % 2 == 0:
                        current_color = color_one if current_color == color_two else color_two
                    posX = j * point
                    posY = i * point
                    rad = randint(magnitude[0], magnitude[1])
                    if fill == 1:
                        fill_type = randint(5, rad // 2)
                    else:
                        fill_type = 0
                    if j % 2 == 0:
                        alpha_surface = pg.Surface((rad * 2, rad * 2))
                        alpha_surface.fill((0, 0, 0))
                        pg.draw.circle(alpha_surface, pg.Color(current_color), (rad, rad), rad, fill_type)
                        alpha_surface.set_colorkey((0, 0, 0))
                        alpha_surface.set_alpha(randint(150, 255))
                        layer.blit(alpha_surface, (posX - rad, posY - rad))

        
        
        # mosaic
        if style == art_styles_list[3]:     
            row_circle_count = complexity
            rad = self.width // row_circle_count
            row_count = self.height // rad + 1
            color_one = cp[randint(0, len(cp) - 1)]
            color_two = cp[randint(0, len(cp) - 1)]
            while color_two == color_one:
                color_two = cp[randint(0, len(cp) - 1)]
            for i in range(row_count):
                for j in range(row_circle_count):
                    if fill == 1:
                        fill_type = rad//4
                    else:
                        fill_type = 0
                    current_color = color_one if (i + j) % 2 == 0 else color_two
                    posX = rad + j * (rad+1) * 2
                    posY = rad + i * (rad+1) * 2
                    pg.draw.circle(layer, pg.Color(current_color), (posX, posY), rad, fill_type)

        
        
        # corner
        if style == art_styles_list[4]:     
            for i in range(complexity*2):
                current_color = cp[randint(0, len(cp)-1)]
                corner = randint(0, 3)
                x_area, y_area = (0, 0), (0, 0)
                if corner == 0:
                    x_area, y_area = (-50, self.width//3), (-50, self.height//3)
                if corner == 1:
                    x_area, y_area = (self.width//1.5, self.width+50), (-50, self.height//3)
                if corner == 2:
                    x_area, y_area = (self.width//1.5, self.width+50), (self.height//1.5, self.height+50)
                if corner == 3:
                    x_area, y_area = (-50, self.width//3), (self.height//1.5, self.height+50)

                posX = randint(x_area[0], x_area[1])
                posY = randint(y_area[0], y_area[1])
                rad = randint(magnitude[0], magnitude[1])

                if fill == 1:
                    fill_type = randint(5, rad//2)
                else:
                    fill_type = 0

                alpha_surface = pg.Surface((rad * 2, rad * 2))
                alpha_surface.fill((0, 0, 0))
                pg.draw.circle(alpha_surface, pg.Color(current_color), (rad, rad), rad, fill_type)
                alpha_surface.set_colorkey((0, 0, 0))
                alpha_surface.set_alpha(randint(150, 255))
                layer.blit(alpha_surface, (posX - rad, posY - rad))

        
        
        # center
        if style == art_styles_list[5]:     
            in_x_area, in_y_area = (self.width//4, 3*self.width//4), (self.height//4, 3*self.height//4)
            out_x_area, out_y_area = (self.width//6, 5*self.width//6), (self.height//6, 5*self.height//6)

            for i in range(complexity):
                if fill == 1:
                    fill_type = randint(magnitude[0], magnitude[1])
                else:
                    fill_type = 0
                random_number = randint(0, 5)
                if random_number < 4:
                    center_x = randint(in_x_area[0], in_x_area[1])
                    center_y = randint(in_y_area[0], in_y_area[1])
                else:
                    center_x = randint(out_x_area[0], out_x_area[1])
                    center_y = randint(out_y_area[0], out_y_area[1])

                rad = randint(magnitude[0], magnitude[1])
                current_color = cp[randint(0, len(cp)-1)]

                if fill == 1:
                    fill_type = randint(5, rad//2)
                else:
                    fill_type = 0

                alpha_surface = pg.Surface((rad * 2, rad * 2))
                alpha_surface.fill((0, 0, 0))
                pg.draw.circle(alpha_surface, pg.Color(current_color), (rad, rad), rad, fill_type)
                alpha_surface.set_colorkey((0, 0, 0))
                alpha_surface.set_alpha(randint(150, 255))
                layer.blit(alpha_surface, (center_x - rad, center_y - rad))

        
        
        # empty
        if style == art_styles_list[6]:    
            pass
        
        
    
    # polygon all
    
    def generate_polygons(self, complexity, cp, style, layer, magnitude, fill):
        
        
        # chaotic
        if style == art_styles_list[0]:     
            for i in range(complexity//2):
                current_color = cp[randint(0, len(cp)-1)]
                if fill == 0:
                    fill_type = 0
                else:
                    fill_type = randint(magnitude[0]//5, magnitude[1]//5)
                points_count = randint(3, 5)
                points = []
                first_point = [randint(0, self.width), randint(0, self.height)]
                for _ in range(points_count):
                    points.append([randint(first_point[0]-magnitude[1]*2, first_point[0]+magnitude[1]*2),
                                   randint(first_point[1]-magnitude[1]*2, first_point[1]+magnitude[1]*2)])

                pg.draw.polygon(layer, pg.Color(current_color), points, fill_type)

        
        
        # horizontal
        
        if style == art_styles_list[1]:     
            row_polygon_count = int(complexity // 2)
            row_count = complexity // 3
            x_interval = self.width // row_polygon_count
            y_interval = self.height // row_count

            color_one = cp[randint(0, len(cp) - 1)]
            color_two = cp[randint(0, len(cp) - 1)]
            while color_two == color_one:
                color_two = cp[randint(0, len(cp) - 1)]
            current_color = color_one
            for i in range(row_count):
                if (i + 1) % 2 == 0:
                    current_color = color_one if current_color == color_two else color_two
                for j in range(row_polygon_count):
                    if fill == 0:
                        fill_type = 0
                    else:
                        fill_type = randint(magnitude[0] // 10, magnitude[1] // 10)

                    x_area = (x_interval * j, x_interval * (j + 1))
                    y_area = (y_interval * i, y_interval * (i + 1))
                    point_count = randint(3, 5)
                    points = []
                    if (i + 1) % 2 == 0:
                        for k in range(point_count):
                            points.append((randint(x_area[0], x_area[1]), randint(y_area[0], y_area[1])))
                        pg.draw.polygon(layer, pg.Color(current_color), points, fill_type)

        
        
        # vertical
        if style == art_styles_list[2]:    
            row_polygon_count = int(complexity // 2)
            row_count = complexity // 3
            x_interval = self.width // row_polygon_count
            y_interval = self.height // row_count

            color_one = cp[randint(0, len(cp) - 1)]
            color_two = cp[randint(0, len(cp) - 1)]
            while color_two == color_one:
                color_two = cp[randint(0, len(cp) - 1)]
            current_color = color_one
            for i in range(row_count):
                for j in range(row_polygon_count):
                    if fill == 0:
                        fill_type = 0
                    else:
                        fill_type = randint(magnitude[0] // 10, magnitude[1] // 10)

                    x_area = (x_interval * j, x_interval * (j + 1))
                    y_area = (y_interval * i, y_interval * (i + 1))
                    point_count = randint(3, 5)
                    points = []
                    if j % 2 == 0:
                        current_color = color_one if current_color == color_two else color_two
                        for k in range(point_count):
                            points.append((randint(x_area[0], x_area[1]), randint(y_area[0], y_area[1])))
                        pg.draw.polygon(layer, pg.Color(current_color), points, fill_type)

        
        
         # mosaic
        if style == art_styles_list[3]:    
            row_polygon_count = int(complexity // 2)
            row_count = complexity // 3
            x_interval = self.width // row_polygon_count
            y_interval = self.height // row_count

            color_one = cp[randint(0, len(cp) - 1)]
            color_two = cp[randint(0, len(cp) - 1)]
            while color_two == color_one:
                color_two = cp[randint(0, len(cp) - 1)]
            for i in range(row_count):
                for j in range(row_polygon_count):
                    if fill == 0:
                        fill_type = 0
                    else:
                        fill_type = randint(magnitude[0] // 10, magnitude[1] // 10)

                    current_color = color_one if (i + j) % 2 == 0 else color_two
                    x_area = (x_interval*j, x_interval*(j+1))
                    y_area = (y_interval*i, y_interval*(i+1))
                    point_count = randint(3, 5)
                    points = []
                    for k in range(point_count):
                        points.append((randint(x_area[0], x_area[1]), randint(y_area[0], y_area[1])))
                    pg.draw.polygon(layer, pg.Color(current_color), points, fill_type)

        
        
        # corner
        if style == art_styles_list[4]:     
            x_areas = [(-100, self.width//3), (2*self.width//3, self.width+100),
                       (2*self.width//3, self.width+100), (-100, self.width//3)]

            y_areas = [(-100, self.height//2-50), (-100, self.height//2-100),
                       (self.height//2+100, self.height+100), (self.height//2+100, self.height+100)]

            point_count = randint(3, 5)
            for i in range(complexity//2):
                corner = randint(0, 3)
                if fill == 0:
                    fill_type = 0
                else:
                    fill_type = randint(magnitude[0] // 10, magnitude[1] // 10)
                current_color = cp[randint(0, len(cp)-1)]
                points = []
                for j in range(point_count):
                    pos = (randint(x_areas[corner][0], x_areas[corner][1]),
                           randint(y_areas[corner][0], y_areas[corner][1]))
                    points.append(pos)

                pg.draw.polygon(layer, pg.Color(current_color), points, fill_type)

        
        
        # center
        if style == art_styles_list[5]:     
            x_inner_area = [self.width // 4, 3 * self.width // 4]
            x_outer_area = [self.width // 6, 5 * self.width // 6]
            y_area = [self.height // 4, 3 * self.height // 4]
            for i in range(complexity // 4):
                if fill == 0:
                    fill_type = 0
                else:
                    fill_type = randint(magnitude[0] // 10, magnitude[1] // 10)

                current_color = cp[randint(0, len(cp)-1)]

                point_count = randint(3, 4)
                points = []
                for j in range(point_count):
                    if randint(0, 6) <= 4:
                        pos = (randint(x_inner_area[0], x_inner_area[1]), randint(y_area[0], y_area[1]))
                    else:
                        pos = (randint(x_outer_area[0], x_outer_area[1]), randint(y_area[0], y_area[1]))

                    points.append(pos)
                pg.draw.polygon(layer, pg.Color(current_color), points, fill_type)

        
        # mmpty
        if style == art_styles_list[6]:     
            pass
        
        
        
        
        
    def generate_bg(self, color):
        self.bg_layer.fill(pg.Color(color))

    def generate_fg(self, overlay):
        self.clean_layer(self.fg_layer)
        self.fg_layer.blit(overlay, (0, 0))
        self.blit_to_canvas()

    def generate_layer_one(self, art_style, art_shape, color_palette, complexity, magnitude):
        self.generate_art(self.layer_one, art_style, art_shape, color_palette, complexity, magnitude)

    def generate_layer_two(self, art_style, art_shape, color_palette, complexity, magnitude):
        self.generate_art(self.layer_two, art_style, art_shape, color_palette, complexity, magnitude)

    def generate_art(self, layer, art_style, art_shape, color_palette, complexity, magnitude):
        self.clean_layer(layer)
        layer.set_colorkey((0, 0, 0))

        if art_shapes_list[0] == art_shape:
            self.generate_lines(complexity, color_palette, art_style, layer, magnitude)

    def blit_to_canvas(self):
        self.canvas.blit(self.bg_layer, (0, 0))
        self.canvas.blit(self.layer_one, (0, 0))
        self.canvas.blit(self.layer_two, (0, 0))
        self.canvas.blit(self.fg_layer, (0, 0))
        self.canvas.convert()
        self.display_canvas = pg.transform.smoothscale(self.canvas, self.display_size)

    def draw(self, window):
        window.blit(self.display_canvas, self.dsPos)


p1 = Palette()
c1 = Canvas((3840, 2160), (int(SW//1.8), int(SH//1.8)))

current_color_palette = p1.get_random_palette()
current_palette_name = p1.get_name_of_palette(current_color_palette)
layer_one_style = "Striped Vertical"
layer_one_shape = "Lines"
layer_two_style = "Cornered"
layer_two_shape = "Rings"
layer_one_complexity = 15
layer_two_complexity = 15
layer_one_magnitude = [50, 400]
layer_two_magnitude = [50, 400]



export_resolution = resolutions_list[0]
def draw_menu(window, color_palette):
    ui_h1_color = pg.Color("#000000")
    ui_color = pg.Color("#000000")

    # Color  back
    pg.draw.rect(window, pg.Color("#FFC7C7"), (18, 410, 252, 95))        
    # Layer 1 back
    pg.draw.rect(window, pg.Color("#FFC7C7"), (18, 195, 252, 190))      
    
    # name
    text_to_screen(window=window, text="Wallpaper  Infinity", color=ui_h1_color, pos=(430, 35), font_size=40)
    
    # color_section
    text_to_screen(window=window, text="COLOR PALETTE", color=ui_h1_color, pos=(60, 425), font_size=18)
    for i, color in enumerate(color_palette):
        pg.draw.rect(window, (0, 0, 0), (60+(i*50), 475, 26, 26))
        pg.draw.rect(window, pg.Color(color), (63+(i*50), 478, 20, 20))
        
    # layer 1 sevtion
    text_to_screen(window=window, text="LAYER ONE STYLE", color=ui_h1_color, pos=(60, 205), font_size=18)
    text_to_screen(window=window, text="LAYER ONE COMPLEXITY", color=ui_color, pos=(60, 290), font_size=14)
    text_to_screen(window=window, text="LAYER ONE SHAPE SIZE", color=ui_color, pos=(60, 340), font_size=14)
   
    # Layer 2 section
    pg.draw.rect(window, pg.Color("#FFC7C7"), (SW-260, 215, 252, 190))
    text_to_screen(window=window, text="LAYER TWO STYLE", color=ui_h1_color, pos=(SW-220, 220), font_size=18)
    text_to_screen(window=window, text="LAYER TWO COMPLEXITY", color=ui_color, pos=(SW-220, 300), font_size=14)
    text_to_screen(window=window, text="LAYER TWO SHAPE SIZE", color=ui_color, pos=(SW-220, 350), font_size=14)
    
    # resulation/output
    text_to_screen(window=window, text="RESOLUTION", color=ui_color, pos=(SW-215, 450), font_size=24)
    


# All button for the proj
def generate_ui():
    ui_manager.clear_and_reset()
    lm = 40     # Left margin

    current_palette_dropdown = pgui.elements.UIDropDownMenu(options_list=p1.get_all_names(),
                                                            starting_option=current_palette_name,
                                                            relative_rect=pg.Rect(lm, 445, 200, 22), manager=ui_manager,
                                                            object_id="current_palette_dropdown")

    layer_one_style_dropdown = pgui.elements.UIDropDownMenu(options_list=art_styles_list,
                                                            starting_option=layer_one_style,
                                                            relative_rect=pg.Rect(lm, 225, 200, 22), manager=ui_manager,
                                                            object_id="layer_one_style_dropdown")

    layer_one_shape_dropdown = pgui.elements.UIDropDownMenu(options_list=art_shapes_list,
                                                            starting_option=layer_one_shape,
                                                            relative_rect=pg.Rect(lm, 255, 200, 22), manager=ui_manager,
                                                            object_id="layer_one_shape_dropdown")

    layer_one_complexity_slider = pgui.elements.UIHorizontalSlider(relative_rect=pg.Rect(lm, 305, 200, 22),
                                                                   start_value=layer_one_complexity,
                                                                   value_range=(10, 30), manager=ui_manager,
                                                                   object_id="layer_one_complexity_slider")

    layer_one_size_slider = pgui.elements.UIHorizontalSlider(relative_rect=pg.Rect(lm, 355, 200, 22),
                                                             start_value=layer_one_magnitude[1], value_range=(50, 400),
                                                             manager=ui_manager, object_id="layer_one_size_slider")

    layer_two_style_dropdown = pgui.elements.UIDropDownMenu(options_list=art_styles_list,
                                                            starting_option=layer_two_style,
                                                            relative_rect=pg.Rect(SW - 200 - lm, 240, 220, 22), manager=ui_manager,
                                                            object_id="layer_two_style_dropdown")

    layer_two_shape_dropdown = pgui.elements.UIDropDownMenu(options_list=art_shapes_list,
                                                            starting_option=layer_two_shape,
                                                            relative_rect=pg.Rect(SW - 200 - lm, 265, 220, 22), manager=ui_manager,
                                                            object_id="layer_two_shape_dropdown")

    layer_two_complexity_slider = pgui.elements.UIHorizontalSlider(relative_rect=pg.Rect(SW - 200 - lm, 320, 220, 22),
                                                                   start_value=layer_two_complexity,
                                                                   value_range=(10, 30), manager=ui_manager,
                                                                   object_id="layer_two_complexity_slider")

    layer_two_size_slider = pgui.elements.UIHorizontalSlider(relative_rect=pg.Rect(SW - 200 - lm, 370, 220, 22),
                                                             start_value=layer_two_magnitude[1], value_range=(50, 400),
                                                             manager=ui_manager, object_id="layer_two_size_slider")
    
    resolution_dropdown = pgui.elements.UIDropDownMenu(options_list=resolutions_list,
                                                       starting_option=export_resolution,
                                                       relative_rect=pg.Rect(SW-240, 485, 200, 22), manager=ui_manager,
                                                       object_id = "resolution_dropdown")
                                                        
    export_art_button = pgui.elements.UIButton(relative_rect=pg.Rect(SW - 240, SH - 100, 200, 50),
                                               text="Export", manager=ui_manager, object_id="export_art_button")

    generate_button = pgui.elements.UIButton(relative_rect=pg.Rect(lm, SH - 100, 200, 50),
                                             text="Generate", manager=ui_manager, object_id="generate_button")

    random_generate_button = pgui.elements.UIButton(relative_rect=pg.Rect(SW // 2 - 400, SH - 100, 200, 50),
                                                    text="Generate Randomly", manager=ui_manager,
                                                    object_id="random_generate_button")

    exit_button = pgui.elements.UIButton(relative_rect=pg.Rect(SW // 2 - 100, SH - 100, 200, 50), 
                                        text="Exit",manager=ui_manager,
                                        object_id="exit_button")

generate_ui()


run = True
while run:
    delta_time = pg.time.Clock().tick(60)/1000.0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            break

      
        if event.type == pg.USEREVENT:
            if event.user_type == pgui.UI_BUTTON_PRESSED:
                if event.ui_object_id == "exit_button":
                    run = False
                    
                if event.ui_object_id == "generate_button":

                    cp = current_color_palette.copy()
                    bg_color = cp[randint(0, len(cp)-1)]
                    c1.generate_bg(bg_color)
                    cp.remove(bg_color)

                    c1.generate_layer_one(art_style=layer_one_style, art_shape=layer_one_shape,
                                          color_palette=cp, complexity=layer_one_complexity,
                                          magnitude=layer_one_magnitude)
                    c1.generate_layer_two(art_style=layer_two_style, art_shape=layer_two_shape,
                                          color_palette=cp, complexity=layer_two_complexity,
                                          magnitude=layer_two_magnitude)

                    c1.blit_to_canvas()
                    
                if event.ui_object_id == "random_generate_button":
                    current_color_palette = p1.get_random_palette()
                    layer_one_style = art_styles_list[randint(0, len(art_styles_list)-1)]
                    layer_one_shape = art_shapes_list[randint(0, len(art_shapes_list)-1)]
                    layer_one_complexity = randint(10, 30)
                    layer_one_magnitude[1] = randint(51, 400)
                    layer_two_style = art_styles_list[randint(0, len(art_styles_list)-1)]
                    layer_two_shape = art_shapes_list[randint(0, len(art_shapes_list)-1)]
                    layer_two_complexity = randint(10, 30)
                    layer_two_magnitude[1] = randint(51, 400)

                    current_palette_name = p1.get_name_of_palette(current_color_palette)
                    generate_ui()

                    cp = current_color_palette.copy()
                    bg_color = cp[randint(0, len(cp) - 1)]
                    c1.generate_bg(bg_color)
                    cp.remove(bg_color)

                    c1.generate_layer_one(art_style=layer_one_style, art_shape=layer_one_shape,
                                          color_palette=cp, complexity=layer_one_complexity,
                                          magnitude=layer_one_magnitude)
                    c1.generate_layer_two(art_style=layer_two_style, art_shape=layer_two_shape,
                                          color_palette=cp, complexity=layer_two_complexity,
                                          magnitude=layer_two_magnitude)

                    c1.blit_to_canvas()

               
                if event.ui_object_id == "export_art_button":
                    path = c1.export_art()
                    if path:
                        if export_resolution == resolutions_list[0]:
                            pg.image.save(c1.canvas, path + ".png")
                        elif export_resolution == resolutions_list[1]:
                            pg.image.save(pg.transform.smoothscale(c1.canvas, (1920, 1080)), path + ".png")
                        elif export_resolution == resolutions_list[2]:
                            pg.image.save(pg.transform.smoothscale(c1.canvas, (1280, 720)), path + ".png")
                    else:
                        pass
                    
                
            if event.user_type == pgui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_object_id == "resolution_dropdown":
                    export_resolution = event.text
                if event.ui_object_id == "current_palette_dropdown":
                    current_color_palette = p1.get_colors_from_palette(event.text)
                if event.ui_object_id == "layer_one_style_dropdown":
                    layer_one_style = event.text
                if event.ui_object_id == "layer_one_shape_dropdown":
                    layer_one_shape = event.text
                if event.ui_object_id == "layer_two_style_dropdown":
                    layer_two_style = event.text
                if event.ui_object_id == "layer_two_shape_dropdown":
                    layer_two_shape = event.text

            if event.user_type == pgui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_object_id == "layer_one_complexity_slider":
                    layer_one_complexity = event.value
                if event.ui_object_id == "layer_one_size_slider":
                    layer_one_magnitude[1] = event.value
                if event.ui_object_id == "layer_two_complexity_slider":
                    layer_two_complexity = event.value
                if event.ui_object_id == "layer_two_size_slider":
                    layer_two_magnitude[1] = event.value

        ui_manager.process_events(event)

    ui_manager.update(delta_time)
    window.fill(background_color)
    c1.draw(window)
    draw_menu(window, current_color_palette)
    ui_manager.draw_ui(window)
    pg.display.update()

pg.quit()