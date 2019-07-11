let express = require('express');
let router = express.Router();
let path = require('path');
router.get('/',(req, res) => {
  console.log(__dirname + 'public/index.html');
  res.sendFile(path.join(__dirname, '../../public/index.html'));
});
module.exports = router;
