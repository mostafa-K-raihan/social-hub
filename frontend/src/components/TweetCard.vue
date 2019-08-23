<template>
    <div class="card">
        <div class="content"  v-html="tweetWithAnchor"></div>
        <div class="time">{{tweet.date}}</div>
    </div>

</template>

<script>
    import anchorme from 'anchorme';
    export default {
        name: "TweetCard",
        props: {
            tweet : Object,
        },
        computed: {
            tweetWithAnchor() {
                return anchorme(this.tweet.text, {
                    truncate:[26,15],
                });
            },
        }
    }
</script>

<style scoped>
    .card{
        border: 1px solid tomato;
        height: 20vh;
        display: grid;
        align-items: center;
        justify-content: center;
    }
</style>