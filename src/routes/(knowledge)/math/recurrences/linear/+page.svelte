<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Link from "$lib/Elements/Link.svelte"
    import Code from "$lib/Code/Code.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import Image from "$lib/Elements/Image.svelte"
    import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
    import Proof from "$lib/Stencils/Blocks/Proof.svelte"
</script>

<Title title="Линейные рекурренты"
/>

<Definition title="Линейная рекуррента">
    <P>
        <b>Линейная рекуррентная последовательность</b> степени <Math m={`k`}/> &mdash;
        последовательность <Math m={`x_n`}/>, для которой
    </P>
    <Math display
          m={`x_n = c_1 \\cdot x_{n-1} + c_2 \\cdot x_{n-2} + \\dotsb + c_{k-1} \\cdot x_{n-k+1} + c_k \\cdot x_{n-k}`}/>
    <P>
        Также заданы <Math m={`k`}/> первых члены последовательности <Math m={`x_1, x_2, \\dotsc, x_k`}/>.
    </P>
</Definition>


<Heading>Быстрое вычисление и матричная форма</Heading>

<Par>
<P>
    В лоб считать члены последовательностей долго.
    Вычисление <Math m={`n`}/> членов имеет временную сложность <Math m={`\\Theta(nk)`}/>.
</P>
</Par>

<Par>
<P>
    Линейная рекуррентная последовательность хорошо выражается через матрицы.
    А именно, мы можем записать переход от вектора <Math m={`(x_{n-1}, x_{n-2}, \\dotsc, x_{n-k+1}, x_{n-k})^\\T`}/>
    к &laquo;смещенному&raquo; вектору <Math m={`(x_{n}, x_{n-1}, \\dotsc, x_{n-k+2}, x_{n-k+1})^\\T`}/>
</P>
<Math big display
      m={`\\pmatrix{
          c_1 & c_2 & c_3 & \\cdots & c_{k-1} & c_k \\\\
          1 & 0 & 0 & \\cdots & 0 & 0 \\\\
          0 & 1 & 0 & \\cdots & 0 & 0 \\\\
          \\vdots & \\vdots & \\vdots & \\ddots & \\vdots & \\vdots \\\\
          0 & 0 & 0 & \\cdots & 0 & 0 \\\\
          0 & 0 & 0 & \\cdots & 1 & 0
          }
          \\cdot
          \\pmatrix{x_{n-1} \\\\ x_{n-2} \\\\ x_{n-3} \\\\ \\vdots \\\\ x_{n-k+1} \\\\ x_{n-k}}
          =
          \\pmatrix{x_{n} \\\\ x_{n-1} \\\\ x_{n-2} \\\\ \\vdots \\\\ x_{n-k+2} \\\\ x_{n-k+1}}`}/>

<P>
    Получается, если обозначить матрицу перехода за <Math m={`M`}/>, то
    можно получить формулу <Math m={`n`}/>-го члена через первые <Math m={`k`}/> заданных
</P>
<Math display m={`M^{n-k} \\cdot (x_k, x_{k-1}, \\dotsc, x_1) ^\\T = (x_n, x_{n-1}, \\dotsc, x_{n-k+1}) ^\\T`}/>

<P>
    Используя алгоритм быстрого возведения в степень, можно находить значение <Math m={`n`}/>-го члена
    за время <Math m={`O \\big( k^3 \\cdot \\log(n-k) \\big)`}/>.
</P>
<P>
    Но на самом деле, амортизированная сложность <Math m={`O \\big( k^2 \\cdot \\log(n-k) \\big)`}/>,
    потому что мы за раз находим значения сразу <Math m={`k`}/> членов.
    К сожалению, такая &laquo;оптимизация&raquo; времени мало когда применима.
</P>
</Par>


<Heading>Характеристические многочлены</Heading>

<Par>
<P>
    Используя теорему Кэли-Гамильтона можно добиться значительного ускорения реального времени вычисления рекуррентных
    последовательностей.
</P>
</Par>

<Theorem title="Характеристический многочлен матрицы рекуррентного соотношения">
<P>
    Характеристический многочлен матрицы линейного рекуррентного соотношения
    совпадает с этим линейным рекуррентным соотношением.
</P>
</Theorem>

<Proof>
<Par>
<P>
    Пусть <Math m={`M`}/> &mdash; матрица линейного рекуррентного соотношения
    с коэффициентами <Math m={`c_1, c_2, \\dotsb, c_k`}/>:
</P>
<Math big display
      m={`M = \\pmatrix{
          c_1 & c_2 & c_3 & \\cdots & c_{k-1} & c_k \\\\
          1 & 0 & 0 & \\cdots & 0 & 0 \\\\
          0 & 1 & 0 & \\cdots & 0 & 0 \\\\
          \\vdots & \\vdots & \\vdots & \\ddots & \\vdots & \\vdots \\\\
          0 & 0 & 0 & \\cdots & 0 & 0 \\\\
          0 & 0 & 0 & \\cdots & 1 & 0
          }`}/>
<P>
    Характеристический многочлен этой матрицы
</P>
<Math big display
      m={`P(\\lambda) = M - \\lambda \\cdot \\1 = \\vmatrix{
          c_1 - \\lambda & c_2 & c_3 & \\cdots & c_{k-1} & c_k \\\\
          1 & - \\lambda & 0 & \\cdots & 0 & 0 \\\\
          0 & 1 &  - \\lambda & \\cdots & 0 & 0 \\\\
          \\vdots & \\vdots & \\vdots & \\ddots & \\vdots & \\vdots \\\\
          0 & 0 & 0 & \\cdots &  - \\lambda & 0 \\\\
          0 & 0 & 0 & \\cdots & 1 &  - \\lambda
          }
          = \\lambda^k - c_1 \\cdot \\lambda^{k-1} - c_2 \\cdot \\lambda^{k-2} - \\dotsb - c_{k-1} \\cdot \\lambda - c_k`}/>
</Par>
<Par>
<P>
    По теореме Кэли-Гамильтона матрица <Math m={`M`}/> удовлетворяет своему характеристическому многочлену, значит
</P>
<Math display
      m={`M^k = c_1 \\cdot M^{k-1} + c_2 \\cdot M^{k-2} + c_3 \\cdot M^{k-3} + \\dotsb + c_{k-1} \\cdot M + c_k \\cdot \\1`}/>
</Par>
</Proof>

<Par>
<P>
    Из этой теоремы сразу вытекает способ ускорения вычислений степени матрицы <Math m={`M`}/>.
</P>
<P>
    Любую степень <Math m={`M^n`}/> можно представить в виде взвешенной суммы базовых степеней
</P>
<Math display
      m={`M^n = a_{k-1} \\cdot M^{k-1} + a_{k-2} \\cdot M^{k-2} + a_{k-3} \\cdot M^{k-3} + \\dotsb + a_1 \\cdot M^1 + a_0 \\cdot \\1`}/>
<P>
    где <Math m={`a_i`}/> &mdash; коэффициенты, зависящие от <Math m={`n`}/>.
</P>
<P>
    Тогда, если мы знаем <Math m={`M^n`}/>, можно вычислить <Math m={`M^{n+1}`}/>
</P>
<Math big display
      m={`\\align{
          M^{n+1} &= a_{k-1} \\cdot M^{k} + a_{k-2} \\cdot M^{k-1} + a_{k-3} \\cdot M^{k-2} + \\dotsb + a_1 \\cdot M^2 + a_0 \\cdot M
          =\\\\ &= (a_{k-1} c_1 + a_{k-2}) \\cdot M^{k-1} + (a_{k-1} c_2 + a_{k-3}) \\cdot M^{k-1} + \\dotsb + (a_{k-1} c_{k-1} + a_0) \\cdot M + c_k \\cdot \\1
          }`}/>
<P>
    Получается, что умножение матриц мы свели к умножению двух многочленов, у каждого по <Math m={`k`}/> коэффициентов.
    А это можно сделать за <Math m={`k^2`}/> умножений,
    или за <Math m={`O(k \\log k)`}/> с использованием дискретного преобразования Фурье.
</P>
</Par>

<Par>
<P>
    Этот алгоритм позволяет найти <Math m={`n`}/>-й член последовательности за <Math m={`O \\big( k^2 \\log(n-k) \\big)`}/> или за <Math m={`O(k \\log n)`}/>.
</P>
</Par>