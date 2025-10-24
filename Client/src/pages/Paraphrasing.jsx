import React from 'react'
import { useState } from 'react';
import toast from 'react-hot-toast';
import axios from 'axios';
import { server } from '..';
import Loader from './Loader';
import { Link } from 'react-router-dom';
const Notemaking = () => {





  const handlesubmit=async(e)=>{

    if(!equationInput || equationInput.length<=20){
      toast.error("Too short");
      return;

    }

    Setdisable(true)
    Setloader(true)
    try{
        const {data}=await axios.post(`${server}/users/gram`,{
            name:equationInput
        },{headers:{
            "Content-Type":"application/json",
        },withCredentials:true});
        toast.success("Done!")
        Setoutput(data["trying"])
        Setdisable(false)
        Setloader(false)
    }catch(e){toast.error("Error occured, try again");Setdisable(false);Setloader(false)}
}


    const [equationInput, setEquationOutput] = useState('');
    const [output,Setoutput]=useState('')
    const [disable,Setdisable]=useState(false)
    const [loader,Setloader]=useState(false)
    
  
    return (
      <div className="w-[100vw] flex-col items-center justify-center p-8">
        <div className={`w-full bg-white rounded-lg shadow-lg p-3 'h-[85vh]'}`}>
          <h1 className=" text-center">Grammar/Spell Check</h1>
          <div className='flex gap-4 justify-center items-center h-full py-4 px-2'>
            <div className='w-[50%] h-full gap-2  flex flex-col justify-start items-center '>
              <textarea
              onChange={(e) => setEquationOutput(e.target.value)} 
              className={`h-[300px] border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent p-2 w-[100%]`}
              placeholder="input text" value={equationInput}
            />
              <button 
              onClick={handlesubmit}
                className="bg-blue-500 text-white font-semibold px-4 py-2 rounded-md w-full hover:bg-blue-600"
                disabled={disable}
              >
                Get Text
              </button>
            </div >
            <div className='flex items-start justify-center w-[50%] h-full'>
              {!loader?<textarea
            disabled="true"
              className="h-[350px] p-2 w-full  border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              placeholder="Paraphrased text"
              value={output}

            />:<Loader/>}
            </div>
          </div>
        </div>
        <div className='mt-3 ml-3'><Link to={"/feedback"}><button className='btn'>Feedback</button></Link></div>
      </div>
    );
}

export default Notemaking