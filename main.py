from graphics import Canvas
import math

# Canvas dimensions
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400

# Flag dimensions
FLAG_WIDTH = CANVAS_WIDTH
FLAG_HEIGHT = CANVAS_HEIGHT

# Colors
SAFFRON_COLOR = "#FF9933"
WHITE_COLOR = "#FFFFFF"
GREEN_COLOR = "#138808"
NAVY_BLUE_COLOR = "#000080"

# Ashoka Chakra
ASHOKA_RADIUS = CANVAS_WIDTH * 0.1
NUM_SPOKES = 24

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Center coordinates of the flag
    flag_center_x = CANVAS_WIDTH // 2
    flag_center_y = CANVAS_HEIGHT // 2

    # Top-left coordinates of the flag
    flag_top_left_x = flag_center_x - FLAG_WIDTH // 2
    flag_top_left_y = flag_center_y - FLAG_HEIGHT // 2

    # Heights of each section
    section_height = FLAG_HEIGHT // 3

    # # border
    # border_thickness = 1
    # canvas.create_rectangle(flag_top_left_x - border_thickness, flag_top_left_y - border_thickness, 
    #                         flag_top_left_x + FLAG_WIDTH + border_thickness, 
    #                         flag_top_left_y + FLAG_HEIGHT + border_thickness, 
    #                         outline="black")

    # saffron section
    canvas.create_rectangle(flag_top_left_x, flag_top_left_y, 
                            flag_top_left_x + FLAG_WIDTH, flag_top_left_y + section_height, 
                            SAFFRON_COLOR)

    # white section
    canvas.create_rectangle(flag_top_left_x, flag_top_left_y + section_height, 
                            flag_top_left_x + FLAG_WIDTH, flag_top_left_y + 2 * section_height, 
                            WHITE_COLOR)

    #green section
    canvas.create_rectangle(flag_top_left_x, flag_top_left_y + 2 * section_height, 
                            flag_top_left_x + FLAG_WIDTH, flag_top_left_y + 3 * section_height, 
                            GREEN_COLOR)

    # Center of the Ashoka Chakra
    chakra_center_x = flag_center_x
    chakra_center_y = flag_top_left_y + section_height + section_height // 2

    # Ashoka Chakra outer circle
    canvas.create_oval(chakra_center_x - ASHOKA_RADIUS, chakra_center_y - ASHOKA_RADIUS, 
                       chakra_center_x + ASHOKA_RADIUS, chakra_center_y + ASHOKA_RADIUS, 
                       color=WHITE_COLOR, outline=NAVY_BLUE_COLOR)

    # spokes of the Ashoka Chakra
    for i in range(NUM_SPOKES):
        angle = (2 * i * math.pi) / NUM_SPOKES
        spoke_x = chakra_center_x + ASHOKA_RADIUS * math.cos(angle)
        spoke_y = chakra_center_y + ASHOKA_RADIUS * math.sin(angle)
        canvas.create_line(chakra_center_x, chakra_center_y, spoke_x, spoke_y, NAVY_BLUE_COLOR)

    #inner circle of the Ashoka Chakra
    inner_radius = ASHOKA_RADIUS * 0.2
    canvas.create_oval(chakra_center_x - inner_radius, chakra_center_y - inner_radius, 
                       chakra_center_x + inner_radius, chakra_center_y + inner_radius, 
                       color=NAVY_BLUE_COLOR, outline=NAVY_BLUE_COLOR)


if __name__ == '__main__':
    main()
