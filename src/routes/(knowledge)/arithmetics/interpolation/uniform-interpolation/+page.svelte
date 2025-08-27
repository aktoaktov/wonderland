<script>
    import Title from "$lib/Elements/Title.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
    import Proof from "$lib/Stencils/Blocks/Proof.svelte"
</script>

<Title title="Равномерная интерполяция"
/>

<Definition title="Равномерная норма">
    <P>
        Пусть <Math m={`f \\colon \\RR \\to \\RR`}/> &mdash; непрерывная на отрезке <Math m={`[a, b]`}/> функциия.
    </P>
    <P>
        <b>Равномерная норма</b> &mdash; норма
    </P>
    <Math display m={`\\|f\\|_\\oo = \\max_{[a, b]} f`}/>
</Definition>

<Heading>Многочлены Чебышёва</Heading>


<Heading>Равномерная интерполяция</Heading>

<Par>
    <P>
        Многочлены Чебышёва <Math m={`T_n (x)`}/> образуют базис в пространстве непрерывных функций с ограниченной вариацией,
        заданных на отрезке <Math m={`[-1, 1]`}/>.
    </P>
</Par>

<Theorem title="Ряд Чебышёва">
    <P>
        Пусть <Math m={`f \\colon [-1, 1] \\to \\RR`}/> &mdash; непрерывная функция с ограниченной вариацией.
        Тогда эта функция раскладывается в ряд
    </P>
    <Math display m={`f(x) = \\sum_{n=0}^\\oo c_n \\cdot T_n (x)`}/>
    <P>
        где <Math m={`T_n (x)`}/> &mdash; многочлены Чебышёва, а коэффициенты <Math m={`c_n`}/> определяются формулами
    </P>
    <Math display
          m={`c_n = \\frac{2 - [n = 0]}{\\pi} \\int_{-1}^{1} \\frac{f(x) \\cdot T_n(x)}{\\sqrt{1-x^2}} \\cdot dx`}/>
</Theorem>

<Proof>
    <Par>
        <P>
            Доказательство будет читерным. Найдем коэффициенты ряда и докажем равномерную сходимость
        </P>
        <P>
            Сделаем замену переменной <Math m={`x = \\cos \\theta`}/>.
            Тогда, учитывая что <Math m={`T_n(\\cos \\theta) = \\cos(n \\theta)`}/>, получаем
        </P>
        <Math display m={`f(\\cos \\theta) = \\sum_{n=0}^\\oo c_n \\cdot \\cos(n \\theta)`}/>
        <P>
            Сама функция <Math m={`f(\\cos \\theta)`}/> определена на <Math m={`[0, \\pi]`}/>.
            Но это же разложение в ряд Фурье по косинусам! Тогда получаем, что
        </P>
        <Math display m={`c_n = \\frac{2}{\\pi} \\int_0^\\pi f(\\cos \\theta) \\cos (n \\theta) d \\theta`}/>
        <P>
            Делаем обратную замену и получаем формулу для коэфициентов
        </P>
        <Math display
              m={`c_n = \\frac{2 - [n = 0]}{\\pi} \\int_{-1}^{1} \\frac{f(x) \\cdot T_n(x)}{\\sqrt{1-x^2}} \\cdot dx`}/>
    </Par>
</Proof>