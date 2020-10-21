import * as React from 'react';
import { Socket } from './Socket';
import { MessageForm } from './MessageForm';

export function Messages() {
    const [messages, setMessages] = React.useState([]);
    
    function getNewMessages() {
        React.useEffect(() => {
            Socket.on('message history', (data) => {
                console.log("Received messages from server: " + data['allMessages']);
                // setMessages(data['allMessages']);
            });
        });
    }
    
    getNewMessages();
    
    
    return (
         <div className="scroll">
            <ul>
              <li className="box sb5">Hello newUSERxx1 from Joe-Bot</li>
              <li className="box sb5">test</li>
              <li className="box sb5">test</li>
              <li className="box sb5">test</li>
              <li className="box sb5">test</li>
              <li className="box sb5">test</li>
            </ul>
            <MessageForm />
          </div>
    //     </div>
        // <div className="scroll">
        //     <ul>
        //         {messages.map((message, index) => 
        //             <li key={index} className="box sb5">{username}: {message}</li>)}
        //     </ul>
        // </div>
    );
}