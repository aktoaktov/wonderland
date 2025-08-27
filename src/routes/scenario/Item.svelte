<script lang="ts">
    import type {Snippet} from "svelte"

    interface ItemProps {
        optional?: boolean,
        planned?: boolean,
        link?: string,
        children: Snippet
    }

    let {
        optional = false, planned = false, link,
        children,
    }: ItemProps = $props()
</script>

<div class="item" class:planned>
    <a href={link}>{@render children?.()}</a>
</div>

<style>
    a {
        text-decoration: unset;

        &:not(:hover) {
            color: unset;
        }

        &:hover:visited {
            color: var(--link);
        }
    }

    .planned {
        color: var(--text-placeholder)
    }
</style>