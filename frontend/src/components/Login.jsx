import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import axios from 'axios';

function Login() {
    const navigate = useNavigate();
    
    const [state, setState] = useState({
        username: '',
        password: ''
    });

    function handler(field, value) {
        setState({
            ...state,
            [field]: value
        });
    }

    async function submitForm(event, state) {
        event.preventDefault();

        const response = await axios.get('http://127.0.0.1:8000/api/users/', { 
            params: { 
                username: state.username, 
                password: state.password 
            } 
        });
        console.log(response);

        navigate(`/user/${state.username}`)
    }

    return (
        <form onSubmit={(e) => submitForm(e, state)}>
            <input type="text" value={state.username} onChange={(e) => handler('username', e.target.value)}/>
            <input type="password" value={state.password} onChange={(e) => handler('password', e.target.value)}/>

            <button type='submit'>Submit</button>
        </form>
    )
}

export default Login;