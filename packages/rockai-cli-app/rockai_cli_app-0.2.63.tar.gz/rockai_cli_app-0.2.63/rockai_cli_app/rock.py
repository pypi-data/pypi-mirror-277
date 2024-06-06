import typer
from rockai_cli_app.server.http import start_server
from pathlib import Path
from rockai_cli_app.parser.config_util import parse_config_file
from typing_extensions import Annotated
from rockai_cli_app.docker.docker_util import build_final_image
import os

app = typer.Typer()

APP_NAME = "rockai-cli-app"


@app.callback()
def callback():
    """
    Callback for the CLI app before any command
    """
    typer.echo("Callback excuted")


@app.command()
def init():
    file = open('rock.yaml', 'w')
    file.close()
    file = open('predict.py', 'w')
    file.close()



@app.command(name='build')
def build(port: Annotated[int, typer.Option(help="Port of the server, default is 8000")] = 8000):
    """
    Build the image
    """
    if not os.path.exists(str(Path.cwd() / 'requirements_temp')):
        os.makedirs(str(Path.cwd() / 'requirements_temp'))
        print(f"Folder '{str(Path.cwd() / 'requirements_temp')}' created.")
    else:
        print(f"Folder '{str(Path.cwd() / 'requirements_temp')}' already exists.")

    config_path: Path = Path.cwd() / "rock.yaml"
    if not config_path.is_file():
        raise Exception("rock.yaml config file doesn't exist in the current directory")
    else:
        print("rock.yaml config file exist")
    config_map = parse_config_file(config_path)
    print(config_map)
    build_final_image(config_map=config_map,port=port)

    


@app.command()
def start(port: Annotated[int, typer.Option(help="Port of the server, default is 8000")] = 8000):
    """
    start local development server
    """
    start_server(port)
