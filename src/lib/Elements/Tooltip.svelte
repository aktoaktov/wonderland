<script lang="ts">
    import {
        arrow,
        autoUpdate,
        flip,
        shift,
        offset,
        useDismiss,
        useFloating,
        useHover,
        useInteractions,
        useRole,
        inline as inlineMiddleware,
    } from "@skeletonlabs/floating-ui-svelte"
    import {fade} from "svelte/transition"
    import type {Snippet} from "svelte"

    import {FloatingArrow} from "@skeletonlabs/floating-ui-svelte"

    interface TooltipProps {
        content: Snippet,
        children: Snippet
        inline?: boolean
    }

    const PADDING = 8

    let open = $state(false)
    let arrowElement = $state(null)

    let {inline, content, children}: TooltipProps = $props()

    const floating = useFloating({
        whileElementsMounted: autoUpdate,
        get open() {
            return open
        },
        onOpenChange: (v) => {
            open = v
        },
        placement: "top",
        get middleware() {
            return [
                offset(PADDING),
                flip({
                    fallbackAxisSideDirection: "start",
                    padding: PADDING,
                }),
                arrowElement && arrow({element: arrowElement}),
                shift({padding: PADDING}),
                inlineMiddleware(),
            ]
        },
    })

    const role = useRole(floating.context, {role: "tooltip"})
    const hover = useHover(floating.context, {move: false})
    const dismiss = useDismiss(floating.context)
    const interactions = useInteractions([role, hover, dismiss])
</script>

<svelte:element this={inline ? 'span' : 'div'} class="tooltip">
    <!-- Reference Element -->
    <svelte:element this={inline ? 'span' : 'div'}
            bind:this={floating.elements.reference}
            {...interactions.getReferenceProps()}
    >
        {@render children?.()}
    </svelte:element>

    {#if open}
        <div
                bind:this={floating.elements.floating}
                style={floating.floatingStyles}
                {...interactions.getFloatingProps()}
                class="floating"
                transition:fade={{ duration: 100 }}
        >
            {@render content?.()}
            <FloatingArrow bind:ref={arrowElement} context={floating.context} fill="var(--tooltip-back)"/>
        </div>
    {/if}
</svelte:element>

<style>
    .tooltip {
        & .floating {
            font-size: 0.85rem;

            max-width: 24rem;
            border-radius: 0.25rem;
            padding: 0.25rem 0.5rem;

            background: var(--tooltip-back);

            filter: drop-shadow(0 0.15rem 0.25rem color-mix(in oklab, var(--shadow) 25%, transparent));

            z-index: 999;
        }
    }
</style>