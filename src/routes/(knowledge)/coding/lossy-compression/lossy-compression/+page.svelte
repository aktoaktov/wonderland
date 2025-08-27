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

<Title title="Сжатие координат"
/>

<Par>
    <P>
        Несмотря на слово &laquo;координаты&raquo; в названии, речь пойдет не о них, а о технике сжатия с потерями,
        заточенную под уменьшение диапазона и линейного размера данных.
        Этот метод применяется преимущественно для координат
        (номеров элементов в последовательностях, индексов массивов, ...),
        отсюда и пошло название метода <b>сжатие координат</b> (coordinates compression).
    </P>
</Par>