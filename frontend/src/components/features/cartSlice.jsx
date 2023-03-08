import { createSlice } from "@reduxjs/toolkit";
import { toast } from "react-toastify";

const initialState = {
    cartItems: localStorage.getItem('cartItems') ? JSON.parse(localStorage.getItem('cartItems')) : [],
    cartTotalQuantity: 0,
    cartTotalPrice: 0,
};

const cartSlice = createSlice({
    name: 'cart',
    initialState,
    reducers: {
        addItemToCart(state, action) {
            const itemIndex = state.cartItems.findIndex(
                (item) => item.id === action.payload.id
            );
            if (itemIndex >= 0) {
                state.cartItems[itemIndex].cartQuantity += 1;
                toast.info(`${state.cartItems[itemIndex].title} Ticket's Quantity Increased by 1`, {
                    position: 'top-center',
                });
            } else {
                const tempEvent = { ...action.payload, cartQuantity: 1 };
                state.cartItems.push(tempEvent);
                toast.success(`Great! ${action.payload.title} Ticket Added to Cart`, {
                    position: 'top-center',
                });
            }
            // Adding cart items to the local storage to persist the cart items
            // even when the user refreshes the page
            localStorage.setItem('cartItems', JSON.stringify(state.cartItems));
        },
         
    },
});

export const { addItemToCart } = cartSlice.actions;

export default cartSlice.reducer;
