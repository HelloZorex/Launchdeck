import time
import pygame
import pygame.midi
import webbrowser
import subprocess
import keyboard
import ast


hotkeys = ast.literal_eval(open("HotKeys.txt").read())

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

pygame.midi.init()
midi_in = pygame.midi.Input(1)

print("Diagnostics -------------")
print(f"MIDI Device Connected: {pygame.midi.get_init()}")
print(f"Number of MIDI Devices Connected: {pygame.midi.get_count()}")
for i in range(pygame.midi.get_count()):
    print(pygame.midi.get_device_info(i), i)
print("--------------------------")


def runMidi():
    x = True
    while x:
        while(pygame.midi.Input.poll(midi_in) == False):
            time.sleep(0.1)
        midi_data = pygame.midi.Input.read(midi_in, 1)
        midi_note, timestamp = midi_data[0]
        note_status, keynum, velocity, unused = midi_note
        print("Midi Note: \n\tNote Status: ", note_status, " Key Number: ", keynum," Velocity: " , velocity, "\n\tTime Stamp: ", timestamp)
        if note_status == 144:
            key_down = True
        elif note_status == 128: 
            key_down = False
        else:
            print("Unknown status!")

        if str(keynum) in hotkeys and velocity == 127:
            eval(hotkeys[str(keynum)])

        if str(keynum) == "19":
            x = False
    pygame.midi.Input.close(midi_in)

    # runMidi()