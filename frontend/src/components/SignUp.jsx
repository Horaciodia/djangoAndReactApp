import { useState } from 'react';
import axios from 'axios';

function SignUp() {
    const [state, setState] = useState({
        username: '',
        password: '',
        firstName: '',
        lastName: '', 
        posts: []
    });

    function handler(field, value) {
        setState({
            ...state,
            [field]: value
        });
    }

    async function submitForm(event, state) {
        event.preventDefault();
        console.log(state);

        const response = await axios.post('/api/users/', state);
        console.log(response.data);
    }

    return (
        <form onSubmit={(e) => submitForm(e, state)}>
            <input type="text" name='username' value={state.username} onChange={(e) => handler('username', e.target.value)} placeholder='Username'/>
            <input type="password" name='password' value={state.passowrd} onChange={(e) => handler('password', e.target.value)} placeholder='Password'/>
            <input type="text" name='firstName' value={state.firstName} onChange={(e) => handler('firstName', e.target.value)} placeholder='First Name'/>
            <input type="text" name='lastName' value={state.lastName} onChange={(e) => handler('lastName', e.target.value)} placeholder='Last Name'/>

            <button type='submit'>Submit</button>
        </form>
    )
}

export default SignUp;