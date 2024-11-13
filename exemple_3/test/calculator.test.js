const request = require('supertest');
const app = require('../app');  // Import the app (does not start the server by default)

let server;

beforeAll((done) => {
    // Start the server before running the tests
    server = app.listen(5000, done);
});

afterAll((done) => {
    // Close the server after the tests
    server.close(done);
});

describe('Calculator API', () => {
  it('should return the correct result for addition', (done) => {
    request(app)
      .get('/calculate?a=5&b=3')
      .expect(200)  // Check that the response status is 200
      .end((err, res) => {
        if (err) return done(err);
        res.body.result.should.equal(8);  // Check that the result is 8
        done();
      });
  });

  it('should return an error for invalid input', (done) => {
    request(app)
      .get('/calculate?a=invalid&b=3')
      .expect(400)  // Check that the response status is 400 for invalid input
      .end((err, res) => {
        if (err) return done(err);
        res.body.error.should.equal('Invalid input, must be numbers');
        done();
      });
  });
});
