import 'materialize-css/dist/css/materialize.min.css';
import 'materialize-css/dist/js/materialize.js';

import React, { Component } from 'react';
// import logo from './logo.svg';
import './App.css';
import StocksPanel from '../StocksPanel/StocksPanel';

class App extends React.Component {
  render() {
    return (
      <div>
      {/* <img className='logo' src={logo} alt='logo'/> */}
        <div className="container">
          <StocksPanel pageNum = {this.props.pageNum}/>
        </div>
      </div>
    );
  }
}

export default App;
