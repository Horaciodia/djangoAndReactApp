import './App.css';
import SignUp from './components/SignUp.jsx';
import Login from './components/Login.jsx';
import UserProfile from './components/User.jsx';
import NewPost from './components/NewPost.jsx';
import { Route, Routes, BrowserRouter as Router } from 'react-router-dom';

function App() {
  return (
  <div>
    <Router>
      <Routes>
        <Route path='/signup' exact element={<SignUp />} />
        <Route path='/login' exact element={<Login />} />
        <Route path='/user/:username' exact element={<UserProfile />} />
        <Route path='/posts/new' exact element={<NewPost />} />
      </Routes> 
    </Router> 
  </div>);
}
  

export default App;
