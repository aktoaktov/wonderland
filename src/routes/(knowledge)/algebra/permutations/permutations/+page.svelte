<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Code from "$lib/Code/Code.svelte"
    import Link from "$lib/Elements/Link.svelte"
    import EnumList from "$lib/List/EnumList.svelte"
    import ListItem from "$lib/List/ListItem.svelte"
    import Image from "$lib/Elements/Image.svelte"
    import Proof from "$lib/Stencils/Blocks/Proof.svelte"
</script>

<Title title="Перестановки"
/>

<Par>
<P>
    <b>Перестановка</b> <Math m={`n`}/> объектов &mdash; способ последовательного расположения
    этих объектов с учётом их порядка.
</P>
<P>
    Например, все возможные перестановки <Math m={`3`}/> объектов <Math m={`a, b, c`}/>:
</P>
<Math display m={`abc, \\quad acb, \\quad bac, \\quad bca, \\quad cab, \\quad cba`}/>
</Par>

<Par>
<P>
    Количество всевозможных перестановок <Math m={`n`}/> объектов &mdash; факториал числа <Math m={`n`}/>
</P>
<Math display m={`n! \\defeq n \\cdot (n-1) \\cdot (n-2) \\cdot (n-3) \\dotsb 3 \\cdot 2 \\cdot 1 = \\prod_{k=1}^n k`}/>
<P>
    При этом <Math m={`0! = 1`}/>, ведь есть только один способ расположить <Math m={`0`}/> объектов &mdash; никак.
</P>
<P>
    Получаем рекуррентное тождество, справедливое для всех целых <Math m={`n \\ge 1`}/>
</P>
<Math display m={`n! = n \\cdot (n-1)!`}/>
</Par>


<Heading>Автоморфизмы множеств</Heading>

<Par>
<P>
    Возьмём какое-то множество <Math m={`S`}/>.
    <b>Эндоморфизм</b> множества <Math m={`S`}/> &mdash;
    отображение <Math m={`f \\colon S \\to S`}/> множества <Math m={`S`}/> на себя.
</P>
<P>
    Эндоморфизмы можно итерировать.
    <b>Итерация</b> эндоморфизма <Math m={`f`}/> &mdash; композиционная степень <Math m={`f`}/>
</P>
<Math display m={`f^n = \\underbrace{f \\compose f \\compose f \\compose \\dotsb \\compose f}_{n ~\\text{раз}}`}/>
<P>
    Итерации одного множества коммутируют
</P>
<Math display m={`f^n \\compose f^m = f^m \\compose f^n = f^{n+m}`}/>
<P>
    Для любого эндоморфизма <Math m={`f \\colon S \\to S`}/> конечного множества <Math m={`S`}/>
    найдутся два неравных числа <Math m={`n`}/> и <Math m={`m`}/> таких, что
</P>
<Math display m={`\\forall x \\in S \\? f^n(x) = f^m(x)`}/>
</Par>

<Par>
<P>
    <b>Автоморфизм</b> множества <Math m={`S`}/> &mdash; обратимый эндоморфизм множества <Math m={`S`}/>,
    или, другими словами, биекция <Math m={`S \\bijto S`}/> множества <Math m={`S`}/> на себя.
</P>
<P>
    Автоморфизмы тоже можно итерировать, потому что это эндоморфизмы.
    Но итерации автоморфизмов не могут &laquo;сжать&raquo; множество <Math m={`S`}/>,
    то есть если <Math m={`f`}/> &mdash; автоморфизм <Math m={`S`}/>, то <Math m={`f[S] = S`}/>.
</P>
</Par>

<Heading>Перестановки</Heading>

<Par>
<P>
    <b>Перестановка</b> множества <Math m={`S`}/> &mdash; автоморфизм <Math m={`S`}/>.
    В переводе с пришельского на русский, перестановка &mdash;
    это переупорядочивание элементов множества <Math m={`S`}/>.
    Это переупорядочивание, а также сама перестановка, записываются как
</P>
<Math display
      m={`\\sigma = \\pmatrix{a_1 & a_2 & a_3 & \\cdots & a_{n-1} & a_n \\\\
          b_1 & b_2 & b_3 & \\cdots & b_{n-1} & b_n}`}/>
<P>
    Эта запись означает, что при автоморфизме <Math m={`\\sigma`}/>
</P>
<Math display
      m={`a_1 \\mapsto b_1 \\quad a_2 \\mapsto b_2 \\quad a_3 \\mapsto b_3 \\quad \\cdots \\quad a_{n-1} \\mapsto b_{n-1} \\quad a_n \\mapsto b_n`}/>
<P>
    Обычно элементы в записи перестановки превращают в цифры и сортируют первую строку. Получается вот так
</P>
<Math display
      m={`\\sigma = \\pmatrix{1 & 2 & 3 & \\cdots & n-1 & n \\\\ \\sigma(1) & \\sigma(2) & \\sigma(3) & \\cdots & \\sigma(n-1) & \\sigma(n)}`}/>
</Par>

<Par>
<P>
    Точно так же, как и для обычных отображений, для перестановок определяется операция композиции.
    Композиция двух перестановок <Math m={`\\sigma`}/> и <Math m={`\\tau`}/> &mdash; перестановка <Math
        m={`\\sigma \\compose \\tau`}/>.
</P>
<Math display
      m={`\\sigma \\compose \\tau
          = \\pmatrix{1 & 2 & \\cdots & n \\\\ \\sigma(1) & \\sigma(2) & \\cdots & \\sigma(n)}
          \\compose \\pmatrix{1 & 2 & \\cdots & n \\\\ \\tau(1) & \\tau(2) & \\cdots & \\tau(n)}
          = \\pmatrix{1 & 2 & \\cdots & n \\\\ \\sigma\\big(\\tau(1)\\big) & \\sigma\\big(\\tau(2)\\big) & \\cdots & \\sigma\\big(\\tau(n)\\big)}`}/>

<P>
    Композиция перестановок ассоциативна, но не коммутативна
</P>
<Math display
      m={`\\sigma \\compose (\\tau \\compose \\rho) = (\\sigma \\compose \\tau) \\compose \\rho
          \\qquad\\text{и}\\qquad
          \\sigma \\compose \\tau \\neq \\tau \\compose \\sigma`}/>
<P>
    По операции композиции есть единичный элемент <Math m={`\\1`}/>, называемый единичной перестановкой
</P>
<Math display m={`\\1 = \\pmatrix{1 & 2 & 3 & \\cdots & n-1 & n \\\\ 1 & 2 & 3 & \\cdots & n-1 & n}`}/>
<P>
    Эта единичная перестановка оставляет все элементы на своих местах. По этому
</P>
<Math display m={`\\sigma \\compose \\1 = \\1 \\compose \\sigma = \\sigma`}/>
</Par>