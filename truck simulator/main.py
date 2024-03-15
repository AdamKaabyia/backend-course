import logging
from utils.plugin_loader import load_plugins
from simulate import simulate_journey


def setup_logging():
    logging.basicConfig(filename='truck_simulator.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logging.info("Truck Simulator started.")


def user_selection(options, prompt):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = input(prompt)
    try:
        return options[int(choice) - 1]
    except (ValueError, IndexError):
        print("Invalid selection, please try again.")
        return user_selection(options, prompt)


def continue_prompt():
    choice = input("Do you want to simulate another journey?\n1.yes\n2.no\n(1/2) ").lower()
    return choice == "1"


def main():
    setup_logging()
    while True:
        logging.info("Loading plugins...")
        road_types = load_plugins("road_types")
        truck_types = load_plugins("truck_types")

        road_names = list(road_types.keys())
        truck_names = list(truck_types.keys())

        chosen_truck_name = user_selection(truck_names, "Choose a truck: ")
        chosen_road_name = user_selection(road_names, "Choose a road: ")

        chosen_truck = truck_types[chosen_truck_name.lower()]()
        chosen_road = road_types[chosen_road_name.lower()]()

        if chosen_truck.can_complete_journey(chosen_road):
            logging.info(f"The {chosen_truck_name} truck can successfully travel the {chosen_road_name} road.")
            success = simulate_journey(chosen_truck, chosen_road)
            if success:
                logging.info("The journey was successful.")
            else:
                logging.error("The journey was not successful due to insufficient resources or poor condition.")
        else:
            logging.error(
                f"The {chosen_truck_name} truck cannot complete the {chosen_road_name} road due to insufficient resources.")

        if not continue_prompt():
            break


if __name__ == "__main__":
    main()
