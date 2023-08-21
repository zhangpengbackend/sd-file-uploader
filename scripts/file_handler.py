import gradio as gr
import subprocess
import os
import webbrowser
import requests
import logging
import requests
import os
from urllib.parse import unquote
import sys
import re
import json
from modules import script_callbacks
import shutil

def upload_file(file):
    return file.name, [file.name]

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as file_manager:
        # New tab for file upload
        with gr.Tab("Upload File"):
            with gr.Column():
                file_output = gr.File()
                file_link = gr.outputs.Textbox(label="File link")
                upload_button = gr.UploadButton("Click to Upload a File")
                upload_button.upload(upload_file, upload_button, outputs=[file_link, file_output])

    return ((file_manager, "FileManager", "file_handler"),)

script_callbacks.on_ui_tabs(on_ui_tabs)
