from pytube import YouTube
import PySimpleGUI as sg

video_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-URL-"),
        sg.Button("Get Videos"),  # need to add logic to this button to search for a video based on the entered URL
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-VIDEO LIST-"
        )
    ],
]

# For now will only show the name of the video that was chosen
video_viewer_column = [
    [sg.Text("Choose a video from list on left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-VIDEO-")],
]

# ----- Full layout -----
layout = [
    [
        sg.Column(video_list_column),
        sg.VSeperator(),
        sg.Column(video_viewer_column),
    ]
]

window = sg.Window("Image Viewer", layout)



while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break