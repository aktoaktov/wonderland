<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Code from "$lib/Code/Code.svelte"
    import Link from "$lib/Elements/Link.svelte"
    import EnumList from "$lib/List/EnumList.svelte"
    import ListItem from "$lib/List/ListItem.svelte"
    import Image from "$lib/Elements/Image.svelte"
    import Proof from "$lib/Stencils/Blocks/Proof.svelte"
</script>

<Title title="Сжатый бор"
/>

<Par>
    <P>
        Я уже упоминал в статье &laquo;бор&raquo; про способ оптимизации бора.
        Сейчас мы подробно разберем эту оптимизированную структуру данных, называемую сжатым бором.
    </P>
</Par>

<Par>
    <P>
        <b>Сжатый бор</b> &mdash; бор, в котором каждый прямой путь без ветвлений
        превращён в одно ребро со сложной меткой.
    </P>
</Par>

