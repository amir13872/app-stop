# app-stop
# Program Process Monitor

This script continuously monitors and terminates processes with a specified name. It is useful for automatically stopping unwanted processes.

## Prerequisites

- Python 3.x
- `psutil` library

You can install the `psutil` library using pip:

```sh
pip install psutil
```

## Usage

1. Clone this repository or download the script.
2. Open the script file `gamebar.py`.
3. Modify the `target_process` variable to the name of the process you want to monitor and terminate. For example:
    ```python
    target_process = "your app name"
    ```
4. Run the script:

```sh
python gamebar.py
```

## Logging

The script uses the `logging` module to provide detailed information about its operations. Logs include process termination attempts and any errors encountered.

## Stopping the Script

To stop the script, press `Ctrl+C` in the terminal where the script is running.

## License

This project is licensed under the MIT License.
