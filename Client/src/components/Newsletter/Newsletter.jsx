import React, { useState } from "react";
import toast from "react-hot-toast";

const Newsletter = () => {
  const [change, setChange] = useState(false);
  const [email, setEmail] = useState(""); 

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!email) {
      toast.error("email not entered")
      return;
    }
    setChange((prev) => !prev);
  };

  return (
    <div className="w-full flex justify-center items-center">
      <div className="w-[75%] max-w-[700px] min-w-[400px] bg-[#69ecd2] p-5 rounded-3xl my-12">
        <h2 className="mb-4 text-nowrap">Subscribe Our Newsletter</h2>
        <div className="flex w-full justify-center rounded-3xl">
          <form onSubmit={handleSubmit}>
            <div className="flex justify-between w-full bg-white rounded-full">
              <input
                type="email"
                placeholder="Email"
                className="pl-4 rounded-full flex-1 outline-none"
                value={email}
                onChange={(e) => setEmail(e.target.value)} // Capture email input
              />
              <button type="submit" className="btn rounded-full">
                {change ? "Unsubscribe" : "Subscribe"}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Newsletter;
