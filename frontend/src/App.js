import './App.css';
import Home from './components/Home.jsx';
import { Route, Routes, BrowserRouter as Router } from 'react-router-dom';

function App() {
  return (
  <div>
    <Router>
      <Routes>
        <Route path='/' exact element={<Home />} />
      </Routes> 
    </Router> 
  </div>);
}
  

export default App;
