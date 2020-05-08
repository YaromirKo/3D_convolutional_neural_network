import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import { LayoutPlugin } from 'bootstrap-vue'

Vue.use(LayoutPlugin);
Vue.use(BootstrapVue);

export const bus = new Vue();

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
}).$mount('#app');
