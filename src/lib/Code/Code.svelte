<script lang="ts">
    import InternalCode from "$lib/Code/InternalCode.svelte"
    import type {LanguageLiteral} from "$lib/Code/languages"

    interface CodeProps {
        language?: LanguageLiteral,
        c: string
    }

    let {language = "pseudocode", c}: CodeProps = $props()
</script>

<span class="code">
  <InternalCode language={language} code={c}/>
</span>

<style>
    .code {
        print-color-adjust: exact;

        background: var(--box-back);
        padding: 0 0.25rem;
        margin: 0.125rem 0;
        border-radius: 0.25rem;

        display: inline-flex;
        align-items: center;
        gap: 0.25rem;
    }
</style>