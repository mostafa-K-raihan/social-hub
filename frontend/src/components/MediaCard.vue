<template>
    <div class="media_card">
            <img v-if='media.media_type==="photo"' :src="media.media_url">
            <video v-if='media.media_type === "video"' controls>
                <source :src="media.media_url" type="video/mp4">
            </video>
<!--        <div class="media_type"> {{media.media_type}}</div>-->
<!--        <div class="media_content">-->
<!--            -->
<!--        </div>-->


    </div>
</template>

<script>
    export default {
        name: "MediaCard",
        props: {
            media : Object,
        },

    }
</script>

<style scoped>
    .media_card {
        background-image: linear-gradient(to right, #2c3e50, #33545f, #551789);
        background-size: 400%;
        animation: author-animation 10s infinite alternate;
    }
    @keyframes author-animation {
        0% {background-position: left;}
        100%{background-position: right;}
    }

    img, video {
        width: 40vw;
        height: 40vh;
        object-fit: contain;
    }

</style>