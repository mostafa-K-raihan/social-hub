<template>
    <div class="pagination">
        <button v-show='hasMoreTweets' type="button" class="pagination__item" @click="pagination"> Load More Tweets </button>
    </div>
</template>

<script>
    export default {
        name: "PaginationPanel",
        methods: {
            pagination() {
                this.$store.commit('OFFSET_NEXT');
                this.$store.dispatch('getTweets');
            }
        },
        computed: {
            hasMoreTweets() {
                return this.$store.getters.getTweetCount > 0;
            }
        }
    }
</script>

<style scoped>
    .pagination{
        /*border: 1px solid tomato;*/
        display: grid;

        align-items: center;
        justify-content: center;
        grid-template-columns: 1fr;
        margin: .5rem;
    }

    .pagination__item {
        /*border: 1px solid tomato;*/
        background: tomato;
        outline: none;
        color: whitesmoke;
        padding: 1rem;
        font-size: 1.2rem;
        border-radius: .5rem;
        box-shadow: whitesmoke 2px 5px;

        /*width: 5rem;*/
    }

    /*.pagination__item:hover{*/
    /*    transform: scale(1.1);*/
    /*    transition: 300ms transform ease-in-out;*/
    /*    !*cursor: pointer;*!*/
    /*}*/
</style>