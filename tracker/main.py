
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

@app.command()
def track(message: str = None, m: str = None, ticket: str = None, t: str = None):
    message = message or m
    ticket = ticket or t
    date = datetime.now().strftime("%d/%m/%Y")
    start = datetime.now().strftime("%H:%M")
    get_input("Press Enter to end tracking...")
    end = datetime.now().strftime("%H:%M")
    if (message == None):
        message = get_input("Enter message: ")
    if (ticket == None):
        ticket = get_input("Enter ticket: ")
    with open(os.path.join(config_data["output_directory"], "tracks.csv"), "a") as f:
        f.write(";".join([date, start, end, ticket, message]) + "\n")
    f.close()

@app.command()
def config(output: str = None, o: str = None):
    output = output or o
    config_data["output_directory"] = output
    with open(importlib.resources.files("tracker").joinpath("config.yml"), "w") as f:
        yaml.safe_dump(config_data, f)

@app.command()
def show():
    with open(os.path.join(config_data["output_directory"], "tracks.csv"), "r") as f:
        for line in f:
            print(line.replace(";", "   "))
            
@app.command()
def clear():
    os.remove(os.path.join(config_data["output_directory"], "tracks.csv")) 


def run() -> None:
    app()