<script lang="ts">
    import type {Snippet} from "svelte"

    interface BulletListProps {
        wide?: boolean,
        children: Snippet
    }

    let {wide, children}: BulletListProps = $props()
</script>

<ul class:wide>
    {@render children?.()}
</ul>

<style>
    ul {
        padding: 0 1.375rem;
        margin: 0 0 1rem;

        & :global(li::marker) {
            content: "● ";
            color: var(--accent-color, var(--accent));

            font-size: 0.625rem;
            margin-right: 0.625rem;
        }
    }

    .wide :global(li) {
        margin-bottom: 0.125rem;
    }
</style>

