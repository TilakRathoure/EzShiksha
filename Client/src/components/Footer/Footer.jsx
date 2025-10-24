import React from "react";
import { Container, Row, Col } from "reactstrap";
import img1 from "../../assests/images/unnamed.webp";

const Footer = () => {
  return (
    <footer className="bg-[#17bf9e]">
      <Container>
        <Row>
          {/* Logo and Information */}
          <Col lg="3" md="6" className="mb-4">
            <h2 className="d-flex align-items-center gap-1 mb-4">
              <img src={img1} className="w-20 object-contain" alt="logo" /> EzShiksha.
            </h2>
            <div>
              <p className="text-black font-sans font-medium leading-4">
                © 2024 EzShiksha{" "}
                <span className="text-black font-sans font-medium">
                  All rights reserved.
                </span>
              </p>

              {/* Social Media Icons */}
              <div className="mt-2 flex items-center gap-4">
                <a
                  className="link-noundy"
                  href="https://linkedin.com/in/tilakrathoure"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  <i className="ri-linkedin-line text-white text-3xl hover:text-black transition-colors"></i>
                </a>
                <a
                  href="https://github.com/TilakRathoure"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="link-noundy"
                >
                  <i className="ri-github-line text-white text-3xl hover:text-black transition-colors"></i>
                </a>
              </div>
            </div>
          </Col>

          {/* Explore Section */}
          <Col lg="3" md="6" className="mb-4">
            <h6 className="fw-bold">Explore</h6>
            <p className="text-black font-sans">Find various educational resources.</p>
          </Col>

          {/* Information Section */}
          <Col lg="3" md="6" className="mb-4">
            <h6 className="fw-bold">Information</h6>
            <p className="text-black font-sans">Learn more about our policies and services.</p>
          </Col>
        </Row>
      </Container>
    </footer>
  );
};

export default Footer;
