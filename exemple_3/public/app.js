const express = require('express');
const app = express();
const port = 5000;

// Middleware pour parse les données JSON (si vous voulez accepter des requêtes POST avec des JSON)
app.use(express.json());

// Servir les fichiers statiques (HTML, CSS, JS)
app.use(express.static('public'));

// Route principale pour afficher la calculatrice
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/index.html');
});

// Route pour effectuer un calcul (exemple : addition)
app.get('/calculate', (req, res) => {
    const a = parseFloat(req.query.a);
    const b = parseFloat(req.query.b);

    // Vérifier les entrées pour s'assurer qu'elles sont valides
    if (isNaN(a) || isNaN(b)) {
        return res.status(400).json({ error: 'Invalid input, must be numbers' });
    }

    // Effectuer l'addition
    const result = a + b;

    // Retourner le résultat en format JSON
    res.status(200).json({ result });
});

// Lancer le serveur
app.listen(port, () => {
    console.log(`Calculator app listening at http://localhost:${port}`);
});
