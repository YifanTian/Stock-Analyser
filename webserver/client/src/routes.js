import Base from './Base/Base';
import App from './App/App';
import LoginPage from './Login/LoginPage';
import SignUpPage from './SignUp/SignUpPage';
import StocksPanel from './StocksPanel/StocksPanel';
import StockDetail from './StockDetail/StockDetail';
import Auth from './Auth/Auth';

const routes = {
  component: Base,
  // <Route name="stock" path="stock/:stockIndex" handler={}/>
  childRoutes: [
    // {
    //   path: '/:pageNum',
    //   getComponent: (location, callback) => {
    //     // if (Auth.isUserAuthenticated()) {
    //     //   callback(null, App);
    //     // } else {
    //     //   callback(null, LoginPage);
    //     // }
    //     callback(null, App);
    //   }
    // },

    // {
    //   path: '/:pageNum',
    //   component: App
    // },

    {
      path: '/:pageNum',
      component: StocksPanel
    },

    {
        path:'/',
        component: StocksPanel
    },

    {
      name: 'stockDetail',
      path: '/stock/:stockIndex',
      component: StockDetail
    },

    {
      path: '/login',
      component: LoginPage
    },

    {
      path: '/signup',
      component: SignUpPage
    },

    {
      path: '/logout',
      onEnter: (nextState, replace) => {
        Auth.deauthenticate();

        replace('/login');
      }
    }
  ]
};

export default routes;
