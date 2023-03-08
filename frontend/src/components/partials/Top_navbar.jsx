import React from "react";
import './Top-nav.css'
import { Link } from "react-router-dom";
import { FaHome } from "react-icons/fa";
import { FaSignInAlt } from "react-icons/fa";
import { FaSignOutAlt } from "react-icons/fa";
import { SiGnuprivacyguard } from "react-icons/si";
import { FaCartArrowDown } from "react-icons/fa";
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
// import { solid, regular, brands, icon } from '@fortawesome/fontawesome-svg-core/import.macro'

export const NavBar = () => {
    return (
      <nav className="nav-bar">
        <Link to='/' className="link">
          <div className="brand">
            <img src="./akwaaba-low-white.png" width='40px' height='40px' alt="logo" />
          </div>
        </Link>
        <Link to='/' className="link">
          <div className="nav"><FaHome className="icon" />Home</div>
        </Link>
        <Link to='/sign-up' className="link">
          <div className="nav"><SiGnuprivacyguard className="icon" />Sign Up</div>
        </Link>
        <Link to='/sign-in' className="link">
          <div className="nav"><FaSignInAlt className="icon" />Sign In</div>
        </Link>
        <Link to='/cart' className="link">
          <div className="nav"><FaCartArrowDown className="icon" />
            <span className="cart-quantity">3</span>
          </div>
        </Link>
          <div className="nav logout"><FaSignOutAlt className="icon" />Log Out</div>
        
      </nav>
      // <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      //   <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      //     <span className="navbar-toggler-icon"></span>
      //   </button>

      //   <div className="collapse navbar-collapse" id="navbarSupportedContent">
      //     <ul className="navbar-nav mr-auto">
      //     <Link className="navbar-brand active" to='/'>
      //       {/* <img src="./public/akwaaba-logo.png" width="30" height="30" alt="" /> */}
      //       <h4>akwaaba</h4>
      //     </Link>
      //       <li className="nav-item active">
      //         <Link className="nav-link" to='/'>Home <span className="sr-only">(current)</span></Link>
      //       </li>
      //       <li className="nav-item">
      //         <Link className="nav-link active" to='/sign-up'>Register</Link>
      //       </li>
      //       <li className="nav-item">
      //         <Link className="nav-link active" to='/sign-in'>Sign In</Link>
      //       </li>
      //       <li className="nav-item">
      //         <Link className="nav-link active" to='create-event-page'>Create Event</Link>
      //       </li>
      //       <li className="nav-item dropdown">
      //         <Link className="nav-link dropdown-toggle"  role="button" data-toggle="dropdown" aria-expanded="false">
      //           Dropdown
      //         </Link>
      //         <div className="dropdown-menu">
      //           <Link className="dropdown-item" >Action</Link>
      //           <Link className="dropdown-item" >Another action</Link>
      //           <div className="dropdown-divider"></div>
      //           <Link className="dropdown-item" >Something else here</Link>
      //         </div>
      //       </li>
      //       <li className="nav-item">
      //         <Link className="nav-link">Log Out</Link>
      //       </li>
      //     </ul>
      //   </div>
      // </nav>
    )
}

// export default NavBar