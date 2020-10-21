import React, { useState, useEffect } from "react";
import io from "socket.io-client";
import { Socket } from './Socket';

export function UserList() {
  const [users, setUsers] = useState([]);
  
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
          {users.map((user, index) => 
              <div className="userlist">
                <span className="Onlinedot" />
                <span className="Username" key={index}>{user}</span>
              </div> 
              //<li key={index}>{user}</li>
              )}
    </div>
  );
}

  