import * as React from 'react';
import { Socket } from './Socket';
import { MessageForm } from './MessageForm';

export function Messages() {
    const [messages, setMessages] = React.useState([]);
    
    function getNewMessages() {
        React.useEffect(() => {
            Socket.on('message history', (data) => {
                console.log("Received messages from server...");
                setMessages(data['allMessages']);
            });
        });
    }
    
    getNewMessages();
    
    
    return (
        <div className="scroll">
            <ul>
                {messages.map((message, index) => 
                    <li key={index} className="box sb5">{message.sender}: {message.text}</li>)}
            </ul>
            <MessageForm />
        </div>
    );
}