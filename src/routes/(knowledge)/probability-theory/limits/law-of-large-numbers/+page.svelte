<script>
    import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
    import Title from "$lib/Elements/Title.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
</script>

<Title title="Законы больших чисел"
/>

<Theorem title="Закон больших чисел">
    <P>
        Пусть <Math m={`\\xi_1, \\xi_2, \\dotsc, \\xi_n`}/> &mdash; независимые, одинаково распределенные случайные
        величины, и <Math m={`\\expect \\xi_i = \\mu`}/>. Тогда
    </P>
    <Math display m={`\\frac{\\xi_1 + \\xi_2 + \\dotsb + \\xi_n}{n} \\ptoo \\mu \\quad\\text{при}~ n \\to \\oo`}/>
</Theorem>