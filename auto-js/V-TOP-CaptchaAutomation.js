// ==UserScript==
// @name         V-TOP
// @namespace    http://tampermonkey.net/
// @version      1.1
// @description  Rapidly reloads the page until CAPTCHA loads on a specific URL
// @author       Your Name
// @match        https://vtop.vitap.ac.in/vtop/login
// @grant        GM_xmlhttpRequest
// @connect      cap.va.synaptic.gg
// ==/UserScript==

(function() {
    'use strict';

    const xpathtobeclicked = '//*[@id="stdForm"]/a/div/div[2]/button'

    const xpathSelector = '//*[@id="captchaBlock"]/img'; // XPath for the CAPTCHA element

    // Function to check for the CAPTCHA using XPath

    function clickButtonByXPath(xpath) {
  const element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;

  if (element) {
    element.click(); // Simulate a click on the element
    console.log("Button clicked!");
  } else {
    console.log("No element found for the given XPath");
  }
}



    function isCaptchaPresent() {
        const result = document.evaluate(
            xpathSelector,
            document,
            null,
            XPathResult.FIRST_ORDERED_NODE_TYPE,
            null
        );
        return result.singleNodeValue !== null;
    }

    // Function to reload the page rapidly until CAPTCHA is found
    function reloadUntilCaptcha() {
        if (isCaptchaPresent()) {
            console.log("CAPTCHA detected!");
            const source = document.querySelector("#captchaBlock > img").src;
            const conv = btoa(source);
            const url = `https://cap.va.synaptic.gg/cap/${conv}`;
            GM_xmlhttpRequest({
        method: "GET",
        url: url,
        onload: function (response) {
            console.log("CAPTCHA Solved:", response.responseText);
            document.getElementById("captchaStr").value = response.responseText;
            // insert into form or auto-submit if needed
        },
        onerror: function () {
            console.error("Failed to contact CAPTCHA solver");
        }
    });
            return; // Stop reloading if CAPTCHA is found
        }

        console.log("CAPTCHA not detected. Reloading...");
        location.reload(); // Reload immediately without delay
    }

    // Start the process
    clickButtonByXPath(xpathtobeclicked)
    setTimeout(reloadUntilCaptcha,100);
})();
