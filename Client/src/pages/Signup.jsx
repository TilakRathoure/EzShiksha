import React, { useState, useContext } from 'react';
import { Link, Navigate, useNavigate } from 'react-router-dom';
import img1 from '../assests/images/istockphoto-1281150061-612x612.jpg';
import img2 from './images/eye-close.png';
import img3 from './images/eye-open.png';
import toast from 'react-hot-toast';
import axios from 'axios';
import { Contextfirst, server } from '..';

const Signup = () => {
  const [isHovered, setIsHovered] = useState(false);
  const { authentication, Setauthentication } = useContext(Contextfirst);
  const [user, setUser] = useState(true);
  const [show, setShow] = useState(true);
  const navigate = useNavigate();

  const [data, Setdata] = useState({
    name: '',
    email: '',
    password: '',
  });

  const handlesubmit = async (e) => {
    e.preventDefault();
    const { name, email, password } = data;
    try {
      const { data: res } = await axios.post(
        `${server}/users/new`,
        { name, email, password },
        {
          headers: { 'Content-Type': 'application/json' },
          withCredentials: true,
        }
      );
      toast.success(res.message);
      Setauthentication(true);
      navigate('/home');
    } catch (error) {
      toast.error(error.response?.data?.message || 'Signup failed');
    }
  };

  if (authentication) {
    return <Navigate to="/home" />;
  }

  return (
    <div>
      <div className="p-5 md:flex w-[100vw] border-2" id="home">
        {/* Left Image Section */}
        <div className="flex justify-center items-center login-right md:w-[40%]">
          <img
            className="h-full max-h-[50vh] md:max-h-none object-contain"
            src={img1}
            alt="signup"
          />
        </div>

        {/* Right Signup Form Section */}
        <div className="login-left md:w-[60%] p-10">
          <div className="login-header mb-6">
            <h1 className="text-center text-2xl font-semibold mb-2">
              {user ? 'Welcome Join Us' : 'Welcome Back!'}
            </h1>
            <p className="text-center text-gray-600">
              Please {user ? 'Signup' : 'Login'} to continue
            </p>
          </div>

          <form className="login-form" autoComplete="off" onSubmit={handlesubmit}>
            <div className="login-content">
              {/* Name */}
              <div className="form-item flex flex-col mb-4">
                <label>Name</label>
                <input
                  type="text"
                  id="name"
                  required
                  value={data.name}
                  onChange={(e) => Setdata({ ...data, name: e.target.value })}
                  placeholder="Full Name"
                  className="border border-gray-400 rounded-full px-4 py-2 h-[40px] focus:outline-none focus:ring-2 focus:ring-black"
                />
              </div>

              {/* Email */}
              <div className="form-item flex flex-col mb-4">
                <label>Enter Email</label>
                <input
                  type="email"
                  id="email"
                  required
                  value={data.email}
                  onChange={(e) => Setdata({ ...data, email: e.target.value })}
                  placeholder="example@email.com"
                  className="border border-gray-400 rounded-full px-4 py-2 h-[40px] focus:outline-none focus:ring-2 focus:ring-black"
                />
              </div>

              {/* Password */}
              <div className="form-item flex flex-col mb-4">
                <label>Enter Password</label>
                <div className="flex justify-between items-center relative">
                  <input
                    type={!show ? 'text' : 'password'}
                    id="password"
                    required
                    value={data.password}
                    onChange={(e) =>
                      Setdata({ ...data, password: e.target.value })
                    }
                    placeholder="Enter your Password"
                    className="border border-gray-400 rounded-full px-4 py-2 h-[45px] w-full focus:outline-none focus:ring-2 focus:ring-black"
                  />
                  <img
                    src={show ? img2 : img3}
                    onClick={() => setShow(!show)}
                    id="eyeicon"
                    className="w-[25px] absolute right-3 top-3 cursor-pointer"
                    alt="toggle password visibility"
                  />
                </div>
              </div>

              {/* Remember Me */}
              <div className="flex justify-between mb-4">
                <div className="checkbox flex items-center">
                  <input
                    type="checkbox"
                    id="rememberMeCheckbox"
                    className="mr-2 w-4 h-4"
                  />
                  <label
                    htmlFor="rememberMeCheckbox"
                    className="checkboxlabel cursor-pointer text-sm"
                  >
                    Remember Me
                  </label>
                </div>
              </div>

              {/* Signup Button */}
              <button
                type="submit"
                className="flex w-full h-[45px] rounded-full items-center justify-center bg-black text-white mb-3 hover:bg-gray-800 transition"
              >
                Signup
              </button>

              {/* 👇 Signup Later Button */}
              <Link
                to="/home"
                className="flex items-center justify-center gap-2 text-gray-700 hover:text-black transition mb-5"
              >
                <span className="underline underline-offset-4">Signup Later</span>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  strokeWidth={2}
                  stroke="currentColor"
                  className="w-5 h-5"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    d="M9 5l7 7-7 7"
                  />
                </svg>
              </Link>

              {/* Login Redirect */}
              <div className="bg-grey mb-4 text-center text-sm">
                {user ? 'Have an account?' : "Don't have an account?"}{' '}
                <Link
                  to="/login"
                  className="text-black underline underline-offset-2 hover:text-gray-700"
                >
                  Login
                </Link>
              </div>
            </div>

            {/* Social Buttons */}
            <div className="login-footer">
              <div className="relative mb-2">
                <div
                  className={`${
                    isHovered ? 'absolute' : 'hidden'
                  } left-40 bottom-8 bg-white text-black p-1 rounded-lg`}
                >
                  Currently Unavailable
                </div>
                <button
                  onMouseEnter={() => setIsHovered(true)}
                  onMouseLeave={() => setIsHovered(false)}
                  type="button"
                  className="text-black flex w-full h-[40px] rounded-full items-center justify-center bg-gray-200 mb-2 no-underline hover:bg-black hover:text-white transition"
                >
                  <img
                    width="25"
                    src="https://img.icons8.com/color/512/facebook-new.png"
                    alt="facebook"
                    className="mr-2"
                  />
                  Facebook
                </button>
              </div>

              <div>
                <button
                  onMouseEnter={() => setIsHovered(true)}
                  onMouseLeave={() => setIsHovered(false)}
                  type="button"
                  className="text-black flex w-full h-[40px] rounded-full items-center justify-center bg-gray-200 no-underline hover:bg-black hover:text-white transition"
                >
                  <img
                    width="25"
                    src="https://img.icons8.com/fluency/512/google-logo.png"
                    alt="google"
                    className="mr-2"
                  />
                  Google
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Signup;
