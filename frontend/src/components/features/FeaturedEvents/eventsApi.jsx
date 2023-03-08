// Register api service to fetch data from the backend
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

// Create a base query to fetch data from the backend
export const eventsApi = createApi({
    reducerPath: 'eventsApi',
    baseQuery: fetchBaseQuery({ baseUrl: 'http://localhost:5000' }),
    endpoints: (builder) => ({
        getEvents: builder.query({
            query: () => '/api/v1/events',
        }),
    }),
});

// Export the hooks to be used in the components
export const { useGetEventsQuery } = eventsApi;