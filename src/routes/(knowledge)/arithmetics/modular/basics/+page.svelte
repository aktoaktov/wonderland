<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
</script>

<Title title="Основы модулярной арифметики"
/>

<Par>
<P>
    Модулярная арифметика оперирует остатками.
</P>
</Par>

<Par>
<P>
    Пусть <Math m={`a`}/> &mdash; какое-то целое число.
    Мы хотим разделить с остатком <Math m={`a`}/> на целое число <Math m={`m`}/>.
    Разделить с остатком <Math m={`a`}/> на <Math m={`m`}/> &mdash; значит найти два таких целых числа
    <Math m={`c`}/> и <Math m={`r`}/>, что
</P>
<Math display m={`a = c \\cdot m + r \\quad\\text{и при этом}~ 0 \\le r < m`}/>
<P>
    Число <Math m={`c`}/> называется <b>неполным частным</b>, а число <Math m={`r`}/> называется <b>остатком</b>
    при делении <Math m={`a`}/> на <Math m={`m`}/>.
</P>
<Math display
      m={`c = \\left\\lfloor \\frac{a}{m} \\right\\rfloor \\quad\\text{и}\\quad
          r = a - \\left\\lfloor \\frac{a}{m} \\right\\rfloor`}/>
<P>
    Для остатка <Math m={`r`}/> такую громоздкую запись <Math m={`r = a - \\lfloor a/m \\rfloor`}/> заменяют
    обозначением <Math m={`r \\defeq a \\bmod m`}/>.
</P>
</Par>

<Heading>Сравнение по модулю</Heading>

<Par>
<P>
    Возьмем множество целых чисел <Math m={`\\ZZ`}/>.
    Зафиксируем какой-то модуль <Math m={`m`}/>.
</P>
<P>
    Отношение &laquo;иметь один остаток при делении на <Math m={`m`}/>&raquo; является отношением эквивалентности.
    Действительно, это отношение рефлексивно, симметрично и транзитивно.
    Это отношение обозначается <Math m={`\\eqmod{m}`}/>.
    То есть, если <Math m={`a`}/> и <Math m={`b`}/> имеют один и тот же остаток при делении на <Math m={`m`}/>,
    пишут <Math m={`a \\eqmod{m} b`}/> или <Math m={`a \\equiv b \\pmod m`}/>.
</P>
<P>
    Поскольку <Math m={`\\eqmod{m}`}/> &mdash; отношение эквивалентности на <Math m={`\\ZZ`}/>,
    то оно делит множество <Math m={`\\ZZ`}/> на классы эквивалентности <Math m={`[r]`}/>.
</P>
<Math display m={`[r] \\defeq \\{ x \\cdot m + r \\mid \\forall x \\in \\ZZ \\}`}/>
<P>
    Класс эквивалентности <Math m={`[r]`}/> содержит все числа,
    имеющие остаток <Math m={`r`}/> при делении на <Math m={`m`}/>.
    Эти классы эквивалентности ещё называют вычетами по модулю <Math m={`m`}/>.
</P>
<P>
    Всего таких классов <Math m={`m`}/>: от <Math m={`0`}/> до <Math m={`m-1`}/>.
    Значит, фактормножество
</P>
<Math display m={`\\ZZ \\big/ {\\eqmod{m}} = \\bigl\\{ [0], [1], [2], \\dotsc, [m-2], [m-1] \\bigr\\}`}/>
</Par>

<Par>
<P>
    Сравнимость по модулю и делимость тесно связаны
</P>
<Math display m={`a \\equiv b \\pmod m \\iff m \\divides (a - b)`}/>
<P>
    Отсюда выводятся очень важные свойства.
    Пусть <Math m={`a \\equiv a' ~\\text{и}~ b \\equiv b' \\pmod m`}/>.
    Тогда
</P>
<Math display m={`a + b \\equiv a' + b' \\pmod m \\quad\\text{и}\\quad a \\cdot b \\equiv a' \\cdot b' \\pmod m`}/>
<P>
    Более того, для любого многочлена <Math m={`P(x, y)`}/>
</P>
<Math display m={`P(a, b) \\equiv P(a' b') \\pmod m`}/>
</Par>