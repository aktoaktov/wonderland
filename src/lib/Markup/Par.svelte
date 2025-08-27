<script>
  let {children} = $props()
</script>

<div class="par">{@render children?.()}</div>

<style>
  .par {
    margin: 0 0 1.5rem;
  }
</style>