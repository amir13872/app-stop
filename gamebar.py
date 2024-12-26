import psutil
import time
import logging
import traceback

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def kill_process(process_name):
    """Terminates all processes with the specified name."""
    for process in psutil.process_iter(['pid', 'name']):
        try:
            if process.info['name'] and process_name.lower() in process.info['name'].lower():
                logging.info(f"Terminating process: {process.info['name']} (PID: {process.info['pid']})")
                process.terminate()
                process.wait(timeout=5)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            logging.warning(f"Failed to terminate process: {e}")
            logging.debug(traceback.format_exc())

def monitor_and_stop(process_name):
    """Continuously monitor and stop the specified process."""
    try:
        logging.info(f"Monitoring for {process_name}...")
        while True:
            kill_process(process_name)
            time.sleep(2)  # Check every 2 seconds
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        logging.debug(traceback.format_exc())

if __name__ == "__main__":
    target_process = "your game name"
    monitor_and_stop(target_process)
