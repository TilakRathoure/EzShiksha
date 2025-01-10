import React, { useState } from 'react';
import toast from 'react-hot-toast';

const Feedback = () => {
  const [text, setText] = useState("");
  const [email, setEmail] = useState("");

  const onSubmit = (e) => {
    e.preventDefault();

    if (text && email) {
      toast.success("Feedback sent successfully!");
    } else {
      toast.error("Please fill out all fields.");
    }
  };

  return (
    <div className="w-full h-[100vh] flex justify-center items-center bg-gradient-to-r from-blue-100 to-green-200">
      <div className="w-[90%] sm:w-[75%] max-w-[700px] bg-[rgb(105,236,210)] p-8 rounded-3xl my-12 border-black border-1 shadow-xl">
        <h2 className="mb-6 text-2xl font-semibold text-center">Send Feedback!</h2>
        
        <form onSubmit={onSubmit} className="space-y-4">
          {/* Email Input */}
          <input
            type="email"
            placeholder="Your Email"
            className="pl-4 rounded-full w-full outline-none p-3 bg-white text-gray-800 placeholder-gray-500 shadow-md focus:ring-2 focus:ring-blue-500 transition-all"
            value={email}
            required
            onChange={(e) => setEmail(e.target.value)}
          />

          {/* Feedback Input */}
          <textarea
            placeholder="Your Feedback"
            className="pl-4 pt-3 pb-2 rounded-xl w-full outline-none bg-white text-gray-800 placeholder-gray-500 shadow-md focus:ring-2 focus:ring-blue-500 transition-all"
            value={text}
            required
            onChange={(e) => setText(e.target.value)}
          />

          {/* Submit Button */}
          <button type="submit" className="w-full py-3 mt-4 bg-[#17bf9e] text-white rounded-full font-semibold hover:bg-[#077e67] transition-all">
            Send Feedback
          </button>
        </form>
      </div>
    </div>
  );
};

export default Feedback;
