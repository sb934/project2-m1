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
        // message content --> state var
        Socket.emit('new message', {
            'message': message,
        }); 
        
        console.log('Sent a message ' + message + ' to server!');
    
        event.preventDefault();
        // setMsg('');
    }
    
    return (
        <div className="msgip">
        <form onSubmit={handleSubmit}>
            <input onChange={handleChange}/>
            <button>Send</button>
        </form>
        </div>
    );
}
