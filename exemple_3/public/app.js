const express = require('express');
const app = express();
const port = 80;

// Servir les fichiers statiques (HTML, CSS, JS)
app.use(express.static('public'));

// Route principale pour afficher la calculatrice
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/index.html');
});

app.listen(port, () => {
    console.log(`Calculator app listening at http://localhost:${port}`);
});

