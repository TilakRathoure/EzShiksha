import React, { useContext } from "react";
import { Link, Navigate, useNavigate } from "react-router-dom";
import img1 from "../assests/images/unnamed.webp";
import formula from "../assests/images/calculating (1).png";
import note from "../assests/images/writing.png";
import para from "../assests/images/grammar.png";
import { Contextfirst } from "..";

const First = () => {
  const navigate = useNavigate();
  const { authentication } = useContext(Contextfirst);

  if (authentication) {
    return <Navigate to={"/home"} />;
  }

  return (
    <div className="w-full h-[100vh] flex flex-col md:flex-row items-center md:pl-4 p-3">
      <div className="md:w-[60%] h-[70vh]  bg-[#17bf9e] w-full rounded-xl p-4">
        <div className="flex gap-3 mb-5">
          <img src={img1} className="w-[45px] object-contain" alt="" />
          <h1>EzShiksha.</h1>
        </div>
        <div className="flex w-full gap-4 justify-evenly">
          <div className="bg-white w-[25%] h-[250px] flex flex-col items-center justify-center rounded-2xl shadow-2xl p-2 hover:scale-105 transition translate-y-2">
            <img
              src={formula}
              className="w-[50%] h-[30%] object-contain"
              alt=""
            />
            <h5 className="text-[13px] md:text-xl">Solving Questions</h5>
            <p className="text-black text-[10px] lg:text-lg leading-[18px] lg:overflow-hidden">
              Snap, solve. Math made easy. Revolutionize your learning!
            </p>
          </div>
          <div className="bg-white w-[25%] h-[250px] flex flex-col items-center justify-center rounded-2xl shadow-2xl p-2 pt-4 hover:scale-105 transition">
            <img src={note} className="w-[50%] h-[30%] object-contain" alt="" />
            <h5 className="text-sm md:text-xl">Note Making</h5>
            <p className="text-black text-[10px] lg:text-lg leading-[18px] lg:overflow-hidden">
              Upload image, get concise notes instantly. Simplify your studies!{" "}
            </p>
          </div>
          <div className="bg-white w-[25%] h-[250px] flex flex-col items-center justify-center rounded-2xl shadow-2xl p-2 hover:scale-105 transition translate-y-2 text-wrap">
            <img src={para} className="w-[50%] h-[30%] object-contain" alt="" />
            <h5 className="text-sm md:text-xl text-center">Grammar, Spell Check</h5>
            <p className="text-black text-[10px] lg:overflow-hidden lg:text-lg leading-[18px]">
              Upload text or image, get paraphrased version instantly.
            </p>
          </div>
        </div>
        <div>
          <p className="text-white mt-8 text-right font-bold">and more.</p>
        </div>
      </div>
      <div className="h-[70vh] w-[40%] flex flex-col items-center justify-center">
        <div className="flex flex-col gap-3">
          <h2>Get Started</h2>
          <div className="">
            <Link
              className="no-underline px-[1.25rem] py-2 border-1  rounded-md hover:bg-[#077e67] bg-[#17bf9e] text-black "
              to={"/login"}
            >
              Login
            </Link>
            <Link
              className="no-underline px-[1rem] py-2 border-1  rounded-md bg-[#17bf9e] hover:bg-[#077e67] text-black ml-4"
              to={"/signup"}
            >
              Signup
            </Link>
          </div>
          <Link to={"/home"}>
            <span className=" flex-none cursor-pointer px-3  rounded-md text-black">
              Login Later
            </span>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default First;
