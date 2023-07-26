import os
import pygame
import keyboard

# Set sound directory
sound_dir = r'C:\tmp'

# Initialize pygame
pygame.mixer.init()

# Validate files
files_valid = True

for letter in range(ord('a'), ord('z')+1):
    filename = f"{chr(letter)}.mp3"

    filepath = os.path.join(sound_dir, filename)

    if not os.path.isfile(filepath):
        print(f"{filename} not found in {sound_dir}")
        files_valid = False

if not files_valid:
    print("Missing sound files")
else:
    print("All sound files are valid.")

# Handle keyboard input
active_sounds = {}

while True:
    try:
        if keyboard.is_pressed('esc'):
            break

        for letter in range(ord('a'), ord('z')+1):
            if keyboard.is_pressed(chr(letter)):
                filename = f'{chr(letter)}.mp3'
                filepath = os.path.join(sound_dir, filename)

                if letter not in active_sounds or not active_sounds[letter]:
                    pygame.mixer.music.load(filepath)
                    pygame.mixer.music.play()
                    active_sounds[letter] = True

    except KeyboardInterrupt:
        break

    # Check if the currently playing sound has finished
    if pygame.mixer.music.get_busy() == 0:
        for letter, is_playing in active_sounds.items():
            if is_playing:
                active_sounds[letter] = False

# Graceful exit
pygame.mixer.music.stop()
pygame.mixer.quit()

print("Exiting")
