const other_id=JSON.parse(document.getElementById('other_user_id').textContent);             
console.log(window.location.pathname)
const socket = new WebSocket(
  'ws://'
  + window.location.host
  + '/ws/todo/'
  + other_id
  + '/'
);

socket.onopen=(e)=>{
    console.log("websocket connection open...")
 }
   
socket.onmessage =(e)=>{//handle when message receive
    const data = JSON.parse(e.data);
    if(data.username == sender){
        document.querySelector('#textarea').innerHTML += ` <div class="d-flex flex-row justify-content-end mb-4 pt-1">
                                                                                                <div>
                                                                                                <p class="small p-2 me-3 mb-1 text-white rounded-3 bg-primary">${data.message}</p>
                                                                                                </div>
                                                                                                <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava6-bg.webp"
                                                                                                alt="avatar 1" style="width: 45px; height: 100%;">
                                                                                            </div>`
    }else{
        document.querySelector('#textarea').innerHTML += `<div class="d-flex flex-row justify-content-start">
                                                            <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava6-bg.webp"
                                                            alt="avatar 1" style="width: 45px; height: 100%;">
                                                            <div>
                                                            <p class="small p-2 ms-3 mb-1 rounded-3" style="background-color: #f5f6f7;">${data.message}</</p>
                                                            </div>
                                                        </div>`

    }
    let roll = document.getElementById('textarea')
    roll.scrollTop = roll.scrollHeight;
}



socket.onclose=(e)=>{
    console.error('chat socket closed unexpectedly')
}

   
   document.getElementById('text').onkeyup = (event)=> {
    if (event.keyCode === 13) {  // enter, return
        document.getElementById('btn').click();
    }
};
    const sender=JSON.parse(document.getElementById('sender').textContent)
    document.getElementById('btn').onclick=(event)=>{
    const messageInputDom = document.getElementById('text');
    const message = messageInputDom.value;
    socket.send(JSON.stringify({
        'message': message,
        'user':sender,
        
    }));
    messageInputDom.value = '';
};

