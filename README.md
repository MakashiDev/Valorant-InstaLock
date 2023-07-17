# Valorant Instalock App

The Valorant Instalock App is a Python-based application that automates the process of instalocking an agent in Valorant.

## Prerequisites

Before you can use the application, make sure you have the following prerequisites installed on your system:

1. Python: Visit the official Python website (https://www.python.org) and download the latest version of Python for your operating system. Follow the installation instructions provided by Python to complete the installation.

## Installation

IF u cant figure this out go here [click here](#if-youve-never-used-a-computer)



1. Clone the repository or download the source code files to your local machine.

2. Open a command prompt or terminal and navigate to the directory where you have downloaded the source code.

3. Install the required dependencies by running the following command:

This command will install the necessary Python libraries that the application depends on.

## Usage

1. Open a command prompt or terminal and navigate to the directory where you have downloaded the source code.

2. Run the `main.py` script by executing the following command: Windows:`python main.py` | Mac: `python3 main.py` | and if ur smarted enought for linux figure it out


3. The application will prompt you to hover your mouse over the agent in the Valorant client and press `Alt` to capture the coordinates. This step is necessary to identify the agent's position accurately.

4. After capturing the agent coordinates, you will be prompted to hover your mouse over the lock button in the Valorant client and press `Alt` to capture the coordinates. This step helps determine the location of the lock button accurately.

5. The captured coordinates will be saved in a JSON file named `instalock_coords.json`.

6. On subsequent runs of the application, it will automatically load the saved coordinates from the JSON file. If the JSON file is not found or the coordinates are not available, the application will prompt you to capture the coordinates again.

7. Once the application is running, it will display a message indicating that it is waiting for the `Alt` key press to start the instalock process.

8. Press the `Alt` key to initiate the instalock process. The application will continuously click on the agent's coordinates and the lock button's coordinates in rapid succession.

9. To stop the instalock process, press the `Alt` key again.

Please note that automating actions in games may violate the game's terms of service. Use this application responsibly and at your own risk.

## Troubleshooting

If you encounter any issues while using the Valorant Instalock App, consider the following troubleshooting steps:

- Make sure you have the latest version of Python installed on your system.
- Verify that you have installed the required dependencies (`pyautogui` and `keyboard`) by running the command `pip list` and checking the installed packages.
- Ensure that the Valorant client is running and visible on your screen during the installation process.
- If the application fails to capture the coordinates accurately, try adjusting the positioning of your mouse or hover directly over the desired areas.

If you continue to experience problems, please feel free to reach out for assistance by creating an issue on the repository's issue tracker.




# if youve never used a computer 
sooo basicaly click this cute buttone


<img width="100" alt="Screenshot 2023-07-16 at 22 08 14" src="https://github.com/MakashiDev/Valorant-InstaLock/assets/53072442/a64ec141-7367-4f87-a4e5-4b2eb17f9f3a">


then click this


<img width="250" alt="Screenshot 2023-07-16 at 22 08 33" src="https://github.com/MakashiDev/Valorant-InstaLock/assets/53072442/a6b1484f-3cf3-4fde-85c5-5b85af984b9f">

ima hope u can open a zip file lol
next install python **WATCH A YOUTUBE VIDEO ** pls
next now u have that [go here](#usage)
