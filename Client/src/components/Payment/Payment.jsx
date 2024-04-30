import React from 'react';
import './style.css';
import { useLocation} from 'react-router-dom';

function UpgradePlan() {

    const location = useLocation();
    const queryParams = new URLSearchParams(location.search);

    const key1 = queryParams.get('key1');
    const key2 = queryParams.get('key2');

    return (
        <div className="container mt-5 mb-5 flex justify-center">
            <div className="card p-5">
                <div>
                    <h4 className="heading">Upgrade your plan</h4>
                    <p className="text">Please make the payment to start enjoying all the features of our premium plan as soon as possible</p>
                </div>
                <div className="pricing p-3 rounded mt-4 flex justify-between">
                    <div className="images flex flex-row items-center">
                        <img src="https://i.imgur.com/S17BrTx.png" className="rounded" alt="Small Business" width="60" />
                        <div className="flex flex-col ml-4">
                            <span className="business">{key1}</span>
                            <span className="plan">CHANGE PLAN</span>
                        </div>
                    </div>
                    <div className="flex flex-row items-center">
                        <sup className="dollar font-bold">$</sup>
                        <span className="amount ml-1 mr-1">{key2}</span>
                        { key2==="Free"? <div></div>:
                        <span className="year font-bold">/ year</span>}
                    </div>
                </div>
                <span className="detail mt-5">Payment details</span>
                <div className="credit rounded mt-4 flex justify-between items-center">
                    <div className="flex flex-row items-center">
                        <img src="https://i.imgur.com/qHX7vY1.png" className="rounded" alt="Credit Card" width="70" />
                        <div className="flex flex-col ml-3">
                            <span className="business">Credit Card</span>
                            <span className="plan">1234 XXXX XXXX 2570</span>
                        </div>
                    </div>
                    <div>
                        <input type="text" className="form-control cvv" placeholder="CVC" />
                    </div>
                </div>
                <div className="credit rounded mt-2 flex justify-between items-center">
                    <div className="flex flex-row items-center">
                        <img src="https://i.imgur.com/qHX7vY1.png" className="rounded" alt="Credit Card" width="70" />
                        <div className="flex flex-col ml-3">
                            <span className="business">Debit Card</span>
                            <span className="plan">2344 XXXX XXXX 8880</span>
                        </div>
                    </div>
                    <div>
                        <input type="text" className="form-control cvv" placeholder="CVC" />
                    </div>
                </div>
                <h6 className="mt-4 text-primary">ADD PAYMENT METHOD</h6>
                <div className="email mt-2">
                    <input type="text" className="form-control email-text" placeholder="Email Address" />
                </div>
                <div className="mt-3">
                    <button className="btn btn-primary btn-block payment-button">Proceed to payment <i className="fa fa-long-arrow-right"></i></button>
                </div>
            </div>
        </div>
    );
}

export default UpgradePlan;
