import React from "react";
import { Container, Row, Col } from "reactstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faRocket } from "@fortawesome/free-solid-svg-icons";
import heroImg from "../../assests/images/2204_w037_n003_308b_p1_308.jpg";
import "./hero-section.css";



const HeroSection = () => {

  return (
    <section className="bg-gradient-to-r from-blue-100">
      <Container>
        <Row>
          <Col lg="6" md="6">
            <div className="hero__content">
              <h2 className="mb-4 hero__title">
              Ascend Academically<FontAwesomeIcon icon={faRocket} style={{color: "#74C0FC",}} className="ml-2"/>
               <br /> Elevate Your Learning <br /> Journey and Excel in Studies
              </h2>
              <p className="mb-5 text-black font-sans">
              EzShiksha offers instant paraphrasing for uploaded text and solves math problems from images. It's a revolutionary tool, simplifying academic tasks with efficiency and ease, making studying hassle-free.
              </p>
            </div>
            <div className="flex w-full justify-start rounded-3xl mb-3">
              <button className=" btn rounded-full w-[500px]">Dive In</button>
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
