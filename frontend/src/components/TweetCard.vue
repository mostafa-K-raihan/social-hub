<template>
    <div class="card">
        <div class="author">
            <span>{{tweet.user}}</span>
            <div class="time">{{tweetTime}}</div>
        </div>
        <div class="content">
            <div class="tweet" v-html="tweetWithAnchor"></div>

        </div>

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

            tweetTime() {
                return new Date(this.tweet.date).toLocaleTimeString()
            }
        }
    }
</script>

<style scoped>
    .card{
        border: 1px solid tomato;
        height: 20vh;
        display: grid;
        grid-template-columns: 20% 1fr;
        /*align-items: center;*/
        /*justify-content: center;*/

    }

    .author {
        font-size: 1.8rem;
        /*padding: 1.5em 1em;*/
        background-image: linear-gradient(to right, #2c3e50, #9aae45);
        background-size: 400%;
        animation: author-animation 10s infinite alternate;
        /*background: aqua;*/
        display: grid;
        align-items: center;
        justify-content: center;
        color: whitesmoke;
        align-self: center;
        height: 100%;
    }

    .time {
        font-size: 1rem;
    }
    .content {
        background: turquoise;
        color: #2c3e50;
        font-size: 1.2rem;
        padding: 1.5rem 0.2rem;
        align-self: start;
        height: 100%;
    }

    @keyframes author-animation {
        0% {
            background-position: left;
        }
        100%{
            background-position: right;
        }

    }

</style>