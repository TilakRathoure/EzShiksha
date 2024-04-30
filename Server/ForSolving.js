import {spawn} from "child_process"

const Solve=(req,res)=>{
    
// const childPython =spawn('python',['codespace.py']);

const imagePath = req.file.path;

let responseData=''

// const childPython =spawn('python',['codespace.py','OyeKool'])
const childPython =spawn('python',['maths.py',imagePath])


childPython.stdout.on('data',(data)=>{
    responseData += data.toString();
});

childPython.stderr.on('data',(data)=>{
    // console.error(`stdout: ${data}`);
});

childPython.on('close',(code)=>{
    console.log(`child process exited with code ${code}`);

    res.json({ trying: responseData });
})

}

export default Solve

