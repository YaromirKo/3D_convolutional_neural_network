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
        name: "VoxelGrid3d",
        props: ['voxel_grid'],
        data() {
            return {
                camera: null,
                scene: null,
                renderer: null,
                points: null,
                controls: null,
                animation_frame: null
            }
        },
        methods: {
            init() {
                let camera_x = this.voxel_grid['camera_x'];
                let camera_y = this.voxel_grid['camera_y'];
                let camera_z = this.voxel_grid['camera_z'];


                let look_x = this.voxel_grid['look_x'];
                let look_y = this.voxel_grid['look_y'];
                let look_z = this.voxel_grid['look_z'];

                let X = new Float32Array(JSON.parse(this.voxel_grid['X']));
                let Y = new Float32Array(JSON.parse(this.voxel_grid['Y']));
                let Z = new Float32Array(JSON.parse(this.voxel_grid['Z']));

                let R = new Float32Array(JSON.parse(this.voxel_grid['R']));
                let G = new Float32Array(JSON.parse(this.voxel_grid['G']));
                let B = new Float32Array(JSON.parse(this.voxel_grid['B']));

                let S_x = this.voxel_grid['S_x'];
                let S_y = this.voxel_grid['S_y'];
                let S_z = this.voxel_grid['S_z'];

                let n_voxels = this.voxel_grid['n_voxels'];
                let axis_size = this.voxel_grid['axis_size'];

                this.scene = new THREE.Scene();

                let tmp_cam = Math.max.apply(Math, JSON.parse(this.voxel_grid['X'])) + 15;

                this.camera = new THREE.OrthographicCamera( tmp_cam / - 2, tmp_cam / 2,  tmp_cam / 2,  tmp_cam / - 2, 1, 1000);

                this.camera.position.x = camera_x;
                this.camera.position.y = camera_y;
                this.camera.position.z = camera_z;

                this.camera.up = new THREE.Vector3( 0, 1, 0);

                let axesHelper = new THREE.AxesHelper( tmp_cam - 15 );

               this.scene.add( axesHelper );

                let helper = new THREE.GridHelper( tmp_cam, tmp_cam / 3 );

                helper.material.opacity = 0.25;
                helper.material.transparent = true;
                this.scene.add( helper );

                // if (axis_size > 0) {
                //     let axisHelper = new THREE.AxisHelper( axis_size );
                //     this.scene.add( axisHelper );
                // }

                let geometry = new THREE.BoxGeometry( S_x, S_z, S_y );

                for ( let i = 0; i < n_voxels; i ++ ) {{
                    let mesh = new THREE.Mesh( geometry, new THREE.MeshBasicMaterial() );
                    mesh.material.color.setRGB(R[i], G[i], B[i]);
                    mesh.position.x = X[i];
                    mesh.position.y = Y[i];
                    mesh.position.z = Z[i];
                    this.scene.add(mesh);
                }}
                this.renderer = new THREE.WebGLRenderer({canvas: this.$refs.threejs});
                this.renderer.setPixelRatio( window.devicePixelRatio );
                this.renderer.setSize(500, 300);

                this.controls = new OrbitControls( this.camera, this.renderer.domElement );
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
            voxel_grid() {
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