<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
</script>

<Title title="Позиционные системы счисления"
/>

<Par>
    <P>
        <b>Позиционное представление</b> (positional notation) числа <Math m={`n`}/> по основанию <Math m={`b`}/>
        &mdash; способ представить число <Math m={`n`}/> в виде суммы
    </P>
    <Math display
          m={`n = \\bigl( \\dotsm \\, a_2 \\, a_1 \\, a_0 \\, . \\, a_{-1} \\, a_{-2} \\, \\dotsm \\bigr)_b
          = \\dotsb + a_2 \\cdot b^2 + a_1 \\cdot b + a_0 + a_{-1} \\cdot b^{-1} + a_{-2} \\cdot b^{-2} + \\dotsb`}/>
    <P>
        Например, число <Math m={`(173.4)_8 = 1 \\cdot 8^2 + 7 \\cdot 8 + 3 + 4 \\cdot 8^{-1} = 123.5`}/>.
    </P>
    <P>
        Позиционное представление, вопреки школьному запрету, может существовать для любых действительных оснований.
        Числа <Math m={`a_k`}/> называются <b>цифрами</b> в этой системе счисления,
        и для всех них всегда верно неравенство <Math m={`0 \\le a_k < b`}/>.
        Это гарантирует единственность позиционного представления.
    </P>
</Par>

<Par>
    <P>
        Из позиционного представления неотрицательного числа
        <Math m={`n = \\bigl( \\dotsm \\, a_2 \\, a_1 \\, a_0 \\, . \\, a_{-1} \\, a_{-2} \\, \\dotsm \\bigr)_b`}/>
        можно сразу выделить значение произвольного <Math m={`a_k`}/>
    </P>
    <Math display m={`a_k = \\left\\lfloor \\frac{n}{b^k} \\right\\rfloor \\bmod b`}/>
</Par>