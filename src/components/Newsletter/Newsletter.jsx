import React from "react";

const Newsletter = () => {
  return (
    <div className="w-full flex justify-center">
      <div className="w-[75%] max-w-[700px] bg-[#69ecd2] p-5 rounded-3xl my-12">
            <h2 className="mb-4">Subscribe Our Newsletter</h2>
            <div className="flex w-full justify-center rounded-3xl">
              <div className="flex justify-between w-full bg-white rounded-full">
              <input type="text" placeholder="Email" className="pl-4 rounded-full flex-1 outline-none" />
              <button className=" btn rounded-full">Subscribe</button>
              </div>
            </div>
      </div>
      </div>
  );
};

export default Newsletter;
