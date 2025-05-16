import arcade

class Window(arcade.Window):
    def __init__(self):
        super().__init__(800, 500, "Rope Simulation")
        arcade.set_background_color(arcade.color.LIGHT_SLATE_GRAY)
        self.mouse_x = 0
        self.mouse_y = 0
        self.rope = Rope(10, 4, self)

    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(self.mouse_x, self.mouse_y, 3, arcade.color.BLACK)
        self.rope.update()

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.close_window()

class Rope:
    def __init__(self, number_of_points, point_seperation, window_obj):
        self.points = {} # number : [x pos, y pos, x vel, y vel]
        self.number_of_points = number_of_points
        self.max_dist = point_seperation * 2
        self.min_dist = round(point_seperation / 4, 0)
        self.window_obj = window_obj
        self.mouse_x = 0
        self.mouse_y = 0

        last_x = 400
        for i in range(number_of_points):
            self.points[i] = [1, last_x, 0, 0]
            last_x -= point_seperation

    def update(self, drawing = True):
        self.mouse_x = self.window_obj.mouse_x
        self.mouse_y = self.window_obj.mouse_y

        self.points[0] = [self.mouse_x, self.mouse_y, 0, 0]

        for i in reversed(range(1, self.number_of_points)):
            self.x_diff = self.points[i][0] - self.points[i-1][0]
            self.y_diff = self.points[i][1] - self.points[i-1][1]

            self.points[i][1] -= 2 # Gravity

            if self.x_diff != 0:
                self.shift = 1 if self.x_diff > 0 else -1
                self.points[i][0] += self.shift * (abs(self.x_diff) - self.max_dist) / 2

            if self.y_diff < 0:
                self.shift = 1
                self.points[i][1] += self.shift * (abs(self.y_diff) - self.max_dist) / 2

            if drawing and not i == self.number_of_points - 1:
                arcade.draw_line(self.points[i][0], self.points[i][1], self.points[i-1][0], self.points[i-1][1], arcade.color.BLACK, 2)
                arcade.draw_circle_filled(self.points[i][0], self.points[i][1], 2, arcade.color.BLACK)

if __name__ == "__main__":
    window = Window()
    arcade.run()