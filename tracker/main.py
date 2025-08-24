
import typer
import yaml
import datetime
import os
import importlib.resources

app = typer.Typer()
with importlib.resources.files("tracker").joinpath("config.yml").open("r") as f:
    config = yaml.safe_load(f)


@app.command()
def track(message: str = None, m: str = None, ticket: str = None, t: str = None):
    message = message or m
    ticket = ticket or t
    date = datetime.datetime.now().strftime("%d/%m/%Y")
    start = datetime.datetime.now().strftime("%H:%M")
    input("Press Enter to end tracking...")
    end = datetime.datetime.now().strftime("%H:%M")
    if (message == None):
        message = input("Enter message: ")
    if (ticket == None):
        ticket = input("Enter ticket: ")
    with open(os.path.join(config["output_directory"], "tracks.csv"), "a") as f:
        f.write(";".join([date, start, end, ticket, message]) + "\n")
    f.close()

@app.command()
def show():
    with open(os.path.join(config["output_directory"], "tracks.csv"), "r") as f:
        for line in f:
            print(line.replace(";", "   "))
            
@app.command()
def clear():
    os.remove(os.path.join(config["output_directory"], "tracks.csv")) 


def run() -> None:
    app()