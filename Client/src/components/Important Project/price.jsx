import React from 'react';
import './price.css'; // Importing the CSS file
import img1 from './icons/icon1.png'
import img2 from './icons/icon2.png'
import img3 from './icons/icon3.png'
import { Link } from 'react-router-dom';

function PricingPlan({ imgSrc, header, features, price, buttonText, isFeatured,link }) {
    return (
        <Link to={link} className='no-underline'>
        <div className="pricing-box">
            <img src={imgSrc} alt="" className="pricing-image" />
            <h2 className="pricing-heading">{header}</h2>
            <ul className="pricing-features">
                {features.map((feature, index) => (
                    <li key={index} className="pricing-feature-item">{feature}</li>
                ))}
            </ul>
            <span className="pricing-price">{price}</span>
            <a href="#/" className={`pricing-action ${isFeatured ? 'is-featured' : ''}`}>{buttonText}</a>
        </div>
        </Link>
    );
}

function PriceTiers() {
    return (
        <div className="price-body" id='bodynice'>
        <div className="panel-container">
            <PricingPlan
                imgSrc={img1}
                header="Personal"
                features={["Custom domains", "Sleeps after 30 mins of inactivity"]}
                price="Free"
                buttonText="Free Trial"
                link="/payment?key1=Personal&key2=Free"
            />
            <PricingPlan
                imgSrc={img2}
                header="Small team"
                features={["Never sleeps", "Multiple workers for more powerful apps"]}
                price="$150"
                buttonText="Free trial"
                isFeatured
                link="/payment?key1=Small+Team&key2=150"
            />
            <PricingPlan
                imgSrc={img3}
                header="Enterprise"
                features={["Dedicated", "Simple horizontal scalability"]}
                price="$400"
                buttonText="Free trial"
                link="/payment?key1=Enterprise&key2=400"
            />
        </div>
        </div>
    );
}

export default PriceTiers;
