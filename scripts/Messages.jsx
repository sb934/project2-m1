import * as React from 'react';
import { Socket } from './Socket';

export function Messages() {
    const [messages, setMessages] = React.useState([]);
    
    function getNewMessages() {
        React.useEffect(() => {
            Socket.on('message history', (data) => {
                console.log("Received messages from server: " + data['allMessages']);
                setMessages(data['allMessages']);
            });
        });
    }
    
    getNewMessages();
    
    let username = window.sessionStorage.getItem("username");
    
    return (
        <div className="scroll">
            <ul>
                {messages.map((message, index) => 
                    <li key={index} className="box sb5">{username}: {message}</li>)}
            </ul>
        </div>
    );
}