import './StocksPanel.css';
import React from 'react';
import StocksCard from '../StocksCard/StocksCard';
import _ from 'lodash';

import { tsvParse, csvParse } from  "d3-dsv";
import { timeParse } from "d3-time-format";

import { getData } from "../utils";
import Chart from '../Chart';
import { TypeChooser } from "react-stockcharts/lib/helper";

const parseDate = timeParse("%Y-%m-%d");

class StocksPanel extends React.Component {
  
  constructor() {
    super();
    this.state = { stocks:null, pageNum:1, loadedAll:false, data:null };
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

    loadMoreStocks() {

        console.log(this.state.pageNum);

        let url = 'http://localhost:4000/stocks/userId/yifant/pageNum/' + this.state.pageNum;

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
        })

    }

    renderStocks() {

        let num = 0;
        const stocks_list = this.state.stocks.map(function(stocks) {

            console.log(stocks);

            num += 1;
            if (! (typeof stocks.history === "undefined")) {
                stocks.history = stocks.history.map((day) => {
                    return {
                            date: parseDate(day[1]),
                            open: day[2],
                            high: day[3],
                            low: day[4],
                            close: day[5],
                            volume: day[6] 
                        }
                    });
                console.log(stocks.history);
            }


            // let CommentList = (

                // stocks.new_StockTwits_comments.map(function(comment) {

                //     return(
                //         <a className='list-group-item' href='#'>
                //             { comment.created_at }
                //         </a>
                //     )

                // });

            // );

            if(!(typeof stocks.new_StockTwits_comments === "undefined")) {

                let commentsList = stocks.new_StockTwits_comments.splice(0,3).map(function(comment) {
                    
                                        return(
                                            <a className='collection-item' href='#'>
                                                <li> { comment.body } </li>
                                                <br/>
                                            </a>
                                        )
                    
                                    });

                console.log(stocks.new_StockTwits_comments);

                return(
                    // <div className="container">
                        <a className='list-group-item' href='#'>
                            <StocksCard stocks={stocks} />
                            <div className="row">
                                <div className="col s8">
                                    <TypeChooser>
                                        {type => <Chart type={type} data={ stocks.history } />}
                                    </TypeChooser> 
                                </div>
                                <div className="col s4">

                                    {/* <StocksCard stocks={stocks} /> */}
                                    {/* { stocks.new_StockTwits_comments } */}
                                    {/* Comments: { stocks.new_StockTwits_comments.length } */}
                                    
                                    
                                    <ul class="collection with-header">
                                        <li class="collection-header"><h4>Comments:</h4></li>
                                        { commentsList }
                                    </ul>
                                </div>
                            </div>
                            {/* <StocksCard stocks={stocks} /> */}
                            =====================================================================
                        </a>
                        // <br/>
                    // </div>
                );
            } else {
                return(
                    <a className='list-group-item' href='#'>
                        <StocksCard stocks={stocks} />
                        {/* <TypeChooser>
                            {type => <Chart type={type} data={ stocks.history } />}
                        </TypeChooser>  */}
                        {/* <StocksCard stocks={stocks} /> */}
                        =====================================================================
                    </a>
                );
            }

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
                // <TypeChooser>
                //     {type => <Chart type={type} data={this.state.data.splice(1,80)} />}
                // </TypeChooser> 
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