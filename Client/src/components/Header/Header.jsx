import React, { useContext, useRef } from "react";
import { Link, Navigate } from "react-router-dom";
import { Button, Container } from "reactstrap";
import img1 from "../../assests/images/unnamed.webp";
import "./header.css";
import { Contextfirst } from "../..";
import axios from "axios";
import { server } from "../..";
import toast from "react-hot-toast";

const navLinks = [
  {
    display: "Home",
    url: "/home",
  },
  {
    display: <Button className="btn">Dive In</Button>,
    url: "/divein",
  },
  {
    display: "Subscription",
    url: "/subscription",
  },
  {
    display: "Resources",
    url: "/videos",
  }
];

const Header = () => {

  const {authentication,Setauthentication}=useContext(Contextfirst);

  const menuRef = useRef();

  const menuToggle = () => menuRef.current.classList.toggle("active__menu");

  const Logout=()=>{
    axios.get(`${server}/users/logout`,{
      withCredentials:true,
    }).then((res)=>{
      Setauthentication(false);
      toast.success("Logged Out")
    }).catch((error)=>{
      Setauthentication(true);
    })
  }

  if(!authentication){
    return(
      <Navigate to={"/"}/>
    )
  }

  return (
    <header className=" bg-gradient-to-r from-blue-100">
      <Container>
        <div className="navigation d-flex items-center justify-content-between">
          <div className="logo mt-3">
            <h2 className=" d-flex align-items-center gap-1">
              <img src={img1} className="w-20 object-contain mr-2" alt="" /> EzShiksha.
            </h2>
          </div>

          <div className="nav d-flex align-items-center gap-5">
            <div className="nav__menu" ref={menuRef} onClick={menuToggle}>
              <ul className="nav__list flex items-center justify-center">
                {navLinks.map((item, index) => (
                  <li key={index} className="nav__item">
                    <Link to={item.url}>{item.display}</Link>
                  </li>
                ))}
                {authentication? <button className="btn p-1" onClick={Logout}>Logout</button> : <li></li>}
              </ul>
            </div>

            <div className="nav__right">
              <p className="mb-0 d-flex align-items-center gap-2">
              </p>
            </div>
          </div>

          <div className="mobile__menu">
            <span>
              <i class="ri-menu-line" onClick={menuToggle}></i>
            </span>
          </div>
        </div>
      </Container>
    </header>
  );
};

export default Header;
