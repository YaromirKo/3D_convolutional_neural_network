<template>
  <div id="app">
    <b-container fluid v-show="!preloader">
      <b-row class="h-100">

        <b-col cols="4" align-self="center">
          <b-row align-h="center">
            <upload v-show="show"></upload>
          </b-row>
        </b-col>


        <b-col cols="auto">
          <b-row align-h="center">
            <b-img class="img" :src="require('./assets/icon.png')"></b-img>
          </b-row>
          <b-row align-h="center">
            <div class="vl"></div>
          </b-row>
        </b-col>

        <b-col cols="6" align-self="center">
          <info-chart></info-chart>
        </b-col>

      </b-row>
    </b-container>

    <b-container fluid v-if="preloader">
      <b-row class="h-100 preloader" align-h="center">
        <b-col cols="2" align-self="center">
          <b-row align-h="center">
            <b-img class="" :src="require('./assets/loader_1.png')"></b-img>
            <div v-if="recognize && preloader">recognize</div>...
          </b-row>
        </b-col>
      </b-row>
    </b-container>

  </div>
</template>

<script>
  import Upload from './components/Upload'
  import InfoChart from './components/InfoChart'

  export default {
    name: 'App',
    components: {
      Upload,
      InfoChart
    },
    data() {
      return {
        show: true,
        preloader: false,
        recognize: true
      }
    },
    mounted() {
      this.$on('recognize', this.recognize_fun);
    },
    methods: {
      recognize_fun(e) {
        this.recognize = this.preloader = e;
      }
    }
  }
</script>

<style>
  #app {
    background-color: grey;
    color: black;
    max-width: 100%;
    margin: 0;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    height: 100vh;
    display: flex;
    position: fixed;
  }
  .img {
    width: 12vh;
  }
  .vl {
    border: 1px solid black;
    border-radius: 5px;
    height: 70vh;
    position: absolute;
    margin-left: -3px;
    /*left: 50%;*/
    top: 15vh;
  }
  .preloader {
    background-color: #4967a7;
  }
</style>
