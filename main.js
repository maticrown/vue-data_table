import BootstrapVue from "bootstrap-vue";
import Vue from 'vue';
//import App from ./App.vue;
import VueSocketIO from 'vue-socket.io';
import router from "./router";
Vue.use(BootstrapVue);

import { MyVuexStore } from './my-vuex-store.js'

export const SocketInstance = socketio('http://10.99.0.1:5000');

Vue.use(VueSocketIO,SocketInstance)

Vue.config.productionTip = false;
new Vue({
router,
render: h => h(App)
}). $mount("#app");

var firstTable = new Vue({
  el: '#firstTable',
  data: {
    rows: [
      {
        id: 1, name: "phy"
      },
      {
        id: 2, name: "mac"
      },
      {
        id: 3, name: "transport"
      }
    ]
  }
});
