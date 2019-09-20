import React, { useState } from 'react';
import './App.css';
import Loginform from './components/Loginform';
function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="App">
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
      <Loginform />
    </div>
  );
}

export default App;
