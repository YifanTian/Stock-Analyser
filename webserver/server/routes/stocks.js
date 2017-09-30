var express = require('express');
var router = express.Router();
var rpc_client = require('../rpc_client/rpc_client');

// /* GET stocks summary list. */
// router.get('/', function(req, res, next) {
//   stocks = [
//             {
//                 'url':'',
//                 'title':'AGTC',
//                 'open': 4.7,
//                 'price': 4.8,
//                 'volume': 45239,
//                 'trade_datetime': '2017-09-07 20:00:00 UTC+0000',
//                 'reason':'recommand'
//             },
//             {
//                 'url':'',
//                 'title':'AGTC',
//                 'open': 4.7,
//                 'price': 4.8,
//                 'volume': 45239,
//                 'trade_datetime': '2017-09-07 20:00:00 UTC+0000',
//                 'reason':'recommand'
//             },
//             {
//                 'url':'',
//                 'title':'AGTC',
//                 'open': 4.7,
//                 'price': 4.8,
//                 'volume': 45239,
//                 'trade_datetime': '2017-09-07 20:00:00 UTC+0000',
//                 'reason':'recommand'
//             },
//             {
//                 'url':'',
//                 'title':'AGTC',
//                 'open': 4.7,
//                 'price': 4.8,
//                 'volume': 45239,
//                 'trade_datetime': '2017-09-07 20:00:00 UTC+0000',
//                 'reason':'hot'
//             }];
//   res.json(stocks);
// });

/* GET news summary list. */
router.get('/userId/:userId/pageNum/:pageNum', function(req, res, next) {
  console.log('Fetching stocks...');
  user_id = req.params['userId'];
  page_num = req.params['pageNum'];

  rpc_client.getStocksSummariesForUser(user_id, page_num, function(response) {
    res.json(response);
  });
});

router.get('/userId/:userId/stockIndex/:stockIndex', function(req, res, next) {
  console.log('Fetching stocks...');
  user_id = req.params['userId'];
  index = req.params['stockIndex'];

  rpc_client.getStockForUser(user_id, index, function(response) {
    res.json(response);
  });
});

// /* Log news click. */
// router.post('/userId/:userId/newsId/:newsId', function(req,res, next) {
//   console.log('Logging news click...');
//   user_id = req.params['userId'];
//   news_id = req.params['newsId'];

//   rpc_client.logStocksClickForUser(user_id, news_id);
//   res.status(200);
// });

module.exports = router;
