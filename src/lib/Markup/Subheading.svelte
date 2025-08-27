<script lang="ts">
    import type {Snippet} from "svelte"

    interface HeadingProps {
        anchor?: string,
        children?: Snippet
    }

    let {anchor, children}: HeadingProps = $props()
</script>

<h1 id={anchor}>{@render children?.()}</h1>

<style>
    h1 {
        text-wrap: balance;

        font-size: 1.15rem;
        margin: 0.75rem 0 0.625rem;
    }

    h1 :global(.katex) {
        font-weight: 700;
    }
</style>