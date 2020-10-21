import * as React from 'react';
import { Socket } from './Socket';


export function MessageForm() {
    const [message, setMsg] = React.useState("");
    
    // change message value when something typed in text field
    function handleChange(event) {
        setMsg(event.target.value);
        //console.log(message)
    }   
    
    // handle event when message sent button clicked 
    function handleSubmit(event) {
        let username = window.sessionStorage.getItem("username");
        
        Socket.emit('new message', {
            'username':username,
            'message': message,
        }); 
        
        console.log('Sent a message ' + message + ' from ' + username + ' to server!');
    
        event.preventDefault();
    }
    
    React.useEffect(() => { //hook oncomponentmount
            if (window.sessionStorage.getItem("username") !== null) {
                document.getElementById("sendbutton").style.display="block"
        }});
    
    return (
        <div className="msgip">
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="message" className="input_text" onChange={handleChange}/>
                <button id="sendbutton" style={{'display': 'none'}}>Send</button>
            </form>
        </div>
    );
}

       