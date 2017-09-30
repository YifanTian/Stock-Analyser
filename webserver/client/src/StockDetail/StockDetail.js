

import React from 'react';
import './StockDetail.css';

class StockDetail extends React.Component {

    constructor(props) {
        super(props);
        this.state = { stock:null, loadedAll:false, data:null };
        // this.handleScroll = this.handleScroll.bind(this);
      }

      componentDidMount() {
        this.loadStock();
      }

      loadStock() {
        
                console.log(this.props.params.stockIndex);
        
                // let url = 'http://localhost:4000/stocks/userId/yifant/pageNum/' + this.state.pageNum;
        
                let url = 'http://localhost:4000/stocks/userId/yifant/stockIndex/' + this.props.params.stockIndex;
        
                console.log(url);
        
                let request = new Request(encodeURI(url), {
                method: 'GET',
                cache: false
                });
        
                fetch(request)
                .then((res) => res.json())
                .then((stock) => {
                    console.log(stock);
                    this.setState({
                    stock:stock,
                    });
                })
            }


        renderStock() {
                
            if(!(typeof  this.state.stock.new_StockTwits_comments === "undefined")) {

                var styles1 = {
                    color:'red',
                };
    
                var styles2 = {
                    color:'green',
                };

                let commentsList1 = this.state.stock.new_StockTwits_comments.map(function(comment) {
                    
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


                                    let commentsList2 = this.state.stock.twitter_tweets.map(function(comment) {


                                                            console.log(comment)
                                                            return(
                                                                <a className='collection-item' href='#'>
                                                                    <li> 
                                                                        {/* Comment: <p> { comment.body } </p> 
                                                                        <br/> */}
                                                                         <p> { comment.tweet } </p>
                                                                        {/* Azure: <p> { comment.azure_sentiment } </p> */}
                                                                    </li> 
                                                                    <br/> 
                                                                </a>
                                                            )
                                        
                                                        });


                return(
                        // <div className="container">
                            <a className='list-group-item' href='#'>
                                {/* <StocksCard stocks={stocks} /> */}
                                <div className="row">
                                    {/* <div className="col s7">
                                        <TypeChooser>
                                            {type => <Chart type={type} data={ stocks.history } />}
                                        </TypeChooser> 
                                    </div> */}
                                    <div className="col s6">
    
                                        {/* <StocksCard stocks={stocks} /> */}
                                        {/* { stocks.new_StockTwits_comments } */}
                                        {/* Comments: { stocks.new_StockTwits_comments.length } */}
                                                                      
                                        <ul className="collection with-header">
                                            <li className="collection-header"><h5>StockTwits Comments:</h5></li>
                                            { commentsList1 }
                                        </ul>
                                    </div>
                                    <div className="col s6">
    
                                        {/* <StocksCard stocks={stocks} /> */}
                                        {/* { stocks.new_StockTwits_comments } */}
                                        {/* Comments: { stocks.new_StockTwits_comments.length } */}
                                                                      
                                        <ul className="collection with-header">
                                            <li className="collection-header"><h5>Twitter Comments:</h5></li>
                                            { commentsList2 }
                                        </ul>
                                    </div>
    
                                {/* <a class="waves-effect waves-light btn" onClick={}>Details</a> */}
                                
                                </div>
                                {/* <StocksCard stocks={stocks} /> */}
                                {/* <a className="waves-effect waves-light btn" >Details</a> */}
                                =====================================================================
                            </a>
                            // <br/>
                        // </div>

                )

            } else{


                return(

                    <p> No comments to show </p>
                )
            }


        }


      render() {
        console.log(this.state.stock);
        if(this.state.stock) {
            return(
                <div>
                    {this.renderStock()}
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

export default StockDetail