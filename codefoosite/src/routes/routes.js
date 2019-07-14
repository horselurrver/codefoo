let express = require('express');
let router = express.Router();
let path = require('path');
const axios = require('axios');

router.get('/',(req, res) => {
  // res.sendFile(path.join(__dirname, '../../public/index.html'));
  axios.get('https://ign-apis.herokuapp.com/content')
  .then(response => {
    console.log(response.data.data);
    res.render('home.hbs', {
      data: response.data.data
    });
  })
  .catch(error => {
    console.log(error);
  });
});

module.exports = router;
