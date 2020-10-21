import * as React from 'react';
import { MessageForm } from './MessageForm';
import { Socket } from './Socket';
import { Messages } from './Messages';
import { UserList } from './UserList';
import { GoogleButton } from './GoogleButton';

export function Content() {

    return (
        <div id="content">
            <div class="header">
              <h1>Chat App</h1>
              <GoogleButton />
              <div className="sidenav">
                <div>
                  <h1 style={{color: 'white', paddingLeft: '47px'}}>Active Users</h1>
                </div>
                <div>
                    <UserList /> 
                </div>
              </div>
                </div>
            <Messages />
        </div>
    );
}
// <div id="content">
//         <div>
//           <div className="sidenav">
//             <div>
//               <h1 style={{color: 'white', paddingLeft: '47px'}}>Active Users</h1>
//             </div>
//             <div>
//               <div className="userlist">
//                 <span className="Onlinedot" />
//                 <span className="Username">Deepanshu Ahuja</span>
//               </div>
//               <div className="userlist">
//                 <span className="Offlinedot" />
//                 <span className="Username">Rohit</span>
//               </div>
//               <div className="userlist">
//                 <span className="Onlinedot" />
//                 <span className="Username">Kapil</span>
//               </div>
//               <div className="userlist">
//                 <span className="Offlinedot" />
//                 <span className="Username">Shivam</span>
//               </div>
//             </div>
//           </div>
    //       <div className="scroll">
    //         <ul>
    //           <li className="box sb5">Hello newUSERxx1 from Joe-Bot</li>
    //           <li className="box sb5">test</li>
    //           <li className="box sb5">test</li>
    //           <li className="box sb5">test</li>
    //           <li className="box sb5">test</li>
    //           <li className="box sb5">test</li>
    //         </ul>
    //         <div className="msgip">
    //           <form><input type="text" placeholder="message" className="input_text" /><button>Send</button></form>
    //         </div>
    //       </div>
    //     </div>
    //   </div>
