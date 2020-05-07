<template>
    <div>
        <b-row v-if="models.length === 0" align-h="center">
            <div>here will be information about your models</div>
            <div class="w-100"></div>
            <div><b-img :src="require('../assets/loader.png')" width="20"></b-img></div>
        </b-row>
        <b-row v-else>
            123
        </b-row>
    </div>
</template>

<script>
    export default {
        name: "InfoChart",
        data() {
            return {
                models: [1],
            }
        }
    }
</script>

<style scoped>

</style>