const request = require('supertest');
const app = require('../app');  // Importer l'application sans démarrer le serveur

describe('Calculator API', () => {
  it('should return the correct result for addition', (done) => {
    request(app)
      .get('/calculate?a=5&b=3')
      .expect(200)  // Vérifier que le statut de la réponse est 200
      .end((err, res) => {
        if (err) return done(err);
        res.body.result.should.equal(8);  // Vérifier que le résultat est 8
        done();
      });
  });

  it('should return an error for invalid input', (done) => {
    request(app)
      .get('/calculate?a=invalid&b=3')
      .expect(400)  // Vérifier que le statut de la réponse est 400 pour une entrée invalide
      .end((err, res) => {
        if (err) return done(err);
        res.body.error.should.equal('Invalid input, must be numbers');
        done();
      });
  });
});
