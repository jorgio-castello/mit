const express = require('express');
const cors = require('cors');
const controller = require('./controller');

const app = express();

app.use(express.json());
app.use(cors());

app.post('/ps/6.0001', controller.INTRO_TO_PROGRAMMING);

app.listen(3000, () => console.log('Python Scripts available on Port 3000...'));