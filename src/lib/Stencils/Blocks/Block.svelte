<script lang="ts">
    import Icon from "$lib/Elements/Icon.svelte"
    import type {Snippet} from "svelte"

    interface BlockProps {
        kind: string,
        icon: string,
        title: string | Snippet,
        children?: Snippet
    }

    let {kind, icon, title, children}: BlockProps = $props()
</script>

<div class="block"
     class:definition={kind === "definition"}
     class:fact={kind === "fact"}
     class:theorem={kind === "theorem"}>

    <h3>
        <Icon name={icon} size={1.25}/>
        {#if typeof title === 'function'}
            {@render title?.()}
        {:else}
            {title}
        {/if}
    </h3>

    {@render children?.()}
</div>

<style>
    .block {
        padding: 0.75rem 0.85rem;
        border-radius: 0.625rem;
        overflow-x: scroll;

        margin: 0 -0.75rem 1.5rem;

        page-break-inside: avoid;

        &.definition {
            background-color: oklch(95.1% 0.026 236.824); /* sky 100 */
            --accent-color: oklch(50% 0.134 242.749); /* sky 700 */
        }

        &.theorem {
            background-color: oklch(97.3% 0.071 103.193);
            --accent-color: oklch(66.6% 0.179 58.318)

        }

        &.fact {
            background-color: oklch(96.2% 0.044 156.743);
            --accent-color: oklch(62.7% 0.194 149.214)
        }

        & :global(*):last-child {
            margin-bottom: 0;
        }
    }

    h3 {
        display: flex;
        flex-flow: row nowrap;
        gap: 0.5rem;
        align-items: center;

        margin: 0 0 0.375rem;

        font-weight: 600;
        font-size: 1rem;

        color: var(--accent-color)
    }
</style>