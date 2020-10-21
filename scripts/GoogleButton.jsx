import * as React from 'react';
import { Socket } from './Socket';
import { GoogleLogin } from 'react-google-login';

function handleSubmit(response) {
    // TODO replace with name from oauth
    console.log("Reached Submit");

    let name = response.profileObj.name;
    let email = response.profileObj.email;
    Socket.emit('new google user', {
        'name': name,
        'email':email,
    });
    window.sessionStorage.setItem("username",name);
    console.log('Sent the name ' + name + ' to server!');
    window.location.reload()
}

function handleFailure(response) {
    console.log("failure");
    console.log(response);
}

export function GoogleButton() {
    return (
            <GoogleLogin
    clientId="347824852945-g2jnnb98davd2dag3a3619enrkha24ac.apps.googleusercontent.com"
    buttonText="Login"
    onSuccess={handleSubmit}
    onFailure={handleFailure}
    cookiePolicy={'single_host_origin'}
  />
    );
}
