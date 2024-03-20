import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import img1 from '../../assests/images/istockphoto-1281150061-612x612.jpg'
import img2 from './images/eye-close.png'

const Signup = () => {
    const [user,setUser]=useState(true);

  return (
    <div>
    <div className="p-5 flex w-[100vw] h-[100vh] border-2" id="home">
        <div className="login-left w-[60%] p-10">
            <div className="login-header">
            <h1 className='text-center'>{user?'Welcome Join us':'Welcome Back!'}</h1>
                <p>Please {user?'Signup':'Login'} to continue</p>
            </div>
            <form action="" className="login-form" autocomplete="off">
                <div className="login-content">
                    <div className="form-item flex flex-col">
                        <label for="email" className=''>Enter Email</label>
                        <input type="email" name="" id="" placeholder="example@email.com" className='mb-3 w-full border-1 border-black p-4 rounded-full h-[40px]'/>
                    </div>
                    <div className="form-item flex flex-col">
                        <label for="password">Enter Password</label>
                        <div className='flex justify-between items-center relative'>
                        <input type="password" name="" id="password" placeholder="Enter your Password" required className="mb-3 w-full border-1 border-black p-4 rounded-full h-[45px] "/>
                        <img src={img2} id="eyeicon" className="w-[25px] absolute right-3 top-4"/>
                        </div>
                    </div>
                    <div className="flex justify-between mb-4">
                        <div className="checkbox">
                            <input type="checkbox" name="" id="rememberMeCheckbox" className='mr-1 w-5'/>
                            <label for="rememberMeCheckbox" className="checkboxlabel cursor-pointer">Remember Me</label>
                        </div>
                        {user?<div></div>:<div className="remember-forgot">
                        <a href="#">Forgot password?</a></div>}
                    </div>

                    <div className="bg-grey mb-4">
                        <div className="sing-up">{user?'Have an account?':'Dont have an account?'} <a href=""className="no-underline" id="sign-up" >{user?'Login':'Signup'}</a></div>
                    </div>
                </div>
                <Link to={'/login'} className='  flex w-full h-[45px]  rounded-full items-center justify-center bg-gray-200 mb-3 no-underline hover:bg-black hover:text-white'>{user?'Signup':'Login'}</Link>
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

export default Signup;