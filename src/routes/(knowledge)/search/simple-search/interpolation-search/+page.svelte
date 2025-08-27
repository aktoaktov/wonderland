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
</script>

<Title title="Интерполяционный поиск"
/>

<Par>
    <P>
        Давайте снова возьмем словарь и будем искать в нйм слова.
        Если нам поступил запрос на поиск слова &laquo;абака&raquo;, то, кажется, нет смысла открывать словарь
        в середине, ведь слово прям очень близко к началу словаря.
        Такой подход свойственен нам, людям, и абсолютно чужд для машин. Так научим же их!
    </P>
    <P>
        Мы хотим научиться предсказывать позицию искомого элемента, и корректировать область поиска в случае промаха.
    </P>
</Par>

<Par>
    <P>
        У нас есть массив упорядоченных ключей <Math m={`K_1, K_2, K_3, \\dotsc, K_{n-1}, K_n`}/>.
        При этом на ключах нам задано не только линейное отношение порядка, но и способ мерить масштаб.
        Формально, нам нужно, чтобы ключи были элементами
        линейного упорядоченного аффинного пространства над линейным упорядоченным полем.
        Но можно не думать об этих страшных словах и просто считать, что мы ищем среди чисел.
    </P>
    <Math display m={`K_1 < K_2 < K_3 < \\dotsb < K_{n-1} < K_n`}/>
    <P>
        Нам нужно найти в этом массиве номер ключа <Math m={`K`}/>,
        то есть такое <Math m={`j`}/>, что <Math m={`K_j = K`}/>.
    </P>
</Par>

<Par>
    <P>
        Как и с <Link to="../comparison-search">бинарным поиском</Link>, заведем переменные,
        указывающие на границы области поиска <Code c="left"/> и <Code c="right"/>.
        Но опорный индекс мы будем выбирать не как середину, а будем пытаться предсказывать положение целевого элемента
        <Math m={`K`}/>.
    </P>
    <P>
        Для того, чтобы что-то предположить, нам нужно какое-то основание.
        Пусть мы будем надеяться на то, что элементы по индексам подчиняются линейной зависимости.
    </P>
    <P>
        В итоге мы просто линейно интерполируем по двум точкам <Math m={`\\big( \\code{left}, a[\\code{left}] \\big)`}/>
        и <Math m={`\\big( \\code{right}, a[\\code{right}] \\big)`}/>, и вычисляем индекс <Math m={`j`}/>,
        с надеждой, что <Math m={`a[j] = K`}/>. Формула вычисления индекса получается
    </P>
    <Math display m={`j = \\code{left} + \\frac{\\big( K - a[\\code{left}] \\big) \\cdot (\\code{right} - \\code{left})}{a[\\code{right}] - a[\\code{left}]}`}/>
    <P>
        В остальном алгоритм полностью аналогичен бинарному поиску.
    </P>
</Par>

<Codeblock code={
`function interpolation_search(sequence a, target) -> int:
    int left = 0
    int right = length(a) - 1

    while left <= right:
        int j = left + (target - a[left]) * (right - left) / (a[right] - a[left])

        if a[j] == target:
            return j
        else if a[j] < target:
            left = j + 1
        else:
            right = j - 1

    return not found`
}/>


<Subheading>Анализ количества сравнений</Subheading>

<Par>
    <P>
        Оно <Math m={`O(\\log \\log n)`}/>. Надо будет написать доказательство.
    </P>
</Par>