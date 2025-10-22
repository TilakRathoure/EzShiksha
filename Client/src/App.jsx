import Home from "./pages/Home";
import { BrowserRouter as Router,Route,Routes } from "react-router-dom";
import First from "./pages/First";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import Divein from "./pages/Divein";
import Formula from "./pages/Formula";
import axios from "axios"
import { Toaster } from "react-hot-toast";
import Extract from "./pages/Extract";
import Paraphrasing from "./pages/Paraphrasing";
import Notemaking from "./pages/Notemaking";
import PriceTiers from "./components/Important Project/price";
import UpgradePlan from "./components/Payment/Payment";
import './style.css'
import './index.css'
import { useEffect } from "react";
import { server } from ".";
import { useContext } from "react";
import { Contextfirst } from ".";
import Videos from "./pages/Videos";
import Feedback from "./pages/Feedback";
import Header from "./components/Header/Header";
import Footer from "./components/Footer/Footer";


function App() {

  const {Setauthentication,Setuser,authentication,user} = useContext(Contextfirst)

  useEffect(()=>{
    
    axios.get(`${server}/users/me`,{
      withCredentials:true,
    }).then((res)=>{

      const nice=()=>{
        Setuser(res.data.user.name)
        Setauthentication(true);
      }
      nice();

    }).catch((error)=>{
      Setauthentication(false)
    })
  },[authentication,user]);

  return(
    <Router>
      <Header />
      <Routes>
      <Route path="/notemaking" element={<Notemaking/>}/>
        <Route path="/paraphrase" element={<Paraphrasing/>}/>
        <Route path="/extract" element={<Extract/>}/>
        <Route path="/signup" element={<Signup/>}/>
        <Route path="/login" element={<Login/>}/>
        <Route path="/formula" element={<Formula/>}/>
        <Route path="/" element={<First/>}/>
        <Route path="/home" element={<Home/>}/>
        <Route path="/divein" element={<Divein/>}/>
        <Route path="/subscription" element={<PriceTiers/>}/>
        <Route path="/payment" element={<UpgradePlan/>}/>
        <Route path="/videos" element={<Videos/>}/>
        <Route path="/feedback" element={<Feedback/>}/>
      </Routes>
      <Toaster/>
      <Footer/>
    </Router>
  )
}

export default App;
