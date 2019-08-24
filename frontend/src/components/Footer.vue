<template>
    <div class="footer">
        <pagination-panel></pagination-panel>
    </div>
</template>

<script>
    import PaginationPanel from "./PaginationPanel";
    export default {
        name: "Footer",
        components: {
            PaginationPanel
        }
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