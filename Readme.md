# Voice Command Handler

This Python script is a voice command handler for a voice assistant. It uses the Google Speech Recognition service to recognize voice commands and performs various actions based on the content of the command.

## Dependencies

The script requires the following Python libraries:

- `speech_recognition`
- `time`
- `playsound`
- `os`
- `sys`
- `pygetwindow`
- `tkinter`
- `random`
- `googletrans`
- `pynput`
- `pyautogui`

## How it Works

The script defines a function `main_background()` that starts listening to voice commands in the background. When a voice command is recognized, it calls a callback function that processes the command.

The processing of the command is done in the `command()` function defined in the `command` module. This function takes the recognized text as input and performs various actions based on the content of the command.

## Actions

The voice command handler can perform the following actions:

- Play a sound file
- Locate an image on the screen and click on it
- Activate a window with a specified title
- Type specified text
- Press a specified key
- Press a combination of two keys
- Perform media control actions (play, pause, next, previous)
- Adjust the volume
- Set the default sound device
- Open a specified application
- Search for specified text in Firefox
- Search for specified text in the current window
- Put the computer into sleep mode
- Shut down or restart the computer
- Create an audio file with specified title and content

## Usage

To run the script, simply execute the following command:

```bash
python3 main.py
