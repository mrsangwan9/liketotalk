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
    console.log(data)
    document.getElementById('textarea').value+=(data.message+'\n')
    }

socket.onclose=(e)=>{
    console.error('chat socket closed unexpectedly')
}

   document.getElementById('text').focus()
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
