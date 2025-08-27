<script lang="ts">
    import InternalCode from "$lib/Code/InternalCode.svelte"
    import type {LanguageLiteral} from "$lib/Code/languages"

    interface CodeProps {
        language?: LanguageLiteral,
        c: string
    }

    let {language = "pseudocode", c}: CodeProps = $props()
</script>

<div class="code-display">
    <InternalCode language={language} code={c}/>
</div>

<style>
    .code-display {
        print-color-adjust: exact;

        text-align: center;

        padding: 0 1.25rem;
        margin: 0 0 0.85rem;

        overflow-x: scroll;
        overflow-y: hidden;
    }
</style>