var express = require('express');  
const mydata = require('./sample.json')
var app = express();


app.set('view engine','ejs'); 

app.use(express.static('./assets'));


app.get('/',function(req,res){
    res.render('myhouse',{data:mydata});   
});

app.get('/details',function(req,res){    
    res.render('details'); 
});

app.listen(1432);
console.log('you\'re listening to port 1432')