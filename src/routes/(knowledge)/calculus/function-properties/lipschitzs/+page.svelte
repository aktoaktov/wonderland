<script>
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
    import Proof from "$lib/Stencils/Blocks/Proof.svelte"
    import Title from "$lib/Elements/Title.svelte"
</script>

<Title title="Липшицевость"
/>

<Definition title="Липшицевая функция">
    <P>
        Пусть есть два метрических пространства
        <Math m={`A`}/> с метрикой <Math m={`d_A`}/> и <Math m={`B`}/> с метрикой <Math m={`d_B`}/>.
    </P>
    <P>
        Функция <Math m={`f \\colon A \\to B`}/> называется <b><Math m={`L`}/>-липшицевой</b>,
        если для любых <Math m={`x, y \\in A`}/>
    </P>
    <Math display m={`d_B(f(x), f(y)) \\le L \\cdot d_A(x, y)`}/>

    <P>
        Более естественное определение для отображения <Math m={`f \\colon A \\to B`}/>
        для нормированных векторных пространств <Math m={`A`}/> и <Math m={`B`}/>
    </P>
    <Math display m={`\\|f(x) - f(y)\\| \\le L \\cdot \\|x - y\\|`}/>
</Definition>

<Theorem title="Квадратичное ограничение сверху для липшицевой гладкости">
    <P>
        Пусть у функции <Math m={`f \\colon \\RR^n \\to \\RR`}/> градиент <Math m={`\\nabla f`}/> является <Math
            m={`L`}/>-липшицевым:
    </P>
    <Math display
          m={`\\|\\nabla f (y) - \\nabla f (x) \\| \\le L \\cdot \\|y-x\\| \\quad \\text{для всех}~ x,y \\in \\RR^n`}/>

    <P>
        Тогда для всех <Math m={`x, y \\in \\RR^n`}/> верно неравенство
    </P>
    <Math display m={`f(y) \\le f(x) + \\nabla f (x) ^\\T \\cdot (y-x) + \\frac{L}{2} \\cdot \\|y-x\\|^2`}/>
</Theorem>

<Proof>
    <P>
        Выберем <Math m={`x, y \\in \\RR^n`}/> &mdash; две произвольные точки.
    </P>
    <P>
        Посмотри на функцию <Math m={`\\phi(t) = f \\big( x + t \\cdot (y-x) \\big)`}/> при <Math m={`0 \\le t \\le 1`}/>.
        Можем записать <Math m={`f(y) - f(x)`}/> через эту функцию
    </P>
    <Math display
          m={`f(y) - f(x) = \\int_0^1 \\phi'(t) dt = \\int_0^1 \\nabla f \\big( x - t \\cdot (y-x) \\big) ^\\T \\cdot (y-x) dt`}/>

    <P>
        Добавляя и вычитая <Math m={`\\nabla f (x) ^\\T \\cdot (y-x)`}/>, получаем формулу
    </P>
    <Math display
          m={`f(y) - f(x) = \\nabla f (x) ^\\T \\cdot (y-x) + \\int_0^1 \\Big( \\nabla f \\big( x - t \\cdot (y-x) \\big) - \\nabla f (x) \\Big) ^\\T \\cdot (y-x) dt`}/>

    <P>
        Применяя неравенство Коши-Шварца и липшицевость градиента, получаем
    </P>
    <Math display m={`\\begin{align*}
    \\Big(\\nabla f \\big( x - t \\cdot (y-x) \\big) - \\nabla f (x) \\Big) ^\\T \\cdot (y-x) &\\le
    \\Big\\| \\nabla f \\big( x - t \\cdot (y-x) \\big) - \\nabla f (x) \\Big\\| \\cdot \\|y-x\\| \\le \\\\ &\\le
    L \\cdot \\| x - t \\cdot (y-x) - x \\| \\cdot \\|y-x\\| = \\\\ &=
    L \\cdot t \\cdot \\|y-x\\|^2
    \\end{align*}`}/>

    <P>
        Применяем полученное неравенство для оценки интеграла
    </P>
    <Math display m={`f(y) - f(x) \\le \\nabla f (x) ^\\T \\cdot (y-x) + \\int_0^1 L \\cdot t \\cdot \\|y-x\\|^2 dt =
    \\nabla f (x) ^\\T \\cdot (y-x) + \\frac{L}{2} \\cdot \\|y-x\\|^2`}/>

    <P>
        Получили требуемый результат
    </P>

    <Math display m={`f(y) \\le f(x) + \\nabla f (x) ^\\T \\cdot (y-x) + \\frac{L}{2} \\cdot \\|y-x\\|^2`}/>
</Proof>