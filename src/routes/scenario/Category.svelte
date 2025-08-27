<script lang="ts">
    import type {Snippet} from "svelte"

    interface CategoryProps {
        title: string,
        children: Snippet
    }

    let {title, children}: CategoryProps = $props()
</script>

<div class="category">
    <h2>{title}</h2>
    {@render children?.()}
</div>

<style>
    .category {
        display: flex;
        flex-flow: column nowrap;
        gap: 0.25rem;
    }

    h2 {
        font-size: 1.15rem;
        font-weight: 600;
        margin: 0.25rem 0;
    }
</style>