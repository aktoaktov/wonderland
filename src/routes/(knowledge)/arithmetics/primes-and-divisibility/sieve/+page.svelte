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

<Title title="Решета"
/>


<Par>
<P>
    Здесь мы будем находить все простые числа от <Math m={`1`}/> до <Math m={`n`}/>.
</P>
</Par>


<Heading>Решето Эратосфена</Heading>

<Par>
<P>
    <b>Решето Эратосфена</b> &mdash; алгоритм нахождения списка простых чисел.
</P>
<P>
    Идея простая. Запишем ряд чисел <Math m={`2, 3, 4, \\dotsc, n-1, n`}/>.
    Вычеркнем из него все числа, делящиеся на <Math m={`2`}/>, кроме, конечно, <Math m={`2`}/>.
    Затем вычеркнем все числа, делящиеся на <Math m={`3`}/>, кроме <Math m={`3`}/>.
    Число <Math m={`4`}/> уже вычеркнуто, и все числа, кратные <Math m={`4`}/>, тоже. Поэтому идём дальше.
    Вычеркиваем все числа, делящиеся на <Math m={`5`}/>, кроме <Math m={`5`}/>.
    Ну и продолжаем так, пока не дойдем до конца.
</P>
<P>
    Итого, мы для каждого простого числа вычёркиваем все дальнейшие числа, кратные ему.
</P>
</Par>

<Par>
<P>
    Реализовывать программно это можно по-разному, но самый простой способ &mdash;
    завести битовый массив <Code c="is_prime"/>.
    Если число <Math m={`i`}/> вычеркнуто, то <Math m={`\\code{is\\_prime}[i-2] = 0`}/>.
    Вообще можно оставить лишние <Math m={`2`}/> бита в начале и сделать нормальную индексацию.
</P>
</Par>

<Codeblock code={
`input const int n
array[bool] is_prime[n+1] = [true, true, ..., true]

for int i = 2; i <= n; i++:
    if is_prime[i]:
        for int j = 2 * i; j <= n; j += i:
            is_prime[j] = false`
}/>

<Par>
<P>
    Есть несколько очевидных оптимизаций, которые стоит сразу же применить.
</P>
<P>
    Во-первых, начинать вычёркивать кратные числа <Math m={`p`}/> можно с <Math m={`p^2`}/>, а не с <Math m={`2p`}/>.
    Ведь все составные числа, кратные <Math m={`p`}/> и меньшие <Math m={`p^2`}/> были вычеркнуты до этого,
    потому что у них был делитель, меньший <Math m={`p^2/p = p`}/>.
</P>
<P>
    Во-вторых, внешний цикл можно сделать до <Math m={`\\sqrt{n}`}/>.
    Пусть <Math m={`p`}/> &mdash; простое число, большее <Math m={`\\sqrt{n}`}/>.
    Его наименьшее кратное, которое можно вычеркнуть &mdash; <Math m={`p^2`}/>.
    Оно будет находиться за диапазоном поиска простых, ведь <Math m={`p^2 > n`}/>.
</P>
<P>
    С учётом всех оптимизаций, получаем код
</P>
</Par>

<Codeblock code={
`input const int n
array[bool] is_prime[n+1] = [true, true, ..., true]

for int i = 2; i * i <= n; i++:
    if is_prime[i]:
        for int j = i * i; j <= n; j += i:
            is_prime[j] = false`
}/>

<Par>
<P>
    Проанализируем время работы алгоритма.
    Будем измерять число установок в битовом массиве <Code c="is_prime"/>.
</P>
<P>
    Для каждого простого числа <Math m={`p`}/> в диапазоне от <Math m={`2`}/> до <Math m={`\\sqrt{n}`}/>
    мы сделаем <Math m={`\\lfloor n / p \\rfloor - (p-1)`}/> установок.
    Количество чисел в диапазоне от <Math m={`1`}/> до <Math m={`n`}/>, которые кратны <Math m={`p`}/>,
    равно <Math m={`\\lfloor n/p \\rfloor`}/>.
    Тогда общее количество установок, сделанное алгоритмом, равно
</P>
<Math display
      m={`\\sum_{\\substack{p ~\\text{простое} \\\\ p \\le \\sqrt{n}}} \\Biggl( \\left\\lfloor \\frac{n}{p} \\right\\rfloor - p + 1 \\Biggr)
          = n \\ln \\ln n + (M - \\ln 2) \\cdot n - \\frac{n}{\\ln n} + O \\left( \\frac{n}{\\ln^2 n} \\right)`}/>
<P>
    где <Math m={`M \\approx 0.261\\,497`}/> &mdash; константа Мейсселя-Мертенса.
</P>
<P>
    При этом в не оптимизированном алгоритме количество установок равно
</P>
<Math display
      m={`\\sum_{\\substack{p ~\\text{простое} \\\\ p \\le n}} \\Biggl( \\left\\lfloor \\frac{n}{p} \\right\\rfloor - 1 \\Biggr)
          = n \\ln \\ln n + M n + O \\left( \\frac{n}{\\ln^2 n} \\right)`}/>
</Par>


<Heading>Линейное решето Эратосфена</Heading>

<Par>
<P>
    Основная проблема решета Эратосфена в том, что мы неизбежно помечаем некоторые числа как составные несколько раз.
    Мы помечаем число как составное столько раз, сколько у него различных простых делителей.
</P>
<P>
    Пусть <Math m={`d(k) \\defeq \\min_{p ~\\text{простое}} \\{ p \\divides k\\}`}/> &mdash;
    минимальный простой делитель числа <Math m={`k`}/>.
    Любое число <Math m={`k`}/> тогда представимо в виде <Math m={`k = d(k) \\cdot r`}/>,
    где у <Math m={`r`}/> нет простых делителей, меньших <Math m={`d(k)`}/>.
</P>
</Par>

<Par>
<P>
    Давайте для каждого числа <Math m={`k`}/> считать <Math m={`d(k)`}/>.
    Заведем массив <Code c="d"/>, в котором будем хранить найденные значения.
</P>
<P>

</P>
</Par>