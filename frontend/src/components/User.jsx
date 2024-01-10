import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';

function UserProfile() {
    const { username } = useParams();

    const [state, setState] = useState({
        username: '',
        posts: [],
    });

    const getUserData = async () => {
        const response = await axios.get('http://localhost:8000/api/getUser/', {
            params: {
                username: username
            }
        });
    
        return response.data;
    }

    let userData = getUserData();
    
    return (
        <>
            <h1>{userData.username}</h1>

            <h2>Posts: {userData.posts}</h2>
            <Link to='/posts/new'>Create new post</Link>
        </>
    )
}

export default UserProfile;