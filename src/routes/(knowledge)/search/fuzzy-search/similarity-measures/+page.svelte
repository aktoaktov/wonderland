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
</script>

<Title title="Меры схожести"
/>

<Par>
<P>
    При нечётком поиске сразу же встает вопрос: как определять схожесть?
    Центральным объектом нечёткого поиска являются строки, а в общем случае элементы метрических пространств.
</P>
</Par>


<Heading>Расстояние Левенштейна</Heading>

<Par>
<P>
    <b>Расстояние Левенштейна</b> &mdash; метрика на строках, показывающая их схожесть.
    Равна количеству односимвольных операций вставки, удаления и замены символов,
    которые нужно сделать, чтобы превратить одну строку в другую.
</P>
<P>
    Пусть есть две строки <Math m={`a`}/> и <Math m={`b`}/> с длинами <Math m={`n = |a|`}/> и <Math m={`m = |b|`}/>.
    Тогда расстояние Левенштейна между ними равно <Math m={`\\LD(a, b) = d(n, m)`}/>, где
</P>
<Math display
      m={`d(i, j) = \\cases{
          0 & \\if i = 0 \\land j = 0 \\\\
          i & \\if i > 0 \\land j = 0 \\\\
          j & \\if i = 0 \\land j > 0 \\\\
          \\align{
              \\min \\bigl( & d(i, j-1) + 1, \\\\&
                              d(i-1, j) + 1, \\\\&
                              d(i-1, j-1) + [a_i \\neq b_j] \\bigr)
          } & \\otherwise
          }`}/>
<P>
    Для расстояния Левенштейна выполнено важное неравенство
</P>
<Math display m={`\\bigl| |a| - |b| \\bigr| \\le \\LD(a, b) \\le \\max \\bigl( |a|, |b| \\bigr)`}/>
</Par>

<Par>
<P>
    Для экономии памяти можно хранить только две строки: текущую и предыдущую.
</P>
</Par>

<Codeblock code={
`function levenshtein(string a, string b) -> int:
     array[int]

     D(0, 0) = 0
 для всех j от 1 до N
   D(0, j) = D(0, j - 1) + цена вставки символа S2[j]
 для всех i от 1 до M
   D(i, 0) = D(i - 1, 0) + цена удаления символа S1[i]
   для всех j от 1 до N
     D(i, j) = min{
       D(i - 1, j) + цена удаления символа S1[i],
       D(i, j - 1) + цена вставки символа S2[j],
       D(i - 1, j - 1) + цена замены символа S1[i] на символ S2[j]
     }
 вернуть D(M, N)


    if length(a) < length(b):
        a, b = b, a

    int n = length(b)
    array[int] prev[n+1] = [1, 2, 3, ..., n, n+1]

    for int i = 1; i <= n; i++:
        curr = [i] + [0] * len(b)
        for j in range(1, len(b) + 1):
            cost = 0 if a[i-1] == b[j-1] else 1
            curr[j] = min(prev[j] + 1, curr[j-1] + 1, prev[j-1] + cost)
        prev = curr
    return prev[-1]`
}/>


<Subheading>Разная цена операций</Subheading>

<Par>
<P>
    При нечётком поиске некоторые операции редактирования бывают весомее других.
    Расстояние Левенштейна можно модифицировать, и каждой операции приписать свою цену.
    Более того, цена операции может зависеть от самих символов, над которыми производится эта операция.
</P>
<Math display
      m={`\\align{
          \\mathrm{ci}(x) &= \\text{цена вставки символа}~ x \\\\
          \\mathrm{cd}(x) &= \\text{цена удаления символа}~ x \\\\
          \\mathrm{cr}(x, y) &= \\text{цена замены символа}~ x ~\\text{на символ}~ y \\\\
          }`}/>
<P>
    Рекуррентная формула для <Math m={`d(i, j)`}/> преобразуется следующим образом
</P>
<Math display
      m={`d(i, j) = \\cases{
          0 & \\if i = 0 \\land j = 0 \\\\
          \\sum_{k=1}^i \\mathrm{cd}(a_k) & \\if i > 0 \\land j = 0 \\\\
          \\sum_{k=1}^j \\mathrm{ci}(b_k) & \\if i = 0 \\land j > 0 \\\\
          \\align{
              \\min \\bigl( & d(i, j-1) + \\mathrm{ci}(b_j), \\\\&
                              d(i-1, j) + \\mathrm{cd}(a_i), \\\\&
                              d(i-1, j-1) + \\mathrm{cr}(a_i, b_j) \\bigr)
          } & \\otherwise
          }`}/>

<P>
    Таким образом, расстояние Левенштейна &mdash; минимальная стоимость редактирования строк.
</P>
<P>
    При это важно понимать, что если <Math m={`\\mathrm{cd}(x) + \\mathrm{ci}(y) \\le \\mathrm{cr}(x, y)`}/>,
    то алгоритмы всегда будут предпочитать одной операции редактирования две операции: удаление и вставку.
</P>
</Par>