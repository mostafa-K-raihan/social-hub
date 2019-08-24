<template>
    <div class="content">
        <TweetCard v-for="(tweet,index) in computedTweets" :key="index" :tweet="tweet"></TweetCard>
        <div v-if="!computedTweets.length">
            No More Tweets
        </div>
    </div>
</template>

<script>
    /* eslint-disable no-console */

    import TweetCard from "./TweetCard";


    export default {
        name: "MainContent",
        components: {
            TweetCard,
        },
        mounted() {
            this.$store.dispatch('getTweets');
        },
        computed: {
            computedTweets() {
                return this.$store.state.twitter.tweets;
            }
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