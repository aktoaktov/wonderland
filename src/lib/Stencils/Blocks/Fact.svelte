<script lang="ts">
    import Block from "$lib/Stencils/Blocks/Block.svelte"
    import type {Snippet} from "svelte"

    interface TitleProps {
        title: string | Snippet,
        children?: Snippet
    }

    let {title, children}: TitleProps = $props()
</script>

<Block kind="fact" icon="lamp" {title} {children}/>