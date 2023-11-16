class game_of_life:
    def gameOfLife(self, board: List[List[int]]) -> None:
        
        # Neighbors array to find 8 neighboring cells for a given cell
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        rows = len(board)
        cols = len(board[0])

        # Create a copy of the original board
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

        # Iterate through board cell by cell.
        for row in range(rows):
            for col in range(cols):

                # For each cell count the number of live neighbors.
                live_neighbors = 0
                for neighbor in neighbors:

                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    # Check the validity of the neighboring cell and if it was originally a live cell.
                    # The evaluation is done against the copy, since that is never updated.
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and (copy_board[r][c] == 1):
                        live_neighbors += 1

                # Rule 1 or Rule 3        
                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                # Rule 4
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1

# main.py
from flask import Flask, render_template, jsonify, request
from typing import List

app = Flask(__name__)

class GameOfLife:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # Your existing Game of Life logic

# Create an instance of the GameOfLife class
game = GameOfLife()

# Flask routes
@app.route('/')
def index():
    return render_template('frontend.html')

@app.route('/update_board', methods=['POST'])
def update_board():
    global game  # Use the same instance of GameOfLife throughout the application

    # Extract the board from the request data
    board = request.json['board']

    # Update the board using the GameOfLife logic
    game.gameOfLife(board)

    # Return the updated board to the frontend
    return jsonify(board)

if __name__ == '__main__':
    app.run(debug=True)

