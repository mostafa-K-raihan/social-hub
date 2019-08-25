<template>
    <div class="container">

        <div v-show="url === 'text'" class="content">
            <TweetCard v-for="(tweet,index) in computedTweets" :key="index" :tweet="tweet"></TweetCard>
            <div v-if="!computedTweets.length">
                No More Tweets
            </div>
        </div>
        <div v-show="url==='media'" class="content">
            <MediaCard v-for="(media, index) in computedMedia" :key="index" :media="media"></MediaCard>
        </div>
    </div>

</template>

<script>
    /* eslint-disable no-console */

    import TweetCard from "./TweetCard";
    import MediaCard from "./MediaCard";


    export default {
        name: "MainContent",
        props: {
            url: String,
        },
        components: {
            TweetCard,
            MediaCard,
        },
        mounted() {
            if(this.url === 'text')this.$store.dispatch('getTweets');
            else if(this.url === 'media')this.$store.dispatch('getMedia');
        },
        computed: {
            computedTweets() {
                return this.$store.state.twitter.tweets;
            },

            computedMedia() {
                return this.$store.state.twitter.media;
            }
        }
    }
</script>

<style scoped>
    .container {
        grid-column: 2/3;
        /*border: 1px solid red;*/
        display: grid;
        /*justify-content: center;*/
        /*align-items: center;*/
        overflow-y: scroll;
        grid-template-rows: auto;
        grid-template-columns: 1fr;
    }

    .content {

        /*border: 1px solid red;*/
        display: grid;
        grid-gap: .5rem;
        grid-template-columns: 50%;
        grid-template-rows: repeat(10, auto);

        justify-content: center;
        align-items: center;

    }
</style>