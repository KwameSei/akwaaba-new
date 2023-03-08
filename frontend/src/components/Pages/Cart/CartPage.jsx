import React from "react";
import { useSelector } from "react-redux";
import { Link } from "react-router-dom";
import { BsFillArrowLeftCircleFill } from "react-icons/bs";
import './CartStyle.css';

export const CartPage = () => {
    const cart = useSelector(state => state.cart);
    console.log(cart);

    return (
        <div className="cart-container">
            <h2>Tickets You've Requested to Buy</h2>
            { cart.cartItems.length === 0 ? (
                <div className="empty-cart">
                    <p> You currently do not have any ticket to buy</p>
                    <div className="start-shopping">
                        <Link to="/"> 
                            <span> <BsFillArrowLeftCircleFill /> Buy Ticket</span>
                        </Link>
                    </div>
                </div>
            ) : (
                <div>
                    <div className="titles">
                        <h3 className="item-title">Items</h3>
                        <h3 className="price">Price</h3>
                        <h3 className="quantity">Quantity</h3>
                        <h3 className="total">Total</h3>
                    </div>
                    <div className="cart-items">
                        {cart.cartItems.map(item => (
                            <div className="cart-item" key={item.id}>
                                <div className="one-item">
                                    <img src={item.featuredImage} alt={item.title} />
                                    <div className="item-info">
                                        <h3>{item.title}</h3>
                                        <p>{item.description}</p>
                                        <button>Remove</button>
                                    </div>
                                </div>
                                <div className="item-price">₵{item.cost}</div>
                                <div className="item-quantity">
                                    <button><span className="button-sign">-</span></button>
                                        <div className="count">{item.cartQuantity}</div>
                                    <button><span className="button-sign">+</span></button>
                                </div>
                                <div className="item-total">
                                    ₵{item.cost * item.cartQuantity}
                                </div>
                            </div> 
                        ))}
                    </div>
                    <div className="summary">
                        <button className="clear-cart">Clear Items</button>
                        <div className="checkout">
                            <div className="subtotal">
                                <span>SUBTOTAL</span>
                                <span className="amount">₵{cart.cartTotalPrice}</span>
                            </div>
                            <p>Taxes may apply</p>
                            <button className="checkout-btn">Buy</button>
                            <div className="start-shopping">
                                <Link to="/"> 
                                    <span> <BsFillArrowLeftCircleFill /> Buy More Tickets </span>
                                </Link>
                            </div>
                        </div>
                    </div>
                </div>
            )}
        </div>
    )
}