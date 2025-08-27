<script>
    import Title from "$lib/Elements/Title.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
</script>

<Title title="Сочетания"
/>

<Definition title="Сочетания">
    <P>
        <b>Сочетания</b> из <Math m={`n`}/> объектов по <Math m={`k`}/> &mdash; все возможные варианты
        выбора <Math m={`k`}/> различных элементов из набора <Math m={`n`}/> объектов без учёта порядка.
    </P>
</Definition>

<Par>
    <P>
        Например, сочетания из <Math m={`5`}/> объектов <Math m={`\\{a, b, c, d, e\\}`}/> по <Math m={`3`}/> это
    </P>
    <Math display
          m={`abc,\\quad abd,\\quad abe,\\quad acd,\\quad ace,\\quad ade,\\quad bcd,\\quad bce,\\quad bde,\\quad cde`}/>
</Par>

<Par>
    <P>
        Количество сочетаний из <Math m={`n`}/> по <Math m={`k`}/> ещё называется
        <b>биномиальным коэффициентом</b> и обозначается
    </P>
    <Math display m={`\\binom{n}{k} \\defeq \\frac{n!}{(n-k)! \\cdot k!}`}/>
</Par>

<Par>
    <P>
        В нашем примере
    </P>
    <Math display
          m={`\\binom{5}{3} = \\frac{5!}{(5-3)! \\cdot 3!} = \\frac{5 \\cdot 4 \\cdot 3}{3 \\cdot 2 \\cdot 1} = 10`}/>
</Par>

<Subheading>Треугольник Паскаля</Subheading>


<Subheading>Вещественное обобщение</Subheading>

<Par>
    <P>
        Формулу из определения биномиальных коэффициентов можно обобщить и на случай нецелых <Math m={`n`}/>
    </P>
    <Math display m={`\\binom{r}{k} \\defeq \\cases{
    \\displaystyle \\frac{r^{\\underline{k}}}{k!} = \\prod_{i=1}^k \\frac{r+1-i}{i} & k \\ge 0 \\\\
    0 & k < 0
    }`}/>
    <P>
        При этом, для определенности, при <Math m={`k < 0`}/> полагают <Math m={`\\binom{r}{k} = 0`}/>.
    </P>
    <P>
        Различные свойства и формулы применимы при разных условиях на переменные.
        Далее я буду писать <Math m={`n`}/> и <Math m={`k`}/>, подразумевая, что они целые, а <Math m={`r`}/> у меня будет действительной.
    </P>
</Par>


<Heading>Свойства биномиальных коэффициентов</Heading>

<Par>
    <P>
        <b>Симметрия.</b> Из определения получаем, что биномиальные коэффициенты симметричны в том смысле, что
    </P>
    <Math display m={`\\binom{n}{k} = \\binom{n}{n-k}`}/>
</Par>

<Par>
    <P>
        <b>Вынесение и внесение.</b> Опять же, из определения можно вынести по одному члену и получить формулу
    </P>
    <Math display m={`\\binom{r}{k} = \\frac{r}{k} \\cdot \\binom{r-1}{k-1}`}/>

    <P>
        Используя это свойство, можно получить два очень полезных факта, которые используются повсеместно
    </P>
    <Math display m={`k \\cdot \\binom{r}{k} = r \\cdot \\binom{r-1}{k-1} \\quad\\text{и}\\quad \\frac{1}{r} \\cdot \\binom{r}{k} = \\frac{1}{k} \\cdot \\binom{r-1}{k-1}`}/>

    <P>
        Применяя поочередно свойства внесения-вынесения и симметрии, можно получить еще одну формулу
    </P>
    <Math display m={`r \\cdot \\binom{r-1}{k} = (r-k) \\cdot \\binom{r}{k}`}/>
</Par>