import graphics as gr


def main():
    window = gr.GraphWin("My Image", 600, 600)
    draw_image(window)
    window.getMouse()

def draw_image(window):
    house_x, house_y = window.width // 2, window.height * 2 // 3
    house_width = window.width // 3
    house_height = house_width * 4 // 3

    draw_background(window)
    draw_house(window, house_x, house_y, house_width, house_height)

def draw_background(widow):
    pass  # TODO

def draw_house(window, house_x, house_y, house_width, house_height):
    pass  # TODO

if __name__ == "__main__":
    main()