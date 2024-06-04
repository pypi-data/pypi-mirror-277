class e{constructor(e){this.data=e,this.node_id=e.node_id,this.date_commissioned=e.date_commissioned,this.last_interview=e.last_interview,this.interview_version=e.interview_version,this.available=e.available,this.is_bridge=e.is_bridge,this.attributes=e.attributes,this.attribute_subscriptions=e.attribute_subscriptions}get nodeLabel(){const e=this.attributes["0/40/5"];return e?e.includes("\0\0")?"":e.trim():""}get vendorName(){return this.attributes["0/40/1"]}get productName(){return this.attributes["0/40/3"]}get serialNumber(){return this.attributes["0/40/15"]}update(t){return new e({...this.data,...t})}}class t{constructor(e){this.ws_server_url=e,this.serverInfo=void 0,this.ws_server_url=e}get connected(){var e;return(null===(e=this.socket)||void 0===e?void 0:e.readyState)===WebSocket.OPEN}async connect(e){if(this.socket)throw new Error("Already connected");return console.debug("Trying to connect"),new Promise(((t,s)=>{this.socket=new WebSocket(this.ws_server_url),this.socket.onopen=()=>{console.log("WebSocket Connected")},this.socket.onclose=e=>{console.log(`WebSocket Closed: Code=${e.code}, Reason=${e.reason}`),s(new Error("Connection Closed"))},this.socket.onerror=e=>{console.error("WebSocket Error: ",e),console.dir(e),s(new Error("WebSocket Error"))},this.socket.onmessage=s=>{const n=JSON.parse(s.data);if(console.log("WebSocket OnMessage",n),!this.serverInfo)return this.serverInfo=n,void t(void 0);e(n)}}))}disconnect(){this.socket&&(this.socket.close(),this.socket=void 0)}sendMessage(e){if(!this.socket)throw new Error("Not connected");console.log("WebSocket send message",e),this.socket.send(JSON.stringify(e))}}class s extends Error{}class n extends s{}class o{constructor(e,s){this.url=e,this.isProduction=s,this.connection=new t(this.url),this.nodes={},this.serverBaseAddress=this.url.split("://")[1].split(":")[0]||"",this._result_futures={},this.msgId=0,this.eventListeners={},this.url=e,this.isProduction=s}get serverInfo(){return this.connection.serverInfo}addEventListener(e,t){return this.eventListeners[e]||(this.eventListeners[e]=[]),this.eventListeners[e].push(t),()=>{this.eventListeners[e]=this.eventListeners[e].filter((e=>e!==t))}}async commissionWithCode(e,t){console.log("TODO")}async commissionOnNetwork(e,t){console.log("TODO")}async setWifiCredentials(e,t){console.log("TODO")}async setThreadOperationalDataset(e){console.log("TODO")}async openCommissioningWindow(e,t=300,s=1e3,n=1,o=void 0){console.log("TODO")}async discoverCommissionableNodes(){console.log("TODO")}async getMatterFabrics(e){console.log("TODO")}async removeMatterFabric(e,t){console.log("TODO")}async pingNode(e){await this.sendCommand("ping_node",0,{node_id:e})}async removeNode(e){await this.sendCommand("remove_node",0,{node_id:e})}async interviewNode(e){await this.sendCommand("interview_node",0,{node_id:e})}async importTestNode(e){await this.sendCommand("import_test_node",0,{dump:e})}async sendCommand(e,t=void 0,s){if(t&&this.serverInfo.schema_version<t)throw new n(`Command not available due to incompatible server version. Update the Matter Server to a version that supports at least api schema ${t}.`);const o=++this.msgId,i={message_id:o.toString(),command:e,args:s},r=new Promise(((e,t)=>{this._result_futures[o]={resolve:e,reject:t},this.connection.sendMessage(i)}));return r.finally((()=>{delete this._result_futures[o]})),r}async connect(){this.connection.connected||await this.connection.connect((e=>this._handleIncomingMessage(e)))}disconnect(e=!0){this.connection&&this.connection.connected&&this.connection.disconnect(),e&&(localStorage.removeItem("matterURL"),location.reload())}async startListening(){await this.connect();const t=await this.sendCommand("start_listening",0,{}),s={};for(const n of t)s[n.node_id]=new e(n);this.nodes=s}_handleIncomingMessage(e){if("event"in e)this._handleEventMessage(e);else if("error_code"in e){const t=e,s=this._result_futures[t.message_id];s&&(s.reject(new Error(t.details)),delete this._result_futures[t.message_id])}else if("result"in e){const t=e,s=this._result_futures[t.message_id];s&&(s.resolve(t.result),delete this._result_futures[t.message_id])}else console.warn("Received message with unknown format",e)}_handleEventMessage(t){if(console.log("Incoming event",t),"node_added"===t.event){const s=new e(t.data);return this.nodes={...this.nodes,[s.node_id]:s},void this.fireEvent("nodes_changed")}if("node_removed"===t.event)return delete this.nodes[t.data],this.nodes={...this.nodes},void this.fireEvent("nodes_changed");if("node_updated"===t.event){const s=new e(t.data);return this.nodes={...this.nodes,[s.node_id]:s},void this.fireEvent("nodes_changed")}if("attribute_updated"===t.event){const[s,n,o]=t.data,i=new e(this.nodes[s]);return i.attributes[n]=o,this.nodes={...this.nodes,[i.node_id]:i},void this.fireEvent("nodes_changed")}}fireEvent(e,t){const s=this.eventListeners[e];if(s)for(const e of s)e()}}!async function(){import("./matter-dashboard-app-pMm2fVnD.js").then((function(e){return e.m}));let e="";const t=location.href.includes(":5580")||location.href.includes("hassio_ingress");if(t){let t=window.location.origin+window.location.pathname;t.endsWith("/")&&(t=t.slice(0,-1)),e=t.replace("http","ws")+"/ws",console.log(`Connecting to Matter Server API using url: ${e}`)}else{let t=localStorage.getItem("matterURL");if(!t){if(t=prompt("Enter Websocket URL to a running Matter Server","ws://localhost:5580/ws"),!t)return void alert("Unable to connect without URL");localStorage.setItem("matterURL",t)}e=t}const s=new o(e,t),n=document.createElement("matter-dashboard-app");n.client=s,document.body.append(n)}();
