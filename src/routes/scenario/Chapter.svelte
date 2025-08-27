<script lang="ts">

    import type {Snippet} from "svelte"

    interface ChapterProps {
        children: Snippet
    }

    let {children}: ChapterProps = $props()
</script>

<div class="chapter">
    {@render children?.()}
</div>

<style>
    .chapter {
        display: flex;
        flex-flow: row wrap;
        column-gap: 3rem;
        row-gap: 1rem;

        margin: 0 0 2rem;
    }

</style>