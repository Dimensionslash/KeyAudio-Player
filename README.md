# Keyboard-Controlled Audio Player Program

## Introduction:

The Keyboard-Controlled Audio Player is a simple program that allows users to play sound files by pressing specific letters on the keyboard. It is written in [insert the programming language you choose].

## Requirements:

- Python [insert version]: The program requires Python to be installed on your computer.

## Usage:

1. Install Dependencies:

   Before running the program, make sure to install the required dependencies using the following command:

   ```
   pip install pygame keyboard
   ```

2. Sound Files Setup:

   - Create a directory on your computer to store the sound files.
   - Place sound files 'a.wav' to 'z.wav' inside this directory.

3. Running the Program:

   - Download the provided source code and save it in a file named 'audio_player.py'.
   - Open your terminal or command prompt and navigate to the directory where 'audio_player.py' is located.

4. Execute the Program:

   Run the following command in the terminal or command prompt:

   ```
   python audio_player.py
   ```

5. Providing Directory Path:

   - Once the program starts, it will prompt you to provide the full path of the directory where you placed the sound files (e.g., 'C:\Users\YourUsername\sound_files').
   - Enter the path and press Enter.

6. Validating Sound Files:

   - The program will check if all the sound files ('a.wav' to 'z.wav') exist in the specified directory.
   - If any files are missing, it will notify you and exit gracefully.

7. Using the Audio Player:

   - If all sound files are valid, the program will display "All sound files are valid."
   - The audio player is now ready to use.
   - Press any letter from A to Z on your keyboard to play the corresponding sound file.
   - You can press multiple letters at the same time to play multiple sounds simultaneously.

8. Graceful Exit:

   - To exit the program, simply press the 'Esc' key on your keyboard.
   - The program will stop any playing audio and display "Exiting."

## Error Handling:

The program includes error handling to manage unexpected inputs and system-related issues. If you encounter any errors, the program will display meaningful error messages to help you troubleshoot.

Enjoy using the Keyboard-Controlled Audio Player! Customize the sound files in the directory to create your own unique audio experience. Have fun exploring and experimenting with this interactive audio player program!