<script lang="ts">
    import {renderMath} from "./math"

    interface MathProps {
        m: string,
        display?: boolean
        big?: boolean
    }

    let {m, display = false, big = false}: MathProps = $props()
</script>


{#if display}
    <div class="math-display" class:big>
        {@html renderMath(m, true)}
    </div>
{:else}
  <span class="math">
    {@html renderMath(m, false)}
  </span>
{/if}


<style>
    .math-display {
        padding: 0 1.25rem;
        margin: 0 0 0.85rem;

        &.big {
            margin: 0.85rem 0 0.85rem;
        }

        overflow-x: scroll;
        overflow-y: hidden;
    }


    :global(.cyrillic_fallback) {
        font-family: Inter, sans-serif;
        font-size: 0.82em;
    }

    :global(.katex) {
        :global(.text) {
            font-family: Inter, sans-serif;
            font-size: 0.95em;
        }

        :global(.code) > :global(.text) {
            font: 0.81em "JetBrains Mono", "Monospace", monospace !important;
            font-feature-settings: "cv07", "cv14", "cv16";

            background: var(--box-back);
            padding: 0 0.25rem;
            border-radius: 0.25rem;
        }
    }


    :global(.katex-display) {
        margin: 0 !important;
    }

    :global(.katex) {
        white-space: nowrap
    }

    :global(b) :global(.katex) {
        font-weight: 700;
    }
</style>
