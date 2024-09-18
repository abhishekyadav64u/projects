import matplotlib.pyplot as plt
import random

# Define Rectangle class to store dimensions and position
class Rectangle:
    def __init__(self, width, height, x=0, y=0, rotated=False):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rotated = rotated

    def rotate(self):
        self.width, self.height = self.height, self.width
        self.rotated = not self.rotated

# Function to plot the rectangles
def plot_rectangles(rectangles, space_width, space_height):
    fig, ax = plt.subplots()
    ax.set_xlim(0, space_width)
    ax.set_ylim(0, space_height)
    
    for rect in rectangles:
        rect_x, rect_y = rect.x, rect.y
        rect_width, rect_height = rect.width, rect.height
        ax.add_patch(plt.Rectangle((rect_x, rect_y), rect_width, rect_height, edgecolor='blue', facecolor='none', lw=2))
        ax.text(rect_x + rect_width/2, rect_y + rect_height/2, f"{rect.width}x{rect.height}{'R' if rect.rotated else ''}",
                color="red", fontsize=8, ha='center', va='center')
    
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()

# Function to place the rectangle using recursive partitioning
def place_rectangle(space_x, space_y, space_width, space_height, rectangles, placed_rectangles):
    if not rectangles:
        return True

    rect = rectangles.pop(0)
    
    # Try placing the rectangle in current space
    if rect.width + 1 <= space_width and rect.height + 1 <= space_height:
        rect.x, rect.y = space_x, space_y
        placed_rectangles.append(rect)
        
        # Recursively split the remaining space
        remaining_width = space_width - (rect.width + 1)
        remaining_height = space_height - (rect.height + 1)
        
        if remaining_width > remaining_height:
            # Split the space horizontally
            if place_rectangle(space_x + rect.width + 1, space_y, remaining_width, space_height, rectangles, placed_rectangles):
                return True
            if place_rectangle(space_x, space_y + rect.height + 1, space_width, remaining_height, rectangles, placed_rectangles):
                return True
        else:
            # Split the space vertically
            if place_rectangle(space_x, space_y + rect.height + 1, space_width, remaining_height, rectangles, placed_rectangles):
                return True
            if place_rectangle(space_x + rect.width + 1, space_y, remaining_width, space_height, rectangles, placed_rectangles):
                return True

    # Try rotating the rectangle and place it
    rect.rotate()
    if rect.width + 1 <= space_width and rect.height + 1 <= space_height:
        rect.x, rect.y = space_x, space_y
        placed_rectangles.append(rect)
        
        # Recursively split the remaining space
        remaining_width = space_width - (rect.width + 1)
        remaining_height = space_height - (rect.height + 1)
        
        if remaining_width > remaining_height:
            # Split the space horizontally
            if place_rectangle(space_x + rect.width + 1, space_y, remaining_width, space_height, rectangles, placed_rectangles):
                return True
            if place_rectangle(space_x, space_y + rect.height + 1, space_width, remaining_height, rectangles, placed_rectangles):
                return True
        else:
            # Split the space vertically
            if place_rectangle(space_x, space_y + rect.height + 1, space_width, remaining_height, rectangles, placed_rectangles):
                return True
            if place_rectangle(space_x + rect.width + 1, space_y, remaining_width, space_height, rectangles, placed_rectangles):
                return True

    # If placement fails, return False
    rectangles.insert(0, rect)  # Re-insert the rectangle to try a different placement
    return False

# Main function
def main():
    space_width, space_height = 100, 100

    # Generate five random rectangles with widths and heights between 5 and 30 units
    rectangles = [Rectangle(random.randint(5, 30), random.randint(5, 30)) for _ in range(5)]
    
    placed_rectangles = []
    if not place_rectangle(0, 0, space_width, space_height, rectangles, placed_rectangles):
        raise ValueError("Placement not possible within the given space.")

    # Plot the placed rectangles
    plot_rectangles(placed_rectangles, space_width, space_height)

if __name__ == "__main__":
    main()