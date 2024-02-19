const os = require('os')

// info about user 
const user = os.userInfo();
console.log(user)

// method returns the system up time in seconds
const time = os.uptime()
console.log(`The system uptime is ${os.uptime()} seconds.`)
console.log('The system uptime is ' + (time) + 'seconds')


const currentOS = {
    name : os.type(),
    release : os.release(),
    totatMem : os.totalmem(),
    freeMem : os.freemem(),
}
console.log('System stats : ' + currentOS)
console.log(currentOS)