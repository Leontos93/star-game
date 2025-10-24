import arcade
import random

# --- Constants ---
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Star Collection"
PLAYER_MOVEMENT_SPEED = 5
STAR_COUNT = 50


class MyGame(arcade.Window):
    """Main application class."""

    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE

        # Initialize attributes that will be created in the setup method
        self.player_list = None
        self.player_sprite = None
        self.star_list = None

        self.score = 0
        self.game_over = False

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.game_over = False
        self.score = 0

        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()

        # Create the player
        self.player_sprite = arcade.Sprite(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        )
        self.player_sprite.center_x = WINDOW_WIDTH / 2
        self.player_sprite.center_y = WINDOW_HEIGHT / 2
        self.player_list.append(self.player_sprite)

        # Create the stars
        for _ in range(STAR_COUNT):
            star = arcade.Sprite(":resources:images/items/star.png", 0.3)
            star.center_x = random.randrange(WINDOW_WIDTH)
            star.center_y = random.randrange(WINDOW_HEIGHT)
            self.star_list.append(star)

    def on_draw(self):
        """Render the screen."""
        self.clear()

        # Draw all our sprites
        self.star_list.draw()
        self.player_list.draw()

        # Draw the score
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10, 10, arcade.csscolor.WHITE, 18)

        # Draw the 'You Win' screen if the game is over
        if self.game_over:
            arcade.draw_text(
                "YOU WIN!",
                WINDOW_WIDTH / 2,
                WINDOW_HEIGHT / 2,
                arcade.csscolor.WHITE,
                font_size=50,
                anchor_x="center",
            )

    def on_update(self, delta_time):
        """All the game logic."""
        # If the game is over, don't update anything
        if self.game_over:
            return

        # Update sprites (this moves the player)
        self.player_list.update()

        # Check if the player has gone off-screen
        # Left boundary
        if self.player_sprite.left < 0:
            self.player_sprite.left = 0
        # Right boundary
        elif self.player_sprite.right > WINDOW_WIDTH:
            self.player_sprite.right = WINDOW_WIDTH

        # Bottom boundary
        if self.player_sprite.bottom < 0:
            self.player_sprite.bottom = 0
        # Top boundary
        elif self.player_sprite.top > WINDOW_HEIGHT:
            self.player_sprite.top = WINDOW_HEIGHT

        # Check for player-star collisions
        star_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.star_list
        )

        # Process each collision
        for star in star_hit_list:
            star.remove_from_sprite_lists()
            self.score += 1

        # Check for the win condition
        if not self.star_list:
            self.game_over = True

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if self.game_over:
            return

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""
        if self.game_over:
            return

        if (
            key == arcade.key.UP
            or key == arcade.key.W
            or key == arcade.key.DOWN
            or key == arcade.key.S
        ):
            self.player_sprite.change_y = 0

        if (
            key == arcade.key.LEFT
            or key == arcade.key.A
            or key == arcade.key.RIGHT
            or key == arcade.key.D
        ):
            self.player_sprite.change_x = 0


def main():
    """Main function to run the game."""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
