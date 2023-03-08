'use strict';
// Content script file will run in the context of web page.
// With content script you can manipulate the web pages using
// Document Object Model (DOM).
// You can also pass information to the parent extension.
// We execute this script by making an entry in manifest.json file
// under `content_scripts` property
// For more information on Content Scripts,
// See https://developer.chrome.com/extensions/content_scripts

import { Configuration, OpenAIApi } from "openai";

const configuration = new Configuration({
  apiKey: "<your api key>",
});

const openai = new OpenAIApi(configuration);
const prefix = `
You are a software engineer responding to a work email.
Pleaes come up with the most appropriate response to the message below:

`;

// Listen for message
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  console.log(sender);
  let msg = document.getElementsByClassName("nH a98 iY")
  if (request.action === 'pexecute') {
    complete(msg).then(sendResponse)
    return true;
  }
  return false;
});

async function complete(msg) {
  const prompt = prefix + msg[0].textContent;
  const resp = await openai.createChatCompletion({
    model: "gpt-3.5-turbo",
    messages: [{ role: "user", content: prompt }],
    temperature: 0.7
  })
  const completionText = resp.data.choices[0].message.content;
  console.log(prompt);
  console.log(completionText);
  return { content: completionText }
}
