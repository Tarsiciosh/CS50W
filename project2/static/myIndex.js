let myChannel = {
  "id": "",
  "name": ""
};
let name = "";
let socketReady = false;
let counter = 0;
const quantity = 3;
let allowFetching = true; //

// things to add:
// in the window scroll lets put a

//template example:
const messageTemplate = Handlebars.compile(document.querySelector('#templateTest').innerHTML);

//scroll functionallity:
window.onscroll = () => {
  if (allowFetching == true && (window.innerHeight + window.scrollY >= document.body.offsetHeight)) {
    allowFetching = false;
    updateMessages();
  }
}

document.addEventListener("DOMContentLoaded", () => {

  // history API: - not working as intended..
  window.onpopstate = e => { //info of the state to load
    const data = e.state;
    document.title = data.title;
    user = e.user;
    //document.querySelector('#body').innerHTML = data.text;
  };

  //messages and channel part is hidden before login:
  document.querySelector("#main").style.display = "none";

  //LOGIN HANDLING:
  document.querySelector("#enter").onclick = () => {
    name = document.querySelector("#displayName").value;
    if (name.includes(" ", )) { //check for good string
      console.log("no white spaces allowed");
      document.querySelector("#displayName").value = "";
    } else {
      const request = new XMLHttpRequest();
      request.open("POST", "/add_name");
      request.onload = () => {
        const data = JSON.parse(request.responseText);
        if (data.success == false) {
          console.log("name already chosen");
          document.querySelector("#displayName").value = "";
        } else {
          document.querySelector("#login").style.animationPlayState = "running";
          document.querySelector("#login").addEventListener('animationend', () => {
            document.querySelector("#login").remove();
            loadChatPage();
          });
        }
      }
      data = new FormData();
      data.append("name", name);
      request.send(data);
    }
  };

  // LOAD CHAT PAGE:
  function loadChatPage() {
    document.querySelector("#name").innerHTML = name;
    document.querySelector("#main").style.display = "block";

    document.querySelector("#main").style.animationPlayState = "running";
    document.querySelector("#main").addEventListener("animationend", () => {
      // history API:
      history.pushState({
        "title": "Chat",
        "name": name
      }, "Chat of " + name, name);

      // load channels:
      const request = new XMLHttpRequest();
      request.open("POST", "/get_channels");
      request.onload = () => {
        const data = JSON.parse(request.responseText);
        if (data.success == false) {
          console.log("no channels fetched");
          return false;
        }
        const channels = data.channels;
        for (channel in channels) {
          select = document.querySelector("#channelSelection")
          option = document.createElement("option");
          option.innerHTML = channels[channel].name;
          option.value = channel;
          option.id = channel; //for further reference
          select.append(option);
        }
        // update content from storage:
        if (localStorage.getItem("myChannelId")) {
          myChannel.id = localStorage.getItem("myChannelId")
          myChannel.name = localStorage.getItem("myChannelName")
          document.querySelector("#channelSelection").value = myChannel.id;
          updateMessages();
        } else { // show content if there is any, otherwise do nothing
          if (myChannel.id != null) {
            updateMyChannel();
            updateMessages();
          }
        }
      }
      request.send();
    });
  }

  // UPDATE MESSAGES FROM SELECTED CHANNEL:
  document.querySelector("#channelSelection").onchange = () => {
    //remove messages and reset counter
    updateMyChannel();
    let myMessages = document.querySelector("#messages");
    myMessages.remove();
    myMessages = document.createElement("div");
    myMessages.id = "messages";
    document.querySelector("#main").appendChild(myMessages);
    counter = 0;
    updateMessages();
  };

  // SOCKECT CONNECTION:
  const socket = io.connect(location.protocol + "//" + document.domain + ":" + location.port)
  socket.on("connect", () => {
    socketReady = true;
  });

  // CHANNEL CREATE - SOCKET IO:
  document.querySelector("#createChannel").onclick = () => {
    if (socketReady) {
      const newChannelName = document.querySelector("#newChannel").value;
      if (newChannelName == "") return false;
      const newChannelId = newChannelName.replace(" ", "-");
      socket.emit("publish channel", {
        "channelId": newChannelId,
        "channelName": newChannelName
      });
    }
  }

  // RECEIVING CHANNELS FROM SERVER - SOCKET IO:
  socket.on("broadcast channel", data => {
    console.log("channel added: " + data.channelId)
    document.querySelector("#newChannel").value = "";
    newChannelId = data.channelId;
    newChannelName = data.channelName;

    select = document.querySelector("#channelSelection")
    option = document.createElement("option");
    option.innerHTML = newChannelName;
    option.value = newChannelId;
    option.id = newChannelId; //for further reference
    select.append(option);

    if (myChannel.id == "") { //the first time
      updateMyChannel();
      updateMessages();
    }
  });

  // SENDING MESSEGE TO SERVER - SOCKET IO:
  document.querySelector("#send").onclick = () => {
    if (socketReady == true) {
      const message = document.querySelector("#message").value;
      document.querySelector("#message").value = "";
      console.log("sending message..")
      const timeStamp = new Date();
      socket.emit("publish message", {
        "channelId": myChannel.id,
        "message": message,
        "name": name,
        "date": timeStamp.toString()
      });
    }
  }

  // RECEIVING MESSAGES FROM SERVER - SOCKET IO
  socket.on("broadcast message", data => {
    if (myChannel.id == data.channelId) { //if user is in that chat
      console.log("message received from " + data.channelId)
      const myMessages = document.querySelector("#messages");
      const renderedMessage = messageTemplate({
        "name": data.name,
        "text": data.message,
        "date": data.date
      });
      const p = document.createElement("div");
      p.innerHTML += renderedMessage;
      firstElement = myMessages.childNodes[0];
      myMessages.insertBefore(p, firstElement)
      counter++;
    }

  });
});

// UTILITY FUNCTIONS:

function updateMyChannel() {
  sel = document.querySelector("#channelSelection").value;
  myChannel.id = sel;
  myChannel.name = document.getElementById(sel).innerHTML;
  localStorage.setItem("myChannelId", myChannel.id);
  localStorage.setItem("myChannelName", myChannel.name);
}

function updateMessages() {
  //update the variables:
  const start = counter;
  const end = start + quantity;

  const request = new XMLHttpRequest();
  request.open("POST", "/get_messages");
  request.onload = () => {
    const data = JSON.parse(request.responseText);
    let myMessages = document.querySelector("#messages");
    if (data.success) {
      counter = start + data.readed;
      for (message of data.messages) {
        const p = messageTemplate({
          "name": message.name,
          "text": message.text,
          "date": message.date
        });
        myMessages.innerHTML += p;
      }
      allowFetching = true;
    } else {
      console.log("error while fetching messages from server");
    }
  }
  data = new FormData();
  data.append("channel", myChannel.id);
  data.append("start", start);
  data.append("end", end);
  request.send(data);
}
