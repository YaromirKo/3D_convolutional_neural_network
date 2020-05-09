<template>
    <div>
        <canvas ref="threejs"></canvas>
    </div>
</template>

<script>
    /* eslint-disable */
    import * as THREE from 'three'
    import { OrbitControls } from "three/examples/jsm/controls/OrbitControls"
    import jsondata from '../assets/data'
    export default {
        name: "Points3d",
        data() {
            return {
                models: [],
                objs: [],
                recognize: [],
                raycaster: null,
                mouse: null,
                container: null,
                stats: null,
                camera: null,
                scene: null,
                renderer: null,
                points: null,
                controls: null,
                camera_x: jsondata[0]['camera_x'],
                camera_y: jsondata[0]['camera_y'],
                camera_z: jsondata[0]['camera_z'],
                look_x: jsondata[0]['look_x'],
                look_y: jsondata[0]['look_y'],
                look_z: jsondata[0]['look_z'],
                positions: jsondata[0]['positions'],
                colors: jsondata[0]['colors'],
                points_size: jsondata[0]['points_size'],
                axis_size: jsondata[0]['axis_size'],
            }
        },
        methods: {
            init(model) {
                let camera_x = this.camera_x;
                let camera_y = this.camera_y;
                let camera_z = this.camera_z;

                let look_x = this.look_x;
                let look_y = this.look_y;
                let look_z = this.look_z;
                let positions = new Float32Array(JSON.parse(this.positions));
                let colors = new Float32Array(JSON.parse(this.colors));

                let points_size = this.points_size;

                let axis_size = this.axis_size;

                this.scene = new THREE.Scene();

                let tmp_cam = Math.max.apply(Math, JSON.parse(this.positions)) + 5

                this.camera = new THREE.OrthographicCamera( tmp_cam / - 2, tmp_cam / 2,  tmp_cam / 2,  tmp_cam / - 2, 1, 1000);

                //this.camera = new THREE.PerspectiveCamera( 95, window.innerWidth / window.innerHeight, 0.1, 1000 );
                this.camera.position.x = camera_x;
                this.camera.position.y = camera_y;
                this.camera.position.z = camera_z;
                this.camera.up = new THREE.Vector3( 0, 1, 0 );


                // this.raycaster = new THREE.Raycaster();
                // this.mouse = new THREE.Vector3();
                //
                // function onMouseMove( event ) {
                //
                //     // calculate mouse position in normalized device coordinates
                //     // (-1 to +1) for both components
                //
                //     this.mouse.x = ( event.clientX / window.innerWidth ) * 2 - 1;
                //     this.mouse.y = - ( event.clientY / window.innerHeight ) * 2 + 1;
                //
                // }
                // // update the picking ray with the camera and mouse position
                // this.raycaster.setFromCamera( this.mouse, this.camera );
                //
                // window.addEventListener( 'mousemove', onMouseMove, false );

                // this.controls = new THREE.TrackballControls( this.camera );
                // this.controls.target.set( 0, 0, 0 )

                if (axis_size > 0) {
                    let axisHelper = new THREE.AxisHelper( axis_size );
                    this.scene.add( axisHelper );
                }

                let geometry = new THREE.BufferGeometry();
                geometry.setAttribute( 'position', new THREE.BufferAttribute( positions, 3 ) );
                geometry.setAttribute( 'ca', new THREE.BufferAttribute( colors, 3 ) );
                geometry.computeBoundingSphere();

                let material = new THREE.PointsMaterial({ size: points_size, color: 'red', sizeAttenuation: false });
                let points = new THREE.Points( geometry, material );
                this.scene.add( points );

                let axesHelper = new THREE.AxesHelper( 5 );
                this.scene.add( axesHelper );

                let helper = new THREE.GridHelper( 10, 10 );
                //helper.position.z = 0;
                helper.material.opacity = 0.25;
                helper.material.transparent = true;
                this.scene.add( helper );

                this.renderer = new THREE.WebGLRenderer({canvas: this.$refs.threejs});
                this.renderer.setPixelRatio( window.devicePixelRatio );
                this.renderer.setSize(500, 300);

                this.controls = new OrbitControls( this.camera, this.renderer.domElement );
                this.controls.autoRotate = true
                //this.controls.target.copy( new THREE.Vector3(look_x, look_y, look_z) );
                this.camera.lookAt( new THREE.Vector3(look_x, look_y, look_z));

                window.addEventListener( 'resize', this.onWindowResize, true );

            },
            onWindowResize() {
                this.renderer.setSize(500, 300);
            },

            animate() {
                requestAnimationFrame( this.animate );
                this.controls.update();
                this.renderer.render( this.scene, this.camera );
            },

            render() {
                requestAnimationFrame( this.animate );
                this.renderer.render( this.scene, this.camera );
            },

            set_models(models) {
                this.models = models;
            }
        },
        mounted() {

            this.init();
            this.animate();
        }
    }
</script>

<style scoped>

</style>