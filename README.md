# Star Collector Game


*(You can replace this placeholder image with a real screenshot of your game)*

A simple 2D game built with Python and the [Arcade library](https://arcade.academy/). The player controls a character and must collect all the stars on the screen to win. This project was created as a step-by-step exercise to learn the basics of the Arcade library.

## Features

-   Player movement using **WASD** and **Arrow Keys**.
-   Randomly spawned collectible items (stars).
-   Collision detection for collecting items.
-   A real-time score counter.
-   A "You Win!" game-over state.
-   Screen boundaries to keep the player within the window.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

-   Python 3.7+
-   `pip` (Python package installer)

### Installation

1.  **Clone the repository or download the `main.py` file.**
    ```sh
    git clone https://github.com/Leontos93/star-game.git
    cd your-project-folder
    ```

2.  **It is highly recommended to create and activate a virtual environment.**
    -   On Windows:
        ```sh
        python -m venv .venv
        .\.venv\Scripts\activate
        ```
    -   On macOS/Linux:
        ```sh
        python3 -m venv .venv
        source .venv/bin/activate
        ```

3.  **Install the required dependencies.**
    ```sh
    pip install arcade
    ```

### How to Run

Once the setup is complete, run the game with the following command:

```sh
python main.py
```

## How to Play

-   Use the **Arrow Keys** or **WASD** keys to move your character around the screen.
-   Fly over the stars to collect them.
-   The game is won when you collect all 50 stars.
