import React from 'react';
import ReactDOM from 'react-dom';
import App from './App/App';
import './index.css';

import { browserHistory, Router } from 'react-router';
import routes from './routes';

ReactDOM.render(
  // <App />,
  <Router history={browserHistory} routes={routes} />,
  document.getElementById('root')
)
