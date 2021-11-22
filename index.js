console.log("Welcome to my Calculator");

let screen = document.getElementById('screen');
let buttons = document.querySelectorAll('button');
let screenValue = "";
for(item of buttons){
    item.addEventListener('click', (e) =>{
        buttonText = e.target.innerText;
        console.log('Button text is: ', buttonText);
        if(buttonText == 'C'){
            screenValue = "";
            screen.value = screenValue;
        }
        else if(buttonText == '='){
            screen.value = eval(screenValue);
        }

        else if(buttonText == 'x'){
            screenValue = screenValue.substr(0, screenValue.length-1);
            screen.value = screenValue;
        }
        // else if(buttonText == 'x'){
            //     if(screenValue == ''){
                //         screenValue = 0;
                //         screen.value = screenValue;
                //         setTimeout(()=>{
                    //             screenValue = '';
                    //             screen.value = screenValue;
                    //         }, 400);
                    //     }
                    //     else{
                        //         screenValue = screenValue.substr(0, screenValue.length-1);
                        //         screen.value = screenValue;
                        
                        //     }
                        // }
                        
                        
                        else{
                            screenValue += buttonText;
                            screen.value = screenValue;
                        }
                    })
                }
                
                
//This 2 lines are my Personal Code line. Not related to Calculator.
for(item of buttons){
    item.addEventListener('dblclick', (e) =>{
        buttonText = e.target.innerText;
        if(buttonText == '('){
            screenValue = "S+S";
            screen.value = screenValue;
        }
        else if(buttonText == ')'){
            screenValue = "Love You...";
            screen.value = screenValue;
        }
        else if(buttonText == '='){
            screenValue = 'S+S = Love You...'
            screen.value = screenValue;
        }
    })

}