import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';

function UserProfile() {
    const { username } = useParams();
    const [state, setState] = useState(null);

    const getUserData = async () => {
        const response = await axios.get('http://localhost:8000/api/getUser/', {
            params: {
                username: username
            }
        });

        console.log(response);
    
        return response.data;
    }

    useEffect(() => {
        const userReciever = async () => {
            let userData = await getUserData();
            setState(userData);
        }

        userReciever();
    }, []);
    
    return (
        state ? (
            <>
                <h1>{state.username}</h1>
                <h2>Posts: {state.posts}</h2>
                <Link to='/posts/new'>Create new post</Link>
            </>
        ) : (
            <h1>Loading...</h1>
        )
    );
}

export default UserProfile;