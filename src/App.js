import Home from "./pages/Home";
import { BrowserRouter as Router,Route,Routes } from "react-router-dom";
import First from "./pages/First";
import Signup from "./components/Login/Signup";
import Login from "./components/Login/Login";
import './style.css'


function App() {
  return(
    <Router>
      <Routes>
        <Route path="/signup" element={<Signup/>}/>
        <Route path="/login" element={<Login/>}/>
        <Route path="/" element={<First/>}/>
        <Route path="/home" element={<Home/>}/>
      </Routes>
    </Router>
  )
}

export default App;
