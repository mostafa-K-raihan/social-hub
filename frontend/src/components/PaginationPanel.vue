<template>
    <div class="pagination">
        <div> << </div>
        <div> < </div>
        <div> > </div>
        <div> >> </div>
    </div>
</template>

<script>
    export default {
        name: "PaginationPanel"
    }
</script>

<style scoped>
    .pagination{
        border: 1px solid tomato;
        display: grid;
        align-items: center;
        justify-content: center;
    }
</style>