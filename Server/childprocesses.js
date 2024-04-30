import {spawn} from "child_process"

// const childPython =spawn('python',['codespace.py']);

let obj={channel:"oyecool"};

// const childPython =spawn('python',['codespace.py','OyeKool'])
const childPython =spawn('python',['codespace.py',JSON.stringify(obj)])


childPython.stdout.on('data',(data)=>{
    console.log(`stdout: ${data}`);
});

childPython.stderr.on('data',(data)=>{
    console.error(`stdout: ${data}`);
});

childPython.on('close',(code)=>{
    console.log(`child process ${code}`);
})

