var jayson = require('jayson');

// Create a client connected to backend server
var client = jayson.client.http({
  port: 4040,
  hostname: 'localhost'
});

// Test RPC method
function add(a, b, callback) {
  client.request('add', [a, b], function(err, error, response) {
    if (err) throw err;
    console.log(response);
    callback(response);
  });
}

// Get news summaries for a user
function getStocksSummariesForUser(user_id, page_num, callback) {
  client.request('getStocksSummariesForUser', [user_id, page_num], function(err, error, response) {
    if (err) throw err;
    callback(response);
  });
}

// Log a news click event for a user
// function logNewsClickForUser(user_id, news_id) {
//   client.request('logNewsClickForUser', [user_id, news_id], function(err, error, response) {
//     if (err) throw err;
//     console.log(response);
//   });
// }

module.exports = {
  add : add,
  getStocksSummariesForUser : getStocksSummariesForUser
//   logNewsClickForUser : logNewsClickForUser
};
