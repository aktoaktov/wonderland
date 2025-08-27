<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
</script>

<Title title="Оценки Чернова"
/>

<Theorem title="Оценки Чернова">
    <P>
        Пусть у нас есть независимые случайные величины <Math m={`\\xi_1, \\xi_2, \\dotsc, \\xi_n`}/>.
        Каждая случайная величина <Math m={`\\xi_i \\in [0, 1]`}/> и <Math m={`\\expect \\xi_i = p_i`}/>.
    </P>
    <P>
        Пусть <Math m={`S = \\xi_1 + \\xi_2 + \\dotsc + \\xi_n`}/>
        и <Math m={`\\mu = \\expect S = p_1 + p_2 + \\dotsc p_n`}/>.
        Тогда для любого <Math m={`\\delta > 0`}/>
    </P>
    <Math display m={`
    \\prob \\big( S \\ge (1 + \\delta) \\cdot \\mu \\big) \\le \\left( \\frac{e^\\delta}{(1+\\delta)^{1+\\delta}} \\right)^\\mu
    \\quad\\text{и}\\quad
    \\prob \\big( S \\le (1 - \\delta) \\cdot \\mu \\big) \\le \\left( \\frac{e^{-\\delta}}{(1-\\delta)^{1-\\delta}} \\right)^\\mu
    `}/>
</Theorem>