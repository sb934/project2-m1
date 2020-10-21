import React, { useState, useEffect } from "react";
import io from "socket.io-client";
import { Socket } from './Socket';

export function UserList() {
  const [users, setUsers] = useState([]);
  //const [message, setMessage] = useState("");
  
  function getNewUsers() {
        React.useEffect(() => {
            Socket.on('user history', (data) => {
                console.log("Received users from server: " + data['allUsers']);
                setUsers(data['allUsers']);
            });
        });
    }
    
  getNewUsers();
  
  return (
    <div>
      <ul>
          {users.map((user, index) => 
              <li key={index}>{user}</li>)}
      </ul>
    </div>
  );
}

  