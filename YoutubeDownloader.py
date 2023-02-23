from pytube import YouTube
import PySimpleGUI as sg

video_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-URL-"),
        sg.Button("Get Videos"),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-VIDEO LIST-"
        )
    ],
]

# For now will only show the name of the file that was chosen
video_viewer_column = [
    [sg.Text("Choose an image from list on left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-VIDEO-")],
]
