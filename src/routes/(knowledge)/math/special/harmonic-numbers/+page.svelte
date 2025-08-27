<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Statement from "$lib/Stencils/Blocks/Statement.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
    import Code from "$lib/Code/Code.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Math from "$lib/Math/Math.svelte"
    import BulletList from "$lib/List/BulletList.svelte"
    import ListItem from "$lib/List/ListItem.svelte"
</script>

<Title title="Гармонические числа"
/>

<Par>
<P>
    <b>Гармонические числа</b> (harmonic numbers) &mdash; числа
</P>
<Math display
      m={`H_n \\defeq 1 + \\frac{1}{2} + \\frac{1}{3} + \\frac{1}{4} + \\dotsb + \\frac{1}{n-1} + \\frac{1}{n}
          = \\sum_{k=1}^n \\frac{1}{k}`}/>
<P>
    Эти числа повсеместно встречаются в анализе алгоритмов.
</P>
</Par>

<Subheading>Асимптотические формулы</Subheading>

<Par>
<P>
    Важное свойство гармонических чисел, основа их асимптотического анализа &mdash; <Math m={`H_n \\sim \\ln n`}/>.
    Доказать это можно, рассмотреть если ограничить <Math m={`H_n`}/> с двух сторон интегралами
</P>
<Math display
      m={`\\int_{1}^{n} \\frac{dx}{x} \\le H_n \\le 1 + \\int_{1}^n \\frac{dx}{x}
          \\iff \\ln n \\le H_n \\le 1 + \\ln n`}/>
<P>
    Делим все части неравенства на <Math m={`\\ln n`}/> и переходим к пределу.
</P>
<Math display m={`H_n \\sim \\ln n \\quad\\text{при}~ n \\to \\oo`}/>
<P>
    Есть более общая формула, использующая константу Эйлера-Маскерони
    <Math m={`\\gamma \\defeq \\lim_{n \\to \\oo} \\big( H_n - \\ln n \\big)`}/>
</P>
<Math display m={`H_n = \\gamma + \\ln n + \\frac{1}{2n} - \\sum_{k=1}^\\oo \\frac{B_{2k}}{2k \\cdot n^{2k}}`}/>
</Par>

<Par>
<P>
    Асимптотическую формулу можно применять для нахождение времени работы алгоритмов.
    Например, следующая конструкция достаточно часто встречается
</P>
</Par>

<Codeblock code={
`for int j = 1; i <= n; i++:
    for int j = i; j <= n; j += i:
        do something`
}/>

<Par>
<P>
    Количество итераций вложенного цикла, которое совпадает с количеством выполнения куска кода <Code c="do something"/>,
    равно
</P>
<Math display
      m={`\\sum_{j=1}^n \\left\\lfloor \\frac{n}{j} \\right\\rfloor \\le \\sum_{j=1}^n \\frac{n}{j} = n \\cdot H_n \\sim n \\ln n`}/>
</Par>


<Heading>Обобщённые гармоноческие числа</Heading>

<Par>
<P>
    Можно рассматривать суммы обратных <Math m={`s`}/>-х степеней натуральных чисел.
    Тогда мы получим обобщённые гармонические числа, которые тоже иногда встречаются при анализе алгоримтов
</P>
<Math display
      m={`H^{(s)}_n \\defeq 1 + \\frac{1}{2^s} + \\frac{1}{3^s} + \\frac{1}{4^s} + \\dotsb + \\frac{1}{(n-1)^s} + \\frac{1}{n^s}
           = \\sum_{k=1}^n \\frac{1}{k^s}`}/>
</Par>

<Par>
<P>
    Обобщённые гармонические числа можно использовать, например, для приближения обычных гармонических чисел.
    Посмотрим на ряд
</P>
<Math display
      m={`\\ln \\left( \\frac{k}{k-1} \\right) = \\frac{1}{k} + \\frac{1}{2k^2} + \\frac{1}{3k^3} + \\frac{1}{4k^4} + \\dotsb = \\sum_{j=1}^\\oo \\frac{1}{j \\cdot k^j}`}/>
<P>
    Справа написано <Math m={`\\ln k - \\ln (k-1)`}/>, а значит можно выразить <Math m={`\\ln n - \\ln 1`}/> как
    сумму
</P>
<Math display
      m={`\\ln n - \\ln 1 = \\sum_{k=2}^n \\ln \\left( \\frac{k}{k-1} \\right) = \\sum_{k=2}^n \\sum_{j=1}^\\oo \\frac{1}{j \\cdot k^j} = \\sum_{j=1}^\\oo \\frac{H^{(j)}_n - 1}{j}`}/>
<P>
    Отсюда можно, например, получить значение <Math m={`\\gamma`}/> с большой сходимостью,
    порядка <Math m={`1/2^s`}/>
</P>
<Math display
      m={`H_n - \\ln n = 1 - \\frac{1}{2} \\big( H^{(2)}_n - 1 \\big) - \\frac{1}{3} \\big( H^{(3)}_n - 1 \\big) - \\frac{1}{4} \\big( H^{(4)}_n - 1 \\big) - \\dotsb = 1 - \\sum_{s=2}^\\oo \\frac{H^{(j)}_n - 1}{j}`}/>
<P>
    Переходя к пределу <Math m={`n \\to \\oo`}/> получаем
</P>
<Math display m={`\\gamma = 1 - \\sum_{s=2}^\\oo \\frac{\\zeta(j) - 1}{j}`}/>
<P>
    где <Math m={`\\zeta(j)`}/> &mdash; дзета-функция Римана, <Math m={`\\zeta(s) = \\sum_{k=1}^\\oo 1/k^s`}/>
</P>
</Par>


<Heading>Значения <Math m={`\\lfloor n/j \\rfloor`}/></Heading>