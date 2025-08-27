<script lang="ts">
    import {onMount, type Snippet} from "svelte"

    interface ImageProps {
        src: string,
        alt?: string,
        placeholder?: string,

        width?: string,
        height?: string,
        children?: Snippet
    }

    let {
        placeholder = undefined,
        src, alt = "",
        width = undefined, height = undefined,
        children,
    }: ImageProps = $props()
</script>

<figure>
    <div class="wrapper"
         style:width={width} style:height={height}>

        <img {src} {alt}
             role={alt === "" ? "presentation": undefined}
             loading="lazy"
             style:width={width} style:height={height}
        />
    </div>

    {#if children}
        <figcaption>{@render children()}</figcaption>
    {/if}
</figure>

<style>
    figure {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 0.25rem;
    }

    :global(article) {
        figure {
            margin: 1.25rem;

            img {
                width: 100%;
                min-height: 8rem;
                object-fit: contain;
            }
        }
    }

    img {
        border-radius: 0.625rem;
        user-select: none;
    }

    figcaption {
        text-align: center;

        font-size: 0.875rem;
        color: var(--text-caption);
    }
</style>