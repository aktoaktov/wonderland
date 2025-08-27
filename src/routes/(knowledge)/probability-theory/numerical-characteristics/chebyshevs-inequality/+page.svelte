<script>
    import Title from "$lib/Elements/Title.svelte"
    import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
    import Math from "$lib/Math/Math.svelte"
    import P from "$lib/Markup/P.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import Proof from "$lib/Stencils/Blocks/Proof.svelte"
</script>

<Title title="Неравенства Чебышёва"
/>


<Theorem title="Неравенство Маркова">
    <P>
        Пусть <Math m={`\\xi`}/>&nbsp;&mdash; неотрицательная случайная величина. Тогда для любого <Math m={`a > 0`}/>
    </P>
    <Math display m={`\\prob \\big( \\xi \\ge a \\big) \\,\\le\\, \\frac{\\expect\\xi}{a}`}/>
</Theorem>

<Proof>
    <P>
        <b>Доказательство.</b>&ensp;
        Пусть <Math m={`A \\subset \\Omega`}/>&nbsp;&mdash; какое-то событие.
        Его индикатором называется случайная величина
    </P>
    <Math display m={`\\I(A) \\defeq [\\text{событие}~ A ~\\text{произошло}] =
                     \\begin{cases} 1 & \\text{событие}~ A ~\\text{произошло} \\\\
                                    0 & \\text{событие}~A ~\\text{не произошло} \\end{cases}`}/>

    <P>
        Учитывая то, что <Math m={`\\I(A) + \\I(\\Omega \\without A) = 1`}/>,
        мы можем оценить снизу случайную величину <Math m={`\\xi`}/>
    </P>
    <Math display m={`\\xi \\,=\\,
                      \\xi \\cdot \\I\\big(\\xi \\lt a\\big) + \\xi \\cdot \\I\\big(\\xi \\ge a\\big) \\,\\ge\\,
                      \\xi \\cdot \\I\\big(\\xi \\ge a\\big) \\,\\ge\\,
                      a \\cdot \\I\\big(\\xi \\ge a\\big)`}/>

    <P>
        Используем свойство индикаторов <Math m={`\\E \\big( \\I(A) \\big) = \\P(A)`}/>. Посчитаем математическое
        ожидание
    </P>
    <Math display
          m={`\\expect\\xi \\,\\ge\\, a \\cdot \\E\\big(\\I (\\xi \\ge a)\\big) = a \\cdot \\prob\\big(x \\ge a\\big)`}/>
</Proof>


<Theorem title="Неравенство Чебышёва">
    <P>
        Пусть <Math m={`\\xi`}/>&nbsp;&mdash; неотрицательная случайная величина с дисперсией <Math m={`\\sigma^2`}/>.
        Тогда для любого <Math m={`a > 0`}/>
    </P>
    <Math display m={`\\prob \\big( |\\xi - \\expect\\xi| \\ge a \\big) \\,\\le\\, \\frac{\\sigma^2}{a^2}`}/>
</Theorem>

<Proof>
    <P>
        <b>Доказательство.</b>&ensp;
        При <Math m={`a > 0`}/> неравенство <Math m={`|\\xi - \\E\\,\\xi| > a`}/>
        равносильно неравенству <Math m={`(\\xi - \\E\\,\\xi)^2 > a^2`}/>.
    </P>
    <Math display
          m={`\\prob \\big( |\\xi - \\expect\\xi| \\ge a \\big) \\,=\\,
              \\prob \\big( (\\xi - \\expect\\xi)^2 \\ge a^2 \\big) \\,\\le\\,
              \\frac{\\expect \\big( (\\xi - \\expect\\xi)^2 \\big)}{a^2} \\,=\\,
              \\frac{\\sigma^2}{a^2}`}/>
</Proof>