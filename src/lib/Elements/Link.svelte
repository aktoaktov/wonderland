<script lang="ts">

    import type {Snippet} from "svelte"

    interface LinkProps {
        to: string,
        colorless?: boolean,
        download?: boolean,
        filename?: string
        children: Snippet
    }

    let {
        to,
        colorless = false,
        download = false, filename = to.split("/").at(-1),
        children,
    }: LinkProps = $props()
</script>

<style>
    a {
        text-decoration: underline;
        cursor: pointer;

        color: var(--link);
        border-radius: 0.25rem;
        /*padding: 0 0.125rem*/

        &::selection {
            text-decoration: underline 1px solid var(--text-contrast);
            text-shadow: none;
            background-image: none;
        }

        &:hover {
            color: var(--link-hover)
        }

        &:visited {
            color: var(--link-visited)
        }

        &:focus-visible {
            outline: 0.125rem solid var(--accent)
        }

        &.colorless {
            text-decoration: none;

            &,
            &:hover,
            &:visited {
                text-shadow: unset;
                background-image: unset;
            }

            &:not(:hover),
            &:visited:not(:hover) {
                color: unset;
            }

            &:visited, &:hover {
                color: var(--link);
            }
        }
    }
</style>


<a class:colorless {...(download ? {download: filename} : {})} href={to}>
    {@render children?.()}
</a>

