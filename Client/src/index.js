import React, { createContext,useState } from "react";
import ReactDOM from "react-dom";

import App from "./App";
import "bootstrap/dist/css/bootstrap.css";
import "remixicon/fonts/remixicon.css";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

export const server="http://localhost:5000/api/v1";

export const Contextfirst=createContext()


const Appwrapper = () =>{

  const [authentication,Setauthentication]=useState(false)
  const [user,Setuser]=useState("");

  return (
    <Contextfirst.Provider value={{authentication,Setauthentication,user,Setuser}}>
      <App />
    </Contextfirst.Provider>
  )
}

ReactDOM.render(
  <React.StrictMode>
    <Appwrapper/>
  </React.StrictMode>,
  document.getElementById("root")
);
