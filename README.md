# Fitness-Tracker-Desktop-App
Track your fitness by the Fitness Tracker App


# FitTrack

FitTrack is a PyQt5-based desktop application for tracking fitness activities, particularly focused on running or jogging. It allows users to log their workouts, including the date, calories burned, distance covered, and a brief description. The app also provides data visualization to help users understand their progress over time.

## Features

- Log workout sessions with date, calories burned, distance, and description
- View workout history in a table format
- Delete individual workout entries
- Visualize the relationship between distance and calories burned
- Toggle between light and dark mode for comfortable viewing

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6+
- PyQt5
- Matplotlib
- NumPy
- SQLite3

## Installation

1. Clone the repository:
     
     git clone https://github.com/Pabitra3/fittrack.git

2. Navigate to the project directory:
        
        cd fittrack   

3. Install the required packages:
      
        pip install -r requirements.txt


        This file specifies the main Python libraries required for the FitTrack application along with their versions. Here's a breakdown of each requirement:

    1. PyQt5: The GUI framework used for building the application.
    2. matplotlib: Used for creating the data visualization     (scatter plot).
    3. numpy: Often used in conjunction with matplotlib for numerical operations.

    A few notes:

    1. The versions specified here are examples and represent stable, recent versions as of my last update. You may want to use the specific versions that you've tested your application with.
    2. SQLite is not included because it's part of Python's standard library and doesn't need to be installed separately.
    3. You might want to add any additional libraries if you've used them in parts of your code that weren't shown.
    4. It's a good practice to use a virtual environment for your project. This allows you to specify exact versions of libraries without affecting other projects on your system.

     To use this requirements.txt file:

     1. Save it in the root directory of your project.
     2. Users can then install all required libraries with the command:
     3. pip install -r requirements.txt


This ensures that anyone who wants to run your project will have the correct versions of all necessary libraries.

## Usage

To run FitTrack, execute the following command in the project directory:

          python fittrack.py

## How to Use

1. **Adding a Workout**: 
   - Fill in the date, calories burned, distance, and description fields.
   - Click the "Add" button to save the workout.

2. **Viewing Workouts**: 
   - All workouts are displayed in the table on the right side of the application.

3. **Deleting a Workout**: 
   - Select a workout from the table.
   - Click the "Delete" button.

4. **Visualizing Data**: 
   - Click the "Submit" button to generate a scatter plot of distance vs. calories.

5. **Toggling Dark Mode**: 
   - Click the "Dark Mode" button to switch between light and dark themes.

## Contributing

Contributions to FitTrack are welcome. Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- PyQt5 for the GUI framework
- Matplotlib for data visualization
- SQLite for local data storage                  