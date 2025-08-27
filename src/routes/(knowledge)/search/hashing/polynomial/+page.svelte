<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
</script>

<Title title="Полиномиальное хеширование"
/>

<Par>
    <P>
        Мы научились хешировать числа. Теперь мы хотим научиться хешировать последовательности чисел.
        Точнее, формально, мы хотим научиться хешировать строки из языка <Math m={`A^*`}/>,
        где каждый символ в алфавите <Math m={`A`}/> закодирован каким-то числом.
    </P>
    <P>
        Строку <Math m={`s`}/> будем представлять как упорядоченный набор символов <Math m={`s_i`}/>,
        которые будем воспринимать как числа.
    </P>
    <Math display m={`s = s_0 \\, s_1 \\, s_2 \\, s_3 \\dotsm s_{n-3} \\, s_{n-2} \\, s_{n-1} \\, s_n`}/>
</Par>

<Definition title="Полиномиальный хеш">
    <P>
        <b>Прямым полиномиальным хешем</b> строки <Math m={`s`}/> называется число
    </P>
    <Math display
          m={`\\hash(s) = \\sum_{i=0}^{n} s_i \\cdot x^i \\bmod m = \\big( s_0 + s_1 \\cdot x + s_2 \\cdot x^2 + \\dotsb + s_{n-1} \\cdot x^{n-1} + s_n \\cdot x^n \\big) \\bmod m`}/>

    <P>
        <b>Обратным полиномиальным хешем</b> строки <Math m={`s`}/> называется число
    </P>
    <Math display
          m={`\\hash(s) = \\sum_{i=0}^{n} s_i \\cdot x^{n-i} \\bmod m = \\big( s_0 \\cdot x^n + s_1 \\cdot x^{n-1} + s_2 \\cdot x^{n-2} + \\dotsb + s_{n-1} \\cdot x + s_n \\big) \\bmod m`}/>

    <P>
        Здесь <Math m={`x`}/> &mdash; произвольное число, большее размера алфавита,
        а <Math m={`m`}/> &mdash; достаточно большой модуль, взаимнопростый с <Math m={`x`}/>.
    </P>
</Definition>

<Par>
    <P>
        Считаются прямые и обратные полиномиальные хеши почти в лоб.
        Сами значения многочленов можно быстро считать с помощью индуктивных вычислений,
        ведь сам многочлен &mdash; индуктивная функция.
    </P>
    <P>
        Обратный хеш еще и красиво пишется. Однако, он немного непривычен из-за обратного порядка символов.
    </P>
</Par>

<Codeblock code={
`const int x = ...
const int m = ...

function forward_hash(string s) -> int:
    int hash = 0
    int monome = 1

    for c of s:
        hash = (hash + monome * c) % m
        monome = (monome * x) % m

    return hash

function backward_hash(string s) -> int:
    int hash = 0

    for c of s:
        hash = (hash * x + c) % m

    return hash`
}/>

<Subheading>Свойства и быстрый пересчет</Subheading>

<Par>
    <P>
        Если нам известны хеши двух строк <Math m={`a`}/> и <Math m={`b`}/>,
        то мы можем быстро посчитать хеш конкатенации этих строк <Math m={`ab`}/>.
    </P>
    <Math display m={`\\hash(ab) = \\hash(a) + x^{|a|} \\cdot \\hash(b)`}/>
    <P>
        Отсюда легко выводятся алгоритмы удаления префикса и суффикса строки
    </P>
    <P>
        Для удаления суффикса достаточно просто вычесть хеш суффикса
    </P>
    <Math display m={`\\hash(a) = \\hash(ab) - x^{|a|} \\cdot \\hash(b)`}/>

    <P>
        А для удаления префикса придется делить по модулю <Math m={`m`}/>,
        то есть умножать на обратный по модулю <Math m={`m`}/> элемент
    </P>
    <Math display m={`\\hash(b) = \\big( \\hash(ab) - \\hash(a) \\big) \\cdot \\big( x^{|a|} \\big)^{-1}`}/>

</Par>

<Par>
    <P>
        Использовав две предыдущие формулы, можно получить формулу вычисления любого среза строки.
    </P>
    <P>
        Нам нужна некоторая подготовка. Если мы хотим для данной строки быстро находить хеш любого её среза,
        то нам придется предварительно посчитать хеши всех префиксов этой строки.
        Хранить всё будем в массиве <Math m={`h`}/>,
        где <Math m={`h_i`}/> &mdash; хеш префикса, состоящего из <Math m={`i`}/> символов.
    </P>
</Par>

<Codeblock code={
`const int x = ...
const int m = ...

string s
array[int] h

h[0] = 0  # Хеш пустой строки равен 0

for i = 1; i <= length(s); i++:
    h[i+1] = (h[i] + x ** i * s[i]) % m`
}/>

<Par>
    <P>
        Теперь хеш среза <Math m={`s_{l:r}`}/> строки <Math m={`s`}/> легко считается по формуле
    </P>
    <Math display m={`\\hash(s_{l:r}) = (h_r - h_l) \\cdot \\big( x^l \\big)^{-1}`}/>
</Par>
