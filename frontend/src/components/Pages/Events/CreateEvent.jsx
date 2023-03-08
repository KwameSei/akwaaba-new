import React, { useState } from "react";
import { useDispatch } from "react-redux";
import axios from 'axios';
import './EventStyles.css';
import { createEvents } from "../../features/FeaturedEvents/eventsSlice";

// function ImageUpload({ onSuccess }) {
//   const [imageUrl, setImageUrl] = useState('');

//   function handleSuccess(res) {
//     setImageUrl(res.url);
//     onSuccess(res.url);
//   }

//   function handleError(err) {
//     console.error(err);
//   }

//   function handleRemove() {
//     setImageUrl('');
//   }
  
//   return (
//     <div>
//         <input type="file" name="file" onChange={event => {
//             const file = event.target.files[0];
//             const formData = new FormData();
//             formData.append('file', file);
//             console.log(event.target.files[0])
//             fetch('/api/v1/image_upload', {
//                 method: 'POST',
//                 body: formData
//         })
//           .then(res => {
//             if (!res.ok) {
//               throw new Error('Image upload failed');
//             }
//             return res.json();
//           })
//           .then(data => handleSuccess(data))
//           .catch(err => handleError(err));
//         }}
//         />
//         {imageUrl && (
//             <div className="image-preview" style={{ display: 'flex', alignItems: 'center' }}>
//                 <img src={imageUrl} alt="uploaded display" style={{ width: '100px', height: '100px', marginRight: '10px' }} />
//                 <button onClick={handleRemove}>Remove</button>
//             </div>
//         )}
//     </div>
//   );
// }

export const CreateEvent = () => {

    const dispatch = useDispatch();

    const [user_id, setUser_id] = useState('');
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [featuredImage, setFeaturedImage] = useState(null);
    const [category, setCategory] = useState('');
    const [start_date, setStart_date] = useState('');
    const [end_date, setEnd_date] = useState('');
    const [location, setLocation] = useState('');
    const [region, setRegion] = useState('');
    const [cost, setCost] = useState('');
    const [registration, setRegistration] = useState('');
    const [isPublic, setIsPublic] = useState('');
    const [views, setViews] = useState('');

    console.log(featuredImage);

    function handleImageUpload(event) {
        const file = event.target.files[0];
        console.log("The file uploaded is " + file)   
        convertFile(file);
    }
    // Convert file to base64
    function convertFile(file) {
        const reader = new FileReader();
        if (file) {
            reader.readAsDataURL(file);
            reader.onload = () => {
                setFeaturedImage(reader.result);
            };
        } else {
            setFeaturedImage(null);
        }
    }

    function handleSubmit(event) {
        event.preventDefault();
    
        const formData = new FormData();
        formData.append('user_id', user_id);
        formData.append('title', title);
        formData.append('description', description);
        formData.append('category', category);
        formData.append('start_date', start_date);
        formData.append('end_date', end_date);
        formData.append('location', location);
        formData.append('region', region);
        formData.append('cost', cost);
        formData.append('registration', registration);
        formData.append('isPublic', isPublic);
        formData.append('views', views);
        formData.append('file', featuredImage);
    
        dispatch(createEvents(formData));
    }
    // function handleError(err) {
    // console.error(err);
    // }
    
    // function handleRemove() {
    // setFeaturedImage('');
    // }

    // async function addEvent(event) {
    //     event.preventDefault();

    //     // Ensure that featuredImage is not null
    //     if (!featuredImage) {
    //         console.error('Featured Image is required');
    //         return;
    //     }

    //     try {
    //         const formData = new FormData();
    //             formData.append('user_id', user_id);
    //             formData.append('title', title);
    //             formData.append('description', description);
    //             formData.append('category', category);
    //             formData.append('start_date', start_date);
    //             formData.append('end_date', end_date);
    //             formData.append('location', location);
    //             formData.append('region', region);
    //             formData.append('cost', cost);
    //             formData.append('registration', registration);
    //             formData.append('isPublic', isPublic);
    //             formData.append('views', views);
    //             formData.append('file', featuredImage);

    //         const response = await axios.post('/api/v1/create_event', formData, {
    //             headers: {
    //                 'Content-Type': 'application/json'
    //             },
    //         })
    //         .then(response => response.json())
    //         .then(data => {
    //             console.log('Success:', data);
    //         })
    //         .catch((error) => {
    //             console.error('Error:', error);
    //         })
            
    //         // console.log(response);
    //         // console.log(response.data);

    //         resetForm();

    //         } catch (error) {
    //         console.error(error);
    //         }
    //     };

    //     const resetForm = () => {
    //         setUser_id('');
    //         setTitle('');
    //         setDescription('');
    //         setFeaturedImage('');
    //         setCategory('');
    //         setStart_date('');
    //         setEnd_date('');
    //         setLocation('');
    //         setRegion('');
    //         setCost('');
    //         setRegistration('');
    //         setIsPublic('');
    //         setViews('');
    //     };
    // function handleSubmit(event) {
    //     event.preventDefault();
    //     // send data to server
    //     fetch('/api/v1/create_event', {
    //         method: 'POST',
    //         body: JSON.stringify({
    //             title,
    //             description,
    //             featuredImage,
    //             category,
    //             start_date,
    //             end_date,
    //             location,
    //             region,
    //             cost,
    //             registration,
    //             isPublic,
    //             views
    //         }),
    //         headers: {
    //             'Content-Type': 'application/json'
    //         }
    //     })
    //     .then(res => {
    //         if (!res.ok) {
    //             throw new Error('Event creation failed');
    //         }
    //         return res.json();
    //     })
    //     .then(event => {
    //         console.log(event);
    //         setTitle('');
    //         setDescription('');
    //         setFeaturedImage('');
    //         setCategory('');
    //         setStart_date('');
    //         setEnd_date('');
    //         setLocation('');
    //         setRegion('');
    //         setCost('');
    //         setRegistration('');
    //         setIsPublic('');
    //         setViews('');
    //     })
    //     .catch(err => console.error(err));
    // }

    return (
        // <form onSubmit={handleSubmit} className="main" encType="multipart/form-data">
        //     <div>
        //         <label htmlFor="featuredImage">Featured Image:</label>
        //         <input
        //             type="file"
        //             id="featuredImage"
        //             name="file"
        //             accept="image/*"
        //             onChange={handleFileChange}
        //         />
        //     </div>

        /* <input type="file" name="file" onChange={event => {
            const file = event.target.files[0];
            const formData = new FormData();
            formData.append('file', file);
            console.log(event.target.files[0])
            fetch('/api/v1/image_upload', {
                method: 'POST',
                body: formData
        })
          .then(res => {
            if (!res.ok) {
              throw new Error('Image upload failed');
            }
            return res.json();
          })
          .then(data => handleSuccess(data))
          .catch(err => handleError(err));
        }}
        /> */
        /* {imageUrl && (
            <div className="image-preview" style={{ display: 'flex', alignItems: 'center' }}>
                <img src={imageUrl} alt="uploaded display" style={{ width: '100px', height: '100px', marginRight: '10px' }} />
                <button onClick={handleRemove}>Remove</button>
            </div>
        )} */
            /* <div>
                <label htmlFor="user_id">User ID</label>
                <input type="text" name="user_id" value={user_id} onChange={event => setUser_id(event.target.value)} />
            </div>
            <div>
                <label htmlFor="title">Title</label>
                <input type="text" name="title" value={title} onChange={event => setTitle(event.target.value)} />
            </div>
            <div>
                <label htmlFor="description">Description</label>
                <textarea name="description" value={description} onChange={event => setDescription(event.target.value)} />
            </div> */
            /* <div>
                <label htmlFor="featuredImage">Featured Image</label>
                <ImageUpload onSuccess={handleImageUploadSuccess} />
            </div> */
            /* <div>
                <label htmlFor="category">Category</label>
                <input type="text" name="category" value={category} onChange={event => setCategory(event.target.value)} />
            </div>
            <div>
                <label htmlFor="start_date">Start Date</label>
                <input type="text" name="start_date" value={start_date} onChange={event => setStart_date(event.target.value)} />
            </div>
            <div>
                <label htmlFor="end_date">End Date</label>
                <input type="text" name="end_date" value={end_date} onChange={event => setEnd_date(event.target.value)} />
            </div>
            <div>
                <label htmlFor="location">Location</label>
                <input type="text" name="location" value={location} onChange={event => setLocation(event.target.value)} />
            </div>
            <div>
                <label htmlFor="region">Region</label>
                <input type="text" name="region" value={region} onChange={event => setRegion(event.target.value)} />
            </div>
            <div>
                <label htmlFor="cost">Cost</label>
                <input type="text" name="cost" value={cost} onChange={event => setCost(event.target.value)} />
            </div>
            <div>
                <label htmlFor="registration">Registration</label>
                <input type="text" name="registration" value={registration} onChange={event => setRegistration(event.target.value)} />
            </div>
            <div>
                <label htmlFor="isPublic">Is Public</label>
                <input type="text" name="isPublic" value={isPublic} onChange={event => setIsPublic(event.target.value)} />
            </div>
            <div>
                <label htmlFor="views">Views</label>
                <input type="text" name="views" value={views} onChange={event => setViews(event.target.value)} />
            </div>
            <button type="submit">Create Event</button>
        </form> */

        <div className="main">
            <form className="form" onSubmit={handleSubmit} encType='multipart/form-data'>
                <input className="form-control" 
                    type="file"
                    name="file"
                    id="featuredImage"
                    placeholder="Featured Image"
                    accept="image/*"
                    onChange={handleImageUpload}
                    required
                />
                <input className="form-control" 
                    type="text"
                    name="user_id"
                    placeholder="User ID"
                    onChange={event => setUser_id(event.target.value)} 
                />
                <input className="form-control" 
                    type="text"
                    name="title"
                    placeholder="Title"
                    onChange={event => setTitle(event.target.value)} 
                />
                <input className="form-control" 
                    type="text"
                    name="description"
                    placeholder="Description"
                    onChange={event => setDescription(event.target.value)} 
                />
                <input className="form-control" 
                    type="text"
                    name="category"
                    placeholder="Category"
                    onChange={event => setCategory(event.target.value)} 
                />
                <input className="form-control" 
                    type="text"
                    name="start_date"
                    placeholder="Start Date"
                    onChange={event => setStart_date(event.target.value)} 
                />
                <input className="form-control"
                    type="text"
                    name="end_date"
                    placeholder="End Date"
                    onChange={event => setEnd_date(event.target.value)}
                />
                <input className="form-control"
                    type="text"
                    name="location"
                    placeholder="Location"
                    onChange={event => setLocation(event.target.value)}
                />
                <input className="form-control"
                    type="text"
                    name="region"
                    placeholder="Region"
                    onChange={event => setRegion(event.target.value)}
                />
                <input className="form-control"
                    type="text"
                    name="cost"
                    placeholder="Cost"
                    onChange={event => setCost(event.target.value)}
                />
                <input className="form-control"
                    type="text"
                    name="registration"
                    placeholder="Registration"
                    onChange={event => setRegistration(event.target.value)} 
                />
                <input className="form-control"
                    type="text"
                    name="isPublic"
                    placeholder="Is Public"
                    onChange={event => setIsPublic(event.target.value)}
                />
                <input className="form-control"
                    type="text"
                    name="views"
                    placeholder="Views"
                    onChange={event => setViews(event.target.value)}   
                />
                <button type="submit" className="btn btn-primary">Create Event</button>
            </form>
        </div>
    )
}

// export default ImageUpload;