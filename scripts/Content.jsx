import * as React from 'react';
import { MessageForm } from './MessageForm';
import { Socket } from './Socket';
import { Messages } from './Messages';
import { UserList } from './UserList';
import { GoogleButton } from './GoogleButton';

export function Content() {
    // const [message, setMessage] = React.useState(0); //hook -> shifted to MessageForm
    
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
            <div class="header">
              <h1>Chat App</h1>
              <p>Project 2 Milestone 2</p>
              <GoogleButton />
            </div>
            <UserList />
            <Messages />
            <MessageForm />
        </div>
    );
}
