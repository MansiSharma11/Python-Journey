from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        # 1. Use random.choice once to get a random move
        move = random.choice(self.moves)
        
        # 2. Add x and y coordinates individually to update position
        new_x = self.position[0] + move[0]
        new_y = self.position[1] + move[1]
        self.position = (new_x, new_y)
        
        # 3. Append the new position tuple to the path attribute
        self.path.append(self.position)
        
        # 4. Return the updated position
        return self.position

    @abstractmethod
    def level_up(self):
        pass


class Pawn(Player):
    def __init__(self):
        # 1. Call parent's __init__ using super()
        super().__init__()
        
        # 2. Set moves to 1 unit movements: up (0, 1), down (0, -1), left (-1, 0), right (1, 0)
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def level_up(self):
        # Add the four diagonal movements of 1 unit to the moves list
        diagonal_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.moves.extend(diagonal_moves)
# --- TEST EXECUTION BLOCK (Safe to add at the bottom) ---
if __name__ == "__main__":
    print("--- Initializing Pawn ---")
    pawn = Pawn()
    print(f"Starting Position: {pawn.position}")
    print(f"Starting Moves:    {pawn.moves}")
    print(f"Starting Path:     {pawn.path}")

    print("\n--- Making 3 Random Moves ---")
    for i in range(1, 4):
        next_pos = pawn.make_move()
        print(f"Move {i}: Selected random step -> New Position: {next_pos}")

    print(f"Path History: {pawn.path}")

    print("\n--- Leveling Up Pawn ---")
    pawn.level_up()
    print(f"Upgraded Moves (With Diagonals): {pawn.moves}")

    print("\n--- Making 1 Diagonal-Capable Move ---")
    final_pos = pawn.make_move()
    print(f"Final Position: {final_pos}")
    print(f"Final Path:     {pawn.path}")
