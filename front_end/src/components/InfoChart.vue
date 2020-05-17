<template>
    <div>
        <b-row v-if="model.length === 0" align-h="center">
            <div>here will be information about your models</div>
            <div class="w-100"></div>
            <div><b-img :src="require('../assets/loader.png')" width="20"></b-img></div>
        </b-row>

        <b-row v-if="model.length !== 0">
            <b-col>
                <b-row>
                    <b-col>
                        <div class="class_name class_name_header">
                            <h3>Class: {{model['recognized']}}</h3>
                        </div>
                    </b-col>
                </b-row>
                <b-row align-h="center">
                    <b-col>
                        <div class="class_name">Points</div>
                    </b-col>
                </b-row>
                <b-row align-h="center">
                    <points-3d :points="model['points']"></points-3d>
                </b-row>
                <b-row align-h="center">
                    <b-col>
                        <div class="class_name">Voxel Grid</div>
                    </b-col>
                </b-row>
                <b-row align-h="center">
                    <voxel-grid-3d :voxel_grid="model['voxel_grid']"></voxel-grid-3d>
                </b-row>
            </b-col>
        </b-row>
    </div>
</template>

<script>
    /* eslint-disable */
    import VoxelGrid3d from "./VoxelGrid3d";
    import Points3d from "./Points3d";
    import { bus } from '../main'

    export default {
        name: "InfoChart",
        components: {
            VoxelGrid3d,
            Points3d
        },
        data() {
            return {
                model: []
            }
        },
        methods: {
            view(model) {
                this.model = model;
            },
            delete_animate() {
                this.model = [];
            }
        },
        mounted() {
            bus.$on('view_model', this.view);
            bus.$on('delete_animate', this.delete_animate)
        }
    }
</script>

<style scoped>
    .class_name {
        border-bottom: 1px solid black;
        padding: 5px;
        margin: 10px;
    }
    .class_name_header {
        align-items: center;
    }
</style>