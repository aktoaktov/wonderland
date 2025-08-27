<script lang="ts">
    import InternalCode from "$lib/Code/InternalCode.svelte"
    import type {LanguageLiteral} from "$lib/Code/languages"

    interface CodeProps {
        language?: LanguageLiteral,
        code: string
    }

    let {language = "pseudocode", code}: CodeProps = $props()
    code = code.trim()
</script>

<div class="codeblock">
    <div class="overflow-box">
        <InternalCode language={language} code={code}/>
    </div>
    <!--<CopyButton text={children}/>-->
</div>


<style>
    .codeblock {
        position: relative;

        background: var(--box-back);
        padding: 0.5rem 0.85rem;
        border-radius: 0.625rem;

        margin: 0 -0.85rem 1.5rem;

        page-break-inside: avoid;
        print-color-adjust: exact;

        & > .overflow-box {
            overflow-x: scroll;
        }

        /*& > .copy-button {*/
        /*    position: absolute;*/
        /*    top: 0.5rem;*/
        /*    right: 0.5rem;*/
        /*}*/
    }
</style>