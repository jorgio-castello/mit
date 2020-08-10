const path = require('path');
const spawn = require('child_process').spawn;

module.exports = (req, res) => {
    const filePath = path.join(__dirname, '../../../../', 'Introduction\ to\ Programming\ (6.0001)', 'Problem\ Sets', 'ps0.py')
    const data = JSON.stringify(req.body.data);
    const args = [filePath, data];
    console.log(args[1]);

    const pyspawn = spawn('python3', args);

    pyspawn.stdout.on('data', (data) => {
        res.json(data.toString('utf8'));
    });

    pyspawn.stderr.on('data', (err) => {
        // Do something with error data, maybe write it in a log file?
        res.status(404);
        res.send();
    });

    pyspawn.on('close', (code) => {
        console.log('Child Process exited with code: ' + code);
    });
}

