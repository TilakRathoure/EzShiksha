import {spawn} from "child_process"

const Grammerly=(req,res)=>{
    
// const childPython =spawn('python',['codespace.py']);

const inputtext=req.body.name

let responseData=''

// const childPython =spawn('python',['codespace.py','OyeKool'])
const childPython =spawn('python',['Notegeneration.py',inputtext])


childPython.stdout.on('data',(data)=>{
    responseData += data.toString();
});

childPython.stderr.on('data',(data)=>{
    // console.error(`stdout: ${data}`);
});

childPython.on('close',(code)=>{
    console.log(`child process exited with code ${code}`);
        
    // Once the child process has finished, remove the \r\n characters from responseData

    // Send the modified responseData back in the response
    res.json({ trying: responseData });
})

}

export default Grammerly

