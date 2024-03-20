import React from "react";
import { Container, Row, Col, ListGroup, ListGroupItem } from "reactstrap";
import img1 from '../../assests/images/unnamed.webp';


const footerQuickLinks = [
  {
    display: "Home",
    url: "#",
  },
  {
    display: "About US",
    url: "#",
  },

  {
    display: "Blog",
    url: "#",
  },
];

const footerInfoLinks = [
  {
    display: "Privacy Policy",
    url: "#",
  },
  {
    display: "Membership",
    url: "#",
  },

  {
    display: "Purchases Guide",
    url: "#",
  },

  {
    display: "Terms of Service",
    url: "#",
  },
];

const Footer = () => {
  return (
    <footer className="bg-[#17bf9e]">
      <Container className="">
        <Row>
          <Col lg="3" md="6" className="mb-4">
            <h2 className=" d-flex align-items-center gap-1 mb-4">
            <img src={img1} className="w-20 object-contain" alt="" /> EzShiksha.
            </h2>

            <div className="">
              <p className="text-black font-sans font-medium leading-4">© 2024 EzShiksha <p className="text-black font-sans font-medium">All rights reserved.</p></p>
              <p className="">
                <a href="facebook.com" className="no-underline">
                  <i className="ri-facebook-line text-white mr-2 w-[100px]"></i>
                </a>

              <span>
                <a href="facebook.com" className="no-underline">
                  <i class="ri-instagram-line text-white mr-2"></i>
                </a>
              </span>

              <span>
                <a href="facebook.com" className="no-underline">
                  <i class="ri-linkedin-line text-white mr-2"></i>
                </a>
              </span>

              <span className>
                <a href="facebook.com" className="no-underline">
                  <i class="ri-twitter-line text-white"></i>
                </a>
              </span>
              </p>
            </div>
          </Col>

          <Col lg="3" md="6" className="mb-4">
            <h6 className="fw-bold">Explore</h6>
            <ListGroup className="leading-4 ">
              {footerQuickLinks.map((item, index) => (
                <ListGroupItem key={index} className="border-0 ps-0  bg-transparent">
                  {" "}
                  <a href={item.url} className="no-underline text-black">{item.display}</a>
                </ListGroupItem>
              ))}
            </ListGroup>
          </Col>

          <Col lg="3" md="6" className="mb-4">
            <h6 className="fw-bold">Information</h6>
            <ListGroup className="leading-4">
              {footerInfoLinks.map((item, index) => (
                <ListGroupItem key={index} className="border-0 ps-0 bg-transparent">
                  {" "}
                  <a href={item.url} className="no-underline text-black" >{item.display}</a>
                </ListGroupItem>
              ))}
            </ListGroup>
          </Col>

          <Col lg="3" md="6">
            <h6 className="fw-bold mb-4">Get in Touch</h6>
            <p className="leading-4">
            <p className="text-black font-sans font-normal leading-4">Address: Greater Noida,India</p>
            <p className="text-black font-sans font-normal leading-4"> Phone: +88 0123456789 </p>
            <p className="text-black font-sans font-normal leading-4">Email: example@gmail.com</p>
            </p>
          </Col>
        </Row>
      </Container>
    </footer>
  );
};

export default Footer;
