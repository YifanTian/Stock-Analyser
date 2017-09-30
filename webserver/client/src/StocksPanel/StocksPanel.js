import 'materialize-css/dist/css/materialize.min.css';
import 'materialize-css/dist/js/materialize.js';

import './StocksPanel.css';
import React from 'react';
import StocksCard from '../StocksCard/StocksCard';
import _ from 'lodash';
import 'materialize-css/dist/css/materialize.min.css';
import { Link } from 'react-router'

import { tsvParse, csvParse } from  "d3-dsv";
import { timeParse } from "d3-time-format";

import { getData } from "../utils";
import Chart from '../Chart';
import { TypeChooser } from "react-stockcharts/lib/helper";

const parseDate = timeParse("%Y-%m-%d");

class StocksPanel extends React.Component {
  
  constructor(props) {
    super(props);
    this.state = { stocks:null, pageNum:1, loadedAll:false, data:null };
    this.handleScroll = this.handleScroll.bind(this);
  }

  componentDidMount() {
    this.loadMoreStocks();
    this.loadMoreStocks = _.debounce(this.loadMoreStocks, 1000);
    window.addEventListener('scroll', this.handleScroll);
  }

  handleScroll() {
    // let scrollY = window.scrollY ||
    //               window.pageYOffset ||
    //               document.documentElement.scrollTop;
    // if ((window.innerHeight + scrollY) >= (document.body.offsetHeight - 50)) {
    //   console.log('Loading more news');
    //   this.loadMoreStocks();
    // }
  }

    loadMoreStocks() {

        if (typeof (this.props.params.pageNum) === "undefined") {
            this.props.params.pageNum = 1;
        }

        // let url = 'http://localhost:4000/stocks/userId/yifant/pageNum/' + this.state.pageNum;

        let url = 'http://localhost:4000/stocks/userId/yifant/pageNum/' + this.props.params.pageNum;

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

    activateLasers() {
        console.log("pagination");
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

            var styles1 = {
                color:'red',
            };

            var styles2 = {
                color:'green',
            };

            if(!(typeof stocks.new_StockTwits_comments === "undefined")) {

                let commentsList = stocks.new_StockTwits_comments.splice(0,3).map(function(comment) {
                    
                                        return(
                                            <a className='collection-item' href='#'>
                                                <li> 
                                                    {/* Comment: <p> { comment.body } </p> 
                                                    <br/> */}
                                                     <p> { comment.core_body } </p>
                                                    <p> 
                                                        {/* NLTK: { comment.nltk_sentiment } &nbsp;&nbsp;&nbsp; */}
                                                        {
                                                            comment.nltk_sentiment=="negative"? <h6 style={styles1}> NLTK:  { comment.nltk_sentiment } </h6> : <h6 style={styles2}> NLTK: { comment.nltk_sentiment } </h6>
                                                        }
                                                        {
                                                            comment.azure_sentiment>0.5?  <h6 style={styles1}> Azure:  { comment.azure_sentiment } </h6> : <h6 style={styles2}> Azure: { comment.azure_sentiment } </h6>
                                                        }
                                                          {/* <p style={styles}> { comment.azure_sentiment } </p> */}
                                                     </p>
                                                    {/* Azure: <p> { comment.azure_sentiment } </p> */}
                                                </li> 
                                                <br/> 
                                            </a>
                                        )
                    
                                    });

                console.log(stocks.new_StockTwits_comments);

                return(
                    // <div className="container">
                        <a className='list-group-item' href='#'>
                            <StocksCard stocks={stocks} />
                            <div className="stock-panel">
                                <div className="col s10">
                                    <TypeChooser>
                                        {type => <Chart type={type} data={ stocks.history } />}
                                    </TypeChooser> 
                                </div>
                                <div className="col s10">

                                    {/* <StocksCard stocks={stocks} /> */}
                                    {/* { stocks.new_StockTwits_comments } */}
                                    {/* Comments: { stocks.new_StockTwits_comments.length } */}
                                                                  
                                    <ul className="collection with-header">
                                        <li className="collection-header"><h5>Comments:</h5></li>
                                        { commentsList }
                                    </ul>
                                </div>

                            {/* <a class="waves-effect waves-light btn" onClick={}>Details</a> */}
    <Link className="waves-effect waves-light btn" to="stock/AAPL" params={{stockIndex:'AAPL'}}>Details</Link>
                            </div>
                            {/* <StocksCard stocks={stocks} /> */}

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
                    <div className="stock-panel">
                    {this.renderStocks()}

                    {/* <a className="waves-effect waves-light btn" onClick={this.activateLasers}>Next page</a> */}
                    <ul className="pagination">
                        <li className="disabled"><a href="#!"><i className="material-icons">chevron_left</i></a></li>
                        {/* <li className="active" ><a href="/1">1</a></li> */}
                        <li className="waves-effect"><a href="/1">1</a></li>
                        <li className="waves-effect"><a href="/2">2</a></li>
                        <li className="waves-effect"><a href="/3">3</a></li>
                        <li className="waves-effect"><a href="#!">4</a></li>
                        <li className="waves-effect"><a href="#!">5</a></li>
                        <li className="waves-effect"><a href="#!">
                        <i className="material-icons">chevron_right</i></a></li>
                    </ul>
                    {/* <Link to='/:pagNum' component={ StocksPanel } /> */}

                    </div>
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