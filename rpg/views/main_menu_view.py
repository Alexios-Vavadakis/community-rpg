"""
Main Menu
"""
import arcade
import arcade.gui
from rpg.views import *

# For now it does not do anything
class SettingsButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        pass

class MainMenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.started = False
        # We create the buttons here
        self.createButtons()
        arcade.set_background_color(arcade.color.ALMOND)

    def createButtons(self):
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.v_box = arcade.gui.UIBoxLayout()

        # Start Button
        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))

        #It starts a new game
        @start_button.event("on_click")
        def on_click_start(event):
            self.window.views["main_menu"] = MainMenuView()
            self.window.views["main_menu"].setup()
            current_view = LoadingView()
            current_view.setup()
            self.window.show_view(current_view)

        # Settings Button
        settings_button = SettingsButton(text="Settings", width=200)
        self.v_box.add(settings_button.with_space_around(bottom=20))

        # Quit Button
        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)
        self.v_box.add(quit_button.with_space_around(bottom=20))

        # It closes the game
        @quit_button.event("on_click")
        def on_click_quit(event):
            arcade.exit()


        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_draw(self):
        arcade.start_render()
        # Some simple text to welcome the player
        arcade.draw_text(
            "Welcome to the Python Arcade "
            "Community RPG Game!",
            self.window.width / 2,
            self.window.height - 200,
            arcade.color.ALLOY_ORANGE,
            font_size=30,
            anchor_x="center",
            anchor_y="center",
            align="center",
            width=self.window.width,
        )
        self.manager.draw()

    def setup(self):
        pass

    def on_show_view(self):
        arcade.set_background_color(arcade.color.ALMOND)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self.window.show_view(self.window.views["game"])
