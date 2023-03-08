// Calling the api service from the component
import React from 'react';
import { useGetEventsQuery} from '../../features/FeaturedEvents/eventsApi';
import '../Events/EventStyles.css';
import { useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { addItemToCart } from '../../features/cartSlice';

const Events = () => {
    const { data, error, isLoading } = useGetEventsQuery();
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const handleAddEventToCart = (event) => {
        dispatch(addItemToCart(event))
        // Redirect to cart page when user clicks on buy ticket
        navigate('/cart');
    };
    // if (isLoading) {
    //     return <p>Loading...</p>;
    // }

    // if (error) {
    //     return <p>Something went wrong... {error.data}</p>;
    // }

    return (
        <div className='events-container'>
            {isLoading ? ( 
                <p>Loading...</p> 
                ) : error ? ( 
                <p>Something went wrong... {error.data}</p> 
                ) : (
                    <>
                    <h2>Latest Events</h2>
                    <div className='events'>
                        {data.map( event => <div className='event' key={event.id}>
                            <h3>{event.title}</h3>
                            <img src={event.featuredImage} alt={event.title} />
                            <div className='event-info'>
                                <span>{event.description}</span>
                                <span className='cost'>₵{event.cost}</span>
                            </div>
                            <div className='button-container'>
                                <button onClick={() => handleAddEventToCart(event)}>Buy Ticket</button>
                            </div>
                        </div>)}
                    </div>
                    </>
                )}
        </div>

            /* <div className='events'>
                {data.map((event) => (
                    <div key={event.id} className='event'>
                        <h3>{event.title}</h3>
                        <img src={event.featuredImage} alt='event.title' />
                        {console.log(event)};
                        <div className='event-info'>
                            <span>{event.description}</span>
                            <span className='cost'>${event.cost}</span>
                        </div>
                        <button>Buy Ticket</button>
                    </div>
                ))}
            </div> */
    );
};

export default Events;

// import React from "react";
// import { Grid } from "@mui/material/Grid";

// import SingleEvent from "./SingleEvent";

// const events = [
//     { id: "e1", title: "Programming for everyone", price: "5", description: "In this event, we will learn programming together", location: "Somewhere in the world", date: "2021-05-12" },
//     { id: "e2", title: "Networking for introverts", price: "17", description: "You probably need this event", location: "Somewhere in the world", date: "2021-05-30" },
//     { id: "e3", title: "Networking for extroverts", price: "24", description: "You probably need this event", location: "Somewhere in the world", date: "2021-05-30" },
//     { id: "e4", title: "A fun evening with friends", price: "3", description: "Just a nearby event with friends", location: "Somewhere in the world", date: "2021-05-30"},
// ]

// export const AllEvents = () => {
//     return (
//         <main>
//         <Grid container justify="center" spacing={4}>
//             {events.map((event) => (
//                 <Grid item key={event.id} xs={12} sm={6} md={4}>
//                     <SingleEvent event={event} />
//                 </Grid>
//             ))}
//         </Grid>
//     </main>
//     )
// }