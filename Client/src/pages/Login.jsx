import React, { useContext, useState } from "react";
import { Link, Navigate } from "react-router-dom";
import img1 from "../assests/images/computer-login-concept-illustration_114360-7962.avif";
import img2 from "./images/eye-close.png";
import img3 from "./images/eye-open.png";
import axios from "axios";
import toast from "react-hot-toast";
import { Contextfirst, server } from "..";

const Login = () => {
  const [isHovered, setIsHovered] = useState(false);
  const { authentication, Setauthentication } = useContext(Contextfirst);
  const [user, setUser] = useState(false);
  const [show, Setshow] = useState(true);
  const [data, Setdata] = useState({
    email: "",
    password: "",
  });

  const handlesubmit = async (e) => {
    e.preventDefault();
    const { email, password } = data;
    try {
      const { data: res } = await axios.post(
        `${server}/users/login`,
        { email, password },
        {
          headers: { "Content-Type": "application/json" },
          withCredentials: true,
        }
      );
      toast.success("Logged In Successfully");
      Setauthentication(true);
    } catch (e) {
      toast.error(e.response?.data?.message || "Login failed");
    }
  };

  if (authentication) {
    return <Navigate to="/home" />;
  }

  return (
    <div>
      <div className="p-5 md:flex w-[100vw] border-2" id="home">
        <div className="login-left md:w-[60%] p-10">
          <div className="login-header">
            <h1 className="text-center text-2xl font-semibold mb-2">
              {user ? "Welcome Join us" : "Welcome Back!"}
            </h1>
            <p className="text-center text-gray-600 mb-6">
              Please {user ? "Signup" : "Login"} to continue
            </p>
          </div>

          <form
            className="login-form"
            autoComplete="off"
            onSubmit={handlesubmit}
          >
            <div className="login-content">
              <div className="form-item flex flex-col mb-4">
                <label>Enter Email</label>
                <input
                  type="email"
                  value={data.email}
                  onChange={(e) => Setdata({ ...data, email: e.target.value })}
                  placeholder="example@email.com"
                  className="border border-gray-400 rounded-full px-4 py-2 h-[40px] focus:outline-none focus:ring-2 focus:ring-black"
                />
              </div>

              <div className="form-item flex flex-col mb-4">
                <label>Enter Password</label>
                <div className="flex items-center relative">
                  <input
                    type={!show ? "text" : "password"}
                    value={data.password}
                    onChange={(e) =>
                      Setdata({ ...data, password: e.target.value })
                    }
                    placeholder="Enter your Password"
                    required
                    className="border border-gray-400 rounded-full px-4 py-2 w-full h-[45px] focus:outline-none focus:ring-2 focus:ring-black"
                  />
                  <img
                    src={show ? img2 : img3}
                    onClick={() => Setshow(!show)}
                    className="w-[25px] absolute right-3 top-3 cursor-pointer"
                    alt="toggle visibility"
                  />
                </div>
              </div>

              <div className="flex justify-between items-center mb-4">
                <div className="checkbox flex items-center">
                  <input
                    type="checkbox"
                    id="rememberMeCheckbox"
                    className="mr-2 w-4 h-4"
                  />
                  <label
                    htmlFor="rememberMeCheckbox"
                    className="cursor-pointer text-sm"
                  >
                    Remember Me
                  </label>
                </div>
                {!user && (
                  <a href="#" className="text-sm text-gray-500 hover:underline">
                    Forgot password?
                  </a>
                )}
              </div>

              <button
                type="submit"
                className="flex w-full h-[45px] rounded-full items-center justify-center bg-black text-white mb-3 hover:bg-gray-800 transition"
              >
                Login
              </button>

              <Link
                to="/home"
                className="flex items-center justify-center gap-2 text-gray-700 hover:text-black transition mb-5"
              >
                <span className="underline underline-offset-4">
                  Login Later
                </span>
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

              <div className="bg-grey mb-4 text-center text-sm">
                {user ? "Have an account?" : "Don't have an account?"}{" "}
                <Link
                  to="/signup"
                  className="text-black underline underline-offset-2 hover:text-gray-700"
                >
                  Signup
                </Link>
              </div>
            </div>

            <div className="login-footer">
              <div className="relative mb-2">
                <div
                  className={`${
                    isHovered ? "absolute" : "hidden"
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

        <div className="login-right md:w-[40%]">
          <img className="h-full object-contain" src={img1} alt="" />
        </div>
      </div>
    </div>
  );
};

export default Login;
