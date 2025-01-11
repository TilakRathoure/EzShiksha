import React from 'react'
import { useState } from 'react';
import toast from 'react-hot-toast';
import axios from 'axios';
import { server } from '..';
import Loader from './Loader';
import { Link } from 'react-router-dom';


const EquationSolver = () => {
  // const [equationOutput, setEquationOutput] = useState('');
  const [selectedImage, setSelectedImage] = useState(null);
  const [disable,Setdisable]=useState(false)
  const [output,Setoutput]=useState("")
  const [loader,Setloader]=useState(false);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    
    if (file) {
      setSelectedImage(file);
    } else {
      setSelectedImage(null);
    }
  };

  const removeImage = () => {
    setSelectedImage(null);
  };

  const handlesubmit=async(e)=>{

    if (selectedImage) {
      Setdisable(true)
      Setloader(true)
      const formData = new FormData();
      formData.append('image', selectedImage);


    try{
        const {data}=await axios.post(`${server}/users/upload`,
          formData,{headers:{
            "Content-Type": "multipart/form-data"
        },withCredentials:true});    
        Setoutput(data["trying"])
        Setdisable(false)
        Setloader(false);
        toast.success("Done!");
    }catch(e){toast.error("Error occured, try again");Setdisable(false);Setloader(false)}
  }
  else{
    toast.error("No file selected");
  }
}

  return (
    <div className="w-[100vw] h-[100vh] flex-col items-center justify-center p-8">
      <div className={`relative w-full bg-white rounded-lg shadow-lg p-8 ${selectedImage?'h-auto' : 'h-[75vh]'}`}>
      <a href='/Testing/test_image.png' download="test_image.png" className='bg-gray-400 absolute -top-5 right-0 text-white px-2 py-2 rounded-lg no-underline'>download sample image</a>
        <h1 className=" text-center">Extract Text</h1>
        <div className='flex gap-4 justify-center items-center h-full pt-4'>
          <div className='w-[50%] h-full gap-2 flex pt-5 flex-col  items-center'>
            <input 
              type="file" 
              accept="image/*" 
              id='fileInput'
              onChange={handleFileChange} 
              className="hidden"/>
              <button 
  className="w-full px-4 py-2 border border-gray-300 rounded-md text-center focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent hover:bg-blue-50"
  onClick={() => document.getElementById('fileInput').click()}
>
  Upload Image
</button>
            <div id="imagePreview" className="mb-4">
              {selectedImage && (
                <div className="relative">
                  <img src={URL.createObjectURL(selectedImage)} className="w-full max-h-[50vh] rounded-md" alt="Preview" />
                  <button className="absolute top-0 right-0 mt-1 mr-1 text-red-600" onClick={removeImage}>
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM7 9a1 1 0 011-1h4a1 1 0 110 2H8a1 1 0 01-1-1z" clipRule="evenodd" />
                    </svg>
                  </button>
                </div>
              )}
            </div>
            <button 
              onClick={handlesubmit} 
              disabled={disable}
              className="bg-blue-500 text-white font-semibold px-4 py-2 rounded-md w-full hover:bg-blue-600"
            >
              Extract Text
            </button>
          </div>
          <div className='flex items-start justify-center w-[50%] h-full'>
            {loader? <Loader/>:          <textarea 
          disabled="true"
            className="w-full h-[300px] p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            placeholder="Extracted Text"
            value={output}/>  }

          </div>
        </div>
      </div>
      <div className='mt-3 ml-3'><Link to={"/feedback"}><button className='btn'>Feedback</button></Link></div>
    </div>
  );
};

export default EquationSolver;
