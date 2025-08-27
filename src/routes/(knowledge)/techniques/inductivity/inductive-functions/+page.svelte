<script>
    import Title from "$lib/Elements/Title.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
</script>

<Title title="Индуктивные функции"
/>

<Par>
    <P>
        Напомню, что <Math m="X^*"/> &mdash; множество конечных кортежей из элементов множества <Math m="X"/>,
        и <Math m="\omega \concat x"/> &mdash; операция присоединения элемента <Math m="x \in X"/> в конец кортежа <Math
            m="\omega \in X^*"/>.
    </P>
</Par>

<Definition title="Индуктивная функция">
    <P>
        Функция <Math m="f \colon X^* \to A"/> называется <b>индуктивной</b>, если существует
        такая функция <Math m="F \colon X^* \times X \to A"/>, что
    </P>
    <Math display m="f(\omega \concat x) = F \big(f(\omega), x\big)"/>
    <P>
        Функция <Math m="F"/> называется <b>функцией пересчёта</b> функции <Math m="f"/>.
    </P>
</Definition>

<Par>
    <P>
        Другими словами, мы можем восстановить значение функции <Math m="f"/> на кортеже
    </P>
    <Math display m={`f(x_1, x_2, \\dotsc, x_{n-1}, x_n) = F \\big( f(x_1, x_2, \\dotsc, x_{n-1}), x_n \\big)`}/>
</Par>

<Par>
    <P>
        Значение индуктивной функции для любого кортежа можно легко найти, если известна функция пересчёта
    </P>
    <Math display
          m={`f(x_1, x_2, \\dotsc, x_{n-1}, x_n) = F (F(F(\\dots F(F(f(\\epsilon), x_1), x_2), \\dots), x_{n-1}), x_n)`}/>
    <P>
        Соответственно, код, вычисляющий значение <Math m="f"/>
    </P>

    <Codeblock code={
`function f(tuple x):
    result = f(empty)
    for element in x:
        result = F(result, element)

    return result`
}/>
    <P>
        Для кортежа длины <Math m="n"/> время работы алгоритма составляет <Math m="O(n) \cdot \time F"/>,
        где <Math m="\time F"/> &mdash; время работы функции <Math m="F"/>.
    </P>
</Par>


<Heading>Некоторые индуктивные функции</Heading>

<Subheading>Длина кортежа</Subheading>

<Par>
    <P>
        Функция <Math m="\length(x)"/>, равная длине кортежа <Math m="x"/>, является индуктивной:
    </P>
    <Math display m={`\\length(x \\concat a) = \\length(x) + 1 \\quad \\text{при}~ \\length(\\epsilon) = 0`}/>
</Par>


<Heading>Стационарные значения</Heading>

<Par>
    <P>
        В некоторых случаях можно сократить вычисление индуктивной функции.
        Если в процессе вычисления мы получили значение, которое никакими перевычислениями не изменить,
        то функцию можно дальше не считать и вернуть результат.
        Такие значения для функции называются стационарными.
    </P>
    <P>
        <b>Стационарное значение</b> индуктивной функции <Math m="f"/> &mdash; такое значение <Math m="y"/>, что
    </P>
    <Math display m="\forall x \in X \? F(y, x) = y"/>
    <P>
        Или, по-другому,
    </P>
    <Math display m="\forall x \in X \? f(\omega \concat x) = f(\omega)"/>
</Par>
<Par>
    <P>
        То есть, если мы достигли стационарного значения, можно сразу же объявить ответ, не досчитывая до конца.
    </P>
    <P>
        С учетом этого, код вычисления индуктивной функции немного изменится
    </P>
        <Codeblock code={
`function f(tuple x):
    result = f(empty)
    for element in x:
        result = F(result, element)
        break if result is стационарное значение f()

    return result`
}/>
</Par>