import React from 'react';
import './StocksCard.css';
import BarChart from '../BarChart'
import { Plot, Axis, Line } from 'react-plot';

const data = [
    [ 10, 490 ],
    [ 140, 380 ],
    [ 310, 420 ],
    [ 490, 10 ]
];

class StocksCard extends React.Component {
    redirectToUrl(url) {
        window.open(url, '_blank');
    }

    historical_data() {
        this.props.history;
    }

    render() {

        console.log(this.props.stocks.history != null);
        console.log(data);

        return (
            <div className="stocks-container" onClick={() => this.redirectToUrl(this.props.stocks.url)}>
                <div className='stock'>
                    <h4>{this.props.stocks.index}</h4>
                        <div className='stockInfo'>
                            
                            <div className='priceInfo'>   
                                Open: {this.props.stocks.open}
                                {'             '}
                                Price: {this.props.stocks.price}  

                                <div>volume: {this.props.stocks.volume}</div>                          
                            </div>


                            <p>trade_datetime: {this.props.stocks.trade_datetime}</p>
                            <p>reason: {this.props.stocks.reason}</p>
                        </div>

                    history: {this.props.stocks.history}

                {/* { this.props.stocks.history!=null && <Plot width={500} height={500} data={this.props.stocks.history}>
                        <Line color="#6fc1ff" />
                    </Plot> } */}

                {   this.props.stocks.history!=null && <Plot width={1000} height={200} xStep={10} yStep={1} data={this.props.stocks.history} >
                    
                    <Line width={10} />
                    <Line color="#6fc1ff" />

                    <Axis orientation="left" />
                    <Axis orientation="bottom" />
                </Plot> }

                <div>
                    <BarChart data={[5,10,1,3]} size={[500,500]} />
                </div>

                </div>
                    
            </div>
        
        );
    }
}

export default StocksCard;