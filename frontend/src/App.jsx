import {NavBar} from './components/partials/Top_navbar';
import {
  BrowserRouter as Router,
  Routes, Route, Navigate
} from 'react-router-dom';
import { ToastContainer } from 'react-toastify';

import {HomePage} from './components/Pages/Home';
import {SignUp} from './components/Pages/Sign-Up-In/SignUp';
import {SignIn} from './components/Pages/Sign-Up-In/SignIn';
import {CreateEvent} from './components/Pages/Events/CreateEvent';
import './App.css';
import 'react-toastify/dist/ReactToastify.css';
import {CartPage} from './components/Pages/Cart/CartPage';
import { NotFound } from './components/partials/NotFound';

function App() {
  return (
    <div className="App">
      <Router>
        <ToastContainer />
        <div>
          <NavBar />
          <Routes>
            <Route path='/cart' element={<CartPage />} />
            <Route path='/create-event-page' element={<CreateEvent />} />
            <Route path='/sign-up' element={<SignUp />} />
            <Route path='/sign-in' element={<SignIn />} />
            {/* <Route path='/not-found' element={<NotFound />} /> */}
            <Route path='/' exact element={<HomePage />} />
            <Route path='*' element={<NotFound />} />
          </Routes>
        </div>
      </Router>
    </div>
  );
}

export default App;
