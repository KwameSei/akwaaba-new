// import React from "react";
// import { Card, CardMedia, CardContent, CardActions, Typography, Button } from "@mui/icons-material";
// import { AddShoppingCart } from "@mui/icons-material";

// import "./EventStyles.css";
// const classes = useStyles();

// export const SingleEvent = ({ event }) => {
//     return (
//         <Card className="root">
//             <CardMedia className={classes.media} image='' title={event.title} />
//             <CardContent>
//                 <div className="cardContent">
//                     <Typography variant="h5" gutterBottom>
//                         {event.title}
//                     </Typography>
//                     <Typography variant="h5">
//                         {event.price}
//                     </Typography>
//                 </div>
//                 <Typography variant="h2" color="textSecondary">{event.description}</Typography>
//             </CardContent>
//             <CardActions disableSpacing className="cardActions">
//                 <Button aria-label="Add to Cart">
//                     <AddShoppingCart />
//                 </Button>
//             </CardActions>
//         </Card>
//     )
// }