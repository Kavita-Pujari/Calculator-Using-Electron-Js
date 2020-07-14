



async function Answer(Id){


    
	let Value1=document.getElementById("Value1").value;
	let Value2=document.getElementById("Value2").value;

	console.log(Value1);
	console.log(Value2);
    //eel.total(Value1,Value2)();
    let output = await eel.total(Value1, Value2,Id)();//wait for the output of the total_t and store into the output
    let Ans = document.getElementById("Ans").value = output;


}

