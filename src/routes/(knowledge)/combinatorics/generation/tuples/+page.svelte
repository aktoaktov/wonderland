<script>
    import Heading from "$lib/Markup/Heading.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Title from "$lib/Elements/Title.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Link from "$lib/Elements/Link.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
    import Image from "$lib/Elements/Image.svelte"
</script>

<Title title="Генерация кортежей"
/>

<Par>
<P>
    Начнём с простого. Пусть нам нужно сгенерировать все <Math m={`2^n`}/> бинарных строк длины <Math m={`n`}/>.
    Точнее, нам нужно сделать итератор, который выдает нам все возможные битовые строки по одному разу.
</P>
<P>
    Битовую строку можно рассматривать как число в двоичной системе счисления.
    Тогда нам достаточно просто перебирать все числа от <Math m={`0`}/> до <Math m={`2^n-1`}/>
    и переводить их в двоичную систему счисления:
</P>
</Par>

<Codeblock code={
`generator binary_tuples(int n) -> tuple[{0, 1}]:
    for int i = 0; i < 2 ** n; i++:
        yield convert(n, to base 2)`
}/>

<Par>
<P>
    Точно также можно поступить и когда нам нужно сгенерировать <Math m={`d`}/>-арные строки длины <Math m={`n`}/>.
    Это строки из множества <Math m={`\\{0, 1, 2, \\dotsc, d-1, d\\}^n`}/>.
</P>
<P>
    Представляем все числа от <Math m={`0`}/> до <Math m={`d^n-1`}/> в системе счисления по основанию <Math m={`d`}/>
    и выдаём их по порядку.
</P>
</Par>

<Codeblock code={
`generator tuples(int n, int d) -> tuple[int]:
    for int i = 0; i < d ** n; i++:
        yield convert(n, to base d)`
}/>

<Par>
<P>
    Такой лобовой метод, конечно, имеет право на существования, но он немного неэффективен.
</P>
<P>
    Перевод числа <Math m={`n`}/> в систему счисления по основанию <Math m={`d`}/>
    требует <Math m={`\\lfloor \\log_d n \\rfloor + 1`}/> итераций,
    а каждая итерация выполняет одно деление на <Math m={`d`}/> и одно взятие по модулю <Math m={`d`}/>.
    Итого для полной генерации количество итераций равно
</P>
<Math display
      m={`1 + \\sum_{k=1}^{d^n-1} \\bigl( \\lfloor \\log_d n \\rfloor + 1\\bigr) = n \\cdot d^n - \\frac{d^n - 1}{d - 1} + 1`}/>
</Par>

<Par>
<P>
    На самом деле нам не нужно каждый раз переводить число в систему счисления по основанию <Math m={`d`}/>.
    Следующее число отличается от предыдущего только на <Math m={`1`}/>,
    поэтому можно просто прибавлять <Math m={`1`}/>, но уже в позиционном представлении числа.
    Добавление происходит прям также, как при сложении в столбик: переносим разряды когда надо.
</P>
</Par>


<Subheading>Смешанная система счисления</Subheading>

<Par>
<P>
    Вообще, для такой задачи генерации есть обобщение: сгенерировать все возможные кортежи длины <Math m={`n`}/>,
    где на позиции <Math m={`j`}/> стоит число <Math m={`a_j`}/>, которое <Math m={`0 \\le a_j < m_j`}/>.
</P>
<P>
    Получается, задача генерации сводится к задаче &laquo;добавления <Math m={`1`}/>&raquo; к &laquo;числу&raquo;
    <Math m={`a_1 \\, a_2 \\, a_3 \\, \\dotsm \\, a_{n-1} \\, a_n`}/>, записанному
    в смешанной позиционной счисления по основанию <Math m={`(m_1, m_2, m_3, \\dotsc, m_{n-1}, m_n)`}/>:
</P>
<Math display
      m={`\\bmatrix{a_1 & a_2 & a_3 & \\cdots & a_{n-1} & a_n \\\\ m_1 & m_2 & m_3 & \\cdots & m_{n-1} & m_n}`}/>
</Par>

<Par>
<P>
    Для удобства введем дополнительные переменные <Math m={`a_0`}/> и <Math m={`m_0`}/>.
</P>
</Par>

<Codeblock code={
`generator radix_tuples(tuple[int] m[n]) -> tuple[int]:
    array[int] a = [0, 0, ..., 0]

    yield tuple(a)

    forever:
        a[-1] += 1

        for int i = n - 1; i >= 0; i--:
            if a[i] >= m[i]:
                if i == 0: stop
                a[i] = 0
                a[i - 1] += 1
            else:
                break

        yield tuple(a)`
}/>

<Par>
<P>
    Всего будет сгенерировано <Math m={`\\prod_{j=1}^n m_j`}/> кортежей в лексикографическом порядке.
</P>
</Par>