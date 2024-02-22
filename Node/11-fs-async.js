const {readFile, writeFile, write} = require('fs');

console.log('start')
readFile('./content/first.txt','utf8',(err,result)=>{
    if(err){ 
        console.log(err);
        return
    }
    const first = result;
    //console.log(result)
    readFile('./content/second.txt','utf8',(err,result)=>{
        if(err){ 
            console.log(err);
            return
        }
        const second = result;
        writeFile('./content/result-async.txt',    
        `Here is the result: ${first},${second}`,(err,result)=>{
            if(err){
                console.log(err)
                return
            }
            console.log('done with async')
        })
    })
})

console.log('starting next')