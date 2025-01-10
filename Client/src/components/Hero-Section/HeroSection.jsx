import React from "react";
import { Link } from "react-router-dom";
import { Container, Row, Col } from "reactstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faRocket } from "@fortawesome/free-solid-svg-icons";
import heroImg from "../../assests/images/2204_w037_n003_308b_p1_308.jpg";
import "./hero-section.css";
import { useContext } from "react";
import { Contextfirst } from "../..";



const HeroSection = () => {

  return (
<section className="-mt-10 sm:mt-0 bg-gradient-to-r from-blue-100">
  <Container className="relative">

    <Row>
      <Col lg="6" md="6" className="w-full">
        <div className="hero__content">
          <h2 className="mb-4 hero__title">
            Ascend Academically
            <FontAwesomeIcon
              icon={faRocket}
              style={{ color: "#74C0FC" }}
              className="ml-2"
            />
            <br /> Elevate Your Learning <br /> Journey and Excel in Studies
          </h2>
          <p className="mb-5 text-black font-sans">
            Simplify academics with ease. Upload math problems or text, receive
            instant solutions or paraphrased notes. Enjoy spell check, grammar
            correction, and text extraction from images. Streamline your
            learning experience today.
          </p>
        </div>
        <div className="w-full">
          <Link to={"/divein"}>
            <button className="btn rounded-full w-full">Dive In</button>
          </Link>
        </div>
      </Col>


          <Col lg="6" md="6">
            <img src={heroImg} alt="" className="w-100 h-full rounded-2xl object-cover" />
          </Col>
        </Row>
      </Container>
    </section>
  );
};

export default HeroSection;
