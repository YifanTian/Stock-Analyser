

import { tsvParse, csvParse } from  "d3-dsv";
import { timeParse } from "d3-time-format";

function parseData(parse) {
	return function(d) {
		d.date = parse(d.date);
		d.open = +d.open;
		d.high = +d.high;
		d.low = +d.low;
		d.close = +d.close;
		d.volume = +d.volume;

		return d;
	};
}

const parseDate = timeParse("%Y-%m-%d");

export function getData() {

    // const MSFT = fetch("//rrag.github.io/react-stockcharts/data/MSFT.tsv")
    // .then(response => { console.log(response.text()) });

	// var reader = new FileReader();
	// var file = reader.readAsText('/home/yifantian/Downloads/MSFT.tsv');

	const promiseMSFT = fetch("//rrag.github.io/react-stockcharts/data/MSFT.tsv")
		.then(response => response.text())
        .then(data => tsvParse(data, parseData(parseDate)));
        
    //     data = {

	//     }

    // const promiseMSFT = tsvParse(data, parseData(parseDate);  
    // console.log(promiseMSFT);  
	return promiseMSFT;
}
