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
    import CodeObject from "$lib/Code/CodeObject.svelte"
</script>

<Title title="Кодирование длин серий"
/>

<Par>
<P>
    Флаги в отдельный поток
</P>
</Par>

<Heading>Pack bits</Heading>

<Par>
<P>
    Программисты из Apple придумали другой алгоритм, дающий стабильно неплохие результаты.
</P>
</Par>

<Par>
<P>
    Давайте схлопывать последовательности, состоящие из одного повторяющегося символа.
    Выделим в исходной строке символы, которые повторяются более двух раз и вычислим счётчики
</P>
<CodeObject c={`"aaaaaldaaarttttoxevvv" -> ("a" * 5) + "ld" + ("a" * 3) + "r" + ("t" * 4) + "oxe" + ("v" * 3)`}/>
<P>
    У нас получилась последовательность блоков двух типов: сжатый и несжатый.
    Сжатые блоки содержат один символ и количество повторений этого символа.
    Несжатые блоки содержат сами несжатые данные.
</P>
<P>
    Можем сериализовать эту последовательность блоков следующим образом.
</P>
</Par>