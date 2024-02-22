const http = require('http');

const server =  http.createServer((req,res)=>{
    if(req.url === '/'){
        res.end('Welcome to our home page')
    }
    if(req.url === '/about'){
        res.end('This is the about page')
    }
    res.end(`
    <h1>Oops!</h1>
    <p>Cant find the page that you are looking for</p>
    <a href="/">back home</a>
    `)
})

server.listen(5000)