<template>
    <div>
        <div v-if="files.length === 0" class="upload-btn-wrapper">
            <span class="btn">
                <b-img class="img_upload" :src="require('../assets/upload.png')"></b-img>
                upload file or files
            </span>
            <input type="file" id="input" multiple @change="onFileChange" accept=".ply"/>
        </div>

       <div v-else>
           <b-row>
               <div class="table_f" style="background-color:rgba(0, 0, 0, 0.2); height: 60vh; width: 50vh">
                   <table class="table">
                       <thead>
                           <tr>
                               <th scope="col">#</th>
                               <th scope="col">name</th>
                               <th scope="col" v-if="models.length === 0">size</th>
                               <th scope="col" v-if="models.length === 0">delete</th>
                               <th scope="col" v-if="models.length">class</th>
                               <th scope="col" v-if="models.length">view data</th>
                           </tr>
                       </thead>
                       <tbody v-if="models.length === 0">
                           <tr  v-for="(i, j) in files" :key="j" class="row_table">
                               <th scope="row">{{j+1}}</th>
                               <td>{{i.name}}</td>
                               <td>{{(i.size / 1024).toFixed(2)}} kb</td>
                               <td>
                                   <span>
                                       <img alt ='img' title="delete this item" @click="delete_item(j)" width="25px" style="cursor: pointer; border-radius: 13px" :src="require('../assets/delete.png')">
                                   </span>
                               </td>
                           </tr>
                       </tbody>
                       <tbody v-if="models.length !== 0">
                           <tr v-for="(i, j) in models" :key="j" class="row_table">
                               <th scope="row">{{j+1}}</th>
                               <td>{{files[j].name}}</td>
                               <td>{{i.class}}</td>
                               <td>
                                   <span v-if="models.length !== 0">
                                       <img alt ='img' title="delete this item" @click="delete_item(j)" width="25px" style="cursor: pointer; border-radius: 13px" :src="require('../assets/view.png')">
                                   </span>
                               </td>
                           </tr>
                       </tbody>
                   </table>
               </div>
           </b-row>
           <b-row align-h="center">
               <div class="btn_send" @click="send">classify</div>
           </b-row>
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
                    this.$parent.$emit('recognize', true);
                    let files_pack = new FormData();
                    for (let i = 0; i < this.files.length; i++) {
                        files_pack.append("file", this.files[i])
                    }
                    const headers = {
                        headers: {
                            'Content-Type': 'multipart/form-data',
                            'Access-Control-Allow-Origin': "*"
                        }};
                    axios.post('localhost:5000/get_3d_cnn', files_pack, headers)
                    .then((response) => {
                        console.log(response);
                        this.models = response.data;
                        this.$parent.$emit('recognize', false);
                    })
                    .catch((error) => {
                        this.$parent.$emit('recognize', false);
                    })
                }
            }
        }

    }
</script>

<style scoped>

    .btn_send {
        margin: 15px;
        padding: 5px 15px 5px 15px;
        border: 1px solid greenyellow;
        border-radius: 5px;
        background-color: #8acb27;
        width: 100px;
        cursor: pointer;
        text-align: center;
    }
    .btn_send:hover {
        border: 1px solid black;
        background-color: greenyellow;
    }
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
    .table_f::-webkit-scrollbar-track {
        -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
        background-color: #555555;
    }
    .table_f::-webkit-scrollbar {
        width: 5px;
        background-color: #F5F5F5;
    }
    .table_f::-webkit-scrollbar-thumb {
        background-color: #000000;
        border: 0px solid #555555;
    }
    tr {
        text-align: center;
    }


</style>