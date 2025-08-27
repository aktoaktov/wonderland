<script lang="ts">
    import type {Snippet} from "svelte"

    interface EnumListProps {
        wide?: boolean,
        children: Snippet
    }

    let {wide, children}: EnumListProps = $props()
</script>


<ol class:wide>
    {@render children?.()}
</ol>

<style>
    ol {
        padding: 0 1.375rem;
        margin: 0 0 1rem;

        page-break-inside: avoid;

        :global(li)::marker {
            color: var(--accent-color, var(--accent));
            font-weight: 600;
        }
    }

    .wide :global(li) {
        margin-bottom: 0.125rem;
    }
</style>
