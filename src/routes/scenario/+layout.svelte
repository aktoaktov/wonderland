<script>
    let {children} = $props()
</script>

<div class="contents">
    {@render children?.()}
</div>

<style>
    .contents {
        max-width: 64rem;
        margin: 0 auto;
        position: relative;
    }
</style>