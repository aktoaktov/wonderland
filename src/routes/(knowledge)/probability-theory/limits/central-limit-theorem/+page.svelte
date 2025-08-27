<script>
    import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
</script>

<Theorem title="Центральная предельная теорема">
    <P>
        Пусть <Math m={`\\xi_1, \\xi_2, \\dotsb, \\xi_n`}/> &mdash;
        набор независимых, одинаково распределенных случайных величин.
    </P>
    <P>
        Пусть <Math m={`\\mu = \\expect \\xi_i`}/> и <Math m={`\\sigma^2 = \\var \\xi_i`}/>.
    </P>

    <Math display
          m={`\\frac{\\xi_1 + \\xi_2 + \\dotsb + \\xi_n - n \\cdot \\mu}{\\sqrt{n} \\cdot \\sigma} \\dtoo \\Norm(0, 1)`}/>
</Theorem>