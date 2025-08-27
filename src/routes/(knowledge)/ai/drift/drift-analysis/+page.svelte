<script>
    import Title from "$lib/Elements/Title.svelte"
    import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
    import Math from "$lib/Math/Math.svelte"
    import P from "$lib/Markup/P.svelte"
</script>

<Title title="Дрифт"
/>

<Theorem title="Аддитивная теорема о дрифте">
    <P>
        Пусть <Math m="x_t"/> &mdash; последовательность неотрицательных случайных величин
        с конечной областью значений <Math m="S \subset \RR"/>.
        Пусть <Math m={`T \\defeq \\min \\{ t \\colon x_t = 0 \\}`}/> &mdash; время затухания последовательности.
    </P>

    <P>Если существует такое число <Math m="\delta > 0"/>, что для всех <Math m={`s \\in S \\without \\{0\\}`}/> и для всех <Math m="t \ge 0"/></P>

    <Math display m={`\\Delta_t(s) \\defeq \\E(x_t - x_{t+1} \\mid x_t = s) \\ge \\delta`}/>

    <P>то</P>

    <Math display m={`\\E(T) \\le \\frac{\\E(x_0)}{\\delta}`}/>
</Theorem>

