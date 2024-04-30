import React from 'react'

const Feedback = () => {
  return (
    <div className="w-full h-[75vh] flex justify-center items-center">
    <div className="w-[75%] max-w-[700px]  bg-[rgb(105,236,210)]  p-5 rounded-3xl my-12 border-black border-1">
          <h2 className="mb-4">Send Feedback!</h2>
          {/* <div className="flex-col w-full justify-center rounded-3xl "> */}
            <input type="text" placeholder="Email" className="pl-4 rounded-full w-full outline-none mb-3 p-2" /> 
            <input type="text" placeholder="Feedback" className="pl-4 rounded-full w-full outline-none p-2" />
          {/* </div> */}
          <button className=" btn rounded-full mt-3">Send</button>
    </div>
    </div>
  )
}

export default Feedback