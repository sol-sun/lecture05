
function Calc(){

 var inputL = document.getElementById('inputL');
 var inputR = document.getElementById('inputR');

 if( isFinite(inputL.value) && isFinite(inputR.value) ){
    var output = document.getElementById("result");
    output.innerHTML = parseInt(inputR.value) + parseInt(inputL.value);
 }

}
