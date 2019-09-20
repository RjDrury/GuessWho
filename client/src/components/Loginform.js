import React from 'react'

const loginForm = (props) => {
    return (
        <div className="loginForm">
            <form>
                <input type="text" name="loginUsername" placeholder="Username"></input>
                <input type="password" name="loginPassword" placeholder="Password"></input>
                <input type="submit"></input>
            </form>
        </div>
    );
}

export default loginForm;