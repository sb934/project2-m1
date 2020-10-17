import * as React from 'react';
import { MessageForm } from './MessageForm';
import { Socket } from './Socket';

export function Content() {
    const [messages, setMessages] = React.useState([]);
    // const [message, setMessage] = React.useState(0); //hook -> shifted to MessageForm
    
    // DUMMY_DATA for testing
    /*
    const DUMMY_DATA = [
      { sender: "foobar", text: "Hello from this side" },
      { sender: "adele", text: "Hello from the other side" }
    ]
    */
    function getNewMessages() {
        React.useEffect(() => {
            Socket.on('message history', (data) => {
                console.log("Received addresses from server: " + data['allMessages']);
                setMessages(data['allMessages']);
            });
        });
    }
    
    getNewMessages();
    
    /*
    function newMessage() {
        React.useEffect(() => { //hook oncomponentmount
            Socket.on('message received', (data) => {
                console.log("Received a number from server: " + data['message']);
                setMessage(data['message']);
            });
        });
    }
    */

    return (
        <div>
            <h1>My First Chat App!</h1>
                <ol>
                    {messages.map((message, index) => 
                        <li key={index} className="box sb5">{message}</li>)}
                </ol>
            <MessageForm />
        </div>
    );
}
