const powers_and_logs = require('./problemSets/problemSet_0');

module.exports = (req, res) => {
    switch(req.body.query) {
        case 'powers_and_logs':
            powers_and_logs(req, res);
            break;
        default:
            res.json('Invalid query for Intro to Programming');
            break;
    }
}