<script lang="ts">
    import type {Snippet} from "svelte"

    interface ListItemProps {
        children: Snippet
    }

    let {children}: ListItemProps = $props()
</script>

<style>
    li {
        margin-bottom: 0.5rem;
        padding-left: 0.125rem;
        min-height: 1.5rem;
    }
</style>

<li>
    {@render children?.()}
</li>