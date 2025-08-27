<script lang="ts">

    import type {Snippet} from "svelte"

    interface HeaderProps {
        navigation?: Snippet
    }

    let {navigation}: HeaderProps = $props()
</script>


<header>
    <img src="/favicon.svg" alt="" role="presentation"/>
    <nav>{@render navigation?.()}</nav>
</header>

<style>
    header {
        top: 0;
        position: sticky;
        z-index: 3;

        display: flex;
        gap: 3rem;
        align-items: center;

        padding: 0.75rem 1.25rem;

        border-bottom: 1px solid #0f172a1a;
        background: color-mix(in oklab, #fafdff 75%, transparent);
        backdrop-filter: blur(0.75rem);

        min-height: 2rem;
        /*width: 100%;*/

        & > img {
            pointer-events: none;
            user-select: none;
            height: 2.25rem;
            width: 2.25rem;
        }

        & > nav {
            display: flex;
            gap: 1.5rem;

            font-weight: 600;
        }

        @media (max-width: 48rem) {
            position: static;
        }
    }
</style>
