import React from 'react';
import { createRoot } from 'react-dom/client';
import { configureStore, createReducer } from '@reduxjs/toolkit';
import { Provider } from 'react-redux';

import 'bootstrap/dist/css/bootstrap.min.css';

import App from './App';

// REDUX TOOLKIT
import eventsReducer, { fetchEvents } from '../src/components/features/FeaturedEvents/eventsSlice';
import { eventsApi } from './components/features/FeaturedEvents/eventsApi';
import cartReducer from './components/features/cartSlice';	
// Adding reducers to the store
const store = configureStore({
  reducer: {
    events: eventsReducer,
    cart: cartReducer,
    // [counterApi.reducerPath]: counterApi.reducer,
    [eventsApi.reducerPath]: eventsApi.reducer,
  },
  // Configure the middleware
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(eventsApi.middleware),
});

store.dispatch(fetchEvents());

const root = createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>
);
