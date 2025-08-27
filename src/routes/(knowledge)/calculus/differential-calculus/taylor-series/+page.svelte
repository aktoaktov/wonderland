<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
</script>

<Title title="Ряды Тейлора"
/>


<Heading>Функции одной переменной</Heading>

<Par>
<P>
    Возьмём какую-то гладкую функцию <Math m={`f \\colon \\RR \\to \\RR`}/>
    и попробуем аппроксимировать её каким-то многочленом.
</P>
<Math display m={`f(x) \\approx \\sum_{k=0}^n a_n \\cdot x^k`}/>
</Par>

<Theorem title="Аппроксимация функции многочленом Тейлора">
<P>
    Пусть функция <Math m={`f \\colon \\R \\to \\RR`}/> является <Math m={`n`}/> раз дифференцируемой
    в точке <Math m={`x_0`}/>. Тогда
</P>
<Math display m={`f(x) = \\sum_{k=0}^n \\frac{f^{(k)}(x_0)}{k!} \\cdot (x-x_0)^k + r_n(x)`}/>
<P>
    где <Math m={`r_n(x) = \\mathop{o} \\bigl( (x-x_0)^n \\bigr)`}/> &mdash; остаточный член,
    а аппроксимация запущена из точки <Math m={`x_0`}/>.
</P>
</Theorem>

<Par>
<P>
    В формуле присутствует множитель <Math m={`(x-x_0)^k`}/> для всех степеней <Math m={`k`}/>
    от <Math m={`0`}/> до <Math m={`n`}/>. Значит,
</P>
<Math display m={`T_n^{(k)}(x_0) = f^{(k)}(x_0) \\quad\\text{для всех}~ 0 \\le k \\le n`}/>
</Par>

<Par>
<P>
    Многочлен Тейлора <Math m={`T_n(x)`}/> хорошо аппроксимирует функцию <Math m={`f`}/>
    в окрестности точки <Math m={`x_0`}/>.
    Для доказательства запишем функцию <Math m={`f(x)`}/> в виде
</P>
<Math display m={`f(x) = T_n(x) + r_n(x)`}/>
<P>
    Здесь <Math m={`r_n(x)`}/> &mdash; остаточный член.
</P>
</Par>