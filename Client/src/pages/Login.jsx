import React, { useContext, useState } from 'react'
import { Link, Navigate } from 'react-router-dom'
import img1 from '../assests/images/computer-login-concept-illustration_114360-7962.avif'
import img2 from './images/eye-close.png'
import img3 from './images/eye-open.png'
import axios from 'axios'
import toast from 'react-hot-toast'
import {Contextfirst, server} from '..'

const Login = () => {


    const {authentication,Setauthentication} = useContext(Contextfirst)

    const [user,setUser]=useState(false);
    const [show,Setshow]=useState(true);
    const [data,Setdata]=useState({
        email:"",
        password:""
    })


    const handlesubmit=async(e)=>{
        e.preventDefault();
        const {email,password}=data
        try{
            const {data}=await axios.post(`${server}/users/login`,{
                email,password
            },{headers:{
                "Content-Type":"application/json",
            },withCredentials:true});
            toast.success("Logged In Successfully");
            Setauthentication(true);
        }catch(e){toast.error(e.response.data.message)}
    }

    if(authentication){
        return(
            <Navigate to={"/home"}/>
        )
    }

  return (
    <div>
    <div className="p-5 flex w-[100vw] h-[100vh] border-2" id="home">
        <div className="login-left w-[60%] p-10">
            <div className="login-header">
            <h1 className='text-center'>{user?'Welcome Join us':'Welcome Back!'}</h1>
                <p>Please {user?'Signup':'Login'} to continue</p>
            </div>
            <form action="" className="login-form" autocomplete="off" onSubmit={handlesubmit}>
                <div className="login-content">
                    <div className="form-item flex flex-col">
                        <label className=''>Enter Email</label>
                        <input type="email" name="email" id="email" value={data.email}
                        onChange={(e)=>{Setdata({...data,email: e.target.value})}}  placeholder="example@email.com" className='mb-3 w-full border-1 border-black p-4 rounded-full h-[40px]'/>
                    </div>
                    <div className="form-item flex flex-col">
                        <label>Enter Password</label>
                        <div className='flex justify-between items-center relative'>
                        <input type="password" name="password" id="password" value={data.password}
                        onChange={(e)=>{Setdata({...data,password: e.target.value})}}  placeholder="Enter your Password" required className="mb-3 w-full border-1 border-black p-4 rounded-full h-[45px] "/>
                        <img src={show? img2 : img3} id="eyeicon" onClick={()=>{Setshow(!show)}} className="w-[25px] absolute right-3 top-4 cursor-pointer"/>
                        </div>
                    </div>
                    <div className="flex justify-between mb-4">
                        <div className="checkbox">
                            <input type="checkbox" name="" id="rememberMeCheckbox" className='mr-1 w-5'/>
                            <label className="checkboxlabel cursor-pointer">Remember Me</label>
                        </div>
                        {user?<div></div>:<div className="remember-forgot">
                        <a href="#">Forgot password?</a></div>}
                    </div>

                    <div className="bg-grey mb-4">
                        <div className="sing-up">{user?'Have an account?':'Dont have an account?'} <Link to={"/signup"} className="no-underline" id="sign-up" >Signup</Link></div>
                    </div>
                </div>
                <button type='submit' className='flex w-full h-[45px]  rounded-full items-center justify-center bg-gray-200 mb-3 no-underline hover:bg-black hover:text-white'>Login</button>
                <div className="login-footer">
                    <a href="" className=' text-black flex w-full h-[40px]  rounded-full items-center justify-center bg-gray-200 mb-2 no-underline hover:bg-black'>
                        <img width="30" src="https://img.icons8.com/color/512/facebook-new.png" alt="facebook"/>Facebook
                    </a>
                    <a href="" className=' text-black  flex w-full h-[40px]  rounded-full items-center justify-center bg-gray-200 no-underline hover:bg-black'>
                        <img width="30" src="https://img.icons8.com/fluency/512/google-logo.png" alt="google"/>Google
                    </a>
                </div>
            </form>
        </div>
        <div className="login-right w-[40%] ">
            <img className='h-full object-contain' src={img1} alt="" />
        </div>
    </div>
</div>
  )
}

export default Login;