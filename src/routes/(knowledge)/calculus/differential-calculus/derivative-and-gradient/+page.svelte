<script>
    import Title from "$lib/Elements/Title.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import Math from "$lib/Math/Math.svelte"
    import P from "$lib/Markup/P.svelte"
    import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
</script>

<Title title="Производная и градиент"
/>

<Definition title="Производная">
    <P>
        Пусть <Math m={`f \\colon \\RR \\to \\RR`}/> &mdash; функция одной переменной
    </P>
    <P>
        <b>Производной</b> функции <Math m={`f`}/> называется функция <Math m={`f'`}/>
    </P>
    <Math display m={`f'(x) = \\lim_{\\Delta x \\to 0} \\frac{f(x + \\Delta x) - f(x)}{\\Delta x}`}/>
</Definition>

<Theorem title="Теорема Ферма">
    <P>
        У функции <Math m={`f \\colon \\RR \\to \\RR`}/> точка <Math m={`x`}/> является точкой локального минимума.
        Тогда <Math m={`f(x) = 0`}/>.
    </P>
</Theorem>