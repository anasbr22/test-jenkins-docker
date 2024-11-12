const chai = require('chai');
const chaiHttp = require('chai-http');
const server = 'http://localhost:5000'; // L'adresse où votre app sera déployée

chai.use(chaiHttp);
const { expect } = chai;

describe('Calculator Web Application', () => {
    it('should load the calculator page', (done) => {
        chai.request(server)
            .get('/')
            .end((err, res) => {
                expect(res.status).to.equal(200);
                expect(res.text).to.include('Simple Web Calculator');
                done();
            });
    });
});
