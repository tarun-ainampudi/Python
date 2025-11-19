// ==UserScript==
// @name         creds fill
// @namespace    http://tampermonkey.net/
// @version      2025-07-15
// @description  try to take over the world!
// @author       You
// @match        https://registration.vitap.ac.in/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=ac.in
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    if(document.getElementById("username")){document.getElementById("username").value = "23BCE9816";}
    else{console.log("Username Not Found");}
    if(document.getElementById("password")){document.getElementById("password").value = "Tangeda@15";}
    else{console.log("Password Not Found");}

    if(document.getElementById("loginButton")){
        setTimeout(() => {
    document.getElementById("loginButton").click();
        }, 3000);
    }
    else{console.log("Submit Not Found");}
})();