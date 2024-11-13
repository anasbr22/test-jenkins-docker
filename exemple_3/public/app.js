const express = require('express');
const app = express();
const port = 5000;

// Middleware to parse JSON (for POST requests)
app.use(express.json());

// Serve static files (HTML, CSS, JS)
app.use(express.static('public'));

// Main route to display the calculator
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/index.html');
});

// Route to perform a calculation (e.g., addition)
app.get('/calculate', (req, res) => {
    const a = parseFloat(req.query.a);
    const b = parseFloat(req.query.b);

    // Validate inputs
    if (isNaN(a) || isNaN(b)) {
        return res.status(400).json({ error: 'Invalid input, must be numbers' });
    }

    // Perform the addition
    const result = a + b;

    // Return the result as JSON
    res.status(200).json({ result });
});

// Export the app so it can be used in the test
module.exports = app;

// Only start the server if this file is executed directly
if (require.main === module) {
    app.listen(port, () => {
        console.log(`Calculator app listening at http://localhost:${port}`);
    });
}
