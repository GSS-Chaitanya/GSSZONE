function validateForm(){
    let uname=document.getElementById('uname').value;
    let pass=document.getElementById('pass').value;
    if(uname===''||pass===''){
        alert('Please fill all the fields');
        return false;

    }
    else if(uname.length<8){
            alert('The Username must contain minimum of 8 characters');
            return false;
    }
    else if(pass.length<8){
        alert('The password must contain minimum of 8 characters');
        return false;
    }

}
