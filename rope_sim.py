import arcade

class Window(arcade.Window):
    def __init__(self):
        super().__init__(800, 500, "Rope Simulation")
        arcade.set_background_color(arcade.color.LIGHT_SLATE_GRAY)
        self.mouse_x = 0
        self.mouse_y = 0

    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(self.mouse_x, self.mouse_y, 3, arcade.color.BLACK)

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.close_window()

class Rope:
    def __init__(self, number_of_points, point_seperation):
        self.points = {} # number : [x pos, y pos, x vel, y vel]
        last_x = 400

        for i in range(number_of_points):
            self.points[i] = [1, last_x, 0, 0]
            last_x -= point_seperation

    def update(self, mouse_x, mouse_y):
        self.point_coords = self.points.keys()
        self.point_velocity = self.points.values()



if __name__ == "__main__":
    window = Window()
    arcade.run()