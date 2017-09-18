import 'materialize-css/dist/css/materialize.min.css';

import React, { Component } from 'react';
// import logo from './logo.svg';
import './App.css';
import StocksPanel from '../StocksPanel/StocksPanel';

class App extends Component {
  render() {
    return (
      <div>
      {/* <img className='logo' src={logo} alt='logo'/> */}
        <div className="container">
          Author: Yifan Tian
          <StocksPanel />
        </div>
      </div>
    );
  }
}

export default App;
