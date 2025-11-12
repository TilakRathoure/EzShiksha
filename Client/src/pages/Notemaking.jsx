import React, { useState, useEffect, useRef } from "react";
import toast from "react-hot-toast";
import axios from "axios";
import { server } from "..";
import Loader from "./Loader";
import { Link } from "react-router-dom";

const Notemaking = () => {
  const [inputText, setInputText] = useState("");
  const [summaryOutput, setSummaryOutput] = useState("");
  const [notesOutput, setNotesOutput] = useState("");
  const [disable, setDisable] = useState(false);
  const [loader, setLoader] = useState(false);

  const controllerRef = useRef(null);

  const handleRequest = async (type) => {
    if (!inputText || inputText.length <= 20) {
      toast.error("Too short");
      return;
    }

    setDisable(true);
    setLoader(true);

    // Abort any previous pending request
    if (controllerRef.current) controllerRef.current.abort();
    controllerRef.current = new AbortController();

    try {
      const endpoint = type === "summary" ? "summarize" : "note";

      const { data } = await axios.post(
        `${server}/users/${endpoint}`,
        { name: inputText },
        {
          headers: { "Content-Type": "application/json" },
          withCredentials: true,
          signal: controllerRef.current.signal,
          timeout: 50000,
        }
      );

      if (type === "summary") setSummaryOutput(data.trying);
      else setNotesOutput(data.trying);

      toast.success(`${type === "summary" ? "Summary" : "Notes"} Done!`);
    } catch (e) {
      toast.error("This AI model exceeds Render’s free plan limits.");
    } finally {
      setDisable(false);
      setLoader(false);
    }
  };

  const handleClear = () => {
    setInputText("");
    setSummaryOutput("");
    setNotesOutput("");
  };

  return (
    <div className="w-[100vw] flex-col items-center justify-center p-8 border-black">
      <div className="w-full bg-white rounded-lg shadow-lg p-3">
        <h1 className="text-center">Summary and Note Making</h1>
        <div className="flex gap-4 justify-center items-center h-full py-4 px-2">
          <div className="w-[50%] h-full gap-2 flex flex-col justify-start items-center">
            <textarea
              onChange={(e) => setInputText(e.target.value)}
              className="h-[300px] border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent p-2 w-full"
              placeholder="Input text:"
              value={inputText}
            />
            <button
              onClick={() => handleRequest("summary")}
              className="bg-blue-500 text-white font-semibold px-4 py-2 rounded-md w-full hover:bg-blue-600"
              disabled={disable}
            >
              Get Summary
            </button>
            <button
              onClick={() => handleRequest("notes")}
              className="bg-green-500 text-white font-semibold px-4 py-2 rounded-md w-full hover:bg-green-600"
              disabled={disable}
            >
              Get Notes
            </button>
            <button
              onClick={handleClear}
              className="bg-red-500 text-white font-semibold px-4 py-2 rounded-md w-full hover:bg-red-600"
            >
              Clear
            </button>
          </div>

          <div className="flex flex-col items-start justify-center w-[50%] h-full gap-4">
            {loader ? (
              <Loader />
            ) : (
              <>
                <textarea
                  disabled
                  className="h-[150px] p-2 w-full border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  placeholder="Summary"
                  value={summaryOutput}
                />
                <textarea
                  disabled
                  className="h-[150px] p-2 w-full border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  placeholder="Notes"
                  value={notesOutput}
                />
              </>
            )}
          </div>
        </div>
      </div>

      <div className="mt-3 ml-3">
        <Link to="/feedback">
          <button className="btn">Feedback</button>
        </Link>
      </div>
    </div>
  );
};

export default Notemaking;
