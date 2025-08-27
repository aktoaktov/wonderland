<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import Math from "$lib/Math/Math.svelte"
    import P from "$lib/Markup/P.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
    import Code from "$lib/Code/Code.svelte"
</script>

<Title title="Сортировка вставками"
/>

<Par>
<P>
    Мы решаем задачу сортировки: нам нужно упорядочить ключи <Math m="K_1, K_2, \dotsc, K_n"/>
    по возрастанию относительного какого-то линейного порядка.
</P>
</Par>


<Heading>Метод простых вставок</Heading>
<Par>
<P>
    Допустим, мы уже отсортировали <Math m="j-1"/> записей так, что
</P>
<Math display m={`K_1 \\le K_2 \\le \\dotsb \\le K_{j-2} \\le K_{j-1}`}/>
<P>
    Теперь нам нужно вставить следующий ключ <Math m="K_j"/>.
    Будем сравнивать его по очереди с ключами <Math m={`K_{j-1}, K_{j-2}, \\dotsc K_1`}/>, пока не обнаружим,
    что его нужно вставить между ключами <Math m="K_i"/> и <Math m={`K_{i+1}`}/>.
    Сдвинем все ключи, начиная с <Math m={`K_{i+1}`}/>, на одну позицию и вставим запись <Math m="K_j"/> на место
    <Math m="i+1"/>.
</P>
<P>
    Другими словами, бы каждый раз берем новый ключ и вставляем его в правильное место.
</P>
</Par>

<Codeblock code={
`function insertion_sort(mutable array a[n]):
    for int j = 1; j < n; j++:
        int i = j - 1
        key = a[j]

        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i -= 1

        a[i+1] = key`
}/>

<Par>
<P>
    Количество сравнений в этом алгоритме равно числу инверсий перестановки <Math m={`(K_1, K_2, \\dotsc, K_n)`}/>
    плюс количество выходных сравнений в цикле <Code c="while"/> &mdash; <Math m={`n-1`}/>
</P>
<Math display
      m={`\\min = n-1  ,\\quad
          \\ave = (n^2 + 3n - 4) / 4  ,\\quad
          \\max = (n^2 + n - 2) / 2  ,\\quad
          \\dev = \\frac{1}{6}\\sqrt{n \\cdot (n-1) \\cdot (n + 5/2)}
          `}/>
</Par>


<Heading>Бинарные и двухпутевые вставки</Heading>

<Par>
<P>
    В алгоритме простых вставок новый <Math m={`j`}/>-й элемент сравнивался
    в среднем с <Math m={`(j-1)/2`}/> уже отсортированными элементами по порядку.
    В итоге общее количество сравнений в среднем равно <Math m={`\\sum_{j=2}^n (j-1)/2 = (n^2 - n) / 4 = O(n^2)`}/>.
</P>
<P>
    Можно использовать то, что элементы, в которые мы хотим вставить новый ключ, уже отсортированы.
    Будем искать место вставки с помощью бинарного поиска.
    До конца это проблему не решит, ведь кроме поиска места вставки нужно её произвести.
    Но даже так это неплохой буст к производительности
</P>
<P>
    Итого мы для каждого элемента с номером <Math m={`j+1`}/> проводим бинарный поиск
    в подмассиве размера <Math m={`j`}/> (все, что находится спереди).
    В итоге максимальное количество сравнений
</P>
<Math display
      m={`\\sum_{j=1}^n \\lceil \\log_2 j \\rceil = n \\cdot \\lceil \\log_2 n \\rceil - 2^{\\lceil \\log_2 n \\rceil} + 1 = n \\log_2 n - n + O(1)`}/>
</Par>

<Par>

</Par>