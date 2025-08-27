<script lang="ts">
    import type {Snippet} from "svelte"

    interface TitleProps {
        title: string
        children?: Snippet
    }

    let {title, children}: TitleProps = $props()
</script>

<svelte:head>
    <title>{title}</title>
</svelte:head>

<div class="title">
    {#if children}
        {@render children()}
    {:else}
        <h1>{title}</h1>
    {/if}
</div>

<style>
    .title {
        margin: 0 1.25rem 1.5rem;

        & > h1 {
            font-size: 1.75rem;
            margin: 1.25rem 0 1rem;

            text-align: center;
            text-wrap: balance;
        }
    }
</style>