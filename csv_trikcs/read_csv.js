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
            console.log(csvData.fileData.split('\n')[-1]);
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


function saveData(data1){
    let data = data1;
    $.ajax({
        url : 'http://127.0.0.1:8000/api/drivers/',
        type : 'POST',
        headers : {'X-CSRFToken' : $.cookie('csrftoken')},
        dataType : 'json',
        data : data,
    })
    .done(function(data){
        
        console.log(data);
    })
    .fail(function(data){
        console.log(data);
    });

};
