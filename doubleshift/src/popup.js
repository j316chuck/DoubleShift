'use strict';

import './popup.css';

(function() {
  // // We will make use of Storage API to get and store `count` value
  // // More information on Storage API can we found at
  // // https://developer.chrome.com/extensions/storage

  // // To get storage access, we have to mention it in `permissions` property of manifest.json file
  // // More information on Permissions can we found at
  // // https://developer.chrome.com/extensions/declare_permissions
  // const counterStorage = {
  //   get: (cb) => {
  //     chrome.storage.sync.get(['count'], (result) => {
  //       cb(result.count);
  //     });
  //   },
  //   set: (value, cb) => {
  //     chrome.storage.sync.set(
  //       {
  //         count: value,
  //       },
  //       () => {
  //         cb();
  //       }
  //     );
  //   },
  // };

  function setupCounter(initialValue = "") {
    document.getElementById('completion').innerHTML = initialValue;
    document.getElementById('generateBtn').addEventListener('click', () => {
      chrome.tabs.query({ active: true, currentWindow: true })
        .then((tabs) => {
          const tab = tabs[0];
          chrome.tabs.sendMessage(
            tab.id,
            { action: 'pexecute' },
            ({ content }) => {
              console.log(content);
              document.getElementById('completion').innerHTML = content;
            })
        });
    });
  }

  document.addEventListener('DOMContentLoaded', setupCounter("init"));

  // Communicate with background file by sending a message
  chrome.runtime.sendMessage(
    {
      type: 'GREETINGS',
      payload: {
        message: 'Hello, my name is Pop. I am from Popup.',
      },
    },
    (response) => {
      console.log(response.message);
    }
  );
})();
