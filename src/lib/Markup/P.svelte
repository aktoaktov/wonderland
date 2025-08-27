<script>
    let {children} = $props()
</script>

<p>{@render children?.()}</p>

<style>
    p {
        margin: 0 0 0.5rem;
        text-wrap: pretty;
        line-height: 1.5;
    }
</style>