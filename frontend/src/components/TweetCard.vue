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
        height: 30vh;
        display: grid;
        grid-template-columns: 30% 1fr;
        grid-template-rows: auto;


    }

    .author {
        font-size: 1.8rem;

        background-image:  linear-gradient(45deg, #2c3e50, #33545f, #551789);
        background-size: 400%;
        animation: author-animation 10s infinite alternate;

        display: grid;
        align-items: center;
        justify-content: center;
        color: whitesmoke;


    }

    .time {
        font-size: 1rem;
    }
    .content {
        background-image: linear-gradient(45deg, #456456, #567567, #678678);
        background-size: 400%;
        animation: author-animation 10s infinite alternate;
        font-size: 1.2rem;
        padding: 1.5rem 0.2rem;
    }

    .tweet {
        color: whitesmoke;
        filter: brightness(90%);

    }
    .tweet a {
        color: wheat;
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