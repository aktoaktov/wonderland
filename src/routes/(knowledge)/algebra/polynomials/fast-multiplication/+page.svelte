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
    import Image from "$lib/Elements/Image.svelte"
</script>

<Title title="Быстрое умножение"
/>


<Par>
<P>
    Рассмотрим не только многочлены, но и функции.
</P>
</Par>

<Heading>Алгоритм Карацубы</Heading>

<Par>
<P>
    Пусть мы хотим посчитать произведение двух многочленов
    <Math m={`P(x) = \\sum_{k=0}^n p_k \\cdot x^k`}/> и <Math m={`Q(x) = \\sum_{k=0}^n q_k \\cdot x^k`}/>.
</P>
<P>
    Попробуем применить метод &laquo;разделяй и властвуй&raquo;, чтобы добиться временной сложности меньшей,
    чем <Math m={`O(n^2)`}/>. В лоб, к сожалению, не получится. Применим хитрость.
</P>
<P>
    Сгруппируем множители в многочленах <Math m={`P`}/> и <Math m={`Q`}/> степени <Math m={`n = 2k`}/>,
    превратив каждый многочлен в пару многочленов степени <Math m={`k`}/>.
</P>
<Math display m={`P(x) = a(x) + x^k \\cdot b(x)  \\quad\\text{и}\\quad  Q(x) = c(x) + x^k \\cdot d(x)`}/>
<P>
    Произведение <Math m={`P(x) \\cdot Q(x)`}/> можно произвести, используя только <Math m={`3`}/> умножения
    маленьких многочленов, вместо привычных <Math m={`4`}/>:
</P>
<Math display
      m={`P(x) \\cdot Q(x) = \\bigl( a + x^k \\cdot b \\bigr) \\cdot \\bigl( c + x^k \\cdot d \\bigr)
          = a c + x^k \\cdot \\bigl( (a + b) \\cdot (c + d) - a c - b d \\bigr) + x^{2 k} \\cdot b d`}/>
</Par>

<Codeblock code={
`function karatsuba(array[int] p, array[int] q): ...`
}/>


<Subheading>Анализ алгоритма</Subheading>

<Par>
<P>
    При таком алгоритме на итерацию требуется <Math m={`3`}/> умножения и <Math m={`6`}/> сложений.
    Пусть алгоритм, вычисляющий произведение двух многочленов степени <Math m={`n`}/>,
    требует <Math m={`M(n)`}/> умножений и <Math m={`A(n)`}/> сложений.
</P>
<P>
    Оценим количество умножений.
    Как мы уже говорили, можно дополнить многочлены нулями до длины <Math m={`2^{\\lfloor \\log_2 n \\rfloor + 1}`}/>.
    Тогда вычисления будут проще, но количество умножений возрастет.
</P>
<Math display
      m={`M(n) = \\cases{
          1 & \\if n = 0 \\\\
          2 \\cdot M ( \\lfloor n/2 \\rfloor ) + M ( \\lceil n/2 \\rceil - 1 ) & \\otherwise
          }
          \\quad\\text{или}\\quad
          M_{\\text{грубое}}(n) = 3^{\\lfloor \\log_2 n \\rfloor + 1}`}/>
</Par>

<Image src="">Дополнение нулями до <Math m={`2^{\\lfloor \\log_2 n \\rfloor + 1}`}/> достаточно неэффективное</Image>

<Par>
<P>
    Важное неравенство, позволяющее оценить количество требуемых умножений
</P>
<Math display m={`n^{\\log_2 3} \\le M(n) \\le 3 \\cdot n^{\\log_2 3}`}/>
<P>
    То есть, алгоритм Карацубы (в обоих вариантах, с дополнениями нулями и без)
    требует <Math m={`\\Theta \\bigl( n^{\\log_2 3} \\bigr)`}/> умножений.
</P>
</Par>


<Subheading>Оптимизации</Subheading>

<Par>
<P>
    Накладные расходы на рекурсию иногда становятся слишком большими.
    Можно выполнять алгоритм Карацубы только пока степени многочленов больше какого-то числа <Math m={`N_{\\max}`}/>.
    Для многочленов, чьи степени меньше <Math m={`N_{\\max}`}/>, выполняем обычное умножение.
</P>
<P>
    На практике <Math m={`N_{\\max}`}/> выбирают <Math m={`32`}/> или <Math m={`64`}/>.
</P>
</Par>


<Heading>Алгоритм Тоома-Кука</Heading>