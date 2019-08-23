<template>
    <div class="content">
        <TweetCard v-for="(tweet,index) in tweets" :key="index" :tweet="tweet"></TweetCard>
    </div>
</template>

<script>
    /* eslint-disable no-console */

    import TweetCard from "./TweetCard";
    import axios from 'axios';
    const API_URL = 'http://localhost:8000/app/';
    export default {
        name: "MainContent",
        components: {
            TweetCard,
        },
        data () {
            return {
                tweets:[]
            }
        },
        mounted() {
            axios.get(`${API_URL}home/data`)
                .then(res=>{
                    res.status === 200 ?
                        this.tweets = res.data : console.log("Something went wrong");
                })
                .catch(err=>console.log(err))
        }
    }
</script>

<style scoped>
    .content {
        grid-column: 2/3;
        border: 1px solid red;
        display: grid;
        justify-content: center;
        align-items: center;
        overflow-y: scroll;
    }
</style>