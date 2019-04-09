function main() {
  const webSocket = new WebSocket(`ws://${location.host}/socket`);
  webSocket.onmessage = (event)=> {
    console.debug('event', event.data);
  };
  webSocket.onopen = ()=> {
    webSocket.send('hello!');
    console.debug('open and sent hello');
  };
  webSocket.onclose = ()=> {
    console.debug('closed');
  };
}

main()
