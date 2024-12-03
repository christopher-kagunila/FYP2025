Antenna Control System
Overview
The Antenna Control System is a Kivy-based graphical user interface (GUI) application designed to manage and control antenna alignment. This system allows users to set and verify vertical and horizontal alignments of antennas, reset them to previously configured values, and generate a plot of antenna positions.

Features
Set Antenna Alignment: Allows users to input vertical and horizontal alignment values.
Reset to Configured Values: Resets the antenna to previously configured alignment values.
Position Check: Verifies if the antenna is in the correct position.
Generate Plot: Visualizes antenna positions using a plot created with Plotnine.
Configuration Screen: A separate screen for setting the initial alignment values.

Requirements
-Python 3.x
-Kivy
-Pandas
-Plotnine

Installation
To install the necessary dependencies, run the following command:
Copy code
pip install kivy pandas plotnine
Usage
Run the Application: Start the application by running the following command in your terminal:

bash
Copy code
python main.py
Main Screen:

Send Alignment: Input the vertical and horizontal alignment values and press "Send Alignment" to update the antenna’s position.
Generate Plot: Visualize the antenna’s current and configured positions.
Reset to Configured: Reset the antenna to its original configured position.
Check Position: Verify if the antenna is in the correct position based on its vertical and horizontal alignment.
Configuration Screen:

Set the configured vertical and horizontal alignment values.
Confirm your settings to apply them.
Code Structure
main.py
The main application file where the Kivy app is built. It contains the AntennaControl and ConfigScreen classes, the logic for antenna control, and the plot generation functionality.

app.kv
The Kivy language file that defines the user interface layout, including the main screen and configuration screen.

Troubleshooting
If you encounter issues with missing libraries, ensure that you have installed all the dependencies.
If the plot fails to generate, ensure that the pandas and plotnine packages are correctly installed.
Contributing
If you would like to contribute to the project, feel free to fork the repository, create a branch, and submit a pull request with your improvements or bug fixes.
