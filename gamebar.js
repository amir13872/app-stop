const { exec } = require('child_process');
const ps = require('ps-node');

function killProcess(processName) {
    ps.lookup({ command: processName }, (err, resultList) => {
        if (err) {
            console.error(err);
            return;
        }

        resultList.forEach(process => {
            if (process) {
                console.log(`Terminating process: ${process.command} (PID: ${process.pid})`);
                ps.kill(process.pid, err => {
                    if (err) {
                        console.error(`Failed to terminate process: ${err}`);
                    }
                });
            }
        });
    });
}

function monitorAndStop(processName) {
    console.log(`Monitoring for ${processName}...`);
    const interval = setInterval(() => {
        killProcess(processName);
    }, 2000);

    process.on('SIGINT', () => {
        console.log('Monitoring stopped by user.');
        clearInterval(interval);
        process.exit();
    });
}

const targetProcess = 'your game name';
monitorAndStop(targetProcess);
