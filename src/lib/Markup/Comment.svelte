<script>
    let {children} = $props()
</script>

<p class="comment">{@render children?.()}</p>

<style>
    .comment {
        margin: 0 0 0.5rem;
        text-wrap: pretty;
        font-size: 0.8rem;
        line-height: 1.5;
    }
</style>