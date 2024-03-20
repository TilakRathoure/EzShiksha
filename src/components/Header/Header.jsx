import React, { useRef } from "react";
import { Button, Container } from "reactstrap";
import img1 from "../../assests/images/unnamed.webp";
import "./header.css";

const navLinks = [
  {
    display: "Home",
    url: "#",
  },
  {
    display: <Button className="btn">Dive In</Button>,
    url: "#",
  },
  {
    display: "Services",
    url: "#",
  },
  {
    display: "Subscription",
    url: "#",
  },
];

const Header = () => {
  const menuRef = useRef();

  const menuToggle = () => menuRef.current.classList.toggle("active__menu");

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
                    <a href={item.url}>{item.display}</a>
                  </li>
                ))}
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
