<script lang="ts">
    import Header from "$lib/Layout/Header.svelte"
    import {pageTitle} from "$lib/stores"
    import Link from "$lib/Elements/Link.svelte"

    let {children} = $props()
</script>

<svelte:head>
    <title>{$pageTitle}</title>
</svelte:head>

<Header>
    {#snippet navigation()}
        <Link colorless to="/scenario">Сценарий</Link>
    {/snippet}
</Header>

<main>
    {@render children?.()}
</main>
