let express = require('express');
let mainRoute = require('./routes/routes');
let exphbs  = require('express-handlebars');

let app = express();

app.engine('hbs', exphbs({defaultLayout: 'main', extname: '.hbs'}));
app.set('view engine', 'hbs');

app.use(express.static(__dirname + '/public'));
app.use(mainRoute);
app.use(express.static('public'));

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log('Server has started on port ' + PORT);
});
