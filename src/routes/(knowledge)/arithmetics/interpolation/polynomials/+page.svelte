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

<Title title="Интерполяционный многочлен Лагранжа"
/>

<Par>
    <P>
        Интерполяция &mdash; нахождение промежуточных значений между известными
    </P>
</Par>

<Heading>Интерполяционный многочлен Лагранжа</Heading>

<Theorem title="Задание многочлена">
    <P>
        Многочлен степени <Math m={`n`}/> однозначно задается своими значениями в <Math m={`n+1`}/> точке
        <Math m={`x_0, x_1, \\dotsc, x_n`}/>.
    </P>
    <P>
        Существует ровно один многочлен <Math m={`P`}/> степени <Math m={`n`}/> такой, что для заданного набора точек
        <Math m={`(x_0, y_0), (x_1, y_1), \\dotsc, (x_n, y_n)`}/>
    </P>
    <Math display m={`y_0 = P(x_0) \\quad y_1 = P(x_1) \\quad \\cdots \\quad y_n = P(x_n)`}/>
</Theorem>

<Definition title="Интерполяционный многочлен Лагранжа">
    <P>
        <b>Интерполяционный многочлен Лагранжа</b> &mdash; многочлен степени <Math m={`n`}/>,
        удовлетворяющий условиям теоремы, то есть проходящий через точки
        <Math m={`(x_0, y_0), (x_1, y_1), \\dotsc, (x_n, y_n)`}/>
    </P>
    <Math display m={`P(x) = \\sum_{i=0}^n y_i \\cdot \\prod_{j \\neq i} \\frac{x-x_j}{x_i-x_j}`}/>
</Definition>

<Proof>
    <P>
        В том, что этот многочлен <Math m={`P(x)`}/> действительно проходит через все заданные точки,
        можно убедиться подстановкой.
    </P>
    <P>
        <b>Единственность многочлена.</b>
        Такой многочлен степени <Math m={`n`}/> есть всего один.
    </P>
    <P>
        Предположим, что это не так, и что есть два разных многочлена <Math m={`A(x)`}/> и <Math m={`B(x)`}/>,
        <Math m={`\\deg A = \\deg B = n`}/>, которые оба проходят через заданные точки.
        Их разность <Math m={`A(x) - B(x)`}/> равна <Math m={`0`}/> во всех точках <Math m={`x_0, x_1, \\dotsc, x_n`}/>.
        Тогда
    </P>
    <Math display m={`A(x) - B(x) = \\alpha \\cdot \\prod_{i=0}^n (x-x_i)`}/>
    <P>
        является многочленом степени <Math m={`n+1`}/>, а это невозможно, потому что оба многочлена степени <Math
            m={`n`}/>.
    </P>
</Proof>

<Par>
    <P>
        Велик соблазн превратить этот многочлен в привычный вид, выразив коэффициенты
    </P>
    <Math display m={`P(x) = a_0 + a_1 \\cdot x + a_2 \\cdot x^2 + \\dotsb + a_{n-1} \\cdot x^{n-1} + a_n \\cdot x^n`}/>
    <P>
        К сожалению, эти коэффициенты считаются очень долго.
        Но полезно понимать свойства этих коэффициентов и связь интерполяционного многочлена Лагранжа
        с матрицей Вандермонда.
    </P>
    <P>
        Можно записать систему <Math m={`n+1`}/> линейных уравнений, чтобы выразить коэффициенты.
        Пишу сразу в матричной форме
    </P>
    <Math big display
          m={`
          \\pmatrix{
          ~1 & x_0 & x_0^2 & \\cdots & x_0^{n-1} & x_0^n \\\\!
          ~1 & x_1 & x_1^2 & \\cdots & x_1^{n-1} & x_1^n \\\\!
          ~1 & x_2 & x_2^2 & \\cdots & x_2^{n-1} & x_2^n \\\\!
          ~\\vdots & \\vdots & \\vdots & \\ddots & \\vdots & \\vdots \\\\!
          ~1 & x_{n-1} & x_{n-1}^2 & \\cdots & x_{n-1}^{n-1} & x_{n-1}^n \\\\!
          ~1 & x_n & x_n^2 & \\cdots & x_n^{n-1} & x_n^n
          }
          \\cdot
          \\pmatrix{a_0 \\\\ a_1 \\\\ a_2 \\\\  \\vdots \\\\ a_{n-1} \\\\ a_n}
          =
          \\pmatrix{y_0 \\\\ y_1 \\\\ y_2 \\\\  \\vdots \\\\ y_{n-1} \\\\ y_n}`}/>
</Par>


<Heading>Вычисление</Heading>

<Par>
    <P>
        Понятно, что в лоб считать значение многочлена <Math m={`P(x)`}/> в произвольной точке <Math m={`x`}/>
        не очень эффективно &mdash; временная сложность этой операции <Math m={`\\Theta(n^2)`}/>.
        Таким образом, на вычисления значений одного многочлена в <Math m={`k`}/> различных точках
        нам потребуется время <Math m={`\\Theta(kn^2)`}/>.
    </P>
    <P>
        Есть несколько алгоритмов, которые с некоторым предварительным подсчетом уменьшают время
        вычисления значения многочлена в одной точке до <Math m={`\\Theta(n)`}/>.
    </P>
</Par>

<Subheading>Метод разделенных разностей</Subheading>

<Par>
    <P>
        Можно построить специальную таблицу разделенных разностей,
        а затем на каждом запросе считать значение многочлена итеративно.
    </P>
    <P>
        Интерполяционный многочлен <Math m={`P(x)`}/> можно представить через разделенные разности
    </P>
    <Math display m={`P(x) = \\sum_{k=0}^n y[x_0, x_1, \\dotsc, x_k] \\cdot \\prod_{i=0}^{k-1} (x-x_i)`}/>
    <P>
        где <Math m={`y[x_0; x_1; \\dotsc; x_k]`}/> &mdash; разделенная разность <Math m={`y`}/> порядка <Math m={`k`}/>:
    </P>
    <Math display
          m={`y[x_i] = y_i \\qquad y[x_j; x_{j+1}; \\dotsc; x_{j+k}] = \\frac{ y[x_{j+1}; x_{j+2}; \\dotsc; x_{j+k}] - y[x_j; x_{j+1}; \\dotsc; x_{j+k-1}] }{x_{j+k} - x_j}`}/>
</Par>

<Par>
    <P>
        Нам нужно предварительно за время <Math m={`\\Theta(n^2)`}/>
        посчитать <Math m={`n+1`}/> разделенную разность <Math m={`d_i`}/>
    </P>
    <Math display m={`d_i = y[x_0; x_1; \\dotsc; x_i]`}/>
</Par>

<Codeblock code={
`input const int n
input array[real] x
input array[real] y

array[real] d
d = copy(y)

for int j = 1; j <= n; j++:
    for int i = n; i >= j; i--:
        d[i] = (d[i] - d[i - 1]) / (x[i] - x[i - j])
`}/>

<Par>
    <P>
        Теперь мы можем сделать функцию, которая будет быстро считать значение многочлена <Math m={`P(x)`}/>.
        Используем для вычислений нашу формулу
    </P>
    <Math display m={`P(x) = \\sum_{k=0}^n d_k \\cdot \\prod_{i=0}^{k-1} (x-x_i)`}/>
    <P>
        Это можно считать быстро, за время <Math m={`\\Theta(n)`}/>, если использовать индуктивные вычисления.
    </P>
</Par>

<Codeblock code={
`function P(real t):
    int result = d[n]

    for int i = n-1; i >= 0; i--:
        result = result * (t - x[i]) + d[i]

    return result`
}/>

<Par>
    <P>
        Этот метод хорош тем, что он позволяет добавлять точки.
    </P>
    <P>
        Пусть у нас есть <Math m={`n+1`}/> точка <Math m={`(x_0, y_0), (x_1, y_1), \\dotsc, (x_n, y_n)`}/>,
        построенный массив разделенных разностей <Math m={`d_0, d_1, \\dotsc, d_n`}/>
        и интерполяционный многочлен <Math m={`P_n(x)`}/>.
        Мы хотим добавить еще одну точку <Math m={`(x_{n+1}, y_{n+1})`}/>.
    </P>
    <P>
        При добавлении узла нам нужно будет только досчитать разделенную разность
    </P>
    <Math display m={`d_{n+1} = y[x_0; x_1; \\dotsc; x_{n+1}]`}/>
    <P>
        и тогда к многочлену просто добавится еще один член, а формула не изменится
    </P>
    <Math display m={`P_{n+1}(x) = P_n(x) + d_{n+1} \\cdot \\prod_{i=0}^n (x-x_i)`}/>
</Par>

<Codeblock code={
`function add_node(int x_new, int y_new):
    x.append(x_new)
    y.append(y_new)
    
    array[real] temp[n+1] = [0.0, ..., 0.0]
    temp[0] = y_new
    for int j = 1; j <= n:
        temp[j] = (temp[j-1] - d[j-1]) / (x_new - self.x[n - j])

    d.append(temp[n])
    n += 1`
}/>

<Par>
    <P>
        Подсчёт новой разделенной разности <Math m={`d_k`}/> работает за время <Math m={`\\Theta(n)`}/>.
    </P>
</Par>