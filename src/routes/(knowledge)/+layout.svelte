<script>
    let {children} = $props()
</script>

<article>
    {@render children?.()}
</article>

<div></div>

<style>
    article {
        max-width: 60rem;
        margin: 0 auto;
    }

    div {
        height: 20rem;
    }
</style>