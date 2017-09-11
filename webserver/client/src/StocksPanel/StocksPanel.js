import './StocksPanel.css';
import React from 'react';
import StocksCard from '../StocksCard/StocksCard';
import _ from 'lodash';

class StocksPanel extends React.Component {
  
  constructor() {
    super();
    this.state = { stocks:null, pageNum:1, loadedAll:false };
    this.handleScroll = this.handleScroll.bind(this);
  }

  componentDidMount() {
    this.loadMoreStocks();
    this.loadMoreStocks = _.debounce(this.loadMoreStocks, 1000);
    window.addEventListener('scroll', this.handleScroll);
  }

  handleScroll() {
    let scrollY = window.scrollY ||
                  window.pageYOffset ||
                  document.documentElement.scrollTop;
    if ((window.innerHeight + scrollY) >= (document.body.offsetHeight - 50)) {
      console.log('Loading more news');
      this.loadMoreStocks();
    }
  }


    // print(share.get_open())
    // print(share.get_price())
    // print(share.get_trade_datetime())
    // print(share.get_volume())
    // print(share.get_avg_daily_volume())
    // print(share.get_days_high())
    // print(share.get_days_low())

    loadMoreStocks() {
        // console.log(this.state.stocks);
        // this.setState({
        //     stocks:[
        //         {
        //             'url':'',
        //             'title':'AGTC',
        //             'open': 4.7,
        //             'price': 4.8,
        //             'volume': 45239,
        //             'trade_datetime': '2017-09-07 20:00:00 UTC+0000',
        //             'reason':'recommand'
        //         },
        //         {
        //             'url':'',
        //             'title':'AGTC',
        //             'open': 4.7,
        //             'price': 4.8,
        //             'volume': 45239,
        //             'trade_datetime': '2017-09-07 20:00:00 UTC+0000',
        //             'reason':'hot'
        //         }]
        // });

        // let url = 'http://localhost:3000/news/userId/' + Auth.getEmail()
        // + '/pageNum/' + this.state.pageNum;

        // let url = 'http://localhost:3000/stocks/userId/' + 'yifant'
        // + '/pageNum/' + this.state.pageNum;

        console.log(this.state.pageNum);

        let url = 'http://localhost:4000/stocks/userId/yifant/pageNum/1';

        console.log(url);

        let request = new Request(encodeURI(url), {
        method: 'GET',
        cache: false
        });

        fetch(request)
        .then((res) => res.json())
        .then((stocks) => {
            console.log(stocks);
            this.setState({
            stocks:this.state.stocks ? this.state.stocks.concat(stocks) : stocks,
            pageNum: this.state.pageNum + 1
            });
        });

    }

    renderStocks() {
        const stocks_list = this.state.stocks.map(function(stocks) {



            console.log(stocks.history);
            if (! (typeof stocks.history === "undefined")) {
                stocks.history = stocks.history.map((day)=>[day[0],day[2]]);
            }
            // } else {
            //     stocks.history = [];
            // }

            // stocks.history = [
            //         [ 10, 490 ],
            //         [ 140, 380 ],
            //         [ 310, 420 ],
            //         [ 490, 10 ]
            //     ];
            console.log(stocks.history);

            return(
                <a className='list-group-item' href='#'>
                    <StocksCard stocks={stocks} />
                </a>
            );
        });

        return(
            <div className='container-fluid'>
                <div className='list-group'>
                    {stocks_list}
                </div>
            </div>
        )
    }

    render() {
        console.log(this.state.stocks);
        if(this.state.stocks) {
            return(
                <div>
                    {this.renderStocks()}
                </div>
            );
        } else {
            return(
                <div>
                    <div id='msg-app-loading'>
                        Loading...
                    </div>
                </div>
            );
        }
    }

}

export default StocksPanel