const chai = require('chai');
const chaiHttp = require('chai-http');
const expect = chai.expect;

chai.use(chaiHttp);

const server = 'http://localhost:80';  // L'adresse où l'application sera déployée

describe('Calculator API', () => {
    it('should return the correct result for addition', (done) => {
        chai.request(server)
            .get('/calculate?a=2&b=3')
            .end((err, res) => {
                expect(res.status).to.equal(200);
                expect(res.text).to.include('5'); // Assure que le résultat est 5
                done();
            });
    });

    it('should return an error for invalid input', (done) => {
        chai.request(server)
            .get('/calculate?a=invalid&b=3')
            .end((err, res) => {
                expect(res.status).to.equal(500); // L'application devrait renvoyer une erreur sur entrée invalide
                done();
            });
    });
});

