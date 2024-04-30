import React from "react";
import { Container, Row, Col } from "reactstrap";
import "./features.css";

const FeatureData = [
  {
    title: "Quick Learning",
    desc: "Accelerate your learning with EzShiksha's intuitive tools. From instant math solutions to concise notes, mastering concepts has never been quicker.",
    icon: "ri-draft-line",
  },

  {
    title: "All Time Support",
    desc: "Count on EzShiksha for round-the-clock assistance. Our platform is here to support you whenever you need help, ensuring continuous learning.",
    icon: "ri-discuss-line",
  },

  {
    title: "Certification",
    desc: "EzShiksha offers certification upon completion, validating your mastery of subjects and enhancing your credentials for future endeavors. Boost your career today!",
    icon: "ri-contacts-book-line",
  },
];

const Features = () => {
  return (
    <section>
      <Container>
        <Row>
          {FeatureData.map((item, index) => (
            <Col lg="4" md="6" key={index}>
              <div className="single__feature text-center px-4">
                <h2 className="mb-3">
                  <i class={item.icon}></i>
                </h2>
                <h6>{item.title}</h6>
                <p>{item.desc}</p>
              </div>
            </Col>
          ))}
        </Row>
      </Container>
    </section>
  );
};

export default Features;
