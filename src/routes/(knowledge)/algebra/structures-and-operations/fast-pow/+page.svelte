<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Code from "$lib/Code/Code.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
</script>

<Title title="Быстрое возведение в степень"
/>

<Par>
    <P>
        Пусть у нас есть какая-то ассоциативная бинарная операция <Math m={`\\circ`}/> в алгебре <Math m={`\\AAA`}/>.
        Мы хотим научиться быстро считать степень элемента <Math m={`a`}/> носителя алгебры <Math m={`\\AAA`}/> по этой
        операции, то есть значение
    </P>
    <Math display m={`a^n = \\underbrace{a \\circ a \\circ \\dotsb \\circ a \\circ a}_{n ~\\text{раз}}`}/>
    <P>
        В псевдокоде я заменю операцию <Math m={`\\circ`}/> на умножение, но это просто для удобства написания.
        В формулах я буду использовать оригинальное обозначение, дабы подчеркнуть универсальность.
    </P>
</Par>


<Par>
    <P>
        Можно применить свойство ассоциативности для сведения задачи возведения в степень <Math m={`n`}/>
        к вдвое меньшей задаче, используя простое свойство
    </P>
    <Math display m={`a^n = \\cases{a^{n/2} \\circ a^n & n~\\text{чётное} \\\\ a \\circ a^{n-1} & n~\\text{нечётное}}`}/>

    <P>
        Из этого простого свойства можно сразу вывести простой рекурсивный алгоритм
    </P>
</Par>

<Codeblock code={
`function fast_pow(a, int n):
    if n % 2 == 0:
        return fast_pow(a, n/2) ** 2
    else:
        return a * fast_pow(a, n-1)`
}/>

<Par>
    <P>
        У рекурсии есть оверхед, от которого хотелось бы избавиться.
    </P>
    <P>
        Давайте посмотрим на двоичное представление <Math m={`n`}/>
    </P>
    <Math display m={`n = (n_k \\, n_{k-1} \\, \\dotsm \\, n_2 \\, n_1 \\, n_0)_2 = n_k \\cdot 2^k + n_{k-1} \\cdot 2^{k-1} + \\dotsb + n_2 \\cdot 4 + n_1 \\cdot 2 + n_0`}/>
    <P>
        Тогда нашу степень можно переписать как
    </P>
    <Math display m={`n = ((( \\dotsm ((n_k \\cdot 2 + n_{k-1}) \\cdot 2 + n_{k-2}) \\cdot 2 + \\dotsm) \\cdot 2 + n_2) \\cdot 2 + n_1) \\cdot 2 + n_0`}/>
    <P>
        Ну и здесь сразу видно, как производить вычисления
    </P>
</Par>

<Codeblock code={
`function fast_pow(a, int n):
    int result = 1
    while n > 0:
        if n % 2 == 1:
            result *= a
        a *= a
        n /= 2;
    return result`
}/>

<Par>
    <P>
        Важное замечание: <Math m={`1`}/> в этом алгоритме &mdash; нейтральный элемент по операции <Math m={`\\circ`}/>.
    </P>
</Par>

<Par>
    <P>
        Оценим количество умножений, требуемых алгоритмом (не важно каким, они одинаковые).
        Пусть для возведения числа <Math m={`a`}/> в степень <Math m={`n`}/> требуется <Math m={`M(n)`}/> умножений.
        Тогда, исходя из нашего алгоритма, справедлива формула
    </P>
    <Math display m={`M(n) = M\\left( \\left\\lfloor \\frac{n}{2} \\right\\rfloor \\right) + 1 + (n \\bmod 2)`}/>
    <P>
        Решение этого уравнения
    </P>
    <Math display m={`M(n) = \\lfloor \\log_2 n \\rfloor + \\nu(n) - 1`}/>
    <P>
        где <Math m={`\\nu(n)`}/> &mdash; количество единиц в числе <Math m={`n`}/>
    </P>
</Par>


<Heading>Предподсчёт</Heading>

<Par>
<P>
    Пусть у нас есть фиксированный объект <Math m={`a`}/>.
    К нам поступает <Math m={`q`}/> запросов возведения <Math m={`a`}/> в степень <Math m={`m_i`}/>
    (<Math m={`i`}/> - номер запроса).
</P>
<P>
    Только что мы научились решать эту задачу за
    <Math m={`\\sum_{i=1}^q \\bigl( \\lfloor \\log_2 m_i \\rfloor + \\nu(m_i) \\bigr)`}/>
    умножений, что в итоге выливается в временную сложность <Math m={`O(q \\cdot \\log \\max m) \\cdot \\time(\\text{одно умножение})`}/>
</P>
</Par>

<Heading>Аддитивные цепочки и оптимальный алгоритм</Heading>