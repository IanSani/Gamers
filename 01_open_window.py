
"""
FLappy birds kinda Game
"""

import arcade

#constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Captain Haiji"


class MyGame(arcade.Window):
    """
    The main application class
    """
    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.AMAZON)

    def setUp(self):
        """
        Set up the game here. Call this function to restart the game.
        """
        pass

    def on_draw(self):
        """
        Render the SCREEN
        """

        arcade.start_render()
        #Code to draw the screen starts here def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass



def main():
    """
    Main method
    """
    window =MyGame()
    window.setUp()
    arcade.run()

if __name__ == "__main__":
    main()

