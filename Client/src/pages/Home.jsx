import { useEffect } from "react";
import HeroSection from "../components/Hero-Section/HeroSection";
import CompanySection from "../components/Company-section/Company";
import AboutUs from "../components/About-us/AboutUs";
import ChooseUs from "../components/Choose-us/ChooseUs";
import Features from "../components/Feature-section/Features";
import Testimonials from "../components/Testimonial/Testimonials";
import Newsletter from "../components/Newsletter/Newsletter";

const Home = () => {

  useEffect(() => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  }, []);

  return (
    <div className="overflow-hidden">
      <HeroSection />
      <CompanySection />
      <AboutUs />
      <ChooseUs />
      <Features />
      <Testimonials />
      <Newsletter />
    </div>
  );
};

export default Home;
