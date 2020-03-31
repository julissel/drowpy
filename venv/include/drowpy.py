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


def draw_background(window):
    earth = gr.Rectangle(gr.Point(0, window.height // 2),
                         gr.Point(window.width - 1, window.height - 1))
    earth.setFill("green")
    earth.draw(window)
    scy = gr.Rectangle(gr.Point(0, 0),
                       gr.Point(window.width - 1, window.height // 2))
    scy.setFill("cyan")
    scy.draw(window)


def draw_house(window, x, y, width, height):
    pass  # TODO


if __name__ == "__main__":
    main()