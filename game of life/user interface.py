from game_of_life import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import logging

# Initialize logging
logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


# GUI Update Function
def update(frameNum, img, grid_obj, num_rounds, previous_states):
    # Check if we have reached the desired number of rounds
    if frameNum == num_rounds:
        logging.info("Reached the end of simulation.")
        print("Reached the end of simulation.")
        ani.event_source.stop()
        return img,

    # Hash the state to detect loops
    state_hash = grid_obj.get_state_hash()
    if state_hash in previous_states:
        logging.info("Loop detected! Stopping simulation.")
        print("Loop detected! Stopping simulation.")
        ani.event_source.stop()
        return img,
    previous_states.add(state_hash)

    # Update the grid for the next frame
    grid_obj.update()
    img.set_data(grid_obj.array)
    return img,


# GUI Main Function
def run_gui(grid_obj, num_rounds):
    fig, ax = plt.subplots()
    img = ax.imshow(grid_obj.array, interpolation='nearest', cmap='viridis')
    previous_states = set()  # To keep track of previous states for loop detection

    global ani  # Reference the global animation instance
    ani = animation.FuncAnimation(
        fig,
        update,
        fargs=(img, grid_obj, num_rounds, previous_states),
        frames=num_rounds,  # Stop after 'num_rounds' rounds
        interval=200,
        repeat=False  # Do not repeat the animation
    )

    plt.axis('off')
    plt.show()


# Main Entry Point
def main():
    logging.info("Game of Life started.")
    size = 8  # Define the grid size
    grid_obj = Grid(size)

    # Get user input for initial configuration and the number of rounds to simulate
    num_rounds = get_user_params(grid_obj)

    # Run the GUI version of the game
    run_gui(grid_obj, num_rounds)


if __name__ == "__main__":
    main()