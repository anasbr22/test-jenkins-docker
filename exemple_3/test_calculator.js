const request = require('supertest');
const app = require('../app');  // Assurez-vous que ce chemin est correct

describe('Calculator API', () => {
  it('should return the correct result for addition', (done) => {
    request(app)
      .get('/calculate?a=1&b=2')
      .expect(200)  // S'assurer que la réponse HTTP est 200
      .end((err, res) => {
        if (err) return done(err);
        try {
          // Vérifier que la réponse contient le bon résultat
          res.body.should.have.property('result');
          res.body.result.should.equal(3);
          done();
        } catch (e) {
          done(e);
        }
      });
  });

  it('should return an error for invalid input', (done) => {
    request(app)
      .get('/calculate?a=invalid&b=2')
      .expect(400)  // Attendre une erreur 400 en cas d'entrée invalide
      .end((err, res) => {
        if (err) return done(err);
        try {
          // Vérifier que la réponse d'erreur est appropriée
          res.body.should.have.property('error');
          res.body.error.should.equal('Invalid input');
          done();
        } catch (e) {
          done(e);
        }
      });
  });
});
