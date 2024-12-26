# Programs Process Monitor

This script continuously monitors and terminates processes with a specified name. It is useful for automatically stopping unwanted processes.

## Prerequisites

### Python

- Python 3.x
- `psutil` library

You can install the `psutil` library using pip:

```sh
pip install psutil
```

### JavaScript

- Node.js
- `ps-node` package

You can install the `ps-node` package using npm:

```sh
npm install ps-node
```

## Usage

### Python

1. Clone this repository or download the script.
2. Open the script file `gamebar.py`.
3. Modify the `target_process` variable to the name of the process you want to monitor and terminate. For example:
    ```python
    target_process = "your game name"
    ```
4. Run the script:

```sh
python gamebar.py
```

### JavaScript

1. Clone this repository or download the script.
2. Open the script file `gamebar.js`.
3. Modify the `targetProcess` variable to the name of the process you want to monitor and terminate. For example:
    ```javascript
    const targetProcess = 'your game name';
    ```
4. Run the script:

```sh
node gamebar.js
```

## Logging

The scripts provide detailed information about their operations. Logs include process termination attempts and any errors encountered.

## Stopping the Script

To stop the script, press `Ctrl+C` in the terminal where the script is running.

## License

This project is licensed under the MIT License.
