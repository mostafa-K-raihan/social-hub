/* eslint-disable no-console */
import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';

Vue.use(Vuex);
const API_URL = 'http://localhost:8000/app/';

const GET_TWEETS = 'GET_TWEETS';
const GET_MEDIA = "GET_MEDIA";
const OFFSET_NEXT = 'OFFSET_NEXT';
const MEDIA_PAGE_NEXT = "MEDIA_PAGE_NEXT";

const store = new Vuex.Store({
    state: {
        twitter: {
            tweets:[],
            pageCount: 0,

            media: [],
            mediaPageCount: 0,

        }

    },

    mutations: {
        [GET_TWEETS](state, tweets){
            console.log("Mutating Tweets");
            state.twitter.tweets = tweets;
        },
        [GET_MEDIA](state, media) {
            console.log("Mutating Media");
            state.twitter.media = media;
        },
        [OFFSET_NEXT](state) {
            console.log("Mutating pageCount");
            if(!state.twitter.tweets.length){
                console.log("No More Tweets");
            }else {
                state.twitter.pageCount += 1;
            }
        },
        [MEDIA_PAGE_NEXT](state) {
            console.log("Mutating media page count");
            if(!state.twitter.media.length) {
                console.log("No more Media");
            }else {
                state.twitter.mediaPageCount += 1;
            }
        }
    },

    actions: {
        getTweets( {commit, state} ){

            axios.get(`${API_URL}home/text/data?page=${state.twitter.pageCount}`)
                .then(res=>{
                    res.status === 200 ?
                        commit(GET_TWEETS, res.data) :
                        console.log("Something went wrong");
                })
                .catch(err=>console.log(err))
        },

        getMedia( {commit, state} ) {
            axios.get(`${API_URL}home/media/data?page=${state.twitter.mediaPageCount}`)
                .then(res=> {
                    res.status === 200 ?
                        commit(GET_MEDIA, res.data) :
                        console.log("Something went wrong");
                })
                .catch(err=>console.log(err));
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
        },

        getMedia: state => {
            return state.twitter.media;
        },

        getMediaCount: state => {
            return state.twitter.media.length;
        }


    }
});

export default store;