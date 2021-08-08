var csvData = {
    size:0,
    fileData:[]
};
 
function readCsvFile(input) {
     if (input.files && input.files[0]) {

         let reader = new FileReader();
         reader.readAsBinaryString(input.files[0]);

         reader.onload = function (e) {
            console.log(e);
            csvData.size = e.total;
            csvData.fileData = e.target.result;
            console.log(csvData.fileData);
            parseData(csvData.fileData);
                    
         }
     }
};


function convertToJson(data){
    let dataContent = data;

}

function parseData(data){
    let csvData = [];
    let lineBreak = data.split("\n");
    lineBreak.forEach(result => {
        csvData.push(result.split(","));
    });
    console.table(csvData);
}



