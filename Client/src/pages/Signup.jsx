import React, { useState,useContext} from 'react'
import { Link,Navigate } from 'react-router-dom'
import img1 from '../assests/images/istockphoto-1281150061-612x612.jpg'
import img2 from './images/eye-close.png'
import img3 from './images/eye-open.png'
import toast from "react-hot-toast";
import axios from 'axios'
import {Contextfirst, server} from '..'
import { useNavigate } from 'react-router-dom'

const Signup = () => {
    const [isHovered, setIsHovered] = useState(false);
    const {authentication,Setauthentication} = useContext(Contextfirst)
    const [user,setUser]=useState(true);
    const [show,setShow]=useState(true);

    const navigate=useNavigate();

    const [data,Setdata]=useState({
        name:"",
        email:"",
        password:""
    })
    
    const handlesubmit=async(e)=>{
        e.preventDefault();
        const {name,email,password}=data
        try{
            const {data}=await axios.post(`${server}/users/new`,{
                name, email,password
            },{headers:{
                "Content-Type":"application/json",
            },withCredentials:true});
            toast.success(data.message)
            Setauthentication(true);
            navigate("/home")
        }catch(error){
            toast.error(error.response.data.message)
        }
    }

    if(authentication){
        return(
            <Navigate to={"/home"}/>
        )
    }

  return (
    <div>
    <div className="p-5 md:flex w-[100vw] h-[100vh] border-2" id="home">
    <div className="login-right md:w-[40%] ">
            <img className='h-full object-contain' src={img1} alt="" />
        </div>
        <div className="login-left md:w-[60%] p-10">
            <div className="login-header">
            <h1 className='text-center'>{user?'Welcome Join us':'Welcome Back!'}</h1>
                <p>Please {user?'Signup':'Login'} to continue</p>
            </div>
            <form action="" className="login-form" autocomplete="off" onSubmit={handlesubmit}>
                <div className="login-content">
                <div className="form-item flex flex-col">
                        <label className=''>Name</label>
                        <input type="text" id="name" required value={data.name} onChange={(e)=>{Setdata({...data,name: e.target.value})}} placeholder="Full Name" className='mb-3 w-full border-1 border-black p-4 rounded-full h-[40px]'/>
                    </div>
                    <div className="form-item flex flex-col">
                        <label className=''>Enter Email</label>
                        <input type="email"  id="email" value={data.email}
                        onChange={(e)=>{Setdata({...data,email: e.target.value})}} 
                        placeholder="example@email.com" required className='mb-3 w-full border-1 border-black p-4 rounded-full h-[40px]'/>
                    </div>
                    <div className="form-item flex flex-col">
                        <label>Enter Password</label>
                        <div className='flex justify-between items-center relative'>
                        <input type={!show?"text":"password"} id="password" value={data.password}
                        onChange={(e)=>{Setdata({...data,password: e.target.value})}} 
                        placeholder="Enter your Password" required className="mb-3 w-full border-1 border-black p-4 rounded-full h-[45px] "/>
                        <img src={show? img2 : img3} onClick={()=>{setShow(!show)}} id="eyeicon" className="w-[25px] absolute right-3 top-4 cursor-pointer"/>
                        </div>
                    </div>
                    <div className="flex justify-between mb-4">
                        <div className="checkbox">
                            <input type="checkbox" name="" id="rememberMeCheckbox" className='mr-1 w-5'/>
                            <label className="checkboxlabel cursor-pointer" for="rememberMeCheckbox">Remember Me</label>
                        </div>
                        {user?<div></div>:<div className="remember-forgot">
                        <a href="#">Forgot password?</a></div>}
                    </div>

                    <div className="bg-grey mb-4">
                        <div className="sing-up">{user?'Have an account?':'Dont have an account?'} <Link to={"/login"} className="no-underline" id="sign-up" >Login</Link></div>
                    </div>
                </div>
                <button type='submit' className='  flex w-full h-[45px]  rounded-full items-center justify-center bg-gray-200 mb-3 no-underline hover:bg-black hover:text-white'>Signup</button>
                <div className="login-footer">
                    <div className='relative'>
                    <div className={`${isHovered? "absolute":"hidden"} left-40 bottom-8 bg-white text-black p-1 rounded-lg`}>Currently Unavailable</div>
                    <button onMouseEnter={() => setIsHovered(true)}
        onMouseLeave={() => setIsHovered(false)} type='button' href="" className=' text-black flex w-full h-[40px]  rounded-full items-center justify-center bg-gray-200 mb-2 no-underline hover:bg-black disabled'>
                        <img width="30" src="https://img.icons8.com/color/512/facebook-new.png" alt="facebook" disabled="true"/>Facebook
                    </button>
                    </div>
                    <div>
                    <button onMouseEnter={() => setIsHovered(true)}
        onMouseLeave={() => setIsHovered(false)} href="" type='button' className=' text-black  flex w-full h-[40px]  rounded-full items-center justify-center bg-gray-200 no-underline hover:bg-black'>
                        <img width="30" src="https://img.icons8.com/fluency/512/google-logo.png" alt="google" disabled="true"/>Google
                    </button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</div>
  )
}

export default Signup;