
const objectToCsv = function(data){

	const csvRows = [];

	const headers = Object.keys(data[0]);
	csvRows.push(headers.join(','));

	for(const row of data){
		const valuesRow = headers.map(header => {
			return row[header];
		});
		csvRows.push(valuesRow.join(','));
	}
	return csvRows.join('\n');

},

const download = function(data){
	const blob = new Blob([data], {type: 'text/csv'});
	const url = window.URL.createObjectURL(blob);
	const a = document.createElement('a');
	a.setAttribute('hidden', '');
	a.setAttribute('href', url);
	a.setAttribute('download', 'download.csv');
	document.body.appendChild(a);
	a.click();
	document.body.removeChild(a);
}



const getData = async function(dataUrl){
	const res = await fetch(dataUrl);
	const json = await res.json();

	const csvData = objectToCsv(json);
	download(csvData);
};

(function(){
	const button = document.getElementById('gen-csv');
	button.addEventListener('click', getData("http://127.0.0.1:8000/api/drivers/"));
})();