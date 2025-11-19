// ==UserScript==
// @name         CaptchaSolving
// @namespace    http://tampermonkey.net/
// @version      2025-07-10
// @description  try to take over the world!
// @author       You
// @match        https://*.vitap.ac.in/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=ac.in
// @grant        GM_xmlhttpRequest
// @connect      cap.va.synaptic.gg
// ==/UserScript==

(function() {
    'use strict';

    function getAllIds(){
        const allIds = [...new Set(
            Array.from(document.querySelectorAll('[id]'))
            .map(el => el.id)
            .filter(id => id.trim() !== '')
        )];
        //console.log(allIds);
        return allIds;
    }

    function isCaptchaPresent() {

        var ids = getAllIds();
        var elements = []
        for (var i = 0; i<ids.length;i++){
            if(ids[i].toLowerCase().includes("captcha") && !ids[i].toLowerCase().includes("refresh")){
                elements.push(ids[i]);
            }
        }
        //console.log(elements);
        return elements
    }

    function solveCaptcha(capImgSrc,capImgId,capStrId){
        console.log("Solving Captcha!");
        const source = capImgSrc;
        //console.log(source);
        const conv = btoa(source);
        const url = `https://cap.va.synaptic.gg/cap/${conv}`;
        GM_xmlhttpRequest({
        method: "GET",
        url: url,
        onload: function (response) {
            console.log("CAPTCHA Solved:", response.responseText);
            document.getElementById(capStrId).value = response.responseText;
        },
        onerror: function () {
            console.error("Failed to contact CAPTCHA solver");
        }
    });
            return;
    }

    var cps = isCaptchaPresent();
    var capImgId;
    var capImgSrc;
    var capStrId;
    if(cps){
         for (var i = 0; i<cps.length;i++){
            if(document.getElementById(cps[i]).type==="text" ||(document.getElementById(cps[i]).name && document.getElementById(cps[i]).name.toLowerCase().includes("string") )|| document.getElementById(cps[i]).id.toLowerCase().includes("string")){
                capStrId = cps[i];
            }
            if(document.getElementById(cps[i]).src){
                capImgId = cps[i];
                capImgSrc = document.getElementById(cps[i]).src;
            }
            if(document.getElementById(cps[i]).querySelector("img")?.src){
                capImgId = cps[i];
                capImgSrc = document.getElementById(cps[i]).querySelector("img").src;
            }
        }
    }
    else{console.log("Can't find captcha");}

    if(capImgId && capStrId && capImgSrc){
         solveCaptcha(capImgSrc,capImgId,capStrId);
    }
    else{console.log("Can't find captcha");}


})();