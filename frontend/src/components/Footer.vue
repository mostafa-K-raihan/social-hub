<template>
    <div class="footer">
        This is Footer
    </div>
</template>

<script>
    export default {
        name: "Footer"
    }
</script>

<style scoped>
    .footer {
        grid-column: 1 / 3;
        grid-row: 3 / 4;

        border: 1px solid red;
        display: grid;
        justify-content: center;
        align-items: center;
    }
</style>