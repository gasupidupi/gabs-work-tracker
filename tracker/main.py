
import typer
import yaml
from datetime import datetime
import os
import importlib.resources

app = typer.Typer()
with open(importlib.resources.files("tracker").joinpath("config.yml"), "r") as f:
    config_data = yaml.safe_load(f)

def get_input(text):
    return input(text)

def add_track(date, start, end, ticket, message):
    with open(os.path.join(config_data["output_directory"], "tracks.csv"), "a") as f:
        f.write(";".join([date, start, end, ticket, message]) + "\n")
    f.close()

def safe_config(config_data):
    with open(importlib.resources.files("tracker").joinpath("config.yml"), "w") as f:
        yaml.safe_dump(config_data, f)
    f.close()

def get_last_track():
    with open(os.path.join(config_data["output_directory"], "tracks.csv"), "r") as f:
        for line in f:
            pass
        return line

def remove_last_track():
    # https://stackoverflow.com/a/10289740
    with open(os.path.join(config_data["output_directory"], "tracks.csv"), "r") as f:
        f.seek(0, os.SEEK_END)
        pos = f.tell() - 1
        while pos > 0 and f.read(1) != "\n":
            pos -= 1
            f.seek(pos, os.SEEK_SET)
        if pos > 0:
            f.seek(pos, os.SEEK_SET)
            f.truncate()

@app.command()
def track(message: str = None, m: str = None, ticket: str = None, t: str = None, past: bool = False, p: bool = False):
    message = message or m
    ticket = ticket or t
    past = past or p
    if not past:
        start = datetime.now().strftime("%H:%M")
        get_input("Press Enter to end tracking...")
    else:
        start = get_last_track().split(";")[2]
    end = datetime.now().strftime("%H:%M")
    date = datetime.now().strftime("%d/%m/%Y")
    if (message == None):
        message = get_input("Enter message: ")
    if (ticket == None):
        ticket = get_input("Enter ticket: ")
    add_track(date, start, end, ticket, message)

@app.command()
def config(output: str = None, o: str = None):
    output = output or o
    if (output == None):
        output = get_input("Enter output directory: ")
    config_data["output_directory"] = output
    safe_config(config_data)

@app.command()
def show():
    with open(os.path.join(config_data["output_directory"], "tracks.csv"), "r") as f:
        for line in f:
            print(line.replace(";", "   "))
            
@app.command()
def clear():
    os.remove(os.path.join(config_data["output_directory"], "tracks.csv")) 

@app.command()
def pop():
    remove_last_track()

def run() -> None:
    app()