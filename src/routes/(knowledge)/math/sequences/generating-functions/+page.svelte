<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Link from "$lib/Elements/Link.svelte"
    import Code from "$lib/Code/Code.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import Image from "$lib/Elements/Image.svelte"
    import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
    import Proof from "$lib/Stencils/Blocks/Proof.svelte"
</script>

<Title title="Производящие функции"
/>

<Definition title="Производящая функция">
    <P>
        <b>Производящей функцией</b> последовательности <Math m={`a_n`}/> называется функция
    </P>
    <Math display m={`G(z) = a_0 + a_1 \\cdot z + a_2 \\cdot x^2 + \\dotsb = \\sum_{k=0}^\\oo a_n \\cdot z^n`}/>
</Definition>

<Par>
    <P>
        Производящая функция хранит всю информацию о последовательности.
        Более того, с помощью производящих функций можно находить конкретные формулы для элементов последовательности,
        анализировать асимптотику, раскладывать другие функции в ряд и так далее.
    </P>
    <P>
        По аналогии с многочленами, есть удобное обозначение коэффициентов.
        Пусть <Math m={`G(z)`}/> &mdash; производящая функция последовательности <Math m={`a_n`}/>.
        Коэффициент при <Math m={`z^n`}/> обозначается
    </P>
    <Math display m={`[z^n] G(z) \\defeq a_n`}/>
</Par>

<Heading>Свойства производящих функций</Heading>

<Par>
    <P>
        Здесь везде пусть <Math m={`A(z)`}/> &mdash; производящая функция последовательности <Math m={`a_n`}/>
        и <Math m={`B(z)`}/> &mdash; производящая функция последовательности <Math m={`b_n`}/>.
    </P>
    <P>
        Линейная комбинация производящих функций &mdash; производящая функция линейной комбинации последовательностей.
    </P>
    <Math display m={`[z^n] \\big( \\alpha A(z) + \\beta \\cdot B(z) \\big) = \\alpha \\cdot a_n + \\beta \\cdot b_n`}/>
</Par>