const express = require('express');
const app = express();
const port = 5000;

// Middleware for parsing JSON (if you want to accept POST requests with JSON)
app.use(express.json());

// Serve static files (HTML, CSS, JS)
app.use(express.static('public'));


app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/index.html');
});

//  (example: addition)
app.get('/calculate', (req, res) => {
    const a = parseFloat(req.query.a);
    const b = parseFloat(req.query.b);

    // inputs validation 
    if (isNaN(a) || isNaN(b)) {
        return res.status(400).json({ error: 'Invalid input, must be numbers' });
    }

    // Perform the addition
    const result = a + b;

    // Return the result in JSON format
    res.status(200).json({ result });
});

// Export the application 
module.exports = app;

// Only start the server if this file is executed directly
if (require.main === module) {
    app.listen(port, () => {
        console.log(`Calculator app listening at http://localhost:${port}`);
    });
}
