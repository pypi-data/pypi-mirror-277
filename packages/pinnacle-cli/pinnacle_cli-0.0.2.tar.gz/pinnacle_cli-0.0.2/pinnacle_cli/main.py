import os
import click
from subprocess import Popen
from pinnacle_cli.constants import HOST, PORT, PYTHON_PORT, DIRECTORY
from pinnacle_cli.py.dev_scheduler import run_scheduled
import time
import multiprocessing

cwd = os.getcwd()


@click.command()
@click.argument("mode", required=True, type=click.Choice(["dev", "prod"]))
def main(mode: str) -> None:
    if mode == "dev":
        click.echo("Running in development mode")
        metadata_dir = os.path.join(cwd, DIRECTORY, ".metadata")
        os.makedirs(metadata_dir, exist_ok=True)

        py_endpoints_file = os.path.join(metadata_dir, "py_endpoints.json")
        if os.path.exists(py_endpoints_file):
            os.remove(py_endpoints_file)

        js_endpoints_file = os.path.join(metadata_dir, "js_endpoints.json")
        if os.path.exists(js_endpoints_file):
            os.remove(js_endpoints_file)

        os.environ["PINNACLE_CWD"] = cwd
        python_server = Popen(
            [
                "uvicorn",
                "pinnacle_cli.py.dev_server:app",
                "--host",
                HOST,
                "--port",
                str(PYTHON_PORT),
                "--reload",
            ],
        )

        js_server = Popen(
            ["npm", "run", "start-dev", cwd],
            cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), "js"),
        )

        scheduled_process = multiprocessing.Process(target=run_scheduled)
        scheduled_process.start()

        while not os.path.exists(py_endpoints_file) or not os.path.exists(
            js_endpoints_file
        ):
            time.sleep(0.5)

        reverse_proxy_server = Popen(
            [
                "mitmdump",
                "--listen-host",
                HOST,
                "-p",
                str(PORT),
                "-s",
                f"{os.path.dirname(os.path.abspath(__file__))}/translator/proxy.py",
            ],
            env=os.environ,
            cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)), "translator"),
        )

        try:
            reverse_proxy_server.wait()
        except Exception as e:
            click.echo(f"Error running Python dev server: {e}")
        finally:
            print("Terminating servers")
            reverse_proxy_server.terminate()
            js_server.terminate()
            python_server.terminate()
            scheduled_process.terminate()


if __name__ == "__main__":
    main()
