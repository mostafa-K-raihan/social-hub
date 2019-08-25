<template>
    <div class="sidebar">
        <ul>
            <li> <a href="/app/home/text">Only Tweets with text</a></li>
            <li> <a href="/app/home/media">Only Media</a></li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "Sidebar"
    }
</script>

<style scoped>
    .sidebar {
        grid-column: 1 / 2;

        border: 1px solid red;
        display: grid;
        justify-content: center;
        align-items: center;
    }
</style>