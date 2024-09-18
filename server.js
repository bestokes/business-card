const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const path = require('path');
const querystring = require('querystring');

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.post('/submit-form', async (req, res) => {
    console.log('Received form submission:', req.body);
    try {
        console.log('Forwarding request to Flask server');
        const response = await axios.post('http://127.0.0.1:5000', querystring.stringify(req.body), {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        });
        console.log('Received response from Flask server:', response.data);
        res.redirect('/thank-you');
    } catch (error) {
        console.error('Error:', error.message);
        if (error.response) {
            console.error('Response data:', error.response.data);
            console.error('Response status:', error.response.status);
        } else if (error.request) {
            console.error('No response received:', error.request);
        } else {
            console.error('Error setting up request:', error.message);
        }
        res.status(500).send('An error occurred while processing your request.');
    }
});

app.get('/thank-you', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'thank-you.html'));
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
