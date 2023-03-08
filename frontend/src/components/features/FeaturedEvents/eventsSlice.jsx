import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';
// import { toast } from 'react-toastify';

// Creating a reducer
const initialState = {
    items: [],
    status: null,
    error: null,
    createStatus: null,
};

// Creating an action
export const fetchEvents = createAsyncThunk(
    'events/fetchEvents', 
    async (id = null, {rejectWithValue}) => {
        try {
            const response = await fetch('/api/v1/events');
            const data = await response.json();
            return data;
        }
        catch (err) {
            return rejectWithValue(err.message);
        }
    });

const accessToken = 'nathaniel';

export const createEvents = createAsyncThunk(
    'events/createEvents', 
    async (values) => {
        try {
            const response = await axios.post('/api/v1/create_event', values, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                    'Authorization': `Bearer ${accessToken}`
                  }
            });
            const data = await response.json();
            return data;
        }
        catch (err) {
            console.log(err);
            // toast.error(err.response?.data)
            return rejectWithValue(err.message);
        }
    });

const eventsSlice = createSlice({
    name: 'events',
    initialState,
    reducers: {},
    // Adding an action to the reducer
    extraReducers: {
        [fetchEvents.pending]: (state, action) => {
            state.status = 'loading';
        },
        [fetchEvents.fulfilled]: (state, action) => {
            state.status = 'succeeded';
            state.items = state.items.concat(action.payload);
        },
        [fetchEvents.rejected]: (state, action) => {
            state.status = 'failed';
            state.error = action.error.message;
        },

        // Creating Events
        [createEvents.pending]: (state, action) => {
            state.createStatus = 'loading';
        },
        [createEvents.fulfilled]: (state, action) => {
            state.createStatus = 'succeeded';
            state.items.push(action.payload);
        },
        [createEvents.rejected]: (state, action) => {
            state.createStatus = 'failed';
            state.error = action.error.message;
        }
    }
    });

export default eventsSlice.reducer;