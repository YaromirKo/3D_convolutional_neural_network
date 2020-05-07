<template>
    <div>
        <div v-if="files.length === 0" class="upload-btn-wrapper">
            <span class="btn">
                <b-img class="img_upload" :src="require('../assets/upload.png')"></b-img>
                upload file or files
            </span>
            <input type="file" id="input" multiple @change="onFileChange" accept=".ply"/>
        </div>

        <div class="table_f" v-if="files.length !== 0" style="background-color:rgba(0, 0, 0, 0.2); height: 70vh; width: 50vh">
            <table class="table">
                <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">name</th>
                    <th scope="col">size</th>
                    <th scope="col">delete</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(i, j) in files" :key="j" class="row_table">
                    <th scope="row">{{j+1}}</th>
                    <td>{{i.name}}</td>
                    <td>{{(i.size / 1024).toFixed(2)}} kb</td>
                    <td><span><img alt ='img' title="delete this item" @click="delete_item(j)" width="25px" style="cursor: pointer; border-radius: 13px" :src="require('../assets/delete.png')"></span></td>
                </tr>
                </tbody>
            </table>
        </div>

    </div>
</template>

<script>
    /* eslint-disable */
    import axios from 'axios'

    export default {
        name: 'Upload',
        data() {
            return {
                files: [],
                show_uploader: true,
                preloader: false,
                models: []
            }
        },
        methods: {
            onFileChange(e) {
                this.files = Object.values(e.target.files);
                this.show_uploader = false;
                console.log(this.files);
            },
            delete_item(index) {
                this.files.splice(index, 1)
            },
            send() {
                if (this.files.length !== 0) {
                    this.preloader = true;
                    let files_pack = new FormData();
                    for (let i = 0; i < this.files.length; i++) {
                        files_pack.append("file", this.files[i])
                    }
                    const headers = {headers: {
                            'Content-Type': 'multipart/form-data',
                            'Access-Control-Allow-Origin': "*"
                        }};
                    axios.post('localhost:5000/get_3d_cnn', files_pack, headers)
                    .then((response) => {
                        this.files = [];
                        console.log(response);
                        this.models = response.data;
                        this.preloader = false
                    })
                    .catch((error) => {
                        this.preloader = false
                    })
                }
            }
        }

    }
</script>

<style scoped>

    .img_upload {
        width: 50px;
    }
    .upload-btn-wrapper {
        position: relative;
        overflow: hidden;
        display: inline-block;
    }
    .btn {
        border: 1px solid black;
        padding: 8px 20px;
        border-radius: 8px;
    }
    .upload-btn-wrapper:hover {
        background-color: #bebbbb;
        border-radius: 8px;
    }
    .upload-btn-wrapper input[type=file] {
        font-size: 100px;
        position: absolute;
        left: 0;
        top: 0;
        opacity: 0;
    }
    .row_table:hover {
        background-color: rgba(0, 0, 0, 0.5);
        color: white;
    }
    .table_f {
        overflow: auto;

    }
    .table_f::-webkit-scrollbar-track
    {
        -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
        background-color: #555555;
    }

    .table_f::-webkit-scrollbar
    {
        width: 5px;
        background-color: #F5F5F5;
    }

    .table_f::-webkit-scrollbar-thumb
    {
        background-color: #000000;
        border: 0px solid #555555;
    }


</style>