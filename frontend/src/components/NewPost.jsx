import axios from 'axios';
import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

const NewPost = () => {
    const [state, setState] = useState({
        title: '',
        content: ''
    });

    const navigate = useNavigate();

    let handleChange = (field, value) => {
        setState({
            ...state,
            [field]: value
        });
    }

    let handleSubmit = async (event) => {
        event.preventDefault();
        let response = await axios.post('/api/createPost/', state);
        
        navigate(`/posts/${response.data.postId}`);
    }

    return (
        <form onSubmit={(e) => handleSubmit(e)}>
            <input type="text" value={state.title} onChange={(e) => handleChange('title', e.target.value)} placeholder="Your post's title"/>
            <textarea value={state.content} onChange={(e) => handleChange('content', e.target.value)} cols="30" rows="10" placeholder="Your post's content"/>

            <button type="submit">Create post</button>
        </form>
    )
}

export default NewPost;