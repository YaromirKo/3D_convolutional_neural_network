<template>
    <div>
        <canvas ref="threejs"></canvas>
    </div>
</template>

<script>
    /* eslint-disable */
    import * as THREE from 'three'
    import { OrbitControls } from "three/examples/jsm/controls/OrbitControls"
    export default {
        name: "Points3d",
        props: ['points'],
        data() {
            return {
                camera: null,
                scene: null,
                renderer: null,
                controls: null,
                animation_frame: null
            }
        },
        methods: {
            init() {
                let camera_x = this.points['camera_x'];
                let camera_y = this.points['camera_y'];
                let camera_z = this.points['camera_z'];

                let look_x = this.points['look_x'];
                let look_y = this.points['look_y'];
                let look_z = this.points['look_z'];
                let positions = new Float32Array(JSON.parse(this.points['positions']));
                let colors = new Float32Array(JSON.parse(this.points['colors']));

                let points_size = this.points['points_size'];

                let axis_size = this.points['axis_size'];

                this.scene = new THREE.Scene();

                let tmp_cam = Math.max.apply(Math, JSON.parse(this.points['positions'])) + 5;

                this.camera = new THREE.OrthographicCamera( tmp_cam / - 2, tmp_cam / 2,  tmp_cam / 2,  tmp_cam / - 2, 1, 1000);

                this.camera.position.x = camera_x;
                this.camera.position.y = camera_y;
                this.camera.position.z = camera_z;
                this.camera.up = new THREE.Vector3( 0, 1, 0 );

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
                helper.material.opacity = 0.25;
                helper.material.transparent = true;
                this.scene.add( helper );

                this.renderer = new THREE.WebGLRenderer({canvas: this.$refs.threejs});
                this.renderer.setPixelRatio( window.devicePixelRatio );
                this.renderer.setSize(500, 300);

                this.controls = new OrbitControls( this.camera, this.renderer.domElement );
                this.controls.autoRotate = true;
                this.camera.lookAt( new THREE.Vector3(look_x, look_y, look_z));

                window.addEventListener( 'resize', this.onWindowResize, true );
            },
            onWindowResize() {
                this.renderer.setSize(500, 300);
            },
            animate() {
                this.animation_frame = requestAnimationFrame( this.animate );
                this.controls.update();
                this.renderer.render( this.scene, this.camera );
            },
            delete3d() {
                cancelAnimationFrame(this.animation_frame);
                this.scene = null;
                this.camera = null;
                this.controls = null;
                this.renderer = null;
            },
            render3d() {
                this.delete3d()
                this.init();
                this.animate();
            }
        },
        watch: {
            points() {
                this.render3d();
            }
        },
        mounted() {
            this.render3d();
        }
    }
</script>

<style scoped>

</style>