/* eslint-disable no-console */
import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';

Vue.use(Vuex);
const API_URL = 'http://localhost:8000/app/';

const GET_TWEETS = 'GET_TWEETS';

const OFFSET_NEXT = 'OFFSET_NEXT';

const store = new Vuex.Store({
    state: {
        twitter: {
            tweets:[],
            pageCount: 0,

        }

    },

    mutations: {
        [GET_TWEETS](state, tweets){
            console.log("Mutating Tweets");
            state.twitter.tweets = tweets;
        },

        [OFFSET_NEXT](state) {
            console.log("Mutating pageCount");
            if(!state.twitter.tweets.length){
                console.log("No More Tweets");
            }else {
                state.twitter.pageCount += 1;
            }
        },
    },

    actions: {
        getTweets( {commit, state} ){

            axios.get(`${API_URL}home/data?page=${state.twitter.pageCount}`)
                .then(res=>{
                    res.status === 200 ?
                        commit(GET_TWEETS, res.data) :
                        console.log("Something went wrong");
                })
                .catch(err=>console.log(err))
        }

    },

    getters: {
        getTweets : state => {
            return state.twitter.tweets;
        },

        getOffset: state => {
            return state.twitter.offset;
        },

        getTweetCount: state => {
            return state.twitter.tweets.length;
        }

    }
});

export default store;