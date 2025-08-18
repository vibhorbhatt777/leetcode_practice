import tkinter  # gra[hical interfce library]
import random  # random number generator


ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * ROWS
WINDOW_HEIGHT = TILE_SIZE * COLS

# lets make a tile class to represent each tile in the game to string the x, y position
class Tile:
    def __init__(self,x,y):
        self.x = x
        self.y = y


# LET'S CRETAE GAME WINDOW
window = tkinter.Tk()
window.title("Snake Game")
window.resizable(False,False)

# let's create a canvas to draw the game
canvas = tkinter.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black",borderwidth=0,highlightthickness=0)
canvas.pack()
window.update()

# give window te centre location
window_width = window.winfo_width()
window_height = window.winfo_height()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height /2))

window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{window_x}+{window_y}")


# lets initliaze the game
snake  = Tile(5*TILE_SIZE,5*TILE_SIZE)  # snake starts at position (5,5 in grid)
food = Tile(10*TILE_SIZE , 10*TILE_SIZE)  # food at random position  
snake_body = []  # list to store the body of the snake
# let's create the food at a random position
#   
velocityX = 0 
velocityY = 0
gameOver = False  # flag to check if game is over


def change_direction(e): # e stands for event
    global velocityX , velocityY , gameOver
    # print(e.keysym) #print the key pressed 
    if(gameOver):
        return
    if(e.keysym == "Up" and velocityY != 1):  # prevent snake from going back on itself 
        velocityX = 0
        velocityY = -1
    elif(e.keysym == "Down" and velocityY != -1):
        velocityX = 0
        velocityY = 1
    elif(e.keysym == "Left" and velocityX != 1):
        velocityX = -1
        velocityY = 0
    elif(e.keysym == "Right" and velocityX != -1):
        velocityX = 1
        velocityY = 0

def move_snake():
    global snake , food,snake_body, gameOver

    if(gameOver):
        return
    if(snake.x < 0 or snake.x>= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT):
        gameOver = True
        # canvas.create_text(WINDOW_WIDTH//2, WINDOW_HEIGHT//2, text="Game Over", fill="white", font=("Arial", 24))
        return
    
    for tile in snake_body:
        if(snake.x == tile.x and snake.y == tile.y):
            game_over = True
            return

    #collision
    if (snake.x == food.x and snake.y == food.y):
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, COLS - 1) * TILE_SIZE
        food.y = random.randint(0, ROWS - 1) * TILE_SIZE

    #updtae the snake body
    for i in range(len(snake_body) - 1, 0, -1):
        tile = snake_body[i]
        if(i==0):
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[i - 1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y




    # move the snake in the direction of velocity
    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE
    # check if snake is out of bounds


def draw_snake():
    global snake
    move_snake()
    canvas.delete("all")  # clear the canvas
    canvas.create_rectangle(food.x,food.y,food.x + TILE_SIZE, food.y + TILE_SIZE , fill="red")

    #draw snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill="lime green", outline="")
    # canvas.create_rectangle(food.x,food.y,food.x + TILE_SIZE, food.y + TILE_SIZE , fill="red")
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill="lime green", outline="")
    window.after(100,draw_snake)  # redraw snake every 100 milliseconds 

draw_snake()  # call the function to draw the snake 



window.bind("<KeyPress>", change_direction)
window.mainloop()


