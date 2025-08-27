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

        font-size: 1.36rem;
        margin: 3rem 0 1rem;

        scroll-margin-top: 4rem;
    }

    h1 :global(.katex) {
        font-weight: 700;
    }
</style>