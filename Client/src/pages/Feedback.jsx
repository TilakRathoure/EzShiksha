import React, { useState } from 'react'
import toast from 'react-hot-toast';

const Feedback = () => {


  const [text,Settext]=useState("");
  const [text1,Settext1]=useState("");


  const onsubmit=(e)=>{
    e.preventDefault();

    if(text!=="" && text1!==""){
      toast.success(`email sent`);
    }
  }


  return (
    <div className="w-full h-[75vh] flex justify-center items-center">
    <div className="w-[75%] max-w-[700px]  bg-[rgb(105,236,210)]  p-5 rounded-3xl my-12 border-black border-1">
          <h2 className="mb-4">Send Feedback!</h2>
          <form action="" onSubmit={onsubmit}>
          {/* <div className="flex-col w-full justify-center rounded-3xl "> */}
            <input type="email" placeholder="Email" className="pl-4 rounded-full w-full outline-none mb-3 p-2" value={text1} required onChange={(e)=>{
              Settext1(e.value)
            }}/> 
            <input type="text" placeholder="Feedback" className="pl-4 rounded-full w-full outline-none p-2" value={text} required onChange={(e)=>{
              Settext(e.value)
            }} />
          {/* </div> */}
          <button className=" btn rounded-full mt-3">Send</button>
          </form>
    </div>
    </div>
  )
}

export default Feedback