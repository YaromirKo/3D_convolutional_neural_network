<template>
  <div id="container"></div>
</template>

<script>
  import * as THREE from 'three'

  export default {
    name: 'ThreeTest',

    data() {
      return {
        cube: null,
        renderer: null,
        scene: null,
        camera: null
      }
    },
    methods: {
      init: function() {
        this.scene = new THREE.Scene()
        this.camera = new THREE.PerspectiveCamera(
                75,
                window.innerWidth / window.innerHeight,
                0.1,
                1000
        )

        this.renderer = new THREE.WebGLRenderer()
        this.renderer.setSize(window.innerWidth, window.innerHeight)
        document.body.appendChild(this.renderer.domElement)

        const geometry = new THREE.BoxGeometry(1, 1, 1)
        const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 })
        this.cube = new THREE.Mesh(geometry, material)
        this.scene.add(this.cube)

        this.camera.position.z = 5
      },
      animate: function() {
        requestAnimationFrame(this.animate)
        var time = - performance.now() * 0.0003;

        this.camera.position.x = 400 * Math.cos( time );
        this.camera.position.z = 400 * Math.sin( time );

        this.light.position.x = Math.sin( time * 1.7 ) * 300;
        this.light.position.y = Math.cos( time * 1.5 ) * 400;
        this.light.position.z = Math.cos( time * 1.3 ) * 300;

        if ( vnh ) vnh.update();
        if ( vth ) vth.update();

        renderer.render( scene, camera );
        this.renderer.render(this.scene, this.camera)
      }
    },
    mounted() {
      this.init()
      this.animate()
    }
  }
</script>

<style scoped>
</style>