import * as React from 'react';
import { Socket } from './Socket';
import { MessageForm } from './MessageForm';

export function Messages() {
    const [senders, setSenders] = React.useState([]);
    const [messages, setMessages] = React.useState([]);
    
    function getNewMessages() {
        React.useEffect(() => {
            Socket.on('message history', (data) => {
                console.log("Received messages from server...");
                //console.log(data['allSenders']);
                //console.log(data['allMessages']);
                //setSenders(data['allSenders']);
                setMessages(data['allMessages']);
            });
        });
    }
    
    getNewMessages();
    
    
    return (
        //  <div className="scroll">
        //     <ul>
        //       <li className="box sb5">Hello newUSERxx1 from Joe-Bot</li>
        //       <li className="box sb5">test</li>
        //       <li className="box sb5">test</li>
        //       <li className="box sb5">test</li>
        //       <li className="box sb5">test</li>
        //       <li className="box sb5">test</li>
        //     </ul>
        //     <MessageForm />
        //  </div>
    //     </div>
        <div className="scroll">
            <ul>
                {messages.map((message, index) => 
                    <li key={index} className="box sb5">{message.sender}: {message.text}</li>)}
            </ul>
            <MessageForm />
        </div>
    );
}