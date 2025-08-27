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
    import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
</script>

<Title title="Дискретное преобразование Фурье"
/>

<Par>
<P>
    Давайте научимся быстро умножать многочлены.
</P>
<P>
    Пусть у нас есть два многочлена <Math m={`A(x)`}/> и <Math m={`B(x)`}/> степени <Math m={`n`}/>.
</P>
<Math display
      m={`\\align{
          A(x) &= \\sum_{k=0}^n a_k \\cdot x^k = a_{n} \\cdot x^n + a_{n-1} \\cdot x^{n-1} + \\dotsb + a_2 \\cdot x^2 + a_1 \\cdot x + a_0 \\\\
          B(x) &= \\sum_{k=0}^n b_k \\cdot x^k = b_{n} \\cdot x^n + b_{n-1} \\cdot x^{n-1} + \\dotsb + b_2 \\cdot x^2 + b_1 \\cdot x + b_0
          }`}/>
<P>
    В школе изучался неэффективный метод умножения &laquo;в столбик&raquo;
</P>
<Math display m={`A(x) \\cdot B(x) = \\sum_{k=0}^n x^k \\sum_{i+j=k} a_i b_j`}/>
<P>
    Этот метод требует <Math m={`(n+1)(n+2)/2 = \\Theta(n^2)`}/> умножений.
</P>
</Par>

<Par>
<P>
    Каждый многочлен <Math m={`P(x) = \\sum_{k=0}^n a_k \\cdot x^k`}/> степени <Math m={`n`}/>
    может быть представлен списком своих <Math m={`n+1`}/> коэффициентов <Math m={`a_0, a_1, \\dotsc, a_n`}/>,
    а может быть представлен списком значений в <Math m={`n+1`}/> точках
    <Math m={`\\bigl( x_0, P(x_0) \\bigr), \\bigl( x_1, P(x_1) \\bigr), \\dotsc, \\bigl( x_n, P(x_n) \\bigr)`}/>.
</P>
<P>
    Если два многочлена представлены значениями, а не коэффициентами, то их произведение считается быстро.
    Пусть многочлены <Math m={`A(x)`}/> и <Math m={`B(x)`}/> имеют в точках <Math m={`x_0, x_1, \\dotsc, x_{2n+1}`}/>
    значения <Math m={`A_0, A_1, \\dotsc, A_{2n+1}`}/> и <Math m={`B_0, B_1, \\dotsc, B_{2n+1}`}/>.
    Тогда многочлен <Math m={`A(x) \\cdot B(x)`}/> имеет в этих точках значения
    <Math m={`A_0 B_0, A_1 B_1, \\dotsc, A_{2n+1} B_{2n+1}`}/>.
</P>
<P>
    Такой способ вычисления требует <Math m={`2n+1 = O(n)`}/> умножений.
    Получаем следующий код
</P>
</Par>

<Codeblock code={
`input const int n
input array[int] a[n+1]
input array[int] b[n+1]

array[int] x[2*n+1] = [???, ???, ..., ???]

array[int] A[2*n+1] = evaluate(a, x)
array[int] B[2*n+1] = evaluate(b, x)

array[int] C[2*n+1]
for int i = 0; i < 2*n+1; i++:
    C[i] = A[i] * B[i]

array[int] c[2*n+1] = interpolate(x, C)`
}/>

<Par>
<P>
    Нам осталось придумать эффективную реализацию операций
    <Code c="evaluate(p, x)"/> &mdash; вычисление значений многочлена,
    заданного коэффициентами <Code c="p"/>, в точках <Code c="x"/>
    и <Code c="interpolate(x, P)"/> &mdash; восстановление коэффициентов многочлена
    по его значениям <Code c="P"/> в точках <Code c="x"/>.
</P>
<P>
    Стандартными методами можно реализовать
    операцию <Code c="evaluate(p, x)"/> за <Math m={`n+1`}/> умножений с помощью схемы Горнера
    и операцию <Code c="interpolate(x, P)"/> за <Math m={`O(n^3)`}/> методами обычной интерполяции.
    Можно, конечно, попробовать оптимизировать интерполяцию до <Math m={`O(n^2)`}/>, но это тоже не подходит,
    потому что школьный метод всё еще эффективнее.
</P>
<P>
    Мы вольны выбирать узлы <Math m={`x_j`}/>, и эта способность является ключом к построению эффективного алгоритма.
</P>
</Par>

<Heading>Дискретное преобразование Фурье</Heading>

<Par>
<P>
    Выберем число <Math m={`N \\ge n+1`}/>, чтобы иметь запас на будущее
    (мы из двух многочленов степени <Math m={`n`}/> хотим сделать многочлен степени <Math m={`2n`}/>)
    и чтобы было проще считать.
</P>
<P>
    Для того, чтобы все операции делать эффективно, можно выбрать узлы <Math m={`x_j`}/> следующим образом
</P>
<Math display m={`x_j = e^{2 \\pi i j / N} = w^j`}/>
<P>
    где <Math m={`w = e^{2 \\pi / N}`}/> &mdash; первый комплексный корень из единицы.
</P>
</Par>

<Par>
<P>
    <b>Дискретное преобразование Фурье</b> многочлена <Math m={`P(x)`}/>,
    заданного коэффициентами <Math m={`P(x) = \\sum_{j=0}^{N-1} p_j \\cdot x^j`}/>,
    называется вычисление его значений в <Math m={`N`}/> точках <Math m={`w^0, w^1, w^2, \\dotsc, w^{N-1}`}/>.
    При этом список коэффициентов <Math m={`a_0, a_1, a_2, \\dotsc, a_n`}/> дополнен нулями до длины <Math m={`n`}/>.
</P>
<P>
    Можно сформулировать задачу поиска дискретного преобразования Фурье в матричных терминах
</P>
<Math big display
      m={`\\pmatrix{
          ~ 1 & 1 & 1 & 1 & \\cdots & 1 & 1 \\\\!
          ~ 1 & w & w^2 & w^3 & \\cdots & w^{N-2} & w^{N-1} \\\\!
          ~ 1 & w^2 & w^4 & w^6 & \\cdots & w^{2 (N-2)} & w^{2 (N-1)} \\\\!
          ~ 1 & w^3 & w^6 & w^9 & \\cdots & w^{3 (N-2)} & w^{3 (N-1)} \\\\
          ~ \\vdots & \\vdots & \\vdots & \\vdots & \\ddots & \\vdots & \\vdots \\\\!
          ~ 1 & w^{(N-2)} & w^{(N-2) \\cdot 3} & w^{(N-2) \\cdot 4} & \\cdots & w^{(N-2) \\cdot (N-2)} & w^{(N-2) \\cdot (N-1)} \\\\!
          ~ 1 & w^{(N-1)} & w^{(N-1) \\cdot 3} & w^{(N-1) \\cdot 4} & \\cdots & w^{(N-1) \\cdot (N-2)} & w^{(N-1) \\cdot (N-1)}
          }
          \\cdot
          \\pmatrix{p_0 \\\\ p_1 \\\\ p_2 \\\\ p_3 \\\\ \\vdots \\\\ p_{N-2} \\\\ p_{N-1}}
          =
          \\pmatrix{P_0 \\\\ P_1 \\\\ P_2 \\\\ P_3 \\\\ \\vdots \\\\ P_{N-2} \\\\ P_{N-1}}
          `}/>
</Par>

<Subheading>Алгоритм Кули-Тьюки</Subheading>

<Par>
<P>
    Алгоритм Кули-Тьюки находит дискретного преобразования Фурье
    многочлена <Math m={`P(x) = \\sum_{j=0}^{n} p_j \\cdot x^j`}/>.
</P>
<P>
    Перед всеми манипуляциями нам надо дополнить массив коэффициентов <Math m={`p_j`}/> нулями так,
    чтобы его длина равнялась степени двойки.
    То есть, если исходная степень многочлена <Math m={`P(x)`}/> равнялась <Math m={`n`}/>,
    то после дополнения его степень будет <Math m={`N = 2^{\\lceil \\log_2 n \\rceil}`}/>,
    а коэффициенты <Math m={`p_j = 0`}/> при <Math m={`j > n`}/>.
    Исходный многочлен теперь выглядит так
</P>
<Math display m={`P(x) = \\sum_{j=0}^{N-1} p_j \\cdot x^j`}/>
<P>
    Представим многочлен в виде <Math m={`P(x) = S(x^2) + x \\cdot T(x^2)`}/>,
    где <Math m={`S(x)`}/> состоит из коэффициентов при чётных степенях <Math m={`P(x)`}/>,
    а <Math m={`T(x)`}/> состоит из коэффициентов при нечётных степенях <Math m={`P(x)`}/>.
</P>
<Math display
      m={`S(x) = \\sum_{j=0}^{N/2-1} p_{2j} \\cdot x^j \\qquad T(x) = \\sum_{j=0}^{N/2-1} p_{2j+1} \\cdot x^j`}/>
<P>
    При <Math m={`N = 2k`}/> можно использовать равенство
</P>
<Math display m={`w^{2j} = w^{2j \\bmod 2k} = w^{2 \\cdot (j \\bmod k)}`}/>
<P>
    С помощью этого можно разделить задачу вычисления дискретного преобразования Фурье <Math m={`P(x)`}/>
    к двум вдвое меньшим задачам
</P>
<Math display
      m={`P(w^j) = S(w^{2j}) + w^j \\cdot T(w^{2j}) = S \\big( (w^2)^{j \\bmod k} \\big) + w^j \\cdot T \\big( (w^2)^{j \\bmod k} \\big)`}/>
</Par>

<Codeblock code={
`function fft(array[int] p[N], complex w) -> array[N]:
    if N == 1: return P

    const int k = N / 2

    array[int] s[k], t[k]

    for int i = 0; i < N; i++:
        if i % 2 == 0:
            s[i/2] = p[i]
        else:
            t[i/2] = p[i]

    S = fft(s, w * w)
    T = fft(t, w * w)

    array[int] result[N]
    complex wt = 1

    for int i = 0; i < N; i++:
        result[i] = S[i % k] + wt * T[i % k]
        wt *= w

    return result`
}/>


<Heading>Другие основания</Heading>

<Par>
<P>
    Что нам нужно было от <Math m={`w^j`}/>?
    Только то, что все они являются корнями из единицы, то есть образуют циклическую группу порядка <Math m={`n`}/>.
    Мы выбрали первый попавшийся объект &mdash;
    дискретную подгруппу группы <Math m={`\\CC / \\RR`}/>, имеющую порядок <Math m={`n`}/>.
</P>
</Par>